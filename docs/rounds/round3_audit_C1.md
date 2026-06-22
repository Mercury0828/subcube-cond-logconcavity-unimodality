# Round-3 Audit — C1 (μ_4 Rayleigh-not-SR; independent CAS + literature, 2026-06-21)

> Fresh-context agent: re-verified μ_4 by CAS (sympy), cross-checked the Rayleigh-vs-strongly-Rayleigh
> distinction against the literature, AND found a collateral bug in the C0 code. **The substrate
> correction (N4 / corrected P3) is CONFIRMED.**

## μ_4 verification: V1, V2, V3 all CORRECT (CAS)
- **V1 (Rayleigh on ℝ₊):** `AC−B² = −2y²z²−2y²z−2yz²−3yz−2y−2z−2` (exact match); `Δ_12=B²−AC>0` on `ℝ₊²`,
  independent of `z_1,z_2`; by symmetry `μ_4` is Rayleigh.
- **V2 (not real stable):** `g_4(t,t,t,t)=t⁴+8t³+12t²+8t+1`; `w=t+1/t=−4+√6≈−1.5505∈(−2,2)` ⟹ complex root
  `t₀=−0.7753+0.6316i` (Im>0), nroots confirms; diagonal `(t₀,…,t₀)` is an all-upper-half-plane root ⟹
  not real stable. Real-point witness: `Δ_12(z_3,z_4=−1,−1) = −1/900 < 0`.
- **V3 (constant-far):** per-point Lipschitz lower bound on `d_TV(·,SR)` is a sound mechanism; the lift
  `μ_4×Ber(½)^{⊗(n−4)}` stays non-SR (marginalization preserves SR, P1) and `Ω(1)`-far. **MINOR:** the
  exact constant `1/7200` not re-derived (mechanism robust; re-check the constant before freezing).

## Literature: Rayleigh ⊋ strongly Rayleigh is ESTABLISHED (not a hallucination)
- **Choe–Wagner "Rayleigh Matroids"** (arXiv:math/0307096): Rayleigh = `Δ≥0` for nonnegative (orthant) args.
- **Brändén–Wagner–Wei** (arXiv:1411.7735, Prop 4): the **strong Rayleigh property** needs `Δ_{e,f}(a)≥0`
  for **all `a∈ℝ^{E∖{e,f}}`**; `Z` stable ⇔ strong Rayleigh. Strict containment confirmed (HPP ⊊ Rayleigh).
- **BBL** (arXiv:0707.2340): SR ⇔ real stable; its Def-2.5 Rayleigh-difference characterization of *real
  stability* is the **all-real** condition — the project mis-transcribed it as "on `ℝ₊ⁿ`" (guide §5's
  "[0,1]^n"). n=4 Rayleigh-not-SR examples are consistent with the literature.

## 🔴 COLLATERAL FATAL BUG (caught by the audit) — the C0 oracle was a RAYLEIGH test
`derisk/sr_core.py` probed `Δ_ij` only on the positive orthant ⟹ `is_sr(μ_4)` returned **True** (margin
+0.0023) while `Δ_12(z,−1,−1)=−0.0011<0`. So **every Rayleigh-but-not-SR distribution was misclassified
SR**, contaminating the C0 "SR baseline" and the H2/H3 leans. **FIXED 2026-06-21** (`sr_core.sr_margin`
now probes all real `ℝⁿ`; added `rayleigh_margin` to report both); **C0 re-run in progress** — leans may
shift. *(F2 instances remain genuinely non-SR — they violate `Δ` on the positive orthant, so non-Rayleigh
⟹ non-SR; the contamination was only in the SR baseline.)*

## The round-2 "leans-toward-poly-tester" synthesis is KILLED
μ_4 is a **single** family blind to **both** {Boolean conditional pairwise covariances} **and** {all
positive-field tilted covariances} (both are orthant statistics; μ_4 is Rayleigh). So the round-2 claim
"complementary blind spots ⇒ jointly sufficient ⇒ poly tester" is **false** for covariance statistics.

## The make-or-break DICHOTOMY (now the central question)
The new handle is **conditional-marginal real-stability testing** (T‴). The decisive question:
> **Does a "hidden-high-dimensional off-orthant non-stability" family exist?** — a μ_4-style real-stability
> violation (off-orthant, invisible to all positive-field/Boolean covariances) **spread over `Ω(n)`
> coordinates** so that **no `O(1)`-dimensional conditional marginal exposes it** (à la parity μ_n's
> full-support obstruction N3, transplanted off-orthant).
- **If it EXISTS** (and defeats poly-query conditioning) ⟹ **super-polynomial SUBCOND lower bound /
  impossibility** = the genuine **RED-3** candidate (now much stronger: orthant statistics provably blind).
- **If provably NO such spreading is possible** ⟹ the conditional-marginal real-stability test is the
  **upper-bound** route (R+).
Both outcomes are SODA-grade. **This single dichotomy is make-or-break (round 4).**

## Round-4 direction (audit): repair substrate (DONE) → attack the dichotomy.
