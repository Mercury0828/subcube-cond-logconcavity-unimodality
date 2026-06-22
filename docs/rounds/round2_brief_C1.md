# Round-2 Brief — C1 (the external-field witness-localization theorem)

> **STATUS: SENT to codex GPT-5.5-xhigh (gpt-5.5/xhigh), round 2, 2026-06-21.** Raw →
> `PROOF_REVIEW/codex_raw/round2_response_C1.raw.txt`. Builds on round 1
> (`round1_response_C1.md` + `round1_audit_C1.md`). Skeleton = guide §8 (freeze FACTS, free METHODS).
> Method-agnostic: routes below are *candidate inspiration*, not mandates.

## 0. Role note
You originate the math; we referee via independent audits. Mark proved vs assumed; flag every asserted
step; give an updated confidence. "AI-verified ≠ proved."

## 1. Round-1 recap (what is now FROZEN, and the one corrected fact)
- **Handle `P5` (REFEREE-VERIFIED — use freely).** For the external-field tilt `μ^λ`
  (`μ^λ(S) ∝ μ(S)∏_{i∈S}λ_i`, `λ∈ℝ₊ⁿ`):
  **`Cov_{μ^λ}(X_i,X_j) = −(λ_iλ_j / g(λ)²)·Δ_{ij}(g)(λ)`**, where `Δ_{ij}(g)=∂_i g·∂_j g − g·∂_i∂_j g`.
  Hence `Δ_{ij}(g)(λ)≥0 ⇔ Cov_{μ^λ}(X_i,X_j)≤0`, and `V(μ)=sup_{i<j,λ∈ℝ₊ⁿ}(Cov_{μ^λ}(X_i,X_j))₊` obeys
  **`V(μ)=0 ⇔ μ SR`**. 🔴 NOTE the `1/(λ_iλ_j)` factor (your round-1 reply dropped it); it is harmless to
  the *sign* but **load-bearing for any quantitative `poly(ε,1/n)` bound**.
- **Estimability `P6` (correct in principle; the poly-query realization is the open problem).** A round-1
  audit refuted the claim that SUBCOND can't reach external-field tilts. In fact `Cov_{μ^λ}(X_i,X_j)` is
  computable **without sampling `μ^λ`**: with `B=[n]∖{i,j}`, SUBCOND fixes `X_B=t` (Boolean) and estimates
  `q_t(a,b)=P_μ(X_i{=}a,X_j{=}b|X_B{=}t)` and `P_μ(X_B{=}t)`; the tilt is **deterministic post-processing**
  (`P_{μ^λ}(X_i{=}a,X_j{=}b,X_B{=}t) ∝ λ_i^aλ_j^bλ_B(t)P_μ(X_B{=}t)q_t(a,b)`). **No rejection sampling.**
  🔴 BUT naively this sums over **exp-many** `t∈{0,1}^B` and the λ-multipliers cause variance blowup — so a
  *naive* estimator is `exp(n)`-query. Making it `poly(n)` is exactly the crux below.

## 2. The exact target (the make-or-break theorem)
Prove or refute, and if proved assemble the tester:
> **(T) Robust external-field witness-localization.** There is a `poly(ε,1/n)` function `ρ` and a
> `poly(n,1/ε)`-size, efficiently-enumerable family `Λ ⊆ ℝ₊ⁿ` of **bounded-support / bounded-magnitude /
> low-dimensional** external fields such that:
> `d_TV(μ, SR) ≥ ε ⟹ ∃ i≠j, ∃ λ∈Λ with Cov_{μ^λ}(X_i,X_j) ≥ ρ(ε,1/n)`,
> and for every such `λ∈Λ`, `Cov_{μ^λ}(X_i,X_j)` is **`poly(n,1/ε)`-SUBCOND-estimable to additive
> error ≪ ρ** (the `t`-reweighting collapses to poly — e.g. because `λ` has `O(1)`/`O(log n)` non-unit
> coordinates, or because random restriction makes the conditional near-product).
- **If (T) holds:** assemble Theorem A.2 — the tester estimates `max_{i,j,λ∈Λ} Cov_{μ^λ}(X_i,X_j)` and
  rejects iff it exceeds `~ρ/2`; prove completeness (SR ⇒ all ≤0) + soundness (ε-far ⇒ some ≥ρ) + the
  `poly(n,1/ε)` query bound. **CS3 is automatic**: the handle certifies *SR*, not pairwise/NA, because a
  non-SR but NA distribution still has some `Δ_{ij}(λ)<0`, i.e. some tilted positive covariance in `Λ`.
- **If (T) is FALSE** (no poly-size localized witness family can exist): that is itself decisive — it
  pushes toward the impossibility / lower-bound resolution. **Prove the non-localizability** (e.g. a family
  of ε-far-from-SR `μ` whose only witnesses require `λ` with `ω(log n)` non-unit coordinates / exp-small
  estimable signal). 🔴 A heuristic "seems hard to localize" is NOT a refutation — give a construction.

## 3. Frozen substrate `P*`
P-SR, P1, P2, P3, P-Oracle (as round 1); **P5** (above, verified); **P6** (above, in-principle, poly-query
OPEN); engines 2502.16355 / 2408.02347 (adapt, do not transfer). C0 lean (low-order pairwise/triple
statistics do NOT separate — consistent with needing genuine interior fields, not just Boolean vertices).

## 4. Refuted routes `N*`
- **N1 (refuted obstruction):** "SUBCOND cannot estimate external-field-tilted covariances" — FALSE (P6).
  Do not re-assert it; the open issue is *poly-query localization*, not reachability.
- **N2 (unsound):** any tester certifying only pairwise / conditional-pairwise(Boolean) / marginal / NA
  statistics — accepts NA-but-not-SR (CS3 / C0 F2). The witness must range over genuine interior fields `Λ`.

## 5. Candidate routes (INSPIRATION, not mandates)
(a) **Adapt a Talagrand / local-to-global inequality to the Rayleigh-difference functional** `Δ_{ij}`
(the 2502.16355 architecture: local statistic ⇒ global distance) — the analogue here is "a localized
tilted-covariance witness ⇒ `d_TV` to SR." (b) **Random-restriction tilt-localization** — random subcube
conditionings make conditionals near-product w.h.p. (1911.07357; entropic independence / local-to-global
for SR 2204.02570), potentially collapsing the `t`-sum. (c) **Bounded-field reduction** — since only the
*sign* of `Cov_{μ^λ}` matters and `Cov` is analytic in `λ`, approximate `sup_{λ∈ℝ₊ⁿ}` by a poly grid in a
box `[δ,1/δ]ⁿ`, or by few-coordinate fields; quantify how many non-unit coordinates are actually needed.
(d) **Slice-and-dice / tight conditional simulation** (2506.18444) for the estimation error budget.

## 6. What we need back
(1) a proof or refutation of (T), proved-vs-assumed marked; (2) if proved, the full tester + upper bound +
the (automatic) CS3 soundness; (3) the resulting exponent in `n` and `1/ε` (feeds C3 tightness); (4) if (T)
is refuted, the explicit non-localizable ε-far family (feeds C2 / the impossibility route); (5) updated
confidence + verdict.
