# Round-1 Response — C1 (codex GPT-5.5-xhigh, 2026-06-21)

> Cleaned final message from codex (model gpt-5.5, reasoning_effort xhigh, read-only sandbox). Raw:
> `PROOF_REVIEW/codex_raw/round1_response_C1.raw.txt` (session 019eeac4-…). **NOT proved — AI output,
> conditional until independent verification.** Audit → `round1_audit_C1.md`.

## Verdict (codex): partial / OPEN, not solved
- Confidence: **82%** that the current frozen facts are insufficient for a *proved* `poly(n,1/ε)` tester;
  **60%** that a genuinely new "robust external-field witness theorem" would be needed.
- Did **not** claim closure → 1 independent audit (not 3).

## What codex states it can prove from `P*` (a CORRECT restatement of P3, not a new tester)
- SR ⇔ `Δ_{ij}g(x)=∂_i g·∂_j g − g·∂_i∂_j g ≥ 0` for all `i≠j`, all `x∈ℝ₊ⁿ` (P-SR).
- **External-field form:** for the tilt `μ^λ` (`λ∈ℝ₊ⁿ`), `Δ_{ij}g(λ) = −g(λ)²·Cov_{μ^λ}(X_i,X_j)`, so
  `Δ_{ij}g(λ)≥0 ⇔ Cov_{μ^λ}(X_i,X_j) ≤ 0`. Hence the **global handle**
  `V(μ) = sup_{i<j, λ∈ℝ₊ⁿ} (Cov_{μ^λ}(X_i,X_j))₊` satisfies `V(μ)=0 ⇔ μ is SR`.
  *(This is the analytic criterion re-expressed probabilistically — NOT a SUBCOND-local handle.)*

## The precise missing theorem (the crux, distilled — a GAP, not closed)
> **Robust external-field witness theorem (CONJECTURE, unproved):**
> `d_TV(μ, SR) ≥ ε ⟹ ∃ i,j,λ with Cov_{μ^λ}(X_i,X_j) ≥ poly(ε, 1/n)`, with `λ` efficiently
> searchable / SUBCOND-simulable.

## Real obstruction codex surfaces (to record as a barrier-candidate)
- **SUBCOND ≠ external-field access.** Subcube conditioning gives Boolean restrictions (`z_i∈{0,∞}`
  vertices); SR needs *all positive* external fields `λ∈ℝ₊ⁿ` (interior). Rejection-sampling a bounded
  field can have **exponentially small acceptance** ⇒ no automatic `poly(n)` simulation of `μ^λ`.
  *(This sharpens B3 / the C0 "interior-violation" finding into an oracle-access gap.)*

## CS3 (NA-but-not-SR) — codex's soundness reasoning
- Any tester using only pairwise/conditional-pairwise/marginal/NA statistics is **unsound** (P2: SR⇒NA
  only; C0 family F2 = NA-visible but non-SR at interior fields). The external-field Rayleigh handle
  *would* be sound (non-SR ⇒ some tilted pair has positive covariance) but lacks a `poly(n,1/ε)` SUBCOND
  implementation + a robust lower bound on the violation.

## Frozen facts used
Used: P-SR, P1, P2, P3, P-Oracle. NOT used as a theorem: P-Engine-1 (monotonicity isoperimetry does not
transfer). Used as warning/evidence: P-C0-lean. Neither Theorem A.1/A.2 nor an impossibility was obtained.
