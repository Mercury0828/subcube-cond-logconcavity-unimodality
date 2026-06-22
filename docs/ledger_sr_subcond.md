# Ledger — SR-SUBCOND (Testing Strong Rayleigh-ness in the Subcube-Conditioning Model)

> **Append-only research-line ledger** (guide §10). Re-read this + `PROJECT_STATE.md` + frozen artifacts
> before continuing — never work from memory. Nothing here is "proved": every bound/shape is a *claim to
> be established* by the external attacker (codex GPT-5.5-xhigh → web GPT-5.5-Pro), refereed by
> independent adversarial audits. "AI-verified ≠ proved" (guide §15).

---

## HEADLINE (current status — updated 2026-06-22 round 16; cold-start: read `RESEARCH_SUMMARY.md` first)
**16 attack rounds done (codex 1–7, web GPT-5.5-Pro 8–16). NO theorem yet; lean R+ ~55–60/40–45 — genuinely
open; the problem is now SHARPLY posed as two dual targets.** Bounds: `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n/ε²)`.
Route = **noisy-rank** (SR ⟺ every monotone-channel rank is Poisson-binomial). **Round 16 (BOTH audits clean,
ALL literature verified real): foundation now fully rigorous + both sides reframed crisply.** Proved: A6 closed
(`I_i(g_s)=𝔇(g_s)`); **exact two-block reduction** `d_TV(μ,SR)=d_TV(q,PB[a,b])` ⟹ `NR(g_s)=d_TV(g_s,SR)=
Θ(s^{−2})=Θ(√I_i)` rigorous; 🔴 **a genuinely entangled sparse-paving family defeating EVERY global channel**
(`NR=2^{−Ω(n)}`) + all ≤6-coord conditionals SR, poly-far from SR (a real lower bound vs all non-adaptive
bounded-arity testers) — but NOT R− (a fixed 8-coord excluded minor leaks on poly-fraction descendants).
**The problem is now: R+ ⟺ the CUT-OR-MINOR REMOVAL LEMMA** (`𝔇(h)≥η ⟹` a block `A` with `d_TV(L(|X∩A|),
PB)≥(η/d)^C`, OR a poly-likely `O(log(d/η))`-dim descendant inverse-poly-far from SR); **R− ⟺ an ASYMPTOTIC
pseudorandom excluded-minor family whose conditioning modulus degenerates in `d`** (+ adaptive SUBCOND
indistinguishability). **Round 17 (these two dual forks) = resume point.** 🔴 AI-disclosure unresolved.

### (historical) Phase 0 line
**Phase 0 — setup + kill-scan + C0 lean DONE. NO theorem, NO convergence, NO GO issued. STOP at human gate.**
TARGET (unproven): first `poly(n,1/ε)` SUBCOND tester for strong Rayleigh-ness on `{0,1}^n` **with a
matching lower bound** (a TIGHT characterization), OR a *proven* impossibility (RED-3). Open problem =
**C1** (local handle + tester / upper bound), with **C2** (matching lower bound) in parallel and **C3**
(pin the tight statement) pending. As of 2026-06-20: scaffold built; **kill-scan = GREEN / NO-SCOOP**
(primary + independent second-opinion, niche `(SUBCOND, SR)` open); SR facts confirmed (`P*`), barriers
B1–B3 verified; **C0 lean = a clean LOW-ORDER local handle looks doubtful (n=3 robust; n=4/order-4 open)**
(B3 real → attack C1 harder / non-locally + build C2 in parallel + weigh impossibility, NO-RETREAT). C1/C2 briefs written (NOT sent).
Pending: human gates (a)[no RED fired], (c) venue/scope; (b) not yet.

---

## 1. Frozen model / notation
(Ratify/amend in Phase 1 with a logged reason — guide §5.)

- **Ground set & distributions.** `μ` a distribution over `{0,1}^n` (subsets of `[n]`; equivalently
  `{-1,1}^n`). Generating polynomial `g_μ(z) = Σ_{S⊆[n]} μ(S) ∏_{i∈S} z_i` — multiaffine, degree ≤ 1 in
  each `z_i`.
- **Strong Rayleigh (SR).** `μ` is SR iff `g_μ` is **real stable** (no complex root `z` with
  `Im(z_i) > 0` for all `i`). SR ⊋ DPP ⊋ uniform spanning trees. Frozen structural facts → substrate
  `P*` (filled after Phase-0 special assignment (c)).
- **SUBCOND oracle.** A query is a partial assignment `ρ` fixing a subset `T ⊆ [n]` to `{0,1}` values;
  the oracle returns a sample from `μ` conditioned on the subcube `{x : x|_T = ρ}` (positive-probability
  assumed; degenerate-conditioning convention deferred to Phase 1). Query complexity = number of
  subcube-conditional samples. `T = ∅` recovers i.i.d. sampling.
- **Testing task (frozen target).** Given SUBCOND access to `μ` and `ε > 0`: **accept** if `μ` is SR;
  **reject** (w.p. ≥ 2/3) if `μ` is **ε-far** (in `ℓ₁` / TV) from every SR distribution. Tester uses
  `poly(n, 1/ε)` queries. Standard testing by default (tolerant flagged as a logged scope change).
- **Conjectured bound shape — CONJECTURAL, NOT a fact.** Idea phrasing: `Õ(n/ε^?)` upper, `Ω̃(√n/ε^?)`
  lower. As phrased that is a **GAP** (`n` vs `√n`) for one property, not a dichotomy (the internal
  muddle the fit reviewer flagged). **C3 must pin** one of: (i) `Θ̃(n)` with matching `Ω̃(n)`;
  (ii) `Θ̃(√n)` (SR cheaper than monotonicity via NA) with matching bounds; (iii) a genuine
  **variant dichotomy** (general SR `Θ̃(n)` vs a structured/uniform-SR sub-case `Θ̃(√n)`), mirroring
  monotonicity-vs-monotone-uniformity (2502.16355). "Tight" = matching upper+lower for the *stated*
  quantity, never an `n`-vs-`√n` gap relabeled.

---

## 2. Proven results / substrate — `P*`  ("use freely, do not re-derive")
> **CONFIRMED 2026-06-20** against Borcea–Brändén–Liggett "Negative dependence and the geometry of
> polynomials," arXiv:0707.2340 (J. AMS 22, 2009), via special assignment (c). Full quotes/numbers in
> `lit/SCAN_REPORT.md §3(c)`. Not folklore.

- `P1` *(CONFIRMED, BBL Prop 2.1 + §4)*: SR is **closed under subcube conditioning** (fixing a coordinate
  to 0/1, i.e. specialization `f|_{z_i=α}`, α≥0) and under **projection/marginalization** (`∂^S`) and
  external fields. *(Exact §4 closure-proposition number BLOCKED — ar5iv/PDF access; substance confirmed
  via Prop 2.1 + Oveis Gharan notes + arXiv:1602.05242. Do not cite a fabricated §4 number.)*
- `P2` *(CONFIRMED, BBL Thm 4.10)*: SR ⇒ CNA+ (the strongest negative association) ⇒ **NA**.
  🔴 **NA is necessary, NOT sufficient** for SR (NA strictly contains SR). **No named NA-but-not-SR
  counterexample with a theorem number was located in primary text** — C2/CS3 may need to *construct* one;
  do not assume a canonical BBL counterexample exists.
