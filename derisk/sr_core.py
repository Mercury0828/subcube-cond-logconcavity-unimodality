"""
sr_core.py — C0 de-risking core (guide 6/12). NOT a proof; a small-cube directional probe.

Key objects:
  - distributions mu over {0,1}^n as numpy arrays of length 2^n (index = bitmask, bit i = coord i).
  - generating polynomial g_mu(z) = sum_S mu[S] prod_{i in S} z_i  (multiaffine, nonneg coeffs).
  - SR membership (Branden multiaffine criterion): real-stable <=> Rayleigh-difference
        Delta_ij(x) = d_i g(x) * d_j g(x) - g(x) * d_i d_j g(x) >= 0
    for ALL x in R_+^n and all i != j. We probe this on a fixed grid + random points (a NUMERICAL
    proxy for the lean; not a proof).
  - NOTE (the structural seam): Delta_ij(1,...,1) = p_i p_j - p_ij = -Cov(x_i, x_j). So pairwise
    negative correlation == the Rayleigh inequality AT the all-ones vertex; SR demands it on the whole
    interior. Subcube conditioning probes z_k in {0, infinity} (vertices), not interior x.

All randomness uses a fixed seed (see run_c0.py).
"""
import itertools
import numpy as np

# ----------------------------------------------------------------------------------------
# generating polynomial and its partials
# ----------------------------------------------------------------------------------------

def _subsets(n):
    return range(1 << n)

def _bits(s, n):
    return [(s >> i) & 1 for i in range(n)]

def g_eval(mu, n, z):
    """g_mu(z) = sum_S mu[S] prod_{i in S} z_i."""
    total = 0.0
    for s in range(1 << n):
        if mu[s] == 0.0:
            continue
        prod = 1.0
        for i in range(n):
            if (s >> i) & 1:
                prod *= z[i]
        total += mu[s] * prod
    return total

def dg_eval(mu, n, z, i):
    """partial_i g (z)."""
    total = 0.0
    for s in range(1 << n):
        if not ((s >> i) & 1) or mu[s] == 0.0:
            continue
        prod = 1.0
        for k in range(n):
            if k != i and ((s >> k) & 1):
                prod *= z[k]
        total += mu[s] * prod
    return total

def ddg_eval(mu, n, z, i, j):
    """partial_i partial_j g (z), i != j."""
    total = 0.0
    bi, bj = (1 << i), (1 << j)
    for s in range(1 << n):
        if (s & bi) == 0 or (s & bj) == 0 or mu[s] == 0.0:
            continue
        prod = 1.0
        for k in range(n):
            if k != i and k != j and ((s >> k) & 1):
                prod *= z[k]
        total += mu[s] * prod
    return total

def rayleigh_diff(mu, n, z, i, j):
    """Delta_ij(x) = d_i g * d_j g - g * d_i d_j g."""
    return dg_eval(mu, n, z, i) * dg_eval(mu, n, z, j) - g_eval(mu, n, z) * ddg_eval(mu, n, z, i, j)

# ----------------------------------------------------------------------------------------
# SR membership probe (numerical) + violation witness
# ----------------------------------------------------------------------------------------

# 🔴 CORRECTED 2026-06-21 (round-3 / N4): real stability (STRONGLY RAYLEIGH) requires Delta_ij >= 0 on
# ALL of R^n, NOT just the positive orthant. The old positive-orthant grid tested only the WEAKER RAYLEIGH
# property and misclassified Rayleigh-but-not-SR distributions (e.g. mu_4) as SR. We now probe all reals.
_GRID_1D_POS = np.array([0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 10.0])                    # positive orthant (Rayleigh)
_GRID_1D_REAL = np.array([-10.0, -2.0, -1.0, -0.5, -0.1,
                          0.1, 0.5, 1.0, 2.0, 10.0])                             # all reals (SR), trimmed
                                                                                 # + random signed points

