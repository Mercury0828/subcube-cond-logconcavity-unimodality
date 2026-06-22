# Round-1 Audit — C1 (independent fresh-context agent + referee check, 2026-06-21)

> Audits codex's round-1 C1 reply (`round1_response_C1.md`). Codex claimed OPEN (no tester). Audit was
> adversarial on both directions: is the math correct, and did codex give up too early? Classifications
> below; the orchestrator (referee) independently re-derived the key identity.

## Classification summary
- **No FATAL to a claimed result** (codex claimed none). Net: round-1 C1 = **GAP-level PROGRESS** — the
  open problem is sharpened and one of codex's two stated blockers is **refuted**.

## Findings

### F1 [FATAL-to-formula / MINOR-to-conclusion] — corrected prefactor (REFEREE-VERIFIED, not just AI)
Codex wrote `Δ_ij(g)(λ) = −g(λ)²·Cov_{μ^λ}(X_i,X_j)`, dropping a `λ_iλ_j`. **Correct identity (re-derived
independently by the orchestrator):**
`P_{μ^λ}(X_i{=}1)=λ_i∂_ig(λ)/g(λ)`, `P_{μ^λ}(X_iX_j{=}1)=λ_iλ_j∂_i∂_jg(λ)/g(λ)`
⟹ **`Cov_{μ^λ}(X_i,X_j) = −(λ_iλ_j/g(λ)²)·Δ_ij(g)(λ)`**, i.e. `Δ_ij(g)(λ) = −(g(λ)²/(λ_iλ_j))·Cov_{μ^λ}`.
Sign equivalence `Δ_ij≥0 ⇔ Cov_{μ^λ}≤0` is **unaffected** (λ_i,λ_j>0) → the handle `V(μ)=0⇔SR` survives.
But the `1/(λ_iλ_j)` factor blows up/vanishes at the orthant boundary and **matters for any poly(ε,1/n)
accounting** → must be the starting point of any quantitative ("witness") bound. *(I checked this by hand;
treat as verified substrate, not AI-conjectured.)*

### F2 [MINOR] — `V(μ)=0 ⇔ SR` is correct
Follows from Brändén's multiaffine criterion + F1 (same sign). Subtlety: criterion is on the **open**
orthant; the `sup` witness is attained in the interior by continuity of `Cov_{μ^λ}` in λ. State cleanly.

### F3 [GAP — codex's stated obstruction is FALSE] — tilted covariances ARE SUBCOND-estimable
🔴 The most important correction. Codex claimed SUBCOND can't reach external-field tilts `μ^λ` (rejection
sampling exp-small). **False.** For `B=[n]∖{i,j}`: SUBCOND fixes `X_B=t` (Boolean) and estimates the
4-cell conditional `q_t(a,b)=P_μ(X_i{=}a,X_j{=}b|X_B{=}t)` and the marginal `P_μ(X_B{=}t)`; the tilt enters
as **deterministic post-processing multipliers** (`P_{μ^λ}(X_i{=}a,X_j{=}b,X_B{=}t) ∝ λ_i^aλ_j^bλ_B(t)
P_μ(X_B{=}t)q_t(a,b)`). **No sample is ever drawn from `μ^λ`** — codex conflated "simulate `μ^λ`" with
"estimate one tilted 2nd moment." *(Referee note: correct in principle by total probability; the catch is
poly-query, see below.)*
**The REAL difficulties (genuine open, upper-bound engineering — NOT impossibility):** (a) the reweighting
sums over **exp-many** subcubes `t∈{0,1}^B`; (b) λ-multipliers can be huge → **variance / importance-
sampling** blowup; (c) one still needs the **witness-localization theorem** to confine the `sup` to a
small structured set of `(i,j,λ)`.

### F4 [GAP] — the robust external-field witness theorem is the real missing ingredient
`d_TV(μ,SR)≥ε ⟹ ∃ i,j,λ with Cov_{μ^λ}(X_i,X_j) ≥ poly(ε,1/n)` AND **λ of bounded support / bounded
magnitude / low-dimensional reweighting** (so the exp(n) `t`-sum collapses to poly). Codex named it but did
not attempt it. Natural attack: adapt a Talagrand/local-to-global inequality to the Rayleigh-difference
functional (the 2502.16355 engine codex cited but did not try).

### F5 [MINOR] — routes codex overlooked (candidate directions, NOT mandates)
1. **Tilt-localization via random restriction** — arXiv:1911.07357 (random restrictions + subcube cond.),
   arXiv:2204.02570 (entropic independence / local-to-global for SR): random conditionings make
   conditionals near-product w.h.p. → may collapse the exp `t`-sum to poly.
2. **Bounded-field reduction** — only the *sign* of `Cov_{μ^λ}` matters and `Cov` is analytic in λ, so the
   `sup` over `ℝ₊ⁿ` may be approximable by λ in a poly grid in a box `[δ,1/δ]ⁿ`, or even few-coordinate
   fields. (How much interior is actually needed? Codex never asked.)
3. **Distance-estimation subroutines** — arXiv:2506.18444 (tight conditional-sample simulation), slice-
   and-dice estimators: estimate the reweighted covariance functional to additive error in `Õ(n/ε²)`.

## Verdict + round-2 direction
- Codex's **OPEN** verdict is **defensible, but its 82%-blocking justification (field-simulation) is WRONG**
  and is discarded. The problem is genuinely open but **less blocked** than codex thought — the estimation
  half reduces to Boolean conditioning; the crux is the **witness-localization theorem**.
- **Round-2 = sharpen the UPPER bound:** prove/refute the robust external-field witness theorem with
  **bounded-support/bounded-magnitude λ**, starting from the corrected identity (F1). **Do NOT pivot to the
  lower bound yet** — C2 runs in parallel as planned, but the lower bound becomes the primary target only
  if localization provably fails.
- 🔴 Everything here (F1 aside, which the referee verified) is AI-produced and conditional until human
  verification; F3's reduction is correct in principle but its poly-query realization is exactly the open
  problem — do not record it as a working subroutine without the localization theorem.
