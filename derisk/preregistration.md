# C0 Pre-registration (FROZEN before measuring) — 2026-06-20

> Guide §6 C0 / §12: pre-register the expected trend + a falsifier BEFORE running; fixed seeds; never
> shape-force. This file is written and committed before `run_c0.py` is executed. Mismatch with the
> result is DIAGNOSED and recorded honestly, never tuned away.

## Setup
- Distributions `μ` over `{0,1}^n`, `n ∈ {2,3,4}`, as full probability vectors over the `2^n` subsets.
- Generating polynomial `g_μ(z) = Σ_S μ(S) ∏_{i∈S} z_i` — multiaffine, nonnegative coefficients.
- **SR membership test (small `n`):** by **Brändén's multiaffine criterion** — a multiaffine polynomial
  with nonnegative coefficients is real stable (⇔ SR) **iff** the pairwise **Rayleigh-difference**
  inequalities `Δ_{ij}(g)(x) := ∂_i g(x)·∂_j g(x) − g(x)·∂_i∂_j g(x) ≥ 0` hold for **all** `x ∈ ℝ₊^n`
  and all `i≠j`. We test this numerically on a dense grid + random points of the positive orthant and
  report the **margin** `m(μ) = min_{i≠j, x} Δ_{ij}(g)(x)` (normalized). `m ≥ −tol` ⇒ SR; `m < −tol` ⇒
  the witness `(i,j,x*)` certifies non-SR. *(This is `P3`; for a de-risk the grid is a numerical proxy —
  flagged, not claimed as a proof.)*

## Honest distance-to-SR lower bounds (the two lemmas relied on)
Let `dist₁(μ, SR) = inf_{ν SR} ||μ − ν||₁`. Both lemmas use a confirmed *necessary* condition for SR and
the fact that the witnessing functional is Lipschitz in `ℓ₁`.

- **Lemma C0-L1 (pairwise-correlation margin).** For every SR (indeed NA) ν and all `i,j`:
  `Cov_ν(x_i, x_j) ≤ 0` (`P2`: SR⇒NA⇒pairwise negative correlation). The map `μ ↦ Cov_μ(x_i,x_j)` is
  **3-Lipschitz** in `ℓ₁` (since `Cov = E[x_ix_j] − E[x_i]E[x_j]`, each factor in `[0,1]`, each `E[·]`
  1-Lipschitz). Hence if `Cov_μ(x_i,x_j) = δ > 0` then `dist₁(μ, SR) ≥ δ/3`.
- **Lemma C0-L2 (Rayleigh-difference margin).** For every SR ν and all `i,j,x∈ℝ₊^n`:
  `Δ_{ij}(g_ν)(x) ≥ 0` (`P3`). At a FIXED witness point `x*`, `μ ↦ Δ_{ij}(g_μ)(x*)` is a quadratic
  functional of `μ` with an explicit `ℓ₁`-Lipschitz constant `L(x*)` (computed = max `ℓ∞`-norm of its
  gradient over the simplex). Hence if `Δ_{ij}(g_μ)(x*) = −δ < 0` then `dist₁(μ, SR) ≥ δ / L(x*)`.

Both rely ONLY on confirmed substrate (`P2`,`P3`); `L(x*)` is computed, not assumed. They are **lower
bounds** on the distance (a far instance is *certified* far), which is exactly what a soundness de-risk
needs. ⚠️ Lemma assumptions to discharge later (post-Phase-0, by the attacker/human): the constants are
loose; tightening them is not needed for the lean.

## Candidate local statistics (computable from subcube-conditional samples)
- **S1 — worst conditional pairwise correlation (degree-2 / NA witness).**
  `S1(μ) = max over pairs (i,j) and conditionings ρ on a subset of the other coords of
  Cov_{μ|ρ}(x_i, x_j)` (the most-positive conditional covariance; SR ⇒ S1 ≤ 0). SUBCOND-estimable:
  conditional covariances from subcube-conditional samples.
- **S2 — conditional second-order (triple) negative-dependence proxy.**
  `S2(μ) = max over i,j,k of | Cov_{μ|x_k=1}(x_i,x_j) − Cov_{μ|x_k=0}(x_i,x_j) |`-type discrepancy that
  a *pairwise* statistic cannot see — a low-order proxy for the stability/Rayleigh structure beyond
  pairwise. SUBCOND-estimable (condition on `x_k`). *(A deliberately simple proxy; if even this misses
  F2, that is the falsifier signal.)*

## Far families (adversarial — NOT random)
- **F1 (easy, positive-correlation):** start from an SR `μ0`; add mass to make some pair *positively*
  correlated with margin `δ_corr`. Certified far by **C0-L1** (`dist₁ ≥ δ_corr/3`). Pre-registered:
  **S1 detects F1** (S1 ≈ δ_corr > 0).
- **F2 (hard, pairwise-negatively-correlated but NOT SR):** construct `μ` that is pairwise *negatively*
  correlated (so `S1 ≤ 0`, invisible to the pairwise handle — the CS3 trap) yet **violates a
  Rayleigh-difference inequality** (`Δ_{ij}(x*) < 0`), certified far by **C0-L2**. Pre-registered:
  **S1 FAILS on F2** (S1 ≤ 0, looks SR to the pairwise handle). The open question = **does S2 separate
  F2 from genuine SR?**

## Pre-registered hypotheses + FALSIFIER
- **H1:** S1 separates SR from **F1** (S1≈0 on SR, S1>0 on F1, growing with `δ_corr`). *(sanity)*
- **H2 (the real test):** S1 does **NOT** separate SR from **F2** (both have S1 ≤ 0) — i.e. the natural
  pairwise/NA handle is **blind** to the CS3 family. *(expected — this is why SR ≠ "test product/NA".)*
- **H3 (the lean direction):** does S2 (a bounded-order conditional proxy) separate **F2** from genuine
  SR with a margin that **scales with the Rayleigh-difference violation `δ_Δ`**?
  - **If YES** (S2 clearly > 0 on F2, ≈ 0 on SR, scaling in `δ_Δ`): **lean → a local handle at bounded
    order is plausible → attack the C1 tester first.**
  - **🔴 FALSIFIER (If NO** — S2 on F2 is statistically indistinguishable from S2 on genuine SR, or does
    not scale with `δ_Δ`): **no clean low-order local handle → lean toward harder / weigh the
    impossibility route** (escalate per NO-RETREAT §15; this is NOT RED-3, only a routing lean).

Fixed seed: `SEED = 20260620`. Grids/points fixed in `sr_core.py`. Result → `results/c0_results.json`.
One fresh-context audit agent sanity-checks this setup before the result is frozen in the ledger.
