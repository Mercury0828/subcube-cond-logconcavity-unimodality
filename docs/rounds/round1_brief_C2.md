# Round-1 Brief — C2 (the matching lower bound; Yao-minimax planted-vs-uniform)

> **STATUS: WRITTEN, NOT SENT.** For codex GPT-5.5-xhigh → web GPT-5.5-Pro. Run in the NEXT session after
> the human gate. C2 runs **in parallel** with C1 (guide §7): the hard instances reveal what a tester must
> detect and often inform the upper bound. Skeleton = guide §8. Method-agnostic.

## 0. Role note
You originate the construction + the indistinguishability proof; we referee via independent audits. State
proved vs assumed; "AI-verified ≠ proved."

## 1. The exact target
Produce a **lower bound** on the SUBCOND query complexity of testing strong Rayleigh-ness on `{0,1}^n`
that, ideally, **matches** the C1 upper bound (making the characterization TIGHT). Concretely (Yao's
minimax): two distributions over instances,
- a **planted/SR ensemble** `D_yes` supported on (or close to) SR distributions, and
- a **far ensemble** `D_no` supported on distributions **provably ε-far from SR** (ℓ₁/TV),

such that **every** (possibly adaptive) SUBCOND tester making `q` queries has
`|Pr[accept | D_yes] − Pr[accept | D_no]| < 1/3` unless `q = Ω̃(·)`. **Done =** the construction + the
indistinguishability argument under *subcube-conditional* (not merely i.i.d.) queries + the matching-
exponent confirmation against C1, audited clean.

🔴 **Rigor bar (pre-committed, guide §6 C2):** a **matching** lower bound is the contribution. A **loose**
lower bound (exponent below C1's upper bound) is a strictly weaker result and must be **labeled a gap, NOT
"tight"** (§4 YELLOW-b, §5 C3) — never relabel an `n`-vs-`√n` gap as a dichotomy.

## 2. The #1 audit check this construction must survive (state your defense up front)
**Every instance in `D_no` must be PROVABLY ε-far from the SR set.** A planted "far" instance that is
secretly near-SR proves nothing (guide §9). Distance-to-SR is **not** obviously tractable (do NOT claim
exact projection). Acceptable certifications of ε-far (use one, state which):
- **(margin via a necessary condition)** exhibit a *necessary* SR condition violated by margin `δ` and a
  Lipschitz bound giving `dist₁(·,SR) ≥ δ/c` — e.g. **pairwise positive correlation** `Cov(x_i,x_j)=δ>0`
  ⇒ `dist₁ ≥ δ/3` (since SR⇒NA⇒Cov≤0, and Cov is 3-Lipschitz in ℓ₁; this project's Lemma C0-L1), or a
  **Rayleigh-difference violation** `Δ_{ij}(x*)=−δ<0` at a fixed `x*` ⇒ `dist₁ ≥ δ/L(x*)` (Lemma C0-L2,
  `L(x*)` explicit). These are confirmed-substrate routes.
- Any other *proven* ℓ₁-distance lower bound to SR.

## 3. Frozen substrate — `P*` (same as the C1 brief; abbreviated)
- **P-SR / P1 / P2 / P3** as in `round1_brief_C1.md` (SR ⇔ `g_μ` real stable; closure under subcube
  conditioning; SR⇒NA, NA necessary-not-sufficient; Rayleigh-difference is global-analytic not local).
- **P-Oracle (SUBCOND)** as in the C1 brief.
- **P-Engine (lower-bound toolkit to ADAPT).** 2502.16355 proves SUBCOND **lower bounds** for
  monotonicity (`Ω̃(n/ε²)`) and monotone-uniformity (`Ω̃(√n/ε²)`) — study its planted-vs-uniform /
  indistinguishability machinery under subcube conditioning as a *template*, not a transferring theorem.
  2008.03650 gives the i.i.d. DPP lower bound `Ω(2^{n/2}/ε²)` (B1) — note SUBCOND **escapes** it, so the
  i.i.d. construction does NOT transfer; the hard SUBCOND instances must defeat *conditional* access.
- **P-C0 (hard family seed).** This project's C0 surfaced **F2** = pairwise-negatively-correlated **non-SR**
  distributions whose real-stability failures are **interior** to `ℝ₊^n` and are **invisible to low-order
  conditional pairwise statistics** (see `docs/ledger_sr_subcond.md §7`). 🔴 **This is a natural seed for
  `D_no`:** instances that look SR to every low-order SUBCOND statistic but are certifiably ε-far. Use /
  scale up this family (it is a *lean*, not a theorem — re-derive any property you rely on).

## 4. Barriers / cautions
- **B1**: do not reuse the i.i.d. DPP lower bound — SUBCOND defeats it; you must force queries to be
  *conditional* and still fail.
- 🔴 **Scoop-overlap caution (from the literature scan):** ensure the lower bound is genuinely for **SR
  testing**, not merely re-deriving the known product/equivalence SUBCOND lower bound `Ω(√n/ε²)`
  (2408.02347) on a sub-instance — a referee will reject "you only re-proved the product bound." The
  hard instances must be hard **because of SR-membership**, not because of a coarser property.

## 5. The open question (method-agnostic)
**Construct planted (SR/near-SR) vs far-from-SR ensembles, indistinguishable to any `poly`-query SUBCOND
tester below the target exponent, with every `D_no` instance PROVABLY ε-far from SR; match the C1 upper
bound to make the characterization tight. If the true complexity is `Θ̃(√n)` (SR cheaper than monotonicity
via NA) or a genuine variant dichotomy, pin which (feeds C3).** Any route.

## 6. What we need back
(1) the two ensembles + the ε-far certification for `D_no` (which Lemma/route, with the margin); (2) the
indistinguishability proof under adaptive *subcube-conditional* queries; (3) the resulting exponent and
whether it matches C1 (tight) or leaves a gap (label honestly); (4) updated confidence + verdict.
