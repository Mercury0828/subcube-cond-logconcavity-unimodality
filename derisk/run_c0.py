"""
run_c0.py — execute the pre-registered C0 lean (derisk/preregistration.md). FIXED SEED.
Writes results/c0_results.json + prints a summary. NOT a proof; a directional lean only.

Experiment:
  H1: S1 separates SR from F1 (positive-correlation far instances).         [sanity]
  H2: S1 does NOT separate SR from F2 (pairwise-neg-correlated but not SR).  [the CS3 blindness]
  H3: does S2 (a bounded-order conditional proxy) separate F2 from genuine SR, scaling with delta_Delta?
      YES -> lean: local handle plausible (attack C1). NO (falsifier) -> lean: handle likely absent.
"""
import json
import os
import numpy as np
import itertools
import sr_core as C

SEED = 20260620
OUT = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(OUT, exist_ok=True)


def fast_margin(mu, n):
    """cheaper margin probe used during F2 search (coarse grid, no random)."""
    grid = np.array([0.2, 0.5, 1.0, 2.0, 5.0])
    best = np.inf
    wit = None
    for z in itertools.product(grid, repeat=n):
        z = np.array(z)
        for (i, j) in itertools.combinations(range(n), 2):
            v = C.rayleigh_diff(mu, n, z, i, j)
            if v < best:
                best, wit = v, (i, j, z.copy())
    return best, wit


def sample_sr_rigorous(n, rng, k=40):
    """Genuine SR instances, RIGOROUSLY verified (full fine-grid + random margin >= +thr), to avoid
    contaminating the SR baseline with hidden near-boundary non-SR instances. Includes pure products
    (exactly SR; S2 anchor ~0) and verified-SR perturbations. Returns (mu, S1, S2, margin)."""
    out = []
    tries = 0
    # a few pure products as clean anchors
    for _ in range(min(6, k)):
        p = rng.uniform(0.2, 0.8, size=n)
        mu = C.product_dist(n, p)
        m, _ = C.sr_margin(mu, n, rng=rng, n_random=200)
        s1, _ = C.S1(mu, n)
        s2, _ = C.S2(mu, n)
        out.append((mu, float(s1), float(s2), float(m)))
    while len(out) < k and tries < 6000:
        tries += 1
        p = rng.uniform(0.15, 0.85, size=n)
        mu = C.product_dist(n, p)
        d = rng.normal(size=1 << n)
        d -= d.mean()
        mu2 = mu + rng.uniform(0.0, 0.18) * d / (np.abs(d).max() + 1e-12)
        if (mu2 < 0).any():
            continue
        mu2 = mu2 / mu2.sum()
        if fast_margin(mu2, n)[0] < 5e-4:        # cheap reject
            continue
        m, _ = C.sr_margin(mu2, n, rng=rng, n_random=300)  # RIGOROUS verify
        if m >= 1e-4:                             # genuinely SR with margin
            s1, _ = C.S1(mu2, n)
            s2, _ = C.S2(mu2, n)
            out.append((mu2, float(s1), float(s2), float(m)))
    return out


def search_F2(n, rng, k=40):
    """F2: pairwise-neg-correlated (S1 <= tol, invisible to the pairwise/NA handle) but NOT SR
    (interior Rayleigh violation). Guided random search from the product (SR, S1=0) point."""
    out = []
    tries = 0
    base = C.product_dist(n, np.full(n, 0.5))
    while len(out) < k and tries < 60000:
        tries += 1
        d = rng.normal(size=1 << n)
        d -= d.mean()
        t = rng.uniform(0.02, 0.5)   # wider range -> also reach more-far (larger-margin) F2
        mu = base + t * d / (np.abs(d).max() + 1e-12)
        if (mu < -1e-12).any():
            continue
        mu = np.clip(mu, 0, None)
        mu = mu / mu.sum()
        s1, _ = C.S1(mu, n)
        if s1 > 1e-6:            # must be invisible to the pairwise/NA handle
            continue
        m, wit = fast_margin(mu, n)
        if m < -1e-3:           # must be a genuine interior non-SR violator
            s2, _ = C.S2(mu, n)
            # full-precision margin + witness for the honest distance bound
            mfull, witf = C.sr_margin(mu, n, rng=rng, n_random=300)
            lb2, delta2, L2 = C.dist_lb_L2(mu, n, witf)
            # is the witness x* near the all-ones vertex (=pairwise) or interior?
            i, j, z = witf
            interiorness = float(np.min(np.abs(np.log(z))))  # 0 => some coord at 1 (vertex-ish)
            out.append((mu, float(s1), float(s2), float(mfull),
                        float(lb2), float(delta2), float(L2), float(interiorness)))
    return out, tries