def _margin_over_grid(mu, n, grid1d, rng, n_random, signed):
    """min over i<j and over grid+random x of Delta_ij(x). signed=True samples random x over R^n
    (random sign); signed=False over R_+^n only."""
    pairs = list(itertools.combinations(range(n), 2))
    best = np.inf
    witness = None
    for z in itertools.product(grid1d, repeat=n):
        z = np.array(z)
        for (i, j) in pairs:
            val = rayleigh_diff(mu, n, z, i, j)
            if val < best:
                best, witness = val, (i, j, z.copy())
    if rng is not None and n_random > 0:
        for _ in range(n_random):
            mag = np.exp(rng.uniform(np.log(1e-2), np.log(1e2), size=n))
            z = mag * (rng.choice([-1.0, 1.0], size=n) if signed else 1.0)
            for (i, j) in pairs:
                val = rayleigh_diff(mu, n, z, i, j)
                if val < best:
                    best, witness = val, (i, j, z.copy())
    return best, witness

def sr_margin(mu, n, rng=None, n_random=400, tol=1e-9):
    """SR (real-stability) margin: min Delta_ij over ALL real x (grid + random, random sign).
    margin >= -tol => SR (numerically); margin < -tol => witness (i,j,x*) certifies non-SR.
    🔴 Probes all of R^n (corrected): this is the STRONGLY-RAYLEIGH test, not the orthant Rayleigh test."""
    return _margin_over_grid(mu, n, _GRID_1D_REAL, rng, n_random, signed=True)

def rayleigh_margin(mu, n, rng=None, n_random=400):
    """RAYLEIGH margin: min Delta_ij over the POSITIVE ORTHANT only (the weaker property). Kept so C0 can
    report Rayleigh-vs-SR and surface Rayleigh-but-not-SR instances (margin_rayleigh>=0 but margin_sr<0)."""
    return _margin_over_grid(mu, n, _GRID_1D_POS, rng, n_random, signed=False)

def is_sr(mu, n, rng=None, tol=1e-7):
    m, _ = sr_margin(mu, n, rng=rng)
    return m >= -tol

# ----------------------------------------------------------------------------------------
# moments, conditioning, candidate statistics
# ----------------------------------------------------------------------------------------

def marginal(mu, n, i):
    return sum(mu[s] for s in range(1 << n) if (s >> i) & 1)

def pair_prob(mu, n, i, j):
    return sum(mu[s] for s in range(1 << n) if ((s >> i) & 1) and ((s >> j) & 1))

def cov(mu, n, i, j):
    return pair_prob(mu, n, i, j) - marginal(mu, n, i) * marginal(mu, n, j)

def condition(mu, n, fixed):
    """fixed: dict coord->0/1. Returns (mu_cond, mass) or (None, 0) if zero-prob."""
    mask = 0
    val = 0
    for k, v in fixed.items():
        mask |= (1 << k)
        if v:
            val |= (1 << k)
    out = np.zeros_like(mu)
    mass = 0.0
    for s in range(1 << n):
        if (s & mask) == val:
            out[s] = mu[s]
            mass += mu[s]
    if mass <= 1e-15:
        return None, 0.0
    return out / mass, mass

def _other_coords(n, i, j):
    return [k for k in range(n) if k != i and k != j]

def S1(mu, n, min_mass=1e-6):
    """Worst (most positive) conditional pairwise covariance over all subcube conditionings.
    SR => S1 <= 0 (SR is CNA+, conditional negative association). SUBCOND-estimable."""
    worst = -np.inf
    arg = None
    for (i, j) in itertools.combinations(range(n), 2):
        others = _other_coords(n, i, j)
        # condition on every subset T of others, every 0/1 assignment (T = empty included)
        for r in range(len(others) + 1):
            for T in itertools.combinations(others, r):
                for assign in itertools.product((0, 1), repeat=len(T)):
                    fixed = {T[t]: assign[t] for t in range(len(T))}
                    mc, mass = condition(mu, n, fixed)
                    if mc is None or mass < min_mass:
                        continue
                    c = cov(mc, n, i, j)
                    if c > worst:
                        worst = c
                        arg = (i, j, dict(fixed))
    return worst, arg

