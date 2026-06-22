# Round-13 audit — Pro's NR-rate (regularization + sharp PB separation + class rates) — 2026-06-21

> Independent adversarial agent (symbolic + 300k-sample numeric + literature) + referee. **All claims
> CORRECT (no FATAL/GAP in the proofs).** The audit's decisive open computation (μ_4) was answered in
> parallel by the orchestrator — see the convergence note. Lean: **R+** (strengthening).

## Verdicts
- **Thm 1.1 (regularization): CORRECT** + resolves degeneracy. Composed params `δ+(1−2δ)s_i∈[δ,1−δ]`;
  per-coord flip `=δ`; rank-law TV `≤dδ`; tiny-slope removal `≤dδ`. `NR_δ ≥ NR−dδ` (additive). ⟹ any poly
  defect has a poly-magnitude bounded witness. **The channel-degeneracy doubt is closed.**
- **Thm 2.1 (sharp PB separation): CORRECT.** `u_j=a·e_j`, `Φ(u)=a²(4e_2−e_1²)` (symbolic); the key
  inequality `e_1³+9e_3≥4e_1e_2` ⟹ `w^{3/2}≤9e_3` ⟹ `Φ(u)_+^{3/2}≤9u_{≥3}` holds for **all** `d` (300k
  numeric, min slack ≥0) — a genuine `d`-variable elementary-symmetric inequality (not literally 3-var
  Schur, but TRUE); `|Φ(q)−Φ(u)|≤8Δ≤10Δ`; final `Φ(q)<14.33 Δ^{2/3}<15Δ^{2/3}`. **3/2 exponent forced +
  matches the verified sharpness.**
- **Thm 3.1 (covariance witness): CORRECT.** `Cov(U',V')=(½)²κ=κ/4`; rank on `{0,1,2}` with `Φ=κ` (referee
  ✓) ⟹ Thm 2.1. **Caveat VALID:** needs a *positive* Boolean conditional covariance; Rayleigh-not-SR can
  have all cond. covariances ≤0 ⟹ §3 does NOT settle the general case.
- **Thm 4.1 (product-children rate): CORRECT.** `I₀≤2m√κ ⟹ NR≥I₀³/(8·15^{3/2}m³)`; constant exact
  (`(60)^{3/2}=464.76`); α=1/3, P=poly(d).
- **Thm 5.1 (homogeneous search): CORRECT + correctly downgraded.** ALOV gap `≥1/k` confirmed; Poincaré
  localization + first-moment-reversal sound; link channel `Φ=4Cov(B,Z)=t/2` (symbolic). **(5d) the
  search-vs-bound downgrade is the right call** — `h_S^*` is synthesized (separate-branch queries + remix),
  need not equal the true conditional, so it's a SUBCOND-**search** theorem, NOT an `NR(h)` bound; **but it
  still yields a tester for the homogeneous-selector class** (the model grants separate-branch queries). The
  gap does not break the algorithm, only the reinterpretation as an `NR(h)` bound.
- **Claim 6 (residual (34)): fairly stated.** §2–4 convert any *degree-2* PB defect (`4q_0q_2−q_1²`) into a
  witness + Thm 1.1 removes degeneracy; a nonproduct nonhomogeneous `h` could fail SR through a *higher* PF
  minor with no degree-2 covariance signature — (34) is exactly "this can't happen at super-poly cost." An
  honest "same Schur/PF hardness one level up." **R− threat (open in the audit): a Rayleigh-not-SR family
  with NO positive cond. covariance AND all bounded-channel noisy ranks super-poly-close to PB.**

## 🔑 CONVERGENCE: the audit's "decisive next computation" = the orchestrator's parallel finding
The audit explicitly flagged: *"the one computation to do before claiming R+ is to search μ_4's conditional
covariances and bounded-channel noisy ranks"* (it lacked μ_4's definition). **Orchestrator did exactly this
(see `round13_pro_response.md` referee finding):** μ_4 has worst Boolean conditional covariance `=0` (evades
Thm 3.1 / §3) **BUT is caught by a bounded channel `(0.1,0.55)`** (noisy-rank complex roots `−1.90±0.72j`,
non-PB, CONSTANT margin). ⟹ **μ_4 is NOT an R− instance** — the hardest known higher-order (Rayleigh-not-SR)
obstruction is exposed by the second branch of (34) (the higher Toeplitz/PF minor), with constant margin.
**This directly defuses the audit's 40% R− weight and is strong concrete evidence (34) holds.**

## Net + lean
All proofs CORRECT; the only open item is the GENERAL (34) (degree-≥3 PF defect ⟹ bounded-channel
footprint), now **strongly supported** by the μ_4 computation. **Lean: R+** (audit said ≈60/40 *before*
the μ_4 result; with μ_4 caught, the decisive R− candidate is gone ⟹ ~70/30 R+). **Decisive next step:
prove (34) in general** (the higher-order local-to-global), or find a *spread* nonproduct family whose
higher-PF defect evades ALL bounded channels (the remaining R− hope, now narrower).