def tensor_with_bernoulli(mu3, n3, q):
    """Lift an n-var dist to (n+1)-var by an INDEPENDENT Bernoulli(q) coordinate (new coord = index n3).
    g_{mu (x) Bern} = g_mu * (1-q + q z_{new}); a stable affine factor does NOT fix a bad root of g_mu,
    so a non-SR mu3 lifts to a non-SR mu4; the new coord is independent so S1 (conditional pairwise
    covariances among original coords) is unchanged and covs touching the new coord are 0."""
    n4 = n3 + 1
    mu4 = np.zeros(1 << n4)
    for s in range(1 << n3):
        mu4[s] += mu3[s] * (1 - q)          # new coord = 0
        mu4[s | (1 << n3)] += mu3[s] * q     # new coord = 1
    return mu4 / mu4.sum()


def make_F2_tensor(f2_mus_n3, n3, rng, k=12):
    """n=4 F2 instances built by tensoring n=3 F2 mus with an independent Bernoulli (guaranteed non-SR,
    S1<=0 preserved). Returns the same tuple shape as search_F2."""
    out = []
    if not f2_mus_n3:
        return out
    n4 = n3 + 1
    for idx in range(k):
        mu3 = f2_mus_n3[idx % len(f2_mus_n3)]
        q = float(rng.uniform(0.2, 0.8))
        mu = tensor_with_bernoulli(mu3, n3, q)
        s1, _ = C.S1(mu, n4)
        s2, _ = C.S2(mu, n4)
        mfull, witf = C.sr_margin(mu, n4, rng=rng, n_random=250)
        lb2, delta2, L2 = C.dist_lb_L2(mu, n4, witf)
        i, j, z = witf
        interiorness = float(np.min(np.abs(np.log(z))))
        out.append((mu, float(s1), float(s2), float(mfull), float(lb2),
                    float(delta2), float(L2), float(interiorness)))
    return out


