# Round-2 Response — C1 (codex GPT-5.5-xhigh, 2026-06-21)

> Cleaned from `PROOF_REVIEW/codex_raw/round2_response_C1.raw.txt` (session 019eead4-…). codex confidence:
> 95% in the derivations/counterexample, 85% that it refutes (T)-as-written. **NOT proved until human
> verification** — but the orchestrator (referee) independently re-verified the core claims (below).

## Result: bounded-/sparse-support localization (T) is REFUTED (clean counterexample)
**The even-parity slice** `μ_n(x) = 2^{-(n-1)}·1{Σx_i ≡ 0 (mod 2)}`, with
`g_n(z) = 2^{-n}(∏_i(1+z_i) + ∏_i(1−z_i))`.
1. **Every proper marginal is uniform-product** (any assignment on `C⊊[n]` has `2^{n-|C|-1}` even
   extensions). → invisible to bounded statistics.
2. **Tilted covariance closed form:** with `r_k=(1−λ_k)/(1+λ_k)`, `R=∏_k r_k`,
   `Cov_{μ_n^λ}(X_i,X_j) = (1−r_i²)(1−r_j²)/(4(1+R)²) · ∏_{k≠i,j} r_k`.
   So if **any** off-pair coord has `λ_k=1` (`r_k=0`) the covariance is **0** ⟹ every field with non-unit
   support `|A| ≤ n−3` (indeed any `o(n)`-support field) gives **zero** covariance for every pair ⟹
   **misses `μ_n` entirely**.
3. **`μ_n` is `≥1/8`-far from SR:** per even-parity face `t` on `B={3,…,n}` the `(X_1,X_2)` table is
   `(a,0,0,a)` (`a=2^{-(n-1)}`); SR ⇒ (closure + NA) `ν(00)ν(11) ≤ ν(01)ν(10)`, whose nearest table to
   `(a,0,0,a)` is `≥a` away in ℓ₁; `2^{n-3}` faces ⟹ `‖μ_n−ν‖_1 ≥ 1/4`, `d_TV ≥ 1/8`.
4. **But `μ_n` IS caught by a 1-PARAMETER full-support tilt:** `λ_i=λ_j=1`, `λ_k=δ=1/n²` (all `k≠i,j`)
   gives `Cov ≈ 1/4` — uses `n−2` non-unit coords (full support) but only **one distinct value δ**.

**Referee check (orchestrator):** I re-derived 1–4 independently; all correct. P5 and P6 were also
re-derived by codex, matching the round-1 referee derivation.

## What this means (reframing the crux — NOT a kill, NOT yet impossibility)
- **N3 (refuted route):** sparse/bounded-support external-field witness families CANNOT localize (parity).
  The witness genuinely needs **full-support** fields. *(This kills route 5(c)-"few non-unit coords" and
  the `O(log n)`-support reading of (T).)*
- **Sharpened target (T′):** does a poly-size family of **LOW-PARAMETRIC, full-support** fields (e.g. the
  `O(1)`-parameter "uniform δ on the complement" family, which catches parity) localize the witness for
  *every* ε-far `μ` — AND is each such tilted covariance **poly(n)-SUBCOND-estimable**? OPEN.
- 🔴 **Referee synthesis (connects C0 + round 2 — important):** *neither* natural simplification suffices:
  - **Boolean-conditioning-only (the C0 statistic `S1`)** catches `μ_n` (condition `X_B=t`: `Cov(X_1,X_2|·)=1/4`)
    but is **blind to the C0 family F2** (interior-violation non-SR with all conditional covariances ≤0).
  - **sparse-support fields** catch F2-type interior violations but are **blind to `μ_n`** (need full support).
  ⟹ a correct tester must use **full-support interior fields** (the full handle `V`), and the two known
  cheap relaxations each provably miss a different non-SR family. This **raises the prior on the
  impossibility / lower-bound resolution** (RED-3, an equal-grade result) — to be settled by C2, NOT
  declared now.

## Bonus: `μ_n` is a strong C2 (lower-bound) hard-instance seed
`μ_n` is `k`-wise-independent-flavored (all proper marginals product), `1/8`-far from SR, and **invisible
to every `o(n)`-support field / every bounded local statistic**. This is exactly the profile of a
planted-vs-far hard instance forcing SUBCOND lower bounds. → feed to C2.
