"""
windows_search.py  (round-4 de-risk; engineering, not a proof)

Symmetric/exchangeable reduction (Grace-Walsh-Szego): a symmetric measure with rank weights a=(a_0..a_n)
is SR (real stable) iff the GLOBAL polynomial P(t)=sum_k C(n,k) a_k t^k is REAL-ROOTED. Conditioning on
coordinates leaves a "window": conditioning all but m coords (with u of the conditioned coords =1) gives a
symmetric measure on m coords with poly  W_{u,m}(t)=sum_{j=0}^m C(m,j) a_{u+j} t^j. An O(1)-dim conditional
marginal is SR  <=>  a SHORT window (m<=k) is real-rooted.

QUESTION (the dichotomy, symmetric case): does there exist a nonneg rank sequence a with EVERY window of
size m<=k real-rooted (all bounded conditional marginals SR) but P NOT real-rooted (far-from-SR globally)?
- YES  -> the bounded-marginal handle (T''') is INCOMPLETE even for symmetric measures: a far-from-SR
          measure whose every O(k)-dim conditional marginal is SR (a "spread" violation) -> route (B) flavor.
          [Caveat: symmetric measures are estimable from n+1 rank probabilities, so a true SUBCOND lower
           bound needs a non-symmetric lift; this search only tests the local-to-global *real-rootedness*.]
- NO (provably) -> local (bounded-window) real-rootedness forces global -> route (A) for symmetric measures.

We also record HOW FAR from real-rooted P is (max |Im root|) as a crude proxy for distance-to-SR.
Fixed seed.
"""
import math
import numpy as np

SEED = 20260621
TOL = 1e-7

def real_rooted(coeffs, tol=TOL):
    """coeffs = [c_0, c_1, ..., c_d] (ascending). Real-rooted iff all roots real."""
    c = np.array(coeffs, dtype=float)
    # strip leading/trailing negligible high-degree terms
    while len(c) > 1 and abs(c[-1]) < 1e-14:
        c = c[:-1]
    if len(c) <= 1:
        return True, 0.0
    r = np.roots(c[::-1])  # np.roots wants highest degree first
    max_im = float(np.max(np.abs(r.imag)))
    return max_im < tol, max_im

def window(a, u, m):
    return [math.comb(m, j) * a[u + j] for j in range(m + 1)]

def global_poly(a):
    n = len(a) - 1
    return [math.comb(n, j) * a[j] for j in range(n + 1)]

def all_windows_real_rooted(a, k):
    n = len(a) - 1
    for m in range(2, k + 1):           # m=1 trivially real-rooted
        for u in range(0, n - m + 1):
            ok, _ = real_rooted(window(a, u, m))
            if not ok:
                return False
    return True

def proj_marginal_poly(a, r, m, w):
    """Symmetric measure, conditional leaving m coords with r ones has rank weights (a_r..a_{r+m});
    project to w<=m coords -> exchangeable on w coords with rank weights e_l prop sum_j a_{r+j} C(m-w,j-l).
    Return the marginal polynomial coeffs [e_l * C(w,l)] (SR <=> this real-rooted)."""
    e = []
    for l in range(w + 1):
        s = 0.0
        for j in range(l, l + (m - w) + 1):
            s += a[r + j] * math.comb(m - w, j - l)
        e.append(s)
    return [math.comb(w, l) * e[l] for l in range(w + 1)]

def all_bounded_marginals_real_rooted(a, k):
    """FULL bounded-marginal test (T'''): for EVERY Boolean conditioning leaving m coords with r ones,
    and EVERY projection to w<=k coords, the conditional-projected marginal is SR (real-rooted).
    (By SR-closure it suffices to also include w=m windows; we check all (r,m,w) with w<=k.)"""
    n = len(a) - 1
    for m in range(1, n + 1):                 # leave m coords
        for r in range(0, n - m + 1):         # r ones among the conditioned (n-m) coords
            for w in range(2, min(k, m) + 1): # project to w<=k coords (w=1 trivial)
                ok, _ = real_rooted(proj_marginal_poly(a, r, m, w))
                if not ok:
                    return False
    return True

def search(n, k, trials, rng, gen):
    """gen: callable -> a nonneg sequence of length n+1."""
    best = None
    for _ in range(trials):
        a = gen(n, rng)
        if any(x < 0 for x in a):
            continue
        if not all_bounded_marginals_real_rooted(a, k):   # FULL bounded-marginal test (cond + project)
            continue
        ok, max_im = real_rooted(global_poly(a))
        if not ok:                       # ALL bounded conditional+projected marginals SR but GLOBAL not
            if best is None or max_im > best[1]:
                best = (a, max_im)
    return best

# ---- generators (different shapes of candidate rank sequences) ----
def gen_lognormalish(n, rng):
    # log-concave-ish bumpy: exp of a concave-ish random walk + local bumps
    x = np.cumsum(rng.normal(0, 1, n + 1))
    x = x - np.maximum.accumulate(x) * 0.0     # keep raw
    x -= x.max()
    a = np.exp(x)
    return list(a)

def gen_two_bumps(n, rng):
    # two separated Gaussian bumps in the rank sequence: classic way to break global real-rootedness
    i1 = rng.integers(1, n // 2)
    i2 = rng.integers(n // 2, n)
    w1 = rng.uniform(0.5, 2.0); w2 = rng.uniform(0.5, 2.0)
    h2 = rng.uniform(0.3, 3.0)
    idx = np.arange(n + 1)
    a = np.exp(-((idx - i1) ** 2) / (2 * w1 ** 2)) + h2 * np.exp(-((idx - i2) ** 2) / (2 * w2 ** 2))
    return list(a)

def gen_perturbed_binomial(n, rng):
    # start from a real-rooted base (1+t)^n has a_k=1; perturb multiplicatively
    a = np.ones(n + 1) * np.exp(rng.normal(0, 0.6, n + 1))
    return list(a)

def main():
    rng = np.random.default_rng(SEED)
    print("=== windows -> global real-rootedness search (symmetric reduction) ===")
    gens = {"two_bumps": gen_two_bumps, "lognormalish": gen_lognormalish,
            "perturbed_binomial": gen_perturbed_binomial}
    any_found = False
    for n in (6, 8, 10, 12):
        for k in (2, 3, 4):
            for gname, gen in gens.items():
                best = search(n, k, 8000, rng, gen)
                if best is not None:
                    any_found = True
                    a, max_im = best
                    aa = [round(float(x), 5) for x in (np.array(a) / max(a))]
                    print(f"\nFOUND n={n} k={k} gen={gname}: all windows(m<={k}) real-rooted, "
                          f"GLOBAL NOT (max|Im root|={max_im:.4f})")
                    print(f"   rank seq a (normalized) = {aa}")
                    # report window-2 (log-concavity) holds:
                    print(f"   log-concave (window m=2 all real-rooted) = {all_windows_real_rooted(a, 2)}")
    if not any_found:
        print("\nNO counterexample found in the searched space "
              "(every all-windows-real-rooted sequence had P real-rooted) -> supports local=>global (route A) "
              "for symmetric measures, in this range.")
    print("\ndone")

if __name__ == "__main__":
    main()
