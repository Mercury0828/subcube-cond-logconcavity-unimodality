"""
symmetry_break.py (round-7 de-risk; engineering). Attacks the SHARPENED CRUX:
can the symmetry of an "evade-(i)+(ii)+far" measure be BROKEN?
- (i)  evade conditional pairwise covariances: every Boolean conditional Cov(x_i,x_j|x_T=rho) <= tol.
- (ii) evade bounded marginals: every O(1) conditional marginal is SR  (we test all conditional pairwise
       marginals SR via (i); plus all unconditioned <=3-marginals SR).
- far: not SR (corrected all-R test), with margin clearly < 0.
Start from a symmetric N5 measure (far-from-SR, evades (i)+(ii)). Add random ASYMMETRIC perturbations and
count how many still evade (i)+(ii) and stay far. If MANY survive -> symmetry breakable -> route (B).
If perturbations reliably break (i) or (ii) -> evidence symmetry essential -> route (A).
"""
import numpy as np, itertools, sr_core as C

SEED = 20260621
rng = np.random.default_rng(SEED)
n = 6

def sym_measure(a):
    mu = np.array([a[bin(s).count('1')] for s in range(1 << n)], float)
    return mu / mu.sum()

# N5 symmetric rank weights (per-subset weight a_{|S|}); global rank poly far-from-real-rooted
A = [0.5085, 0.78987, 1.0, 0.93066, 0.53687, 0.2272, 0.05883]

def worst_cond_pair_cov(mu, min_mass=1e-7):
    worst = 0.0
    for i, j in itertools.combinations(range(n), 2):
        others = [k for k in range(n) if k != i and k != j]
        for r in range(len(others) + 1):
            for T in itertools.combinations(others, r):
                for asg in itertools.product((0, 1), repeat=len(T)):
                    fixed = {T[t]: asg[t] for t in range(len(T))}
                    mc, mass = C.condition(mu, n, fixed)
                    if mc is None or mass < min_mass:
                        continue
                    worst = max(worst, C.cov(mc, n, i, j))   # most-positive conditional covariance
    return worst   # <=tol  => evades (i)

def evades_i(mu, tol=1e-6):
    return worst_cond_pair_cov(mu) <= tol

def far_from_sr(mu, thr=1e-3):
    m, _ = C.sr_margin(mu, n, rng=rng, n_random=150)
    return m < -thr, m

def main():
    mu0 = sym_measure(A)
    ev_i0 = evades_i(mu0)
    far0, m0 = far_from_sr(mu0)
    print("=== symmetry-break experiment (n=%d, seed %d) ===" % (n, SEED))
    print("base symmetric N5: evades(i)=%s  far_from_SR=%s (sr_margin=%.4f)" % (ev_i0, far0, m0))

    # random ASYMMETRIC perturbations (NOT a function of |S|), small, keep nonneg
    survive_both = 0
    broke_i = 0
    notfar = 0
    trials = 60
    for t in range(trials):
        d = rng.normal(size=1 << n)
        d -= d.mean()
        eps = rng.uniform(0.02, 0.12)
        mu = mu0 + eps * d / (np.abs(d).max() + 1e-12)
        if (mu < 0).any():
            continue
        mu = mu / mu.sum()
        # is it asymmetric? (it is, generically)
        if not evades_i(mu):
            broke_i += 1
            continue
        far, m = far_from_sr(mu)
        if not far:
            notfar += 1
            continue
        survive_both += 1   # asymmetric, evades (i), still far-from-SR
    print("perturbations: trials~%d | broke (i)=%d | evade(i)-but-not-far=%d | "
          "SURVIVE (asym, evade(i), far)=%d" % (trials, broke_i, notfar, survive_both))
    if survive_both > 0:
        print("=> SYMMETRY BREAKABLE in this probe: non-symmetric evade-(i)+far measures exist "
              "(route (B) candidates). [Still must verify evade-(ii) marginals + build the query lower bound.]")
    else:
        print("=> in this probe, every asymmetric perturbation either broke (i) or stopped being far "
              "=> mild evidence symmetry is hard to break (leans route (A) combined-tester completeness).")

if __name__ == "__main__":
    main()
