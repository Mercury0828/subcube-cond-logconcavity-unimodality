# Round-8 audit — Pro's upper-bound machinery (§1–§5) — independent agent, 2026-06-21

> Fresh-context adversarial audit; all claims re-checked by sympy + literature. **Verdict: ALL FIVE CLAIMS
> CORRECT — no FATAL, no GAP.** Only MINOR caveats (already acknowledged by Pro).

## Per-claim verdict
- **Claim 1 (rank statistic universal): CORRECT.** (1a) `g_μ(t,…,t)` real-rooted via affine-substitution
  closure `z_i↦at+b`,`a≥0` (univariate real-stable=real-rooted). (1b) real-rooted nonneg-coeff PGF ⇔
  Poisson-binomial (Aissen–Edrei–Schoenberg–Whitney). (1c) data-processing direction re-derived correctly:
  `d_TV(rank μ, PB_n) ≤ d_TV(μ, SR)`. (1d) sympy: `1+8t+12t²+8t³+t⁴` has roots `−6.291, −0.159,
  −0.775±0.632i` → non-real-rooted → **μ_4 caught by the rank test**. MINOR: necessary, not sufficient
  (stated correctly by Pro).
- **Claim 2 (projective certificate): CORRECT.** Identity `Δ_ij(R_C g)(z)=(∏_{k∈C}z_k²)Δ_ij(g)(w)` verified
  symbolically (`LHS−RHS=0` exactly); `Δ_ij` independent of `z_i,z_j` confirmed; `g` real stable ⟺ `V(g)=0`.
- **Claim 3 (robust tester Thm 3.1): CORRECT, poly-QUERY.** (3a) `Δ_ij(R_C h)=BC₀−AD`, factors `[−1,1]`,
  d-Lipschitz. (3b) only `log N=O(d log(d/γ))` enters ⇒ `O((d log(d/γ)+log 1/δ)/γ²)` samples; offline exp.
  **(3c, the crux): CORRECT** — SR `h` ⇒ `Δ_ij(h)≥0` at all real `w` (Brändén) ⇒ `Δ_ij(R_C h)≥0` pointwise
  on the grid even though `R_C h` is not SR ⇒ completeness. (3d) ℓ1-Lipschitz + `d_TV(h,SR)≥½V(h)` ✓.
- **Claim 4 (conditional aggregation Lemma 5.1): CORRECT.** Chain re-derived; constant `¼` right.
- **Claim 5 (parity amplification): CORRECT.** `Δ_ij=−4η·4^{−m}∏_{k≠i,j}(1−z_k²)` ⇒ `V(g)=4η·4^{−m}`
  (exp-small); conditional margin `Θ(η)` on half the contexts ⇒ `W_F=η/8` ⇒ `d_TV≥η/32`. (sympy ✓.)

## Overall
The framework is **sound and consistent**: Claim 2 (reversal identity) is the engine (compactifies the
all-real test AND guarantees the correct sign on the grid for SR inputs, Claim 3c); Claim 3 → poly-query
tester for any inverse-poly margin; Claim 4 aggregates with a clean constant; Claim 5 shows the conditional
margin can be exp-larger than the global one (the whole point of SUBCOND).
🔴 **(R+) is within reach MODULO §10** (the "conditional-stability removal lemma" = the soundness converse
connecting small `W_F` back to global closeness to SR without the ½/¼ slack accumulating across a hierarchy
of conditionings). That lemma is **NOT** among Claims 1–5 — it is the open work. Claims 1–5 establish only
the necessity/lower-bound side + per-context completeness.

Sources: Brändén arXiv:0707.2340; Pemantle arXiv:1210.3231; Tang–Lian arXiv:1908.10024 (Poisson-binomial);
Anari–Oveis Gharan arXiv:1602.05242; Berkeley Math 270 lec3 (multiaffine stable polynomials).