def _prod_indicator(mu, n, idxset):
    """E[ prod_{i in idxset} x_i ] = P(all those coords =1)."""
    mask = 0
    for i in idxset:
        mask |= (1 << i)
    return sum(mu[s] for s in range(1 << n) if (s & mask) == mask)


def cov_products(mu, n, A, B):
    """Cov( prod_{i in A} x_i , prod_{j in B} x_j ) for DISJOINT A,B.
    x_A := prod x_i is a non-decreasing function of coords A; SR => NA => this Cov <= 0 (a SIGN-CONSTRAINED
    necessary condition for SR, order |A|+|B|)."""
    eAB = _prod_indicator(mu, n, list(A) + list(B))
    eA = _prod_indicator(mu, n, A)
    eB = _prod_indicator(mu, n, B)
    return eAB - eA * eB


def S3(mu, n, min_mass=1e-6):
    """Sign-constrained ORDER-4 NA witness: worst (most positive) Cov(x_i x_j, x_k x_l) over disjoint
    pairs {i,j},{k,l} and over conditionings on the remaining coords. SR => NA => S3 <= 0 (one-sided,
    unlike S2). SUBCOND-estimable. Needs n>=4. A positive value certifies non-SR via an NA violation."""
    if n < 4:
        return 0.0, None
    coords = list(range(n))
    worst = -np.inf
    arg = None
    for A in itertools.combinations(coords, 2):
        rest = [c for c in coords if c not in A]
        for B in itertools.combinations(rest, 2):
            others = [c for c in coords if c not in A and c not in B]
            # condition on every subset of the remaining coords (incl. empty)
            for r in range(len(others) + 1):
                for T in itertools.combinations(others, r):
                    for assign in itertools.product((0, 1), repeat=len(T)):
                        fixed = {T[t]: assign[t] for t in range(len(T))}
                        mc, mass = condition(mu, n, fixed)
                        if mc is None or mass < min_mass:
                            continue
                        c = cov_products(mc, n, A, B)
                        if c > worst:
                            worst = c
                            arg = (A, B, dict(fixed))
    return (worst if worst > -np.inf else 0.0), arg


def S2(mu, n, min_mass=1e-6):
    """Conditional second-order (triple) discrepancy a pairwise statistic cannot see:
    max_{i,j,k} | Cov_{mu|x_k=1}(x_i,x_j) - Cov_{mu|x_k=0}(x_i,x_j) |. SUBCOND-estimable. n>=3."""
    if n < 3:
        return 0.0, None
    worst = -np.inf
    arg = None
    for (i, j) in itertools.combinations(range(n), 2):
        for k in range(n):
            if k == i or k == j:
                continue
            m1, mass1 = condition(mu, n, {k: 1})
            m0, mass0 = condition(mu, n, {k: 0})
            if m1 is None or m0 is None or mass1 < min_mass or mass0 < min_mass:
                continue
            d = abs(cov(m1, n, i, j) - cov(m0, n, i, j))
            if d > worst:
                worst = d
                arg = (i, j, k)
    return (worst if worst > -np.inf else 0.0), arg

# ----------------------------------------------------------------------------------------
# distance-to-SR lower bounds (the two honest lemmas; see preregistration.md)
# ----------------------------------------------------------------------------------------

def dist_lb_L1(mu, n):
    """Lemma C0-L1: if some Cov_mu(x_i,x_j) = delta > 0, dist_1(mu, SR) >= delta/3."""
    worst = max(cov(mu, n, i, j) for (i, j) in itertools.combinations(range(n), 2))
    return max(0.0, worst) / 3.0, worst

