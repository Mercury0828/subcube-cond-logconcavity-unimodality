# Round-1 Brief — C1 (local handle for SR + the SUBCOND SR tester / upper bound)

> **STATUS: SENT to codex GPT-5.5-xhigh (model gpt-5.5, reasoning_effort xhigh), round 1, 2026-06-21**
> (owner authorized continuation + transport). Raw reply →
> `PROOF_REVIEW/codex_raw/round1_response_C1.raw.txt`; cleaned reply + audit →
> `docs/rounds/round1_response_C1.md` / `round1_audit_C1.md`. Skeleton = guide §8 (freeze FACTS, free
> METHODS). 🔴 Method-agnostic: do NOT prescribe the operator or assert that monotonicity transfers.

## 0. Role note for the solver
You (the solver) **originate the mathematics**. We (orchestrator) referee via independent adversarial
audits and do not produce the proof. State what you prove vs assume; flag every step that is asserted but
not proved; give an updated confidence. "AI-verified ≠ proved" — your output is conditional until
independent human verification.

## 1. The exact target (a precise claim; "done" is unambiguous)
Let `μ` be an unknown distribution over `{0,1}^n` accessed by the **subcube-conditioning (SUBCOND)
oracle** (Frozen substrate P-Oracle below). Fix `ε>0`. Build:
- **(Theorem A.1 — a local / isoperimetry-style handle):** a structural inequality for **strong
  Rayleigh (SR)** distributions on `{0,1}^n` that relates a **SUBCOND-observable statistic** (a quantity
  estimable from `poly(n,1/ε)` subcube-conditional samples) to the **ℓ₁ distance from `μ` to the SR
  set** — i.e. a quantity that is `≈0` when `μ` is SR and **provably bounded below** when `μ` is ε-far
  from SR. (This is the analogue of what the directed-isoperimetric inequality did for monotonicity —
  but for SR it must be **built**, not transferred; see B3 and the C0 lean.)
- **(Theorem A.2 — the tester + upper bound):** a `poly(n,1/ε)`-query SUBCOND algorithm that **accepts**
  (w.p. ≥ 2/3) every SR `μ` and **rejects** (w.p. ≥ 2/3) every `μ` that is ε-far (ℓ₁/TV) from every SR
  distribution, with a proven query upper bound `Õ(·)`.
- **Soundness requirement (load-bearing, CS3):** the tester must **reject** distributions that pass
  pairwise / marginal / negative-association statistics **but are not SR** (NA is necessary, not
  sufficient — see P2 and the C0 family F2). A tester that only certifies "product-like / pairwise-
  negatively-correlated" does **not** solve this target.

**OR** — the *other proven resolution* — a **proof that no `poly(n)` SUBCOND SR tester exists** (a
super-polynomial SUBCOND **query lower bound for the testing task itself**, e.g. a planted-vs-far family
no tester distinguishes with `poly(n)` queries). 🔴 A proof that *no local handle exists* is **NOT** this
(a non-local/global tester could still exist) — that alone is only a routing signal, not the impossibility.

## 2. Frozen substrate — `P*` ("use freely, do not re-derive"; sources in `lit/SCAN_REPORT.md`)
- **P-SR (definition).** `μ` over `{0,1}^n` has generating polynomial `g_μ(z)=Σ_S μ(S)∏_{i∈S}z_i`
  (multiaffine, nonneg coeffs). **`μ` SR ⇔ `g_μ` real stable** (Borcea–Brändén–Liggett, arXiv:0707.2340,
  Def 2.10). Equivalently (Brändén, multiaffine nonneg-coeff criterion) `g_μ` real stable ⇔ the pairwise
  **Rayleigh-difference** `Δ_{ij}(g_μ)(x)=∂_i g·∂_j g − g·∂_i∂_j g ≥ 0` for **all** `x∈ℝ₊^n`, all `i≠j`.
- **P1 (closure).** SR is closed under **subcube conditioning** (fixing coords to 0/1), projection/
  marginalization, and external fields (BBL Prop 2.1 + §4). *(This is exactly what makes the SUBCOND
  oracle natural for SR.)*
- **P2 (negative association).** SR ⇒ CNA+ ⇒ **NA** ⇒ pairwise negative correlation (BBL Thm 4.10).
  🔴 **NA is necessary, NOT sufficient** for SR (no canonical NA-but-not-SR counterexample with a theorem
  number was located in primary text — you may need to construct one; see C0 family F2).
