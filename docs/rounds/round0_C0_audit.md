# Round-0 C0 de-risking audit (independent fresh-context agent) — 2026-06-20

> Phase-0 C0 setup audit (guide §9/§12). NOT an attack-loop audit (no attacker reply yet). Archived for
> the record. Subject: `derisk/preregistration.md`, `derisk/sr_core.py`, `derisk/run_c0.py`,
> `derisk/results/c0_results.json`.

## Verdict: NO FATAL. Lean ("no clean low-order local handle") = QUALIFIED YES (honestly supported, was
mildly over-claimed on generality; corrected in `ledger §7`).

## Verified correct
- Brändén multiaffine real-stability criterion (Rayleigh-difference ≥ 0 on ℝ₊ⁿ) — stated correctly.
- Grid SR test directionality — a found violation is an *exact* non-SR witness (can only false-accept,
  never false-reject); SR baseline uses the full fine-grid + random check, so non-SR cannot leak in.
- Distance lemma **C0-L1** (Cov 3-Lipschitz in ℓ₁, SR⇒Cov≤0 ⇒ dist₁≥δ/3) — correct.
- Distance lemma **C0-L2** (Δ_ij(x*) exactly quadratic in μ; `L=2·max|M|` a valid ℓ₁→value Lipschitz
  constant ⇒ dist₁≥δ/L) — verified analytically + numerically (loose but sound lower bound).
- Tensoring (non-SR ⊗ independent Bernoulli = non-SR; S1,S2 preserved) — correct.
- Moments / conditioning / S1 / S2 — no sign or masking bug.

## Findings folded into `ledger §7`
- **GAP-1 (key):** `S2` is sign-agnostic (SR does not force S2≈0) → its non-separation is weaker evidence.
  Robust core = **H2** (`S1`, a sign-constrained SR-necessary condition, is provably blind to F2). Added a
  **sign-constrained order-4 witness `S3`** (`Cov(x_ix_j,x_kx_l)≤0` under SR) for a fair test.
- **GAP-2:** n=4 SR baseline degenerate (products only) → n=4 H3 unreliable. Flagged.
- **GAP-3:** n=4 F2 were tensor-duplicates of n=3 → no independent evidence. Flagged; added a genuine
  (non-tensored) n=4 search (which was search-limited → count≈0; reported honestly).
- **MINOR-1:** raw Rayleigh margins are unnormalized (scale with zⁿ) → use `dist_lb`, not raw margin.
- MINOR-2/3: H3 thresholds; harmless (n=3 overlap robust to threshold choice).

## Most important fix (adopted)
Lead the lean with the robust, audited **H2 (n=3)**; treat H3/S2 as suggestive-only; keep the order-4
(S3) / genuine-n=4 question explicitly OPEN (search-limited) rather than claiming "no handle exists".
Recommended post-Phase-0: a smarter n=4 NA-but-not-SR construction to test S3 on genuine instances.