def n4_S3_probe(rng, k_sr=16, k_f2=16, budget=120000):  # frozen results.json used budget=120000
    """FAIR order-4 probe at n=4 (addresses audit GAP-1/2/3): a SIGN-CONSTRAINED order-4 NA witness S3
    (SR => S3 <= 0). Clean SR baseline (small verified perturbations, S3 ~<=0) vs GENUINE (non-tensored)
    n=4 F2 (S1 <= 0, non-SR). Questions: (i) does S3>0 detect F2 that S1 misses? (ii) do there exist F2
    with S1<=0 AND S3<=0 (NA up to order 4 yet non-SR) -- the killer falsifier?"""
    n = 4
    # clean SR baseline
    sr = []
    tries = 0
    for _ in range(6):
        p = rng.uniform(0.25, 0.75, size=n)
        mu = C.product_dist(n, p)
        s3, _ = C.S3(mu, n)
        sr.append((float(C.S1(mu, n)[0]), float(C.S2(mu, n)[0]), float(s3)))
    while len(sr) < k_sr and tries < 8000:
        tries += 1
        p = rng.uniform(0.2, 0.8, size=n)
        mu = C.product_dist(n, p) + 0.04 * (lambda d: d - d.mean())(rng.normal(size=1 << n)) \
            / (np.abs(rng.normal(size=1 << n)).max() + 1.0)
        if (mu < 0).any():
            continue
        mu = mu / mu.sum()
        if fast_margin(mu, n)[0] < 5e-4:
            continue
        if C.sr_margin(mu, n, rng=rng, n_random=150)[0] >= 1e-4:
            sr.append((float(C.S1(mu, n)[0]), float(C.S2(mu, n)[0]), float(C.S3(mu, n)[0])))
    # genuine n=4 F2: S1 <= 0 and non-SR
    f2 = []
    base = C.product_dist(n, np.full(n, 0.5))
    b = 0
    while len(f2) < k_f2 and b < budget:
        b += 1
        d = rng.normal(size=1 << n); d -= d.mean()
        mu = base + rng.uniform(0.03, 0.45) * d / (np.abs(d).max() + 1e-12)
        if (mu < -1e-12).any():
            continue
        mu = np.clip(mu, 0, None); mu = mu / mu.sum()
        # fast pre-filter: all UNCONDITIONAL pairwise covs <= 0 (cheap; most perturbations fail here)
        if max(C.cov(mu, n, i, j) for (i, j) in itertools.combinations(range(n), 2)) > 1e-6:
            continue
        if C.S1(mu, n)[0] > 1e-6:      # full filter: invisible to pairwise/NA over ALL conditionings
            continue
        m, _ = fast_margin(mu, n)
        if m < -1e-3:                  # genuine non-SR
            s3, _ = C.S3(mu, n)
            f2.append((float(C.S1(mu, n)[0]), float(C.S2(mu, n)[0]), float(s3), float(m)))
    return sr, f2, b


def make_F1_family(n, rng, k=12):
    out = []
    for _ in range(k):
        p = rng.uniform(0.25, 0.75, size=n)
        dm = rng.uniform(0.05, 0.2)
        mu = C.make_F1(n, p, dm, 0, 1)
        s1, _ = C.S1(mu, n)
        s2, _ = C.S2(mu, n)
        lb1, worstcov = C.dist_lb_L1(mu, n)
        m, _ = fast_margin(mu, n)
        out.append((float(s1), float(s2), float(m), float(lb1), float(worstcov)))
    return out


def summarize(name, vals):
    if not vals:
        return {"name": name, "count": 0}
    a = np.array(vals)
    return {"name": name, "count": len(vals),
            "min": float(a.min()), "median": float(np.median(a)),
            "mean": float(a.mean()), "max": float(a.max())}