def dist_lb_L2(mu, n, witness):
    """Lemma C0-L2: at fixed witness x*, dist_1(mu,SR) >= delta / L(x*),
    delta = -Delta_ij(g_mu)(x*) (>0 for a violator), L(x*) = max ell_inf gradient of mu -> Delta_ij(x*)
    over the simplex (computed explicitly, not assumed)."""
    if witness is None:
        return 0.0, 0.0, 0.0
    i, j, z = witness
    delta = -rayleigh_diff(mu, n, z, i, j)
    if delta <= 0:
        return 0.0, delta, 0.0
    # Delta_ij(x*) as a function of mu is quadratic: sum_{s,t} mu[s] mu[t] Q[s,t] - linear? Actually
    # Delta = (d_i g)(d_j g) - g (d_i d_j g) is a quadratic form mu^T M mu with M[s,t] from monomials.
    # Gradient wrt mu is 2 M mu; ell_inf-Lipschitz const over simplex <= max_s |(2 M mu)_s| bounded by
    # 2 * max_{s,t} |M[s,t]|. We bound L = 2 * max_{s,t}|M[s,t]| using monomial values at x*.
    N = 1 << n
    # monomial value m_s(x*) = prod_{k in s} z_k ; d_i monomial = m_{s}/z_i if i in s else 0, etc.
    def mon(s):
        p = 1.0
        for k in range(n):
            if (s >> k) & 1:
                p *= z[k]
        return p
    bi, bj = (1 << i), (1 << j)
    a = np.array([mon(s) / z[i] if (s & bi) else 0.0 for s in range(N)])   # d_i g coeff vector
    b = np.array([mon(s) / z[j] if (s & bj) else 0.0 for s in range(N)])   # d_j g coeff vector
    gv = np.array([mon(s) for s in range(N)])                              # g coeff vector
    h = np.array([mon(s) / (z[i] * z[j]) if (s & bi) and (s & bj) else 0.0 for s in range(N)])  # d_idj g
    # Delta(mu) = (a.mu)(b.mu) - (g.mu)(h.mu) = mu^T M mu with M = sym(a b^T - g h^T)
    M = 0.5 * (np.outer(a, b) + np.outer(b, a) - np.outer(gv, h) - np.outer(h, gv))
    L = 2.0 * np.max(np.abs(M))
    if L <= 0:
        return 0.0, delta, L
    return delta / L, delta, L

# ----------------------------------------------------------------------------------------
# distribution builders
# ----------------------------------------------------------------------------------------

def product_dist(n, p):
    """SR by construction: independent Bernoulli(p_i). g factorizes -> real stable."""
    mu = np.zeros(1 << n)
    for s in range(1 << n):
        prob = 1.0
        for i in range(n):
            prob *= p[i] if ((s >> i) & 1) else (1 - p[i])
        mu[s] = prob
    return mu

def make_F1(n, p, delta_mass, i=0, j=1):
    """Positive-correlation perturbation of a product (SR) dist: move mass to aligned (x_i=x_j)
    states from anti-aligned states. Creates Cov(x_i,x_j) > 0 -> far by C0-L1."""
    mu = product_dist(n, p).copy()
    bi, bj = (1 << i), (1 << j)
    aligned = [s for s in range(1 << n) if ((s & bi) != 0) == ((s & bj) != 0)]
    anti = [s for s in range(1 << n) if ((s & bi) != 0) != ((s & bj) != 0)]
    take = min(delta_mass, sum(mu[s] for s in anti) * 0.9)
    # remove proportionally from anti, add proportionally to aligned
    anti_tot = sum(mu[s] for s in anti)
    al_tot = sum(mu[s] for s in aligned)
    for s in anti:
        mu[s] -= take * mu[s] / anti_tot
    for s in aligned:
        mu[s] += take * mu[s] / al_tot
    mu = np.clip(mu, 0, None)
    return mu / mu.sum()