- **P3 (analytic criterion is NOT a local handle).** The Rayleigh-difference criterion holds on the whole
  positive orthant `ℝ₊^n` — a **global analytic** condition, **not** a SUBCOND-observable local statistic.
  🔴 Turning it into a SUBCOND-checkable local quantity (or proving you cannot) is precisely C1's burden.
- **P-Oracle (SUBCOND).** A query fixes a subset `T⊆[n]` to `ρ∈{0,1}^T` and returns a sample from `μ`
  conditioned on `{x:x|_T=ρ}`. `T=∅` = i.i.d. sampling. Cost = number of conditional samples.
- **P-Engine-1 (2502.16355, STOC 2025 — an ENGINE TO ADAPT, NOT a transferring theorem).** Monotonicity
  testing in SUBCOND is `Θ̃(n/ε²)`, tight, via a **real-valued directed Talagrand inequality** (their Thm 3:
  `E_x[(Σ_{i:x_i=−1}((f(x)−f(x^{(i)}))⁺)²)^{1/2}] ≥ Ω(1/√log n)·dist₁(f)`) that converts a **local edge-bias**
  measured on 1-dim subcubes into a global ℓ₁ distance-to-monotone bound. 🔴 **The authors give NO
  extension to SR / log-concavity / negative dependence; the transfer is non-obvious (B3).** Use the
  *bridge architecture* (local statistic → isoperimetric inequality → tester) as inspiration, not the
  inequality itself.
- **P-Engine-2 (2408.02347, APPROX/RANDOM 2024).** SUBCOND subroutines estimating conditional marginals /
  equivalence / product structure in `Õ(n/ε²)` queries — use freely to estimate conditional marginals.
- **P-C0-lean (this project, 2026-06-20 — a *lean*, not a theorem).** On `n∈{3,4}`: the natural pairwise/
  NA statistic is **provably blind** to a family F2 of pairwise-negatively-correlated **non-SR**
  distributions whose real-stability failures are at **interior** points of `ℝ₊^n`; a simple bounded-order
  conditional triple proxy does **not** cleanly separate F2 from genuine SR. ⇒ **a clean low-order local
  handle looks doubtful**; non-local / higher-order / global routes are in scope. *(Lean only; see
  `docs/ledger_sr_subcond.md §7`.)*

## 3. Refuted routes — `N*` ("do NOT attempt")
- *(none formally refuted yet — first attack round.)* **Provisional steer (from the C0 lean, not a
  refutation):** do not expect a one-line black-box port of the monotonicity directed-Talagrand inequality
  to certify SR — the C0 lean indicates the pairwise/edge-local signal misses interior real-stability
  failures. If you nonetheless find such a port works, that itself must be proven (and would be flagged
  CS1: if SR were testable by a trivial transfer the result is folklore).

## 4. Barriers in force — `B*`
- **B1** (VERIFIED): standard i.i.d. DPP testing needs `Ω(2^{n/2}/ε²)` samples (2008.03650 Thm 2). ⇒ a
  `poly(n)` SUBCOND tester **must genuinely use conditional access**; an i.i.d.-reducible tester cannot exist.
- **B2** (VERIFIED): deciding M-convexity of a given quadratic set function is co-NP-complete (1704.02836).
  ⇒ target = SR **distribution testing**, NOT exact recognition.
- **B3** (the live risk): **no known local/edge characterization or directed-isoperimetry for SR** — the
  handle must be built or proven impossible; the C0 lean (P-C0-lean) is empirical evidence this is hard.

## 5. The open question (posed method-agnostically)
**Build a SUBCOND-observable structural handle for SR and a `poly(n,1/ε)` SUBCOND SR tester with a proven
upper bound — by ANY route (local edge-isoperimetry, higher-order conditional statistics, a global
real-stability test via conditional access, spectral / HDX, or anything else). If no such `poly(n)`
tester can exist, prove THAT instead** (a super-polynomial SUBCOND query lower bound for the testing
task). The tester must reject NA-but-not-SR distributions (CS3). Do not assume the monotonicity inequality
transfers; do not assume a local handle exists.

## 6. What we need back
(1) the full statement + proof of the handle (or the impossibility), explicitly marking proved vs assumed;
(2) the tester + upper-bound analysis, including the CS3 soundness argument (reject a non-SR distribution
that passes pairwise/marginal stats); (3) where, if anywhere, the argument needs a fact we have not frozen;
(4) an updated confidence (%) and a verdict (closed / partial / open / impossible-on-a-proof).