def main():
    rng = np.random.default_rng(SEED)
    report = {"seed": SEED, "n_values": [3, 4]}

    f2_mus_n3 = []
    for n in (3, 4):
        rprt = {}
        sr = sample_sr_rigorous(n, rng, k=(40 if n == 3 else 24))
        f1 = make_F1_family(n, rng, k=12)
        f2, f2_tries = search_F2(n, rng, k=(40 if n == 3 else 16))
        if n == 3:
            f2_mus_n3 = [x[0] for x in f2]
        else:
            # augment the (sparse) random n=4 search with guaranteed tensored F2 instances
            tensored = make_F2_tensor(f2_mus_n3, 3, rng, k=12)
            rprt["F2_tensored_added"] = len(tensored)
            f2 = f2 + tensored

        rprt["SR_S1"] = summarize("SR.S1", [x[1] for x in sr])
        rprt["SR_S2"] = summarize("SR.S2", [x[2] for x in sr])
        rprt["F1_S1"] = summarize("F1.S1", [x[0] for x in f1])
        rprt["F1_dist_lb_L1"] = summarize("F1.distLB", [x[3] for x in f1])
        rprt["F2_found"] = len(f2)
        rprt["F2_search_tries"] = f2_tries
        rprt["F2_S1"] = summarize("F2.S1", [x[1] for x in f2])
        rprt["F2_S2"] = summarize("F2.S2", [x[2] for x in f2])
        rprt["F2_margin"] = summarize("F2.margin(<0=nonSR)", [x[3] for x in f2])
        rprt["F2_dist_lb_L2"] = summarize("F2.distLB", [x[4] for x in f2])
        rprt["F2_delta_Delta"] = summarize("F2.deltaDelta", [x[5] for x in f2])
        rprt["F2_witness_interiorness"] = summarize("F2.interiorness(0=vertex)", [x[7] for x in f2])

        # H3 read: does S2 separate F2 from genuine SR?
        sr_s2 = np.array([x[2] for x in sr]) if sr else np.array([0.0])
        f2_s2 = np.array([x[2] for x in f2]) if f2 else np.array([0.0])
        # product anchor: pure products are exactly SR -> S2 should be ~0
        prod_s2 = [x[2] for x in sr if abs(x[1]) < 1e-9 and abs(x[3]) < 1e-12]  # margin~0? no; products have margin>=0
        rprt["SR_product_anchor_S2_present"] = bool(len(sr) > 0)
        # F2-strong subset: the third of F2 with the most-negative margin (the "more far" instances)
        if len(f2) >= 3:
            f2_sorted = sorted(f2, key=lambda x: x[3])  # ascending margin (most negative first)
            strong = f2_sorted[: max(1, len(f2) // 3)]
            rprt["F2strong_margin"] = summarize("F2strong.margin", [x[3] for x in strong])
            rprt["F2strong_S1"] = summarize("F2strong.S1", [x[1] for x in strong])
            rprt["F2strong_S2"] = summarize("F2strong.S2", [x[2] for x in strong])
            rprt["F2strong_dist_lb_L2"] = summarize("F2strong.distLB", [x[4] for x in strong])
            dd = np.array([x[5] for x in f2]); s2arr = np.array([x[2] for x in f2])
            corr = float(np.corrcoef(s2arr, dd)[0, 1]) if np.std(s2arr) > 1e-12 and np.std(dd) > 1e-12 else 0.0
        else:
            corr = None
        rprt["H3_S2_corr_with_deltaDelta"] = corr
        rprt["H3_S2_SR_max"] = float(sr_s2.max())
        rprt["H3_S2_SR_median"] = float(np.median(sr_s2))
        rprt["H3_S2_F2_median"] = float(np.median(f2_s2))
        # separation criterion: F2 S2 clearly above the SR S2 range (no overlap) AND scales with delta
        rprt["H3_separates"] = bool(len(f2) > 0 and np.median(f2_s2) > 3 * sr_s2.max() + 1e-6
                                    and (corr is not None and corr > 0.6))

        report[f"n={n}"] = rprt

    # FAIR order-4 sign-constrained probe at n=4 (audit GAP-1/2/3 fix)
    sr4, f24, b4 = n4_S3_probe(rng)
    s3_sr = np.array([x[2] for x in sr4]) if sr4 else np.array([0.0])
    s3_f2 = np.array([x[2] for x in f24]) if f24 else np.array([0.0])
    s1_f2 = np.array([x[0] for x in f24]) if f24 else np.array([0.0])
    # killer subset: genuine F2 with S1<=0 AND S3<=0 (NA up to order 4 yet non-SR)
    killer = [x for x in f24 if x[0] <= 1e-6 and x[2] <= 1e-6]
    report["n4_S3probe"] = {
        "SR_count": len(sr4), "F2_count": len(f24), "search_budget_used": b4,
        "SR_S3": summarize("SR.S3(<=0 expected)", [x[2] for x in sr4]),
        "F2_S1": summarize("F2.S1(<=0 by filter)", [x[0] for x in f24]),
        "F2_S3": summarize("F2.S3", [x[2] for x in f24]),
        "F2_margin_raw": summarize("F2.margin(raw,unnormalized)", [x[3] for x in f24]),
        "S3_detects_F2_frac": float(np.mean(s3_f2 > 3 * (s3_sr.max() if sr4 else 0) + 1e-6)) if f24 else 0.0,
        "killer_count_S1andS3_le0_butNonSR": len(killer),
        "note": "S3 is sign-constrained (SR=>S3<=0), a FAIR order-4 NA witness; raw margins are NOT "
                "normalized and scale with z^n (audit MINOR-1).",
    }

    with open(os.path.join(OUT, "c0_results.json"), "w") as f:
        json.dump(report, f, indent=2)

    # human summary
    def g(d, key, default=float('nan')):
        v = d.get(key) if isinstance(d, dict) else None
        return default if v is None else v
    print("=== C0 lean summary (fixed seed %d) ===" % SEED)
    for n in (3, 4):
        r = report[f"n={n}"]
        print(f"\n-- n={n} --")
        print(f"  H1 (S1 separates F1):   SR.S1 max={g(r['SR_S1'],'max'):+.4f} | "
              f"F1.S1 min={g(r['F1_S1'],'min'):+.4f}  -> separated if F1.S1>>0 and SR.S1<=~0")
        print(f"  H2 (S1 blind to F2):    F2 found={r['F2_found']} | "
              f"F2.S1 max={g(r['F2_S1'],'max'):+.4f} (<=~0 => S1 cannot see F2)")
        print(f"  F2 are non-SR:          F2.margin median={g(r['F2_margin'],'median'):+.4f} (<0) | "
              f"dist_lb_L2 median={g(r['F2_dist_lb_L2'],'median'):.5f}")
        print(f"  F2 witness interiorness median={g(r['F2_witness_interiorness'],'median'):.3f} "
              f"(0=vertex/pairwise; >0=interior, invisible to subcube vertices)")
        if 'F2strong_S2' in r:
            print(f"  F2-strong (most-far 1/3): margin median={g(r['F2strong_margin'],'median'):+.4f} | "
                  f"S1 max={g(r['F2strong_S1'],'max'):+.4f} | S2 median={g(r['F2strong_S2'],'median'):+.4f}")
        print(f"  H3 (S2 separates F2):   SR.S2 max={r['H3_S2_SR_max']:+.4f} med={r['H3_S2_SR_median']:+.4f} | "
              f"F2.S2 median={r['H3_S2_F2_median']:+.4f} | S2~deltaDelta corr={r['H3_S2_corr_with_deltaDelta']}")
        print(f"     => H3_separates = {r['H3_separates']}  "
              f"(True: handle plausible | False: FALSIFIER, no clean low-order handle)")
    p = report["n4_S3probe"]
    print("\n-- n=4 FAIR order-4 sign-constrained probe (S3) --")
    print(f"  SR baseline: count={p['SR_count']} | SR.S3 max={g(p['SR_S3'],'max'):+.5f} "
          f"(expect <=~0; S3 is sign-constrained)")
    print(f"  genuine F2 (S1<=0, non-SR): count={p['F2_count']} (budget {p['search_budget_used']}) | "
          f"F2.S1 max={g(p['F2_S1'],'max'):+.5f}")
    print(f"  F2.S3: min={g(p['F2_S3'],'min'):+.5f} median={g(p['F2_S3'],'median'):+.5f} "
          f"max={g(p['F2_S3'],'max'):+.5f}  -> S3>0 means order-4 NA witness DETECTS this F2")
    print(f"  fraction of F2 detected by S3 (vs missed by S1): {p['S3_detects_F2_frac']:.2f}")
    print(f"  KILLER count (F2 with S1<=0 AND S3<=0, i.e. NA up to order 4 yet NON-SR): "
          f"{p['killer_count_S1andS3_le0_butNonSR']}")
    print("     => killer>0 : even an order-4 sign-constrained NA witness MISSES some non-SR (strong")
    print("        falsifier, lean: no clean low-order local handle).  killer=0 & S3 detects all : an")
    print("        order-4 NA witness suffices on these instances (handle more plausible at order 4).")
    print("\nWrote", os.path.join(OUT, "c0_results.json"))


if __name__ == "__main__":
    main()
