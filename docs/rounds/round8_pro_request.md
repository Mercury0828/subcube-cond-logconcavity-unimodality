# Brief for web GPT-5.5-Pro — the subcube-conditioning complexity of strong Rayleigh-ness
### (copy everything below the line and send as-is)

---

> Deliberately OPEN-ENDED. This brief gives you the **raw problem** first, then freezes only *verified
> facts* (literature / machine-checked) and a few *concrete counterexamples we computed*, and otherwise
> gives you **full freedom of method**. Everything we label "our reading" is a tentative interpretation
> that **may be wrong** — do not let it constrain you. We have already had to correct one substrate error
> ourselves this project (we initially mis-stated the real-stability criterion — see F1). **If you think
> our framing is itself the bottleneck, discard it and tell us.** We want the truth with proof, by
> whatever route you find.

## 0. Goal (the raw problem)

In the **subcube-conditioning (SUBCOND)** sampling model on `{0,1}^n`, determine the query complexity of
**testing strong Rayleigh-ness (SR)**. Concretely, give either:
- **(R+)** a `poly(n, 1/ε)`-query SUBCOND tester for SR (ideally with a matching lower bound — a tight
  characterization); **or**
- **(R−)** a proof that no `poly(n)`-query SUBCOND tester exists (a super-polynomial query lower bound).

Both are first-rate; we want whichever is true, with proof. We do not know which it is.

## 1. Model and definitions (formal)

- **Distributions.** `μ` over `{0,1}^n` (subsets of `[n]`). Generating polynomial
  `g_μ(z) = Σ_{S⊆[n]} μ(S) ∏_{i∈S} z_i` (multiaffine, nonnegative coefficients, `g_μ(1,…,1)=1`).
- **Strong Rayleigh (SR).** `μ` is SR iff `g_μ` is **real stable** (no complex root `z` with
  `Im(z_i) > 0` for all `i`). SR is the hypercube analogue of log-concavity; it contains determinantal
  point processes and uniform-spanning-tree measures, and is closed under conditioning.
- **SUBCOND oracle.** A query specifies a subset `T ⊆ [n]` and an assignment `ρ ∈ {0,1}^T`; it returns an
  independent sample of `μ` conditioned on the subcube `{x : x|_T = ρ}` (positive probability assumed).
  Query cost = number of conditional samples. `T = ∅` is i.i.d. sampling.
- **Testing task.** Given SUBCOND access to `μ` and `ε>0`: accept (w.p. ≥ 2/3) if `μ` is SR; reject
  (w.p. ≥ 2/3) if `μ` is `ε`-far (`ℓ₁`/TV) from every SR distribution.

## 2. Verified facts — use freely, do not re-derive (but flag any error you find)

These are literature results or machine-checked by us.

- **F1 (real-stability criterion — note the domain; this is where WE erred first).** For multiaffine `g`
  with nonnegative coefficients, `g` is real stable (≡ `μ` SR) **iff `Δ_{ij}(g)(x) := ∂_i g·∂_j g −
  g·∂_i∂_j g ≥ 0` for ALL real `x ∈ ℝⁿ`**, every `i≠j` (Brändén). 🔴 The positive-orthant condition
  `Δ_{ij} ≥ 0 on ℝ₊ⁿ` is the strictly **weaker "Rayleigh" property**; **Rayleigh ⊋ strongly Rayleigh**
  (Choe–Wagner, arXiv:math/0307096; Brändén–Wagner–Wei, arXiv:1411.7735, Prop. 4). `Δ_{ij}` is independent
  of `z_i,z_j`. (We initially used the orthant version as if it characterized SR — it does not.)
- **F2 (closure).** SR is closed under subcube conditioning, projection/marginalization, and external
  fields (Borcea–Brändén–Liggett, arXiv:0707.2340).
- **F3 (negative dependence).** SR ⇒ negative association (CNA+) ⇒ pairwise negative correlation. NA is
  necessary, **not sufficient**, for SR.
- **F4 (external-field identity — machine-checked by us).** For the tilt `μ^λ(S) ∝ μ(S)∏_{i∈S}λ_i`,
  `λ∈ℝ₊ⁿ`: `Cov_{μ^λ}(X_i,X_j) = −(λ_iλ_j/g(λ)²)·Δ_{ij}(g)(λ)`. (Positive external fields therefore only
  probe `Δ_{ij}` on the positive orthant.)
- **F5 (symmetric case — Grace–Walsh–Szegő).** If `μ` is symmetric (`μ(S)=a_{|S|}`), then `μ` is SR iff
  the univariate rank polynomial `P(t) = Σ_k a_k C(n,k) t^k` is real-rooted. The rank sequence
  `(P(|S|=k))_k` is `poly(n)`-SUBCOND-estimable (sample, histogram `|S|`), so symmetric SR-testing is easy.
- **F6 (oracle subroutines / neighbors).** SUBCOND can estimate bounded conditional marginals
  `μ(X_W|X_T=ρ)` and low-degree statistics in `Õ(n/ε²)` queries (Adar–Fischer–Levi, arXiv:2408.02347).
  Monotonicity testing in SUBCOND is `Θ̃(n/ε²)` via a directed-isoperimetric inequality (Chakrabarty–Chen–
  Ristic–Seshadhri–Waingarten, arXiv:2502.16355, STOC 2025) — a *local edge* property, with no SR
  extension given. DPP testing in the *i.i.d.* model needs `Ω(2^{n/2}/ε²)` samples (Gatmiry–Aliakbarpour–
  Jegelka, arXiv:2008.03650); conditional access is what could escape that. We found no prior SUBCOND /
  conditional tester for SR / DPP / log-concavity / negative-dependence.

