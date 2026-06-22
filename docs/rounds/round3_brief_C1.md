# Round-3 Brief — C1 (the LOW-PARAMETRIC combined-statistic reformulation (T″))

> **For codex GPT-5.5-xhigh.** Builds on rounds 1–2 (`round{1,2}_response_C1.md`, `round2_audit_C1.md`).
> Skeleton = guide §8 (freeze FACTS, free METHODS). Method-agnostic.

## 0. Role note
You originate the math; we referee via independent audits (which already verified P5, P6, and the round-2
parity counterexample). Mark proved vs assumed; flag every asserted step; honest confidence + verdict.

## 1. Verified state (FROZEN — use freely)
- **P5 (external-field handle).** `Cov_{μ^λ}(X_i,X_j) = −(λ_iλ_j/g(λ)²)·Δ_{ij}(g)(λ)`; with
  `V(μ)=sup_{i<j,λ∈ℝ₊ⁿ}(Cov_{μ^λ}(X_i,X_j))₊`, `V(μ)=0 ⇔ μ SR`.
- **P6 (estimability of a tilted covariance — in principle).** `Cov_{μ^λ}(X_i,X_j)` is a deterministic
  function of SUBCOND-estimable Boolean conditionals `q_t(a,b)=P_μ(X_iX_j|X_B=t)` and `m_t=P_μ(X_B=t)`,
  `B=[n]∖{i,j}`. Two `poly`-query routes and their costs: **(i) exp `t`-sum** (naive); **(ii) importance
  sampling** — `Cov_{μ^λ}` = reweighted moments of `μ` with weight `w(x)=∏_k λ_k^{x_k}`; variance is
  controlled iff the weight range is bounded, i.e. **`|λ_k−1| = O(1/n)`** gives `w∈[Θ(1),Θ(1)]` ⇒
  `poly(n)`-estimable, but a **strong tilt** (`λ_k` order-1 from 1) has `exp(n)` weight range ⇒ IS fails.
- **N3 (parity refutation — VERIFIED).** `μ_n` = uniform even-parity slice is `≥1/8`-far from SR yet
  `Cov_{μ_n^λ}=0` for every field of support `|A|≤n−3`. So **sparse-SUPPORT localization is dead**.
- **KEY INSIGHT (round-2 audit).** The obstruction is **SUPPORT size, not parametric dimension**: a
  **1-parameter** full-support tilt (`λ_k=δ`) catches `μ_n` with `Θ(1)` signal. And `μ_n` is ALSO caught
  by a single **Boolean conditioning** (`Cov(X_i,X_j|X_B=t)=+1/4`).
- **Complementary blind spots.** `μ_n`: blind to sparse fields, caught by Boolean conditioning / 1-param
  tilt. The C0 family **F2** (interior-Rayleigh-violators): caught by an order-1 interior field, **blind to
  ALL Boolean conditional pairwise covariances**. **No known family defeats BOTH primitives at once.**

## 2. The exact target (T″) — two coupled questions, both load-bearing
Define the **combined statistic family**
`𝒮 = { Cov(X_i,X_j | X_T=ρ) : i≠j, Boolean (T,ρ), |T| ≤ n }  ∪  { Cov_{μ^λ}(X_i,X_j) : i≠j, λ in an
efficiently-enumerable poly-size family Λ of low-parametric (O(1) distinct values) full-support fields }`.

- **(T″-a) COMPLETENESS.** Prove or refute: `d_TV(μ,SR) ≥ ε ⟹ some statistic in 𝒮 is ≥ poly(ε,1/n)`.
  (Both `μ_n` and F2 are caught; is **every** ε-far `μ`? Either prove it — ideally via a local-to-global /
  Rayleigh-difference isoperimetric inequality — or exhibit a single `μ` that is ε-far but has **all**
  statistics in `𝒮` below `o(poly)`. The latter is the impossibility seed.)
- **(T″-b) POLY-ESTIMABILITY (the real tension — do NOT assume it away).** The completeness witnesses must
  be `poly(n)`-SUBCOND-estimable. Boolean conditional covariances: yes. **Tilted covariances: only mild
  tilts `|λ_k−1|=O(1/n)` are poly-estimable (P6(ii)); strong/interior tilts are not (exp variance / exp
  sum).** 🔴 **The tension:** F2-type witnesses sit at **order-1 interior** fields — does a **mild
  (`O(1/n)`-magnitude) low-parametric** tilt, possibly **composed with a Boolean conditioning** (condition
  first, then mild-tilt the conditional — which may amplify the signal into the estimable regime), still
  witness every ε-far `μ`? Or does completeness provably require non-estimable strong tilts (⇒ the
  estimable combined statistic is INCOMPLETE ⇒ pushes to the lower bound)?

## 3. Outcomes
- **(T″) HOLDS (completeness with poly-estimable witnesses):** assemble Theorem A.2 — tester estimates
  `max 𝒮` and rejects iff `> ~poly/2`; completeness (SR ⇒ all ≤0), soundness (ε-far ⇒ some ≥poly), query
  bound `Õ(·)`. **CS3 automatic** (the handle certifies SR, not NA). Give the exponent in `n,1/ε` (feeds C3).
- **(T″) FAILS:** exhibit ONE explicit ε-far family that is blind to **every** poly-estimable statistic in
  `𝒮` (all bounded-`|T|` Boolean conditional pairwise covariances AND all mild low-parametric tilted
  covariances). 🔴 This is the **decisive impossibility/lower-bound seed** (RED-3 candidate) — far stronger
  than `μ_n` (which is caught) or F2 (caught) alone. A heuristic "seems hard" is not a refutation.

## 4. Barriers / refuted (do not repeat)
`B1`,`B2`,`B3`; `N1` (tilted-cov reachability is NOT the obstruction); `N2` (NA-only unsound, CS3);
`N3` (sparse-support fields fail). Engines 2502.16355 / 2408.02347 (adapt, not transfer).

## 5. Candidate routes (inspiration, not mandates)
(a) **Local-to-global for the Rayleigh-difference functional** (the 2502.16355 architecture): a localized
combined-statistic witness ⇒ `d_TV` to SR. (b) **Condition-then-mild-tilt**: Boolean-condition a subset,
then apply an `O(1/n)` tilt on the conditional — does conditioning concentrate the witness into the
importance-samplable regime? (c) **Entropic independence / local-to-global for SR** (2204.02570): does
SR's spectral independence bound the number of distinct tilt-parameters / conditioning depth needed?
(d) **Random restriction** (1911.07357) to collapse the exp `t`-sum.

## 6. What we need back
(1) proof or refutation of (T″-a) AND a resolution of (T″-b), proved-vs-assumed marked; (2) if it holds,
the tester + upper bound + exponent + CS3; (3) if it fails, the explicit family blind to all poly-estimable
combined statistics (the lower-bound seed); (4) updated confidence + verdict.