- `P3` *(CORRECTED 2026-06-21 — round-3 found a frozen ERROR; see N4 + `docs/guide_amendments.md`)*:
  μ SR ⇔ `g_μ` **real stable**. 🔴 **The real-stability criterion is `Δ_ij(g)=∂_i g·∂_j g − g·∂_i∂_j g ≥ 0
  on ALL of ℝⁿ** (equivalently: no root with all `Im(z_i)>0`). **`Δ_ij ≥ 0 on the positive orthant ℝ₊ⁿ`
  alone is the WEAKER "RAYLEIGH" property — Rayleigh ⊋ strongly Rayleigh.** The earlier framing
  (`Δ≥0 on ℝ₊ⁿ ⇔ SR`, copied from guide §5's "[0,1]^n") was WRONG. Witness: `μ_4` (N4) is Rayleigh
  (positive-orthant `Δ≥0`) but NOT real stable (a complex root). *(Even the all-real condition is global
  analytic, NOT a SUBCOND-observable local handle — building one remains C1's burden.)*
- `P4` *(engines, CONFIRMED as cited; use as engines to ADAPT, NOT transferring theorems)*:
  (i) **2502.16355** (STOC 2025) directed-isoperimetry → edge-tester bridge — its **Theorem 3** real-valued
  directed Talagrand inequality `E[(Σ_{i:x_i=−1}((f(x)−f(x^{(i)}))⁺)²)^{1/2}] ≥ Ω(1/√log n)·dist₁(f)`
  converts a **local edge-bias** statistic (measured on 1-dim subcubes) into a global `ℓ₁`
  distance-to-monotone bound; **no extension to SR / log-concavity / negative dependence is given** (→ `B3`).
  (ii) **2408.02347** (APPROX/RANDOM 2024) `Õ(n/ε²)` SUBCOND marginal/equivalence/product subroutines.
- `P5` *(identity REFEREE-VERIFIED; but its CONCLUSION was CORRECTED 2026-06-21)*: the identity
  **`Cov_{μ^λ}(X_i,X_j) = −(λ_iλ_j/g(λ)²)·Δ_ij(g)(λ)`** holds for `λ∈ℝ₊ⁿ` (verified). 🔴 **BUT the handle
  `V(μ)=sup_{i<j, λ∈ℝ₊ⁿ}(Cov_{μ^λ})₊` tests only the POSITIVE-ORTHANT condition = RAYLEIGH, NOT SR**
  (`V(μ)=0 ⇔ μ Rayleigh`, which is *strictly weaker* than SR — see corrected P3 + N4). Positive external
  fields `λ∈ℝ₊ⁿ` only probe `Δ_ij` on `ℝ₊ⁿ`; SR needs `Δ_ij≥0` on all real points, including negative
  ones, which positive fields **cannot reach**. ⟹ the whole positive-field covariance route is dead for
  SR (N4).
- `P6-candidate` *(audit-derived, correct-in-principle, poly-query OPEN — do NOT use as a working
  subroutine yet)*: `Cov_{μ^λ}(X_i,X_j)` is **SUBCOND-estimable without sampling `μ^λ`** — fix `X_B=t`
  (`B=[n]∖{i,j}`, Boolean), estimate `q_t(a,b)=P_μ(X_i{=}a,X_j{=}b|X_B{=}t)` + `P_μ(X_B{=}t)`; the tilt is
  deterministic post-processing. 🔴 **Naively exp(n)** (sum over `t∈{0,1}^B`) + variance blowup from large
  λ — making this **poly(n)-query** is exactly the open witness-localization problem. So codex's
  "SUBCOND can't reach external fields" obstruction is **refuted in principle**, but `poly`-query is unproven.

---

## 3. Refuted routes — `N*`  ("do NOT attempt", each with the killing reason)
> 🔴 **CORRECTION (round 8, Pro):** N4/N5 below correctly show the *covariance* and *bounded-marginal*
> handles are individually incomplete — BUT my earlier reading that the witnesses (`μ_4`, the symmetric
> spread example) "defeat all poly statistics / lean toward impossibility" was WRONG: both are caught by
> the **universal rank test** (round-8 §1; `rank(μ)∈PB_n` necessary for SR). The covariance/marginal
> routes are still dead *as standalone handles*, but they are not impossibility evidence. See "after round
> 8" in §5.
- **`N1` (refuted obstruction, round 1):** "SUBCOND cannot estimate external-field-tilted covariances
  `Cov_{μ^λ}`" — **FALSE** (`P6`: Boolean conditioning + deterministic λ-reweighting). The open issue is
  *poly-query localization*, not reachability. Do not re-assert the reachability obstruction.
- **`N2` (unsound tester, round 1):** any tester certifying only pairwise / conditional-pairwise(Boolean)
  / marginal / NA statistics — accepts NA-but-not-SR (CS3 / C0 family F2). Necessary but not sufficient.
- **`N3` (refuted localization, round 2 — REFEREE-VERIFIED counterexample):** **sparse / bounded-support
  external-field witness families cannot localize.** The even-parity slice `μ_n` (uniform on `{Σx_i even}`)
  is `≥1/8`-far from SR yet has `Cov_{μ_n^λ}(X_i,X_j)=0` for **every** field whose non-unit support omits
  even one off-pair coordinate (closed form `Cov ∝ ∏_{k≠i,j} r_k`, `r_k=(1−λ_k)/(1+λ_k)`). ⇒ any
  `o(n)`-support / `O(log n)`-support witness family misses `μ_n`. *(Details: `round2_response_C1.md`.)*
- **`N4` (route death, round 3 — REFEREE-VERIFIED; the big one):** **the entire positive-external-field /
  Boolean-conditioning PAIRWISE-COVARIANCE route cannot test SR** — it certifies only the weaker RAYLEIGH
  property. Witness `μ_4` (`a=(1,2,2,2,1)/30`, `g_4=1+2e_1+2e_2+2e_3+e_4`): `Δ_ij>0` on all of `ℝ₊⁴` (so
  every positive-field & Boolean-conditioning pairwise covariance is ≤0, looks SR) but `g_4` has a complex
  root (`t+1/t=−4+√6`) ⟹ not real stable ⟹ **not SR**, and `d_TV(μ_4,SR)≥1/7200`. Lift
  `μ_4×Ber(½)^{⊗(n−4)}` keeps a constant-far Rayleigh-not-SR instance invisible to all positive fields.
  ⇒ (T)/(T′)/(T″) all die at the root. *(Details: `round3_response_C1.md`; literature cross-check in
  `round3_audit_C1.md`. NOTE this makes `P6` — estimability of tilted covariances — MOOT for SR.)*
- **`N5` (handle death, round 4 — REFEREE-VERIFIED de-risk):** the **bounded-marginal real-stability
  handle (T‴)** is **INCOMPLETE for any fixed `k`**. Via the symmetric/GWS reduction (SR ⇔ rank polynomial
  `Σ C(n,k)a_k t^k` real-rooted), an explicit symmetric measure (e.g. n=6, `a=[0.51,0.79,1,0.93,0.54,0.23,
  0.059]`, global roots `−3.18±1.13i`) is **far-from-SR yet has EVERY `≤k`-coord conditional+projected
  marginal SR** (verified k≤4; families found up to n=12). The violation is **global/spread**, invisible to
  any bounded marginal. *(Details: `derisk/results/windows_search_finding.md`.)* 🔴 **Caveat:** these are
  *symmetric* (n+1 rank params) ⟹ still poly-SUBCOND-testable via the GLOBAL rank statistic — so N5 kills
  the bounded-marginal *handle*, NOT SR-testability. The genuine RED-3 needs a *non-symmetric* spread family.

---

## 4. Barriers in force — `B*`  (pre-seeded; verify exact statements in Phase-0 scan)
- **`B1`** — **VERIFIED 2026-06-20** (2008.03650 Thm 2, NeurIPS 2020): any (ε,0.99)-DPP-tester with
  **i.i.d. sample access** needs `Ω(√N/ε²) = Ω(2^{n/2}/ε²)` samples — **genuinely exponential in `n`**;
  hardness extends to log-submodular. ⇒ a `poly(n)` SUBCOND tester **must genuinely use conditional
  access**; anything reducible to i.i.d. sampling cannot beat `B1`. *(No longer assumed — exact statement
  quoted in `lit/SCAN_REPORT.md §2`.)*
- **`B2`** — Deciding M-convexity of a **given quadratic** set function is **co-NP-complete**
  (arXiv:1704.02836, Iwamasa). ⇒ target = **SR (subcube-closed) as a distribution-testing task**, NOT
  exact M-convexity recognition. *(State precisely; not a vague "all M-concavity is hard".)*
- **`B3`** — **No known local/edge characterization or directed-isoperimetry for SR** ⇒ the local handle
  must be **built** (C1), and the "mirror the monotonicity bound shape" move is **conjectural**, not a
  transfer. *(The single live-or-die point — guide READ FIRST / §16 risk 1.)*

---

## 5. The exact open problem (as currently reduced)
- **C1 (primary, R+):** a usable **local / isoperimetry-style inequality** for SR on `{0,1}^n` +
  conversion into a `poly(n,1/ε)` SUBCOND tester with a proven **upper bound** (sound against non-SR
  distributions that pass marginal/pairwise statistics — CS3). OR a *proof* that no `poly(n)` SUBCOND SR
  tester exists (→ RED-3 impossibility headline; a proof that no *local handle* exists is NOT RED-3, only
  YELLOW-a).
- **C2 (parallel):** a Yao-minimax **planted-vs-uniform** (SR-vs-far) hard instance forcing a lower bound
  that **matches** C1. "Far" instances must be **provably ε-far from SR** (#1 audit check).
- **C3 (pending):** resolve §1 (i)/(ii)/(iii); state the honest tight characterization; never a gap as a
  dichotomy.

**#1 audit check throughout:** does a step secretly assume a local handle never established, or certify
*product / pairwise-NA* instead of *SR*?

### C1 — sharpened crux after round 1 (2026-06-21)
The global handle `P5` (`V(μ)=0⇔SR`) + the estimability reduction `P6-candidate` reduce C1 to a single
named open theorem (the make-or-break for the upper bound):
> **Robust external-field witness-localization theorem (OPEN):** does `d_TV(μ,SR) ≥ ε` force a witness
> `(i,j,λ)` with `Cov_{μ^λ}(X_i,X_j) ≥ poly(ε,1/n)` **AND** `λ` of **bounded support / bounded magnitude /
> low-dimensional reweighting** — so the exp-many-`t` reweighting in `P6-candidate` collapses to `poly(n)`
> SUBCOND queries? Or prove no such localized witness exists (→ pushes toward the impossibility/lower-bound
> route).
Candidate attacks (NOT mandates): adapt a Talagrand/local-to-global inequality to the Rayleigh-difference
functional (2502.16355 engine); random-restriction tilt-localization (1911.07357; entropic independence
2204.02570); bounded-field poly-grid reduction; slice-and-dice tilted-covariance estimators (2506.18444).

### C1 — after round 2 (2026-06-21): sparse localization REFUTED (N3); target re-sharpened to (T′)
- **(T′) OPEN:** does a poly-size family of **LOW-PARAMETRIC, FULL-SUPPORT** fields (e.g. the `O(1)`-param
  "uniform `δ` on the complement of `{i,j}`" family — which catches `μ_n` at `δ=1/n²`) localize the
  witness for *every* ε-far `μ`, AND is each such tilted covariance **poly(n)-SUBCOND-estimable**?
- 🔴 **Synthesis (CORRECTED by the round-2 audit — the obstruction is SUPPORT, not PARAMETRIC dimension):**
  - **Boolean-conditioning-only** (the C0 statistic `S1`): catches `μ_n` (`Cov(X_i,X_j|X_B=t)=+1/4`) but
    is **blind to F2** (C0).
  - **sparse-SUPPORT fields:** catch F2-type interior violations but are **blind to `μ_n`** (N3).
  - 🔴 **BUT** `μ_n` is caught by a **1-parameter FULL-support tilt** (C4: `λ_k=δ` ⇒ `Cov≈1/4`) — so the
    refutation kills only *low-support*, NOT *low-parametric*. *(Round-2 read, now SUPERSEDED.)*
  - ⛔ **SUPERSEDED BY ROUND 3 (N4):** the round-2 "complementary blind spots ⇒ jointly sufficient ⇒ leans
    toward a poly tester" synthesis is **FALSE**. `μ_4` (Rayleigh-not-SR) is a **single** family blind to
    **BOTH** {Boolean conditional pairwise covariances} **and** {all positive-field tilted covariances} —
    because both are *positive-orthant* statistics and `μ_4` is Rayleigh. **The entire covariance route is
    dead (N4).** The new handle is conditional-marginal SR-testing (see "C1 — after round 3").
- **HARD-INSTANCE note for C2 (deferred):** plain `μ_n` is **too easy** for a lower bound (one *full*
  Boolean conditioning detects it, O(1) queries). A real lower bound needs a **hidden-random-parity**
  planted family (random affine subspace / random target parity) so no fixed conditioning aligns with the
  planted constraint. **C2 is held until round-3 settles the (T″) upper-bound reformulation** (audit:
  the lower bound is only needed if (T″) fails).

### C1 — after round 3 (2026-06-21): covariance route DEAD (N4); REDIRECT to conditional-marginal SR-test
🔴 **The covariance handle was testing the WRONG property (Rayleigh, not SR).** (T)/(T′)/(T″) are dead at
the root (N4). **New handle / target (T‴):** test **real stability (SR) of conditional low-dimensional
marginals**, not pairwise covariances. Define
`𝒮‴ = { SR-test of μ(X_W | X_T=ρ) : Boolean (T,ρ), |W| = O(1) or O(log n) }` (real-stability of a
fixed-size multiaffine polynomial is decidable).
- **(T‴) OPEN:** is SR **locally testable on conditional marginals** — `d_TV(μ,SR) ≥ ε ⟹` some bounded
  conditional marginal is `Ω(poly)`-far from SR-on-`W`, with `poly(n)` SUBCOND queries?
- Why it's promising: `μ_4` caught (its 4-bit marginal is non-SR); `μ_n` caught (a conditional `{i,j}`
  marginal is non-SR after deep conditioning); F2 plausibly caught (its real-stability violation should
  surface in some conditional marginal — to check).
- 🔴 **The obstruction to watch (the new RED-3 candidate):** a family that is far-from-SR but whose **every
  bounded conditional marginal is SR** (a *spread-out / global* real-stability violation, like parity is
  for the unconditioned marginals). If such a family exists and defeats poly-query conditioning, that is
  the impossibility (lower bound). The round-3 audit is checking whether such a family is obvious.
- Status: covariance route dead but **NOT impossibility** — a genuinely different (marginal-SR) handle is
  open. Attack (T‴) next (round 4). NO-RETREAT: this is a redirection within the upper-bound attack, not a
  downgrade.

### C1 — after round 4 (2026-06-21): bounded-marginal handle ALSO dead (N5); refined dichotomy
🔴 **Two natural handle classes are now dead:** covariance (N4, `μ_4`) and bounded-marginal (N5, symmetric
spread). The SR-violation can be hidden from BOTH all positive-field covariances AND all bounded conditional
marginals. **Refined dichotomy (the real frontier):**
- **(A) upper bound survives ONLY via a GLOBAL low-dimensional statistic.** For *symmetric* measures the
  rank sequence (`n+1` numbers, SUBCOND-estimable) works — SR ⇔ its real-rootedness. **OPEN:** does a
  `poly(n)`-dimensional SR-determining statistic exist for **general (non-symmetric)** measures? (The
  general analogue of the rank sequence is the full low-degree moment/Fourier profile — `exp(n)` a priori.)
- **(B) impossibility / RED-3 (leading candidate, better supported):** a **NON-symmetric** measure whose
  SR-violation is **spread** (off-orthant, à la `μ_4`) over a high-dimensional mode so that **no `poly(n)`
  SUBCOND statistic** (no covariance, no bounded marginal, no estimable global low-dim profile) detects it,
  with a Yao-minimax indistinguishability vs a planted SR distribution. The symmetric route CANNOT produce
  this (symmetric = low-dim = estimable); a **hidden-random-subspace lift of a `μ_4`-type violation** is the
  natural construction.
- 🔴 **Round-5 CORRECTION to the lean (honesty — I had over-leaned toward (B)):** every concrete
  hard-instance attempt is **caught by SOME poly(n) statistic** — `μ_4` by the bounded-marginal SR-test;
  symmetric N5 by the **global rank statistic** (sample & histogram `|S|`, poly-query); parity/linear codes
  by **Boolean conditioning** (`Cov(x_0,x_1|x_{rest}=0)=0.25`, verified). **NO instance yet defeats
  covariance AND bounded-marginal AND global-low-dim simultaneously.** So the evidence is **roughly
  NEUTRAL**, if anything **mildly toward (A)** (a *combined* multi-mechanism tester may exist), NOT toward
  impossibility. The honest state: **the dichotomy is genuinely OPEN; neither side is favored.**
- **(A) candidate (combined tester):** `{all-depth Boolean conditional ≤k-marginal SR-tests} ∪ {global
  weight/symmetric-type statistics}`. Completeness UNPROVEN. **(B) candidate (RED-3):** an instance
  defeating ALL of these — UNCONSTRUCTED; every attempt so far is caught. Both are hard & open.
- Per NO-RETREAT/§4: attack both at full force; RED-3 needs a *proven* `n^{ω(1)}` SUBCOND lower bound,
  (A) needs a *proven* completeness + tester. Round 6 attacks the combined-tester completeness (the
  higher-EV move given no all-defeating instance exists yet) while keeping the (B) construction alive.

### 🔴 THE CRUX (precisely stated after 7 rounds — the single make-or-break question)
> **Does there exist a distribution `μ` on `{0,1}^n` that is `Ω(1)`-far from SR yet is invisible to BOTH
> (i) every Boolean conditional pairwise covariance `Cov(x_i,x_j|x_T=ρ)` (i.e. `μ` is "conditionally
> Rayleigh" — like `μ_4`) AND (ii) every bounded conditional marginal SR-test (`|W|=O(1)` — i.e. all
> small marginals SR, like the symmetric N5 spread) — AND is not low-dimensionally estimable (non-symmetric)?**
- **YES + a query lower bound ⟹ (B)/RED-3 impossibility.** **Provably NO ⟹ the combined tester (A) is
  complete ⟹ poly tester.** Both are SODA-grade; this single dichotomy decides the project.
- **Status after 7 rounds — the crux SHARPENS to a SYMMETRY question.** Correction to an earlier
  mis-statement: the **symmetric N5 examples ALREADY evade both (i) and (ii)** (all their bounded conditional
  marginals are SR ⟹ all conditional pairwise covariances ≤0 = conditionally Rayleigh, AND all `O(1)`
  marginals SR). They are caught ONLY by **(iii) the global rank statistic** (`|S|`-sampling), which works
  *only because of symmetry*. Every NON-symmetric candidate so far is caught by (i) or (ii) (`μ_4`→(ii);
  char `χ_T`→(i)/(ii); parity/codes→(i)). So:
  > **SHARPENED CRUX: can the symmetry of an evade-(i)+(ii)+far measure be BROKEN?** — is there a
  > **NON-symmetric** `Ω(1)`-far-from-SR `μ` evading (i)+(ii) (hence also (iii), a symmetric-only statistic)?
  - **Symmetry ESSENTIAL** (every evade-(i)+(ii)+far `μ` is low-dim/symmetric-like, estimable) ⟹ combined
    tester {(i)+(ii)+(iii)} **complete ⟹ (A) poly tester.**
  - **Symmetry BREAKABLE** (a non-symmetric evade-both exists) + a query lower bound ⟹ **(B)/RED-3.**
  - Next experiment (engineering): asymmetrically perturb an N5 measure; does it still evade (i)+(ii)+far?
    codex leans 70% "not usefully breakable" (⟹ impossibility, no-compression for non-symmetric) — NOT proven.
    This is the precise, hard, OPEN research core of the project.

### C1/RED-3 — after round 8 (web GPT-5.5-Pro, 2026-06-21): substrate CORRECTED + an R+ framework + a new LB
> All Pro-produced. **BOTH AUDITS DONE:** (1) upper-bound machinery (§1–§5) **AUDIT-CLEAN** — all 5 claims
> CORRECT, no FATAL/GAP (`round8_audit_machinery.md`); (2) lower bound (§7) **CORRECT as argued** — one
> FRAMING gap (it is AFL's product construction with SR-distance bookkeeping; `ε⁻¹` vs AFL's `ε⁻²` is a
> distance-notion artifact, NOT a strengthening; the SR-specific content is the closure-based far-from-SR
> upgrade in step (b)) + MINOR write-up items (`round8_audit_lowerbound.md`). Still pending HUMAN
> verification ("AI-verified ≠ proved"). Full reply: `round8_pro_response.md`.
- 🔴 **CORRECTION to my framing (the owner was right that some of my claims were wrong):**
  - **The rank statistic is UNIVERSAL, not symmetry-specific.** For ALL SR μ, `R_μ(t)=g_μ(t,…,t)` is
    real-rooted ⟹ `|X|` is **Poisson-binomial**. So `d_TV(μ,SR) ≥ d_TV(rank μ, PB_n)` for every μ, and
    this is `O(n/τ²)`-sample testable. ⟹ **μ_4 and the symmetric C-sym example are BOTH caught by the
    universal rank test** (their rank PGFs are non-real-rooted). My N4/N5 "these defeat all poly statistics"
    narrative was over-pessimistic — it missed the universal rank test. [Referee-verified: μ_4's rank PGF
    `1+8t+12t²+8t³+t⁴` is non-real-rooted ✓.]
  - **Off-orthant violations are COMPACTIFIABLE** (projective certificate, §2): coefficient-reversal maps
    any real witness into `[−1,1]^{n−2}`; `g` real stable ⟺ `V(g)=0`. So my "off-orthant is intrinsically
    hard to estimate" was incomplete — the real issue is *margin size* (can be exp-small, parity §6), and
    SUBCOND *conditioning amplifies* a rare-face violation.
- **New results (pending audit):** P-Pro-1 rank-PB universal necessary test; P-Pro-2 projective certificate
  `V(g)=0⟺SR`; P-Pro-3 **robust signed-witness tester (Thm 3.1): `O((d log(d/γ)+log 1/δ)/γ²)` SAMPLES,
  rejects `V(h)≥γ`** (poly-QUERY whenever the margin γ is inverse-poly; offline computation exp);
  P-Pro-4 conditional aggregation `d_TV(μ,SR) ≥ ¼ E_r[V(μ_r)]`; **new lower bounds `Ω(√n/ε)` (anti-product
  blocks + AFL exact SUBCOND→iid simulation + χ²) and `Ω(1/ε²)`**; `O(2^n/ε²)` upper bound.
- **The sharpened open problem (replaces my "symmetry question"):**
  - **(R+)** the **conditional-stability removal lemma**: if `d_TV(μ,SR) ≥ ε`, then either rank law is
    inverse-poly-far from `PB_n`, OR a poly-query procedure finds a positive subcube `E` with `V(μ|E) ≥ γ`
    (inverse-poly `β,γ`); ideally a random-restriction statement. Then Thm 3.1 + aggregation ⟹ poly tester.
  - **(R−)** full-support YES/NO ensembles, every NO `Ω(1)`-far, indistinguishable to all adaptive
    poly-query SUBCOND transcripts — **must HIDE the amplifying face**, not just an exp-variance moment.
  - The 3 known examples (C-sym→rank; μ_4→constant `V`; parity→constant pair-conditional `V`) all fit the
    (R+) dichotomy; missing = a theorem they are representative. **This is the new make-or-break.**

---

## 6. Confidence trend (first-class signal — guide §9)
| date | C1 (tester/upper) | C2 (matching lower) | note |
|---|---|---|---|
| 2026-06-20 | unset (pre-attack); **C0 leans the local-handle route is doubtful** | unset (pre-attack); C2 not yet attacked | Phase-0 setup; no attack round run. Seed only. C0 lean (no clean low-order local handle) is a routing signal to attack C1 *harder / non-locally* and weigh impossibility — **NOT** a confidence drop on a run thread, and NOT a downgrade (NO-RETREAT §15). A sustained drop *during the attack loop* ⇒ escalate / fresh-agent (attack harder), NEVER downgrade. |
| 2026-06-21 (round 1) | **modestly UP vs C0 pessimism.** codex: OPEN, no tester (82% "frozen facts insufficient") — but the audit **refuted codex's blocker**: tilted pairwise covariances `Cov_{μ^λ}` ARE SUBCOND-estimable (Boolean conditioning + deterministic λ-reweighting; no rejection sampling). Estimation half reduces to Boolean conditioning; crux cleanly isolated = the **witness-localization theorem**. | not yet (codex round-1 C2 running) | Round 1 = GAP-level **progress**, not a stall. The global handle `V(μ)=0⇔SR` is referee-verified (corrected identity, F1). Route forward: sharpen upper bound (bounded-support λ witness theorem). NOT escalating yet (K_stall=2; this is round 1 with real progress). |
| 2026-06-22 (round 16, web GPT-5.5-Pro) | **Foundation made RIGOROUS + both sides reframed (lean ~55–60/40, holds).** BOTH audits clean, **ALL matroid-HPP literature VERIFIED REAL** (Kummer–Sert "22 rank-4/8 non-HPP"; "≤6-element ⟹ HPP", smallest non-HPP=Fano F_7). Proved: A6 `I_i(g_s)=𝔇(g_s)`; **exact two-block reduction** `d_TV(μ,SR)=d_TV(q,PB[a,b])` (referee-verified backbone on n=4) ⟹ `NR(g_s)=d_TV(g_s,SR)=Θ(s^{−2})=Θ(√I_i)` rigorous. 🔴 **a genuinely entangled sparse-paving family**: poly-far from SR, `NR=2^{−Ω(n)}` (defeats EVERY global channel — global channel pseudorandomness is EASY, even in matroid measures), all ≤6-coord conditionals SR. | bounds unchanged; **+ a real lower bound vs all non-adaptive bounded-arity testers.** | 🔧 The σ_min/global-channel route is INSUFFICIENT (the sparse-paving family kills it). **R+ ⟺ CUT-OR-MINOR removal lemma** (cut: a block rank stat far from PB; OR minor: a poly-likely `O(log)`-dim far descendant) — fair target, **small-minor branch + exhaustiveness UNPROVEN**. **R− ⟺ a degenerating-margin asymptotic excluded-minor family** (fixed-size classifications can't supply it; "one conceptual step away"). Not closed. |
| 2026-06-22 (round 15, web GPT-5.5-Pro) | 🔑 **The candidate hard core `g_s` is SETTLED FAVORABLY ⟹ lean UP to ~58–62/40.** `NR(g_s)=Θ(s^{−2})`, `I_i(g_s)=Θ(s^{−4})` ⟹ **`NR(g_s)=Θ(√I_i)`** (referee-verified: Toeplitz eigenvalue formula exact, exactly 1 negative eigenvalue, `σ_min≥θ²/20`). An explicit **fully interior** channel (margin `Θ(s^{−3})`) exposes it; `g_s` + all tensor/padded/permuted lifts ruled out as R−. | bounds unchanged. | 🔧 **Certificate CORRECTED:** `[−det]/k^{k/2+1}` is WRONG (`g_s` det `=e^{−Ω(s)}` but `σ_min=Θ(s^{−2})`, referee-verified `-4e-8…-9e-122`); robust object = **negative Toeplitz section with poly `σ_min`** (Lemma 1.1). **Corrected target (§7):** `I_i≥η ⟹` descendant with covariance `≥(η/d)^C` OR negative Toeplitz section `σ_min≥(η/d)^C`. **Only remaining R− hope = a GENUINELY ENTANGLED obstruction.** Not closed. |
| 2026-06-22 (round 14, web GPT-5.5-Pro) | 🔴 **CORRECTION — the orchestrator's proposed R+ route is REFUTED ⟹ lean DOWN to ~55–60/40.** Pro proves a constant-depth complex root can be `2^{−Ω(d)}`-close to PB (Thm 2.1 + an explicit `Bin(d,½)`-perturbation family with root at `−1+i/2`), **even through a fixed bounded channel `(0.1,0.9)`** (referee-verified d=4,8,16). So "root depth ⟹ poly PB-distance" is FALSE; `μ_4` worked only at fixed degree 4. Also: PF-minor bound `d_TV(q,PB)≥v/k^{k/2+1}` (Thm 3.1); an Ω(1)-far family with `NR=2^{−Ω(d)}` (Thm 4.1, but NOT R− — 2-faces show positive covariance ⟹ localization catches it); flip-swap localizes Hellinger, not the compatibility gap `I_i` (Thm 5.1, §5). | bounds unchanged. | **Target CORRECTED (root → normalized PF minor):** `I_i≥η ⟹` a poly-discoverable descendant has covariance `≥(η/d)^C` OR a Toeplitz minor `[−det]_+/k^{k/2+1}≥(η/d)^C`. Needs a **compatibility-aware total-positivity localization** theorem (spectral independence alone insufficient). `g_s` (non-SR parent, SR proper conditionals) = the candidate hard core. **Honest:** my round-13 μ_4→R+ extrapolation was too optimistic. Still moderate R+. Not closed. |
| 2026-06-21 (round 13, web GPT-5.5-Pro) | **Channel-degeneracy doubt SOLVED + class rates proven ⟹ stronger R+ lean.** Thm 1.1 (regularization): a defect-`τ` channel ⟹ a BOUNDED channel (params `Ω(τ/d)` from 0/1) keeps `Ω(τ)` defect — kills the audit's main doubt. Thm 2.1: sharp PB separation `d_TV(q,PB)≥(Φ/15)^{3/2}` (referee-verified). Thm 3.1: positive covariance `κ ⟹ NR≥(κ/15)^{3/2}`. **Thm 4.1: full NR-rate for PRODUCT children** (`NR≥I₀³/poly(d)`, α=1/3). Thm 5.1: homogeneous children — a SUBCOND-*search* witness (honestly downgraded). | bounds unchanged. residual = arbitrary nonproduct nonhomogeneous incompatibility. | **The precise residual (34):** `I_i≥η ⟹` EITHER a poly-likely descendant has positive covariance `poly(η/d)`, OR a bounded channel sees a **negative higher Toeplitz/PF minor** poly-large. (Thm 2.1 = the quadratic case; missing = higher-order.) 🔎 **REFEREE TEST:** `μ_4` (Rayleigh-not-SR) has worst cond. covariance `=0` (evades §3) **but IS caught by a BOUNDED channel** `(0.1,0.55)` (noisy-rank roots `−1.90±0.72j`, non-PB) — the higher-order (34) obstruction exposed with constant margin ⟹ **strong concrete evidence for R+.** **AUDIT DONE (`round13_audit.md`): ALL proofs CORRECT** (regularization, sharp PB sep, product/homogeneous rates); the audit's own "decisive test" = the μ_4 finding (it converged) ⟹ μ_4 NOT an R− instance. **Leans R+ ~70/30.** Residual = the GENERAL (34). Not closed. |
| 2026-06-21 (round 12, web GPT-5.5-Pro — OPENNESS RESET) | **A cleaner R+ ROUTE that abandons V/QHB/interlacer entirely.** **Thm 1.1:** `μ` SR ⟺ for EVERY monotone product channel `K`, the noisy rank `\|Y\|` is Poisson-binomial (Möbius UHP-self-maps preserve stability). `NR(μ)=sup_K d_TV(L\|Y\|,PB_n) ≤ d_TV(μ,SR)`, **estimable in `Õ(n/τ²)` samples over ALL channels**, **strictly stronger than projected ranks** (referee-verified 3-bit example). + **two NEW R− obstructions:** Thm 6.1 product tangent rigidity (kills the Paninski high-degree-perturbation route — SR tangent at a product has Fourier degree ≤2); Thm 7.2 homogeneous-selector localization (down-up spectral gap ≥1/k exposes the link discrepancy). | bounds unchanged `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n)`. | **NEW R+ bottleneck (44): `I_i(h) ≤ poly(d)·NR(h)^α`** — every rejecting statistic is now a 1-D rank-vs-Poisson-binomial distance (no `V`, no interlacer cone). Cleaner + more probabilistic than UQHB. **AUDIT DONE (`round12_audit.md`): Thms 1.1/3.1/6.1/7.2 ALL CORRECT (sympy + literature); both new R− routes validly killed.** Claim 6 = GAP: (44) **partially escapes** the wall (channel-optimization ≠ worst-case cone) but NOT proven full — the root→channel construction is qualitative (`L→∞` degenerate); **the precise remaining crux = the `η→NR` rate independent of channel degeneracy** (does a localized `I_i≥η` give a BOUNDED channel `L=poly` with `NR≥poly(η)`?). **Cautiously R+.** Not closed. |
| 2026-06-21 (round 11, web GPT-5.5-Pro) | **UQHB PROVED for the product-children class + easy refuters ELIMINATED ⟹ leans more firmly R+.** Thm 2.1: `Gap_λ(a_p,b_q) ≤ 2(d−1)√(Ξ_λ)` (α=1/2, witnesses `Δ_{0k}=sδ_k`, `Δ_{rk}=−stδ_rδ_k`, explicit compatible repair). Thm 1.1: exact common-factor invariance (`Gap,Ξ` unchanged by independent SR factors). Lem 4.1: perturbation continuity. | conditional tester (if α=1/2 global): `Õ(n^{10}/ε^{10})`, LB `Ω(max{√n/ε,1/ε²})`. **Refuter spec sharpened:** stable irreducible `(a_d,b_d)` with `Gap≥d^{−O(1)}`, `Ξ=d^{−ω(1)}`, not near a compatible tensor model — the ONLY surviving R− route. | **Tensor-padding & small-perturbation refuters are DEAD** (Thm 1.1 + Lem 4.1). Residual = a single named real-AG question: **degree-uniform Hellinger/metric-regularity error bound for the Wronskian map on irreducible interlacer cones** — literature (KPV, Saunderson, amenability) is SILENT. **AUDIT DONE (`round11_audit.md`): ALL CORRECT** — witnesses numeric-verified; repair SR-ness + δ_k>0 cost confirmed; the V-normalization doubt RESOLVED (V is the raw cube-max, no denominator). Hyperbolicity cones ARE amenable but κ not poly-in-`d` (the exact gap). **Lean: cautiously R+.** Not closed. |
| 2026-06-21 (round 10, web GPT-5.5-Pro) | **All 3 round-9 GAPs CLOSED + the problem reduced to a precise real-AG question.** PROVED (referee-spot-checked + audit pending): exact `V` normalization & `V=0⟺SR`; **d=2 constant `I_i≤4V`**; **exact tensorization `V(pq)=max{V,V}`** (Lem 5.2 now proven); **the EXACT variational formula `I_i=(1−λ)A(a)²+λA(b)²−A_d(h)²`** [REFEREE-VERIFIED] — `I_i` = affinity loss from forcing the children's stable approximations to be *compatible*; **nonuniform QHB in every fixed `d`** (`I_i^{N_d}≤K_d V`, semialgebraic Łojasiewicz). | the EXACT remaining inequality: **dimension-uniform** `Gap_λ(a,b) ≤ poly(d)·Ξ_λ^α` (uniform conditioning of the interlacer/compatibility gluing) — connects to **Kummer–Plaumann–Vinzant** interlacer cones (1212.6696) + Wagner–Wei. | 🔴 **CORRECTS my R− lean:** sporadic/fixed-dim excluded minors **cannot** refute QHB (a Hölder modulus exists in each fixed `d`); **R− needs an ASYMPTOTIC family with Hölder exponent→0**. To evade the strengthened rank test W1, **every** projected `\|X∩A\|` must be PB-close (not just total). **AUDIT DONE (`round10_audit.md`): all claims CORRECT** (d=2, tensorization, variational formula symbolically verified; Łojasiewicz doubly-exp confirmed; KPV confirmed; my R− lean correction confirmed). **Both Pro + audit now lean WEAKLY R+** (exact-multiplicative tensorization, clean d=2) but the load-bearing uniform inequality (5a) is genuinely OPEN — no proof/strategy; literature silent. Not closed. |
| 2026-06-21 (round 9, web GPT-5.5-Pro) | **The whole problem REDUCED to ONE clean question: QHB** (a quantitative Hermite–Biehler / excluded-minor inequality `I_i(h) ≤ poly(d)·V(h)^α`). Prove QHB ⟹ R+ poly tester; a robust counterexample (PB rank + super-poly-small conditional margins) ⟹ R−. **Proved:** strengthened projected-rank test; a localization theorem that **BLOCKS the rare-hidden-face R− strategy**; QHB⟹R+; **QHB in d=2**; an explicit minor-minimal family `g_s` (non-SR, every proper conditional SR) satisfying *linear* QHB. | `g_s` tensor `μ_s` (constant-far, PB rank, all cond. pairwise covs ≤0, all `o(n^{1/5})`-dim conditionals SR) — NOT a (L)-counterexample (`V=Ω(n^{−4/5})`). §6 gives the EXACT bar a real R− construction must clear. | **`g_s` core REFEREE-VERIFIED.** Analytic AUDIT DONE (`round9_audit.md`): localization §2 + QHB⟹R+ §3 CORRECT (the rare-face R− route is rigorously DEAD); Wagner–Wei confirmed. **2 GAPs, both = pinning the normalization of `V`** (d=2 constant; Lem 5.2 `q²≤1` tensoring) — fixable, but load-bearing. **Confidence: my audit leans QHB FALSE at dimension-uniform strength (⟹ R−, due to irregular minor-minimal HPP obstructions); Pro leans DIVIDED. Genuinely OPEN.** Not closed. |
| 2026-06-21 (round 8, web GPT-5.5-Pro) | **MAJOR progress + corrects 2 of my errors. Bounds: `Ω(max{1/ε²,√n/ε}) ≤ Q ≤ O(2^n/ε²)`.** 🔴 **CORRECTION-1: the rank statistic is UNIVERSAL** — for ALL SR μ, `rank(μ)=|X|` is Poisson-binomial (`g_μ(t,…,t)` real-rooted); so μ_4 AND C-sym are caught by the universal rank test (my "symmetry-specific" claim was WRONG). 🔴 **CORRECTION-2:** off-orthant violations are **compactifiable** (projective certificate), not intrinsically hard (my off-orthant heuristic was incomplete). Plus: a robust signed-witness tester (poly-query if margin inverse-poly), conditional aggregation lemma, a NEW `Ω(√n/ε)` lower bound. | new `Ω(√n/ε)` SUBCOND lower bound (anti-product blocks + AFL exact simulation + χ²) and `Ω(1/ε²)`. **Audit running (2 agents): lower bound §7; upper machinery §1–§5.** | **Shifts toward (R+) being MORE plausible** than my over-pessimistic read: the rank test + signed tester + aggregation form a real R+ framework; the ONLY gap is a *conditional-stability removal lemma* (when margin is exp-small but conditioning amplifies — the parity case). NOT closed either way. Pro confidence: high on lemmas/LB, LOW on R+ vs R−. Pending audit + human verification. |
| 2026-06-21 (round 7) | **the single-hidden-character RED-3 construction FAILS (referee analysis).** `NO=uniform+ε·χ_T` (random parity `T`) is caught EITHER way: `|T|=O(1)` ⟹ checking all `C(n,O(1))=poly` marginals finds T's non-SR marginal; `|T|` large ⟹ conditioning all-but-2 coords reveals any free pair `⊆T`, and `~(n/|T|)²=poly` random tries hit one. So a *single* character is detected by the **combined tester** (bounded marginals + deep-conditioning pair covariances). | single-character planting is NOT a valid hard instance. The lower bound needs a violation invisible to BOTH conditional covariances AND bounded marginals — still unconstructed. | **The recurring CRUX, now precisely stated** (see below). codex round-7 timed out; this is the orchestrator's analysis. The crux is genuinely OPEN and hard. |
| 2026-06-21 (round 6) | **thesis crystallized: likely (B)/impossibility (codex 70%).** "Off-orthant SR is an exponentially ill-conditioned analytic-continuation problem": SUBCOND sees only bounded-face statistics; a planted high-degree perturbation can be far-from-SR (off-orthant `Δ<0`) yet invisible to poly bounded-face queries. Non-symmetric measures have no GWS-style compression. | **a lower-bound STRATEGY** (planted YES vs high-degree-planted NO) — but the indistinguishability + the constant-TV-distance + the all-mechanism-invisibility are **ASSERTED, not proven** (GAP). | Leaning (B) but **NOT RED-3** (no proof). Round 7 = make the construction rigorous (the hard core). (A) survives only via an unknown "structural collapse of general stability to bounded Boolean data." |
| 2026-06-21 (round 5) | **lean CORRECTED to NEUTRAL (honesty).** Every concrete hard instance is caught by SOME poly statistic (μ_4→marginal; symmetric N5→global rank/|S|-sampling; parity/linear codes→Boolean conditioning, verified `Cov=0.25`). **No instance defeats ALL mechanisms.** ⟹ dichotomy genuinely OPEN; mildly toward (A) combined tester, NOT impossibility. | linear/parity codes are NOT hard (conditioning catches them). A valid RED-3 instance must defeat covariance+marginal+global-low-dim at once — UNCONSTRUCTED. | The real crux distilled: **is real-stability of `g_μ` determined by a poly(n)-query-estimable functional?** The obstruction = estimating `g_μ(x)=E_μ[∏_{i∈S}x_i]` at OFF-ORTHANT `x` (neg/large entries) has exp variance; symmetric case escapes via GWS (|S|-sampling). Round 6 attacks this. |
| 2026-06-21 (round 4) | **bounded-marginal handle ALSO dead (N5).** Symmetric far-from-SR measures with every `≤k`-coord conditional marginal SR (verified, GWS reduction). Two handle classes dead (N4 covariance, N5 marginal) ⟹ SR-violation hideable from both. **Evidence leans toward (B)/RED-3 impossibility** (a non-symmetric spread family) — a YELLOW-a lean, NOT a proof. | the symmetric N5 families are NOT lower bounds (estimable rank seq). RED-3 needs a NON-symmetric hidden-subspace `μ_4`-lift. C2/RED-3 now the leading thread. | Round 4 = progress (N5 + the refined dichotomy + the symmetric reduction), NOT a stall. (T‴) attacked & killed. Next: round 5 builds the (B) non-symmetric construction; keep (A)-via-global-statistic alive. Upper-bound prior dropping; NO-RETREAT → attack (B) at full force, RED-3 only on a *proof*. |
| 2026-06-21 (round 3) | **MAJOR: covariance route DEAD + substrate error CAUGHT.** codex's `μ_4` is Rayleigh (all positive-field/conditioning pairwise covariances ≤0) but NOT SR (complex root), constant-far ⟹ N4: pairwise-covariance testers certify *Rayleigh ⊋ SR*, cannot test SR. **A frozen-substrate error (positive-orthant criterion ≠ SR) was found & corrected.** REDIRECT to (T‴) conditional-marginal SR-testing. NOT impossibility (different handle open). | `μ_4×Ber` is a constant-far Rayleigh-not-SR instance — but it's *easy* (its O(1)-marginal is non-SR). The real lower-bound seed would be a far-from-SR family whose *every bounded conditional marginal is SR* — not yet exhibited. | Round 3 = **progress via a hard refutation + a caught error** (the adversarial process working as designed), NOT a stall. Confidence in the *covariance* route → 0 (dead). Confidence in *some* poly tester: uncertain — now hinges on (T‴). NO-RETREAT: attack (T‴). |
| 2026-06-21 (round 2) | **upper-bound route NARROWING then RE-WIDENING.** Sparse-*support* localization **REFUTED** (N3, parity `μ_n`, referee + symbolic-audit verified). **But the audit shows the obstruction is SUPPORT, not PARAMETRIC dimension** — a 1-param full-support tilt catches `μ_n`. Reformulated target (T″): low-PARAMETRIC full-support. `μ_n` & F2 are **complementary (not shared) blind spots** ⇒ combined statistic may suffice ⇒ **leans toward a poly tester; impossibility NOT yet supported.** | **deferred.** plain `μ_n` too easy (one full conditioning detects it). Lower bound needs hidden-random-parity; HELD until (T″) resolves. | Round 2 = progress (refutation of the wrong formalization + corrected target + the support-vs-parametric insight), NOT a stall. Round 3 (audit-recommended, high-EV): prove/refute (T″) — does {bounded Boolean conditioning} + {O(1)-param full-support tilt} jointly separate SR from ε-far, AND is the tilt covariance poly-estimable? |

### Resolution lean (D) — assessment only, NOT a proof (guide §6 D)
The C0 lean ("no clean low-order local handle") points toward the **harder** side: a *clean* monotonicity-style
local/edge handle for SR looks **doubtful** at low order. Consequences for the attack loop (no retreat):
- **C1 stays the primary attack at full force**, but the brief must explicitly invite **non-local /
  higher-order / global** tester routes (not only an edge-isoperimetry mirror of 2502.16355), since the
  natural local handle is empirically doubtful.
- **C2 (matching lower bound) is built in parallel from round 1** — and the impossibility route (RED-3,
  *on a proof only*) is a live alternative resolution to weigh, because a doubtful local handle raises the
  prior that the testing task itself may carry a super-polynomial SUBCOND lower bound.
- 🔴 This lean is **NOT RED-3** (no impossibility proof) and **NOT a venue downgrade** — it is a routing
  signal. The headline target (tight SR characterization) is unchanged.

---

## 7. C0 small-cube local-handle lean (Phase 0) — ⚠️ ORACLE BUG FOUND + FIXED 2026-06-21
> 🔴 **The round-3 audit found `derisk/sr_core.py`'s SR test probed only the POSITIVE ORTHANT — a
> RAYLEIGH test, not SR — so the "SR baseline" was contaminated with Rayleigh-but-not-SR instances.**
> FIXED (`sr_margin` now probes all real `ℝⁿ`); C0 re-run done — see "C0 re-run" note at the end of this
> section. F2 instances stay genuinely non-SR (positive-orthant `Δ` violation ⟹ non-Rayleigh ⟹ non-SR).
> The C0 lean is in any case SUPERSEDED as evidence by the rigorous round-1/2/3 results (P5, N3, N4).

### (original 2026-06-20 writeup follows; read with the bug caveat above)
> A *lean*, NOT a proof, NOT a kill (guide §6 C0 / §12). Pre-registered in `derisk/preregistration.md`
> BEFORE measuring (seed 20260620); adversarial far instances only; distance-to-SR via violation-margin
> lower bounds (Lemmas C0-L1/C0-L2), NOT exact projection. Code `derisk/sr_core.py` + `derisk/run_c0.py`;
> numbers `derisk/results/c0_results.json`. **Independent audit: see `docs/rounds/` C0-audit (pending → fold).**

**Key structural fact used (and why the probe is meaningful):** `Δ_ij(g_μ)(1,…,1) = p_i p_j − p_{ij} =
−Cov(x_i,x_j)`. So **pairwise negative correlation = the Rayleigh inequality at the all-ones vertex**,
while SR demands `Δ_ij(x) ≥ 0` at **all interior** `x∈ℝ₊^n`. Subcube conditioning only probes the
combinatorial vertices `z_k ∈ {0, ∞}`. The probe asks: do interior real-stability violations force a
detectable *conditional-correlation* signal at low order?

**Candidate statistics** (SUBCOND-estimable): `S1` = worst conditional pairwise covariance (degree-2 /
NA witness; SR ⇒ S1 ≤ 0); `S2` = max triple discrepancy `|Cov_{μ|x_k=1}(x_i,x_j) − Cov_{μ|x_k=0}(x_i,x_j)|`
(a simple bounded-order proxy beyond pairwise).

**Results (n=3 is the trustworthy baseline — genuine non-product SR verified by full-grid margin):**
- **H1 ✓** S1 separates the easy positive-correlation far family F1 (SR.S1 max ≈ 0; F1.S1 ≥ +0.022,
  certified far by C0-L1).
- **H2 ✓ (the CS3 trap, concrete):** S1 is **BLIND to F2** — pairwise-negatively-correlated **non-SR**
  instances exist with S1 ≤ 0 (n=3: 10 found, S1 ≤ −0.0002; n=4: tensored construction, S1 ≤ 0). A
  tester that only certifies pairwise/NA statistics does **NOT** certify SR.
- F2 are genuinely **non-SR** (Rayleigh margin < 0; certified far by C0-L2, dist_lb > 0) with **interior**
  witnesses (interiorness ≈ 1.0–1.3 ≫ 0) — the failures sit where subcube/vertex probes cannot directly look.
- **H3 — FALSIFIER FIRES (n=3):** the bounded-order proxy S2 does **NOT** cleanly separate F2 from
  genuine SR. SR.S2 range (0 … 0.078) **overlaps** F2.S2 (median 0.065); S2-vs-violation-margin
  correlation only 0.29; only a weak "more-far ⇒ slightly higher S2" trend (F2-strong S2 median 0.10).
  *(n=4: SR baseline collapsed to products-only (S2≡0) → too thin to call; consistent weak signal corr 0.40.)*

**THE LEAN (directional, NOT a theorem, NOT a kill, NOT RED-3):** the evidence **leans toward "no clean
LOW-ORDER local handle"** for SR — the natural pairwise/NA statistic is provably blind to the CS3 family,
and a simple conditional triple proxy gives only a weak, overlapping signal; the obstruction is that SR's
failures are **interior-orthant** phenomena invisible to vertex (subcube) probes at low order. This is
exactly barrier `B3` showing up empirically.

**Independent C0 audit (fresh agent) — folded:** **no FATAL.** SR-membership test (Brändén multiaffine
criterion), both distance lemmas (C0-L1 3-Lipschitz; C0-L2 quadratic with explicit `L=2·max|M|`),
tensoring-preserves-non-SR, and all moment/conditioning code **verified correct**. Caveats raised and
adopted: **GAP-1** — the triple proxy `S2` is **sign-agnostic** (SR does NOT force `S2≈0`), so "S2 fails to
separate" is *by construction* weaker evidence; the **robust core is H2** (`S1` is a genuine *sign-
constrained* SR-necessary condition, SR⇒S1≤0, and it is provably blind to F2). To give H3 a *fair*
sign-constrained test we added **`S3`** = worst `Cov(x_i x_j, x_k x_l)` over disjoint pairs + conditionings
(SR⇒NA⇒`S3≤0`, an order-4 one-sided witness). **GAP-2/GAP-3** — the earlier n=4 SR baseline was thin and
n=4 F2 were tensor-duplicates of n=3; **MINOR-1** — raw Rayleigh margins are unnormalized (scale with `z^n`),
use `dist_lb` not raw margin for distance.

**Order-4 fair probe (S3) outcome — INCONCLUSIVE at n=4, honestly reported:** a crude random search did
**not surface genuine (non-tensored) n=4 distributions that are `S1≤0` AND non-SR** (count≈0 over a large
budget — full conditional negative correlation at n=4 is rare to hit randomly; a *search limitation*, NOT
evidence such instances are absent). Tensored F2 (non-SR localized to a 3-sub-cube + an independent 4th
coord) are `S1≤0`, non-SR, **and** `S3=0` *trivially* (order-4 witnesses are forced through the independent
coord) — a striking but construction-dependent "NA-witness-blind non-SR" example. **Whether a bounded-order
NA-witness family characterizes SR remains OPEN** — consistent with the "no clean low-order handle" lean and
with `B3`, but **not settled** by C0. *(Recommended post-Phase-0 de-risk: a smarter n=4 construction from a
known NA-but-not-SR structure to test S3 on genuine instances.)*

🔴 **Honest scope of this lean (do NOT over-read):** (i) small `n∈{3,4}`, a **finite set of low-order
candidates** (order-2 `S1`, sign-agnostic `S2`, order-4 `S3`) — a higher-order/cleverer SUBCOND statistic,
or a *global* non-local tester, might still separate; "no clean low-order handle among these candidates" ≠
"no handle exists". (ii) The robust, audited signal is **H2 at n=3** (the order-2 sign-constrained NA handle
is blind to interior-violation non-SR). (iii) F2 found are near-boundary; (iv) the order-4 question is open
(search-limited at n=4); (v) the grid SR test is a numerical proxy. **Per NO-RETREAT (§15) this lean ROUTES
the attack, it does not retreat:** attack C1 at full force (higher-order / non-local / global routes) AND
build C2 in parallel; weigh the impossibility route (RED-3 *on a proof only*).

---

## 8. Per-round artifacts index
- Briefs / responses / audits: `docs/rounds/round{n}_{brief|response|audit}.md`.
- **Round 1 (2026-06-21, SENT to codex gpt-5.5/xhigh):**
  - C1: brief `round1_brief_C1.md` · reply `round1_response_C1.md` (raw `PROOF_REVIEW/codex_raw/round1_response_C1.raw.txt`)
    · audit `round1_audit_C1.md` → **GAP-level progress** (handle `P5` verified; blocker refuted; crux =
    witness-localization theorem).
  - C2: brief `round1_brief_C2.md` · round-1 codex run KILLED (stalled 20min/0B, under-specified) →
    superseded by a round-2 C2 with the `μ_n` parity seed (pending).
  - C0 setup audit: `round0_C0_audit.md`.
- **Round 2 (2026-06-21):** C1 brief `round2_brief_C1.md` · reply `round2_response_C1.md` · audit
  `round2_audit_C1.md` → **N3 refutation + (T′) + `μ_n` hard instance.**
- **Round 3 (2026-06-21):** C1 brief `round3_brief_C1.md` · reply `round3_response_C1.md` (raw
  `…/round3_response_C1.raw.txt`; 2 transport failures then OK) · audit `round3_audit_C1.md`
  → **N4: covariance route DEAD (`μ_4` Rayleigh-not-SR) + frozen-substrate error corrected + REDIRECT to
  (T‴) conditional-marginal SR-testing.**
- **Rounds 4–7 (2026-06-21):** `round{4,5,6,7}_response_C1.md` + de-risk `derisk/windows_search.py`,
  `derisk/results/windows_search_finding.md` → **N5** (bounded-marginal handle incomplete), **N6** (single
  hidden character fails), the off-orthant ill-conditioning thesis, and the SHARPENED CRUX (the symmetry
  question, §5). codex transport degraded on long rounds (xhigh timeouts; `high` partial).
- **Round 8 (2026-06-21) — ESCALATION to web GPT-5.5-Pro (owner-relayed, guide §7 ladder).** Brief:
  `docs/rounds/round8_brief_webPro.md` = canonical copy-ready **`BRIEF_FOR_PRO.md`** (repo root). Gives
  Pro the COMPLETE problem + verified facts + our map, with full method freedom (owner directive: raw
  problem, do not constrain Pro, flag our possibly-wrong claims). **Reply: `round8_pro_response.md`**
  (major progress: substrate corrections + R+ framework + new `Ω(√n/ε)` LB; NOT a closure). Brief archived
  `round8_pro_request.md`. **Audits DONE: `round8_audit_machinery.md` (§1–§5 CLEAN) + `round8_audit_lowerbound.md`
  (§7 correct; AFL framing note).**
- **Round 9 (2026-06-21) — web GPT-5.5-Pro:** brief `round9_pro_request.md` · reply `round9_pro_response.md`
  · audit `round9_audit.md` (localization+QHB⟹R+ CORRECT; 2 normalization GAPs; Wagner–Wei confirmed) +
  `g_s` core referee-verified → **whole problem REDUCED to QHB.**
- **Round 10 (2026-06-21) — web GPT-5.5-Pro:** brief `round10_pro_request.md` · reply `round10_pro_response.md`
  · audit `round10_audit.md` (ALL CORRECT) → **3 GAPs closed; variational formula; nonuniform QHB; reduced
  to dimension-uniform UQHB.**
- **Round 11 (2026-06-21) — web GPT-5.5-Pro:** brief `round11_pro_request.md` · reply
  `round11_pro_response.md` · audit `round11_audit.md` (DONE — all correct; V-normalization doubt resolved)
  → **product-class UQHB proved (α=½); common-factor invariance + perturbation continuity ⟹ easy refuters
  dead; residual = irreducible interlacer-cone metric regularity. Lean: cautiously R+.**
- **Round 12 (2026-06-21) — web GPT-5.5-Pro [OPENNESS RESET]:** brief `round12_pro_request.md` · reply
  `round12_pro_response.md` · audit `round12_audit.md` (Thms 1.1/3.1/6.1/7.2 ALL CORRECT; Claim-6 GAP) →
  **NEW noisy-rank route (abandons V/QHB/interlacer) + 2 new R− obstructions. Cautiously R+.**
- **Round 13 (2026-06-21) — web GPT-5.5-Pro:** brief `round13_pro_request.md` · reply
  `round13_pro_response.md` (+ referee μ_4 finding) · audit `round13_audit.md` (ALL CORRECT) →
  **channel degeneracy SOLVED (regularization); sharp degree-2 PB sep; product/covariance/homogeneous
  NR-rates; μ_4 caught by a bounded channel ⟹ R+ ~70/30.**
- **Round 14 (2026-06-22) — web GPT-5.5-Pro:** brief `round14_pro_request.md` · reply
  `round14_pro_response.md` (REFUTES the root-depth route; referee-verified the counterexample) · audit
  `round14_audit.md` (DONE, ALL CORRECT, lean ~52/48) → **root formulation DEAD; target corrected to
  normalized PF minors; spectral independence localizes the WRONG quantity (Hellinger, not the compatibility
  gap); route RENAMED not reduced; lean DOWN to ~52–58, genuinely open.**
- **Round 15 (2026-06-22) — web GPT-5.5-Pro:** brief `round15_pro_request.md` · reply
  `round15_pro_response.md` (g_s SETTLED; σ_min correction; referee-verified) · audit `round15_audit.md`
  (DONE, ALL CORRECT, lean ~57/43; 2 flags: **I_i=𝔇 verification-debt** [folded into r16]; entangled R−
  open) → **`g_s` resolved FAVORABLY (`NR=Θ(√I_i)`, interior channel, product lifts not R−); certificate
  corrected determinant→σ_min (Lemma 1.1); lean ~57–62/40.**
- **Round 16 (2026-06-22) — web GPT-5.5-Pro:** brief `round16_pro_request.md` · reply
  `round16_pro_response.md` (A6 closed; exact two-block reduction; entangled channel-blind sparse-paving
  family) · audit `round16_audit.md` (TWO agents, ALL CORRECT, **all literature verified real**) →
  **foundation rigorous; σ_min/global-channel route killed by the sparse-paving family; reframed to the
  cut-or-minor removal lemma (R+) vs a degenerating excluded-minor family (R−); lean ~55–60/40.**
- **Round 17 (2026-06-22) — web GPT-5.5-Pro [SENT, owner-relayed]:** brief = root `BRIEF_FOR_PRO.md`
  (pointer `round17_pro_request.md`). Target = **the two dual forks**: (R+) prove the **cut-or-minor removal
  lemma** (the small-minor branch + exhaustiveness — the exact open theorem); (R−) build the **asymptotic
  pseudorandom excluded-minor family** whose conditioning modulus degenerates in `d`. Awaiting Pro reply.
- Literature scan (full, un-truncated): `lit/SCAN_REPORT.md`.
- C0 sim: `derisk/` (+ `derisk/results/`).