## 3. Concrete counterexamples we computed (DATA — verify and use; the interpretation in §4 is separate)

These are explicit objects we machine-checked (and one we re-derived by hand). They are facts, not
opinions — please verify them and use them. **Do not read more into them than the statements below.**

- **C-μ4 (a Rayleigh-but-not-SR distribution).** `μ_4` symmetric on 4 bits, `μ_4(S)=a_{|S|}/30`,
  `a=(1,2,2,2,1)`, i.e. `g_4 = 1 + 2e_1 + 2e_2 + 2e_3 + e_4` (`e_k` = elementary symmetric). Then
  `Δ_{ij}(g_4) > 0` on the entire positive orthant `ℝ₊⁴` (so every positive external field and every
  Boolean conditional pairwise covariance is `≤ 0` — it "looks SR" to those), **yet** `g_4(t,t,t,t) =
  1+8t+12t²+8t³+t⁴` has a complex root (`t+1/t = −4+√6 ∈ (−2,2)`), so `g_4` is **not real stable**; `μ_4`
  is `d_TV(μ_4, SR) ≥ 1/7200`-far. (We verified this by hand + CAS + literature.)
- **C-sym (a far-from-SR symmetric measure whose bounded conditional marginals are all SR).** Via F5,
  rank weights `a ≈ [0.51, 0.79, 1, 0.93, 0.54, 0.23, 0.059]` on `n=6` give a global rank polynomial with
  complex roots (`≈ −3.18 ± 1.13 i`, so far from SR), yet **every** `≤ 4`-coordinate conditional+projected
  marginal is SR (real-rooted). (We found such families up to `n=12`. Machine-checked.)
- **C-char (a single hidden parity is detectable).** `μ_T = 2^{-n}(1 + ε·χ_T)`, `χ_T(x)=(−1)^{Σ_{i∈T}x_i}`:
  for any fixed `T`, conditioning all coordinates outside a pair `{i,j}⊆T` exposes a nonzero conditional
  covariance on `{i,j}`; and its `|T|`-coordinate marginal is non-SR. (Machine-checked at small `n`.)

## 4. Our reading — TENTATIVE, may be WRONG, do NOT let it constrain you (ignore if it's the bottleneck)

We spent several rounds and reached the interpretation below. **We flag it as soft** — it is exactly the
kind of synthesis that could be mis-framed (we already mis-stated F1 once). Treat it as one hypothesis.

- From C-μ4 we *believe* pairwise covariances (under positive external fields / Boolean conditioning)
  cannot certify SR — they see only the weaker Rayleigh property (F1, F4). From C-sym we *believe* "test
  real-stability of bounded conditional marginals" is also incomplete. So *if* both readings hold, a tester
  must use something beyond {pairwise covariances} ∪ {bounded marginals}.
- The symmetric measures in C-sym already evade both of those, and are testable (by us) **only** via the
  global rank statistic (F5), which exists **only because of symmetry**. So the question we got stuck on:
  > **Is there a NON-symmetric `Ω(1)`-far-from-SR `μ` that simultaneously (i) has all Boolean conditional
  > pairwise covariances `≤ 0` and (ii) has all bounded conditional marginals SR?**
  > If yes (+ a query lower bound) we'd guess (R−); if every such `μ` is "low-dimensionally estimable like
  > the symmetric case," we'd guess (R+) via a combined statistic generalizing the rank sequence.
- A heuristic we find suggestive (**unproven, possibly misleading**): SR is a condition on `Δ_{ij}` at
  *all real* points including off-orthant (`|x_i|>1`), where the relevant moment `E_μ[∏_{i∈S}x_i]` has
  variance `~(max_k|x_k|)^{2n}` — exponentially expensive to estimate — while SUBCOND cheaply sees only
  the bounded/orthant regime. This *might* point to (R−), or might be an artifact of our framing.

🔴 **None of §4 is established.** If a global low-degree / Fourier statistic, a spectral / HDX argument, a
real-stability certificate, a reduction, or a lower-bound technique resolves the problem while ignoring or
contradicting §4 — that is exactly what we want.

## 5. Deliverable + freedom

Resolve the SUBCOND query complexity of SR-testing: **(R+)** a `poly(n,1/ε)` tester (+ ideally a matching
lower bound) with complete soundness — it must reject NA / Rayleigh-but-not-SR distributions (F1, F3,
C-μ4); **or (R−)** a super-polynomial query lower bound (a planted-vs-far pair indistinguishable to every
adaptive `poly(n)`-query SUBCOND transcript, with the "far" side provably `Ω(1)`-far from SR).

**You have full freedom of method.** Use the symmetric reduction (F5) as a base case or ignore it; revisit
anything in §4 we call "dead" (we give the counterexamples in §3 — check them); bring any technique
(global low-degree/Fourier statistics, spectral / high-dimensional expanders, real-stability certificates,
reductions to/from known-hard problems, communication / planted-distribution / statistical-query /
learning-parity lower bounds). If our framing in §4 is the obstacle, say so and pivot.

**Return:** your resolution (R+ or R−) with full proofs, OR the furthest rigorous partial progress plus the
exact remaining gap; which facts you used; what you assumed vs proved; and your honest confidence. (For our
records, not a constraint on you: anything you produce will be independently human-verified — please make
proofs explicit and checkable.)
