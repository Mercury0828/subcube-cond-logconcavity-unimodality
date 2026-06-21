# Project Constitution — Testing Strong Rayleigh-ness in the Subcube-Conditioning Model (target: SODA)

> **This file is READ-ONLY for the executing agent.** It is the research constitution. Do not edit it.
> **Routing (one rule):** amendments to *this guide* (scope changes, results that contradict a plan
> here) → `docs/guide_amendments.md` (append-only); **design decisions → `DESIGN_DECISIONS.md`**;
> running state → `PROJECT_STATE.md` + the per-line ledger `docs/ledger_sr_subcond.md` (§10);
> human-verification dossiers (the AI-convergence handoff, gate (b)) → `PROOF_REVIEW/`.
>
> **Status: Phase 0 NOT passed. Nothing here is a proven result.** Every theorem/bound/construction
> below is a *claim to be established* — the **testing upper/lower-bound math** by the **external
> attacker** (codex GPT-5.5-xhigh → web GPT-5.5-Pro) with the orchestrator refereeing via independent
> adversarial audits (§§1, 7–9). Treat all bounds/shapes as **conjectural** until proven, audited, and
> carrying the "AI-verified ≠ proved" caveat (§15). In particular the headline "Θ̃(n)-vs-Θ̃(√n)
> characterization" phrasing inherited from the idea is **internally muddled** (it conflates an
> upper–lower *gap* with a *dichotomy*) and **pinning the precise tight statement is itself a Phase-0/1
> deliverable** (§5, C3) — do not write it as settled anywhere.

---

## 🔴 READ FIRST — your role, the crux, and what "SODA-worthy" means here

**This is a pure-theory paper** (sublinear distribution testing). SODA takes **no experiments**; the
result is **theorems + proofs + matching bounds**. The internal simulations described in §12 are
**adversarial de-risking only**, never a paper section.

**The headline (TARGET — unproven):** the **first** `poly(n, 1/ε)` tester in the **subcube-conditioning
(SUBCOND)** model on `{0,1}^n` (≡ `{-1,1}^n`) for whether an unknown distribution `μ` is **strongly
Rayleigh (SR)** — the well-defined hypercube analogue of log-concavity, closed under subcube
conditioning (which is exactly what makes the oracle natural) — **together with a matching lower bound**
so the characterization is **TIGHT** (a real Θ-vs-Θ statement, not a poly gap). The load-bearing
prerequisite is **(i) exhibiting a usable structural / *local* handle (an isoperimetry-style inequality)
for SR on the cube** and **(ii) proving tight bounds for it**. The idea's underspecified
"coordinate-wise unimodality of a product class" half is **DROPPED** (per the fit reviewer; §2).

**Your role (for the math) = orchestrator / referee / archivist, NOT solo prover.** The structural
handle, the tester, the upper-bound proof, and the lower-bound construction are originated by **codex
GPT-5.5-xhigh** (default), escalating to **web GPT-5.5-Pro** (human-relayed) when stalled. You write
method-free briefs, run independent adversarial audits, classify findings FATAL/GAP/MINOR, maintain the
frozen ledger, track the confidence trend, and decide escalate / continue / stop / pivot (§§1, 7–11).
You do **not** produce the frontier proof yourself, and you do **not smuggle unproven implications into
briefs** (§1).

**🔴 The crux (load-bearing) — internalize it:** monotonicity testing in SUBCOND got its Θ̃(n) tester
because monotonicity has a **clean *local* (edge) characterization** that a *directed*-isoperimetric
inequality converts into a tester (Chakrabarty–Chen–Ristic–Seshadhri–Waingarten, arXiv:2502.16355;
STOC 2025† — venue per the §2 note, confirm at Phase 0). **Strong Rayleigh-ness is a GLOBAL real-stability property of the generating
polynomial — there is NO known local / edge characterization of comparable cleanliness, and no
directed-isoperimetry for it.** So **whether SR is even `poly(n)`-SUBCOND-testable is a genuine open
question**, and the "mirror the monotonicity bound shape" move is **conjectural, not a routine
transfer**. This single step — *does a usable local/isoperimetric handle for SR exist?* — is what makes
or breaks the project, and it is the first thing Phase 0 probes (§6 C0) before any full proof.

**🔴 What "SODA-worthy" means here (the conditional, from the fit reviewer — promoted to acceptance/kill
criteria throughout):** SODA-worthy **iff** a **tight** SR characterization (matching upper + lower, a
real dichotomy) actually lands. A merely **non-tight "first nontrivial tester,"** or **only a `√n`
separation via negative association for a sub-class**, is **RANDOM/APPROX-grade, not SODA**. 🔴 **But
per NO-RETREAT (§15): you never *aim* at the lesser result to dodge difficulty.** You attack the tight
SR dichotomy at full force; the venue only steps down to RANDOM/APPROX if **the science proves the tight
result unreachable** (a proven obstruction), and even then **only at the owner's venue/scope gate (c)**,
never by an agent settling early. "Couldn't get tight in time, ship a first-tester at RANDOM/APPROX" is
exactly what §15 forbids.

> **🎯 Paper-first discipline + per-gate contribution check.** This project exists to produce a
> **SODA-submittable paper**, not open-ended research. At **every gate**, spawn one independent subagent
> given the current frozen ledger + SODA requirements (`venue-prompts/soda/` or the live CFP); it judges
> ① on track to be SODA-submittable (a **tight** SR characterization leading — matching upper + lower)?
> ② drifted into publication-irrelevant tangents / over-generalization (chasing full M-concavity,
> general matroid theory, a tolerant-testing detour) — the orchestrator forgets this easily? ③ other
> problems (the tightness claim exceeds what is proved; a step secretly assumes a local handle that was
> never established; the property class quietly degenerated)? Correct course on its advice; log it in
> `PROJECT_STATE.md` + `DESIGN_DECISIONS.md`.

---

## §0. Header

- **Working name:** `subcube-cond-logconcavity-unimodality` — **"SR-SUBCOND"**: *Testing Strong
  Rayleigh-ness in the Subcube-Conditioning Model* (the repo/idea id is a legacy of the original
  two-property framing; the unimodality half is dropped — **flag the stale name** if a pivot changes
  scope).
- **One-line thesis:** give the **first** `poly(n, 1/ε)` SUBCOND tester for strong Rayleigh-ness on the
  hypercube **with a matching lower bound** (a TIGHT characterization of its SUBCOND query complexity),
  by building an isoperimetry-style *local* handle for SR analogous to the directed-isoperimetry engine
  that resolved monotonicity — OR, as a *proven* alternative resolution, an impossibility / barrier
  showing SR is not `poly(n)`-SUBCOND-testable.
- **Target venue: SODA** (ACM–SIAM Symposium on Discrete Algorithms). **Owner-set at invocation
  (2026-06-20).** SODA is the flagship discrete-algorithms / theory venue (with STOC/FOCS); sublinear
  distribution testing in conditional-sampling models is squarely in-scope.
  - Venue YAML: `venues/conferences/soda.yaml` (provenance `verified_by=auto`, last_verified
    2026-06-20, status `confirmed`). **Deadline — SODA 2027 full paper `2026-07-09`** (AoE; verify
    against the live official SODA CFP in Phase 0), conference **Philadelphia 2027-01-24–27**, CORE
    **A\***, acceptance ≈29%. 🔴 **No GO-relevant decision may be keyed to the exact date until
    confirmed against the official SODA-27 call** (re-fetch the homepage in the YAML).
  - **Format (per the SODA venue-prompt + live SODA-27 submissions page, re-verify at Phase 0):** SIAM
    template; **no page limit** (a full version is encouraged); **the first ten pages after the title page
    must carry the merits** — problem + prior frontier + key idea + formal theorems + proof sketches —
    with **material beyond that read at the committee's discretion**; **proofs must be verifiable** (full
    proofs in the appendix); **references at the end**; **2024+ SODA is lightweight double-blind**
    (anonymize from day 1, no first-person self-citation — verify the exact policy in the current CFP).
    Format violations = summary rejection.
  - **Writing pipeline (already built): `venue-prompts/soda/`** — 4 stages (`1-results-selfcheck` →
    `2-writing-guide` → `3-page-trim` → `4-pre-submission-check`). Used at the writing phase only, after
    the theorems converge + the human gate. ⚠️ The SODA venue-prompt's deep-read star-paper profile is
    **online-algorithms / caching-flavored** (NSW dependent rounding SODA'25 arXiv:2301.08680; the
    learning-augmented caching/MTS exemplars), **NOT distribution testing** — at writing time
    **structure-clone an actual SUBCOND / distribution-testing theory paper** (the monotonicity
    predecessor 2502.16355 is the natural exemplar; see §14), and optionally flag to the owner that a
    distribution-testing SODA star-paper profile could be added per the ~20-paper rule.
- **Own-work dedup (Jason 2026-06-18 rule):** checked via `python scripts/own_work_corpus.py`.
  🔴 **Soft overlap, NOT a contribution clash — surfaced to owner, owner confirmed深挖.** The owner's
  delivered SODA line `mts-sublinear-smoothness` and the submitted `soda27-weighted-caching` (HotCRP #36)
  are **online algorithms with predictions / weighted caching** — a *different problem* from sublinear
  **distribution testing**. The only contact point is that `soda27-weighted-caching`'s SODA writing
  guide lists "negative dependence / strong Rayleigh" as a generic *bibliography tool thread*; that is a
  citation thread, not a shared contribution. 🔴 **Explicit exclusion:** this project is NOT
  online-algorithms / caching / MTS; it is **property testing of distributions in a conditional-sampling
  oracle**. No shared machinery. Proceed. If a kill→pivot (§11) changes scope, re-run `own_work_corpus.py`.

---

## §1. Roles & division of labor (establish on day 0, before any proof effort)

*(Standard section — `deepdive/_templates/external_solver_attack_playbook.md` §0, slots filled. The
attacker is engaged for the structural handle + upper bound + lower bound; the small-cube de-risking
sims are normal engineering you may run.)*

| Role | Who | Does | Does NOT |
|---|---|---|---|
| **Attacker** | codex GPT-5.5-xhigh (default); web GPT-5.5-Pro (escalation) | Originate the math: the local/isoperimetric handle for SR (C1); the SUBCOND tester + upper-bound proof (C1); the Yao-minimax planted-vs-uniform matching lower bound (C2); any impossibility proof (R−) | — |
| **Orchestrator / referee / archivist** | **Claude Code (you)** | Structure method-free briefs; run independent adversarial audits; classify FATAL/GAP/MINOR; maintain the ledger; detect drift/circularity; track confidence; decide escalate/continue/stop/pivot. **Build the small-cube de-risking sims directly** (engineering) | Originate the testing proofs; "solve it itself"; smuggle unproven implications into briefs |
| **Auditor** | independent fresh-context agents | Adversarially break each attacker reply (find the step that secretly assumes a local handle that was never established; the missing union-bound / variance term; an "isoperimetric inequality for SR" asserted but unproved; a lower-bound instance that isn't actually far-from-SR; an upper bound that quietly tests *product* not *SR*) | Share context with the attacker or the orchestrator |
| **Decider** | the human (owner) | Final verification; approve kill→pivot (proof-of-death only); the **SODA-strength / venue-step-down** gate; AI-convergence handoff | — |

**The orchestrator is a referee, not a relay and not a prover.** Understand the problem well enough to
tell progress from drift from circularity — but route the math out, state only what is *known*, and
🔴 **do not smuggle unproven implications into briefs.** The specific traps here:
- Do **not** brief the attacker that "a directed-isoperimetric inequality for SR holds" or that "SR has
  a local edge characterization" — those are **exactly** the unproven steps the attacker must establish
  (B3, §4). Asserting them as fact poisons the audit.
- Do **not** brief that "the monotonicity Θ̃(n) tester transfers to SR" — the bound *shape* is
  conjectural (§5).
- State what is genuinely known: the SR structural facts (negative association, closure under subcube
  conditioning, real-stability characterization), the two prior engines, the barriers. Pose the open
  question cleanly; let the attacker reason.

---

## §2. The Idea

### Current state of the art (a lightly-mapped oracle, an unstudied property)

The SUBCOND model on `{0,1}^n` is **active but lightly mapped**. Resolved properties (verify in Phase 0):

| property in SUBCOND | bound | source |
|---|---|---|
| uniformity | `Õ(√n/ε²)` | Canonne–Chen–Kamath–Levi–Waingarten |
| equivalence / product / identity | `Õ(n/ε²)` up, `Ω(√n/ε²)` low | arXiv:2408.02347 (RANDOM 2024, verified) |
| mean testing | — | (verify) |
| **monotonicity** | **`Θ̃(n/ε²)` — TIGHT** (first directed-isoperimetry in distribution testing) | **arXiv:2502.16355** (STOC 2025†) — the direct predecessor |
| **monotone-uniformity** (uniformity given monotone) | **`Θ̃(√n/ε²)` — TIGHT** | **arXiv:2502.16355** (STOC 2025†) — the genuine `n`-vs-`√n` *variant dichotomy* |

> **† Venue-year labels are provenance, not load-bearing.** The **arXiv IDs and the cited mathematical
> results** are what is asserted; the venue/year tags (STOC 2025 / RANDOM 2024 / NeurIPS 2020) were
> verified against official sources during the deepdive review, but **re-confirm every venue/year at Phase
> 0 anyway** (the §4 scan re-verifies all citations). Do not rely on a venue tag without a source.

**Nobody has tested unimodality, log-concavity, strong Rayleigh-ness, or negative dependence in
SUBCOND.** The model+property pairing `(SUBCOND, SR)` is genuinely unoccupied (the novelty verdict is
`real-gap`; the live risk is **feasibility**, not novelty).

### Why this path is plausible (the foothold, not a guarantee)

- **SR is the *right* target object for this oracle.** SR distributions are **closed under conditioning
  on a subcube** (fixing coordinates to 0/1) and under projection — *exactly* the operations the
  SUBCOND oracle performs — and they satisfy **negative association (NA)**, which gives concentration /
  correlation leverage a tester can try to exploit. This is why SR, not full M-concavity, is the
  defensible target.
- **The enabling engines are real and cited.** The directed-isoperimetry → edge-tester bridge
  (2502.16355) and the SUBCOND marginal/equivalence subroutines (2408.02347) exist and do what the idea
  says (both verified in the novelty/feasibility panel; re-verify in Phase 0).
- **The hard barrier that SUBCOND is meant to bypass is named.** Testing DPPs (⊂ SR) in the *standard*
  i.i.d. model has **exponential-in-dimension** lower bounds (arXiv:2008.03650 — quote the exact theorem
  in Phase 0; this "exp-in-dimension" claim is load-bearing for barrier B1, do not assume it); SUBCOND's conditional
  access is precisely the extra power that can escape that — so a `poly(n)` SUBCOND result is not a
  priori dead.

### Boundary argument (what makes novelty stand — and the load-bearing risk it exposes)

"Test another structured property in SUBCOND" is a recognized genre ("first conditional tester for
property X" — grainedness ITCS 2025; DPP testing; the equivalence/product line). Restating the genre
earns nothing. SR-SUBCOND must stay sharp on the conjunction:

1. the property is **strong Rayleigh-ness** (well-defined, deep, matroid/HDX-connected) — **not** the
   degenerate "product-class unimodality" half (dropped);
2. in the **SUBCOND oracle** (escapes the standard-model exp lower bound, B1);
3. with **tight (matching) bounds** — the SODA命门 (a poly *gap* is only a workshop note).

🔴 **The boundary that makes this hard is the same one that makes it novel:** SR is a **global**
real-stability property with **no known local/edge characterization**, whereas every Θ̃(n)-type SUBCOND
upper bound so far rode a *local* structure (monotone edges; product marginals). **C1 must build that
local handle from scratch or prove it cannot exist** — it is not a corollary of 2502.16355.

### Nearest neighbors and the exact delta

- **vs monotonicity-in-SUBCOND (2502.16355) — the direct predecessor / engine source.** Same oracle,
  same hypercube setting; it delivered a **tight** `Θ̃(n)` for monotonicity and a **tight** `Θ̃(√n)` for
  monotone-uniformity (a genuine variant dichotomy — the shape SR-SUBCOND aspires to mirror). Delta: a
  *different, global* property (SR) that
  **lacks** the directed-isoperimetric local handle monotonicity enjoyed. The contribution is building
  the missing handle + the tight bounds — not transferring the old ones.
- **vs DPP testing (arXiv:2008.03650) — the nearest threat.** Tests `q` = DPP vs ε-far (`ℓ₁`) with a
  matching *sample* lower bound, extends hardness to log-submodular. DPPs ⊂ SR, so most overlapping.
  **But different problem:** (a) STANDARD i.i.d. sampling, not subcube-conditional; (b) its lower bounds
  are exponential-in-dimension — exactly what SUBCOND bypasses; (c) does not target the full SR class,
  gives no `poly(n)` tester. **Does NOT pre-empt** a `poly(n,1/ε)` SUBCOND SR tester — but is why this
  is "incremental-but-new," not greenfield. (Phase-0 RED-1 re-checks for any *SUBCOND* SR/DPP follow-up.)
- **vs 1-D discrete log-concavity (Acharya–Daskalakis–Kamath; Canonne et al.; lower bounds
  arXiv:2308.00089) — `Θ̃(√n/ε²)` in the standard model.** No hypercube / SUBCOND version. So the
  high-dimensional target is unoccupied — but the *right* hypercube definition (M-concave / matroid /
  SR) is where the definitional risk lives; SR is the well-defined choice, which is why the unimodality
  half is dropped.

---

## §3. Differentiation / Positioning

| | conditional (SUBCOND) oracle | property = strong Rayleigh (global stability) | tight matching bounds | this paper's row |
|---|---|---|---|---|
| Monotonicity-in-SUBCOND (2502.16355) | ✓ | ✗ (monotonicity — *local* edge property) | ✓ (TIGHT: monotonicity `Θ̃(n)`, monotone-uniformity `Θ̃(√n)` — a genuine variant dichotomy) | |
| Equivalence/product-in-SUBCOND (2408.02347) | ✓ | ✗ (product/equivalence) | ✓ (for that property) | |
| DPP testing (2008.03650) | ✗ (standard i.i.d.) | partial (DPP ⊊ SR) | ✓ (matching *sample* bound, but exp-in-dim) | |
| 1-D log-concavity (ADK / Canonne) | ✗ (standard, 1-D) | ✗ (1-D log-concave) | ✓ (`Θ̃(√n)`) | |
| **THIS (SR-SUBCOND, TARGET, unproven)** | **✓** | **✓** | **target: ✓ (tight)** | **only row with all three — but the tight cell is a GOAL, not a delivered result** |

🔴 **The bottom row's "tight" cell is a GOAL, not an accomplishment.** It is unproven, and Phase 0 (§6
C0) may show no usable local handle exists (→ the bound shape collapses, §4 YELLOW / RED−). Do not
present this row as achieved anywhere (intro/abstract) before C1/C2 prove it. Verify/expand every other
row against the live literature in Phase 0 (the comparison must be to the *true* best-known bound per
setting — a SODA rejection trigger is comparing to a non-SOTA bound).

**Contact surfaces and the mandated defense each forces** (brief content + audit foci):

- **CS1 (vs "just mirror the monotonicity bound").** *Defense:* monotonicity's tester rests on a
  *directed-isoperimetric* inequality for a *local* (edge-monotone) property; SR is *global* real
  stability with **no known local characterization** — the handle must be **built** (C1), and the
  upper-bound proof must show *why* the monotonicity engine does **not** transfer black-box. If it turns
  out to transfer with a one-line change → **RED** (the result is then folklore; §4).
- **CS2 (vs "tight" being only a gap — the SODA命门).** *Defense:* a `poly(n)` upper bound is SODA-grade
  **only** with a **matching** lower bound (C2). The contribution is a *tight* Θ-vs-Θ statement; an
  upper–lower **gap** (e.g. an `Õ(n)` upper bound against only an `Ω̃(√n)` lower bound for the *same*
  property — note the predecessor 2502.16355 does NOT have this: its monotonicity bound is tight `Θ̃(n)`,
  with `Θ̃(√n)` for the *separate* monotone-uniformity property) is **NOT** a
  dichotomy and must be labeled honestly as a gap, not "tight" (§5 C3; §4 YELLOW). The two bounds are
  co-load-bearing.
- **CS3 (vs testing *product* instead of *SR*).** *Defense:* SR ⊋ product distributions; a tester that
  only certifies "looks like a product / has negative correlations" does **not** certify SR (NA is
  *necessary not sufficient* for SR). The upper bound must reject distributions that are NA / pairwise-
  negatively-correlated **but not SR**. Audit foundation: the #1 soundness check is "does this tester
  accept a non-SR distribution that merely passes the pairwise/marginal statistics?"

---

## §4. Literature Landscape & Phase-0 Kill Criteria

**Kill criteria are FROZEN here, before the scan runs.** Apply verbatim. Do not move goalposts after.

### Known nearest neighbors (threat table)

| paper | id | threat | why | action if confirmed |
|---|---|---|---|---|
| Monotonicity testing in SUBCOND (Chakrabarty–Chen–Ristic–Seshadhri–Waingarten; STOC 2025† — verify) | arXiv:2502.16355 | GREEN (engine) / YELLOW if extended | the predecessor + the directed-isoperimetry → edge-tester engine | use as the engine; **if it (or a follow-up) already tests SR / log-concavity / negative-dependence → RED** |
| Improved SUBCOND equivalence/product testing | arXiv:2408.02347 (RANDOM 2024) | GREEN (subroutine) | `Õ(n/ε²)` marginal/equivalence subroutines | use to estimate conditional marginals |
| Testing DPPs (standard model) | arXiv:2008.03650 (venue "NeurIPS 2020" per idea records — verify in Phase 0) | YELLOW | DPP ⊊ SR, but standard i.i.d. + (claimed) exp-in-dim lower bound | confirm it does NOT give a `poly(n)` **SUBCOND** SR/DPP tester; **quote the exact lower-bound statement** (the "exp-in-dimension" claim is load-bearing for B1 — verify, don't assume); **if a SUBCOND DPP/SR tester exists → RED** |
| 1-D discrete log-concavity testing (ADK; Canonne et al.; lower bounds) | arXiv:2308.00089 | GREEN | `Θ̃(√n)` standard 1-D; no hypercube/SUBCOND version | cite as the 1-D anchor; confirm no high-dim/SUBCOND lift exists |
| Testing grainedness (ITCS 2025) | (verify id) | GREEN | "first tester for structured property X" genre evidence | cite as genre precedent |
| Quadratic M-convexity *testing* is co-NP-complete | arXiv:1704.02836 (Iwamasa) | GREEN (boundary) | exact recognition of (even quadratic) M-convexity is hard | **state precisely** ("deciding M-convexity of a given quadratic set function is co-NP-complete" — not a vague "all M-concavity is hard"); cite to justify targeting **SR** (subcube-closed) + the *distribution-testing* task, NOT exact M-convexity recognition |

### Frozen kill criteria

- **🔴 RED-1 (scoop kill):** a paper already gives a **SUBCOND tester (any bound) for strong Rayleigh-
  ness, log-concavity, strong-log-concavity, M-concavity, DPPs, or negative dependence on the cube** —
  or a SUBCOND instantiation that subsumes it (e.g. a 2502.16355 follow-up extending the isoperimetry
  engine to SR). Then the gap is filled → **kill or pivot** to a strictly-different angle (a still-open
  property; or only the matching lower bound if their tester is non-tight).
- **🔴 RED-2 (definitional collapse / triviality):** Phase-0 small-scale analysis (§6 C0) or a literature
  fact shows **SR-testing in SUBCOND trivially reduces to an already-solved property** (e.g. it collapses
  to product/equivalence testing, or the "right" hypercube definition forces a degenerate class) → the
  load-bearing novelty evaporates → **reposition or kill** (surface the reduction as the finding).
- **🔴 RED-3 (the `(R+)`↔impossibility resolution, NOT a difficulty hatch — surface to human):** RED-3
  fires **only** on a proof that **SR is not `poly(n)`-SUBCOND-testable** — i.e. an `exp(n)` /
  super-polynomial SUBCOND **query lower bound for the testing task itself** (e.g. a planted-vs-far
  construction no tester can pass with `poly(n)` queries). Then the positive tester `(R+)` is dead — but
  **the impossibility / barrier is itself a deliverable** (a strong SUBCOND lower bound is SODA-relevant)
  and becomes the headline. 🔴 **A proof that "no *local* handle exists" is NOT by itself RED-3** — a
  non-local / global tester could still exist, so absence-of-a-local-handle is at most YELLOW-a (a routing
  signal to attack harder for a non-local tester, or to push toward the *testing-task* lower bound), **not**
  an untestability proof. 🔴 **Being unable to build a handle in time/budget is NOT RED-3** — that is
  difficulty → escalate (NO-RETREAT, §15). RED-3 is an owner-gate decision on a *proof of untestability*,
  never a self-downgrade.
- **YELLOW (re-position) — two triggers:**
  - **(a) no usable local handle (the load-bearing death-adjacent point):** C0 + early C1 give strong
    evidence that **no clean local/isoperimetric handle for SR exists** but **without a proof** of
    impossibility. Then the conjectured Θ̃(n) upper bound is in doubt. **Do NOT downgrade on this alone
    (NO-RETREAT §15)** — escalate the attack (web-Pro / fresh agent) to either *build* a handle by
    another route (local or non-local), or *prove* SR is untestable in `poly(n)` queries (which is RED-3,
    a real result). A YELLOW-a is a signal to attack harder and to track the confidence trend, not to retreat.
  - **(b) upper–lower *gap* (not tight):** C1 gives a `poly(n)` upper bound and C2 a lower bound, but
    they **don't match** (an `n`-vs-`√n` gap *for the same property* — unlike 2502.16355, whose
    monotonicity bound is tight `Θ̃(n)`). Then the result is "a first SUBCOND SR
    tester with an exponent gap" — **honestly a gap, not a dichotomy** (§5 C3). Push whichever bound is
    closeable at full force; the **venue step-down to RANDOM/APPROX is an owner gate-(c) decision**, only
    if the gap provably resists closing — never an agent settling early (§15).
- **GREEN:** more SUBCOND results, new isoperimetry techniques, better marginal-estimation subroutines,
  SR/HDX structural advances — these *strengthen* SR-SUBCOND → proceed; the model is hot, move fast.

### Mandatory search coverage (Phase-0 scan; log every query in `lit/SCAN_REPORT.md`)

- **Queries (each logged with engine + date + top hits triaged):** "subcube conditioning strongly
  Rayleigh / negative dependence testing"; "distribution testing log-concave hypercube conditional
  sampling"; "testing strongly Rayleigh / determinantal subcube"; "isoperimetric inequality strongly
  Rayleigh / real stable / negative association"; "high-dimensional distribution testing conditional
  oracle 2025 2026"; "M-concave / matroid distribution testing"; "directed isoperimetry distribution
  testing follow-up"; "negative dependence property testing sublinear".
- **Sources:** arXiv cs.DS + math.PR + cs.CC + cs.LG (last 24 months — the area formalizes in real
  time); **SODA / STOC / FOCS / ICALP / ESA / ITCS / SOSA / RANDOM-APPROX / COLT / NeurIPS 2024–2026**;
  forward-citations of **2502.16355, 2408.02347, 2008.03650**; DBLP of **Seshadhri, Waingarten,
  Chakrabarty, Chen, Canonne, Daskalakis, Acharya, Kamath, Ristic** and the strong-Rayleigh /
  real-stability authors (Borcea–Brändén, Anari, Oveis Gharan, Vishnoi).
- **Special assignments (independent subagents, depth-cap each ≤1 page, yes/no/uncertain — the moment a
  full proof is needed, STOP and record "post-Phase-0"):**
  (a) hunt **only** for the RED-1 scoop (any SUBCOND/conditional tester for SR / DPP / log-concavity /
  negative-dependence on the cube, or a 2502.16355 follow-up extending the engine);
  (b) **read 2502.16355's body** to extract *precisely* what the directed-isoperimetric inequality says,
  what is local about it, and whether the authors comment on extension beyond monotonicity (this scopes
  what C1 must rebuild) — quote, don't paraphrase;
  (c) **confirm the SR structural facts** to be used as frozen substrate (closure under subcube
  conditioning, negative association, real-stable-polynomial characterization) against an authoritative
  source (Borcea–Brändén; the Anari–Oveis Gharan line) — so the substrate `P*` is not folklore.
  Paywalled/unreachable → list URL/query under "Blocked items" and continue; **never guess contents.**
  **Absence of a closing result is itself a logged finding.**

---

## §5. Formal Framework / System Model

Freeze exact notation in `PROJECT_STATE.md` to avoid drift. (Ratify / amend this in Phase 1 with a
logged reason.)

- **Ground set & distributions.** Distributions `μ` over `{0,1}^n` (subsets of `[n]`; equivalently
  `{-1,1}^n`). Generating polynomial `g_μ(z) = Σ_{S⊆[n]} μ(S) ∏_{i∈S} z_i` (multiaffine).
- **Strong Rayleigh (SR).** `μ` is SR iff `g_μ` is **real stable** (no roots with all `Im(z_i) > 0`).
  SR ⊋ DPP ⊋ uniform spanning trees; SR distributions are **closed under conditioning** (`z_i ← 0/1`),
  **projection / marginalization**, and satisfy **negative association**. (These are the frozen
  structural facts — substrate `P*`, confirmed in Phase-0 special assignment (c); the canonical reference
  is Borcea–Brändén–Liggett, "Negative dependence and the geometry of polynomials," arXiv:0707.2340.)
  🔴 **A caution for C1:** Borcea–Brändén's equivalent *Rayleigh-difference* criterion
  (`∂_i g · ∂_j g − g · ∂_i∂_j g ≥ 0` on `[0,1]^n` for all `i,j`) is a **global analytic** condition over
  the whole polytope, **not** a SUBCOND-observable *local* handle — it does not, by itself, give a tester.
  Turning any such characterization into a SUBCOND-checkable local statistic is precisely C1's burden; do
  not treat the analytic criterion as if it were the handle.
- **SUBCOND oracle.** A query specifies a partial assignment `ρ` fixing a subset `T ⊆ [n]` of
  coordinates to `{0,1}` values; the oracle returns a sample from `μ` conditioned on the subcube
  `{x : x|_T = ρ}` (assuming positive probability; define the degenerate-conditioning convention in
  Phase 1). **Query complexity** = number of subcube-conditional samples. `T = ∅` recovers ordinary
  i.i.d. sampling.
- **The testing task (frozen target).** Given SUBCOND access to `μ` and `ε > 0`, **accept** if `μ` is SR,
  **reject** (w.p. ≥ 2/3) if `μ` is **ε-far** from every SR distribution in `ℓ₁` / TV. Tester uses
  `poly(n, 1/ε)` queries. (Decide tolerant vs standard testing in Phase 1 — default **standard**; flag
  any move to tolerant as a logged scope change, since tolerance usually costs more.)
- **The conjectured bound shape (CONJECTURAL — do not state as fact).** The idea's stated shape is an
  `Õ(n/ε^{?})` upper bound and an `Ω̃(√n/ε^{?})` lower bound. 🔴 **As *the idea phrased it* this is a GAP
  (`n` vs `√n`) for one property, not a dichotomy** — the internal inconsistency the fit reviewer flagged.
  (Note: the predecessor 2502.16355 itself is NOT a gap — it is tight `Θ̃(n)` for monotonicity and tight
  `Θ̃(√n)` for monotone-uniformity, i.e. a real two-variant dichotomy; so the honest reading the idea was
  reaching for is option (iii) below.) **C3 must pin the precise *tight* statement**, which is one of:
  (i) the true complexity is `Θ̃(n)` with a *matching*
  `Ω̃(n)` lower bound; (ii) the true complexity is `Θ̃(√n)` (SR is *cheaper* than monotonicity via NA)
  with a matching upper bound; or (iii) a genuine **dichotomy between two natural variants** — e.g.
  *general* SR-testing is `Θ̃(n)` while a *structured / uniform-SR* sub-case is `Θ̃(√n)`, mirroring the
  monotonicity-vs-monotone-uniformity split (2502.16355). **Which one holds is a deliverable, not an
  assumption.** "Tight" means *matching upper and lower for the stated quantity*, never an `n`-vs-`√n`
  gap relabeled as a characterization.

### The hard sub-problems, named (load-bearing claims — death points)

- **C1 — the local handle + the tester (the make-or-break, R+):** a usable **local / isoperimetry-style
  inequality** for SR on the cube, converted (via the 2502.16355 directed-isoperimetry → edge-tester
  bridge + the 2408.02347 marginal subroutines) into a `poly(n)` SUBCOND tester with a proven upper
  bound. **Death-adjacent:** SR may have *no* such handle (→ YELLOW-a → escalate; or → RED-3 if
  *proven* impossible).
- **C2 — the matching lower bound:** a Yao-minimax **planted-vs-uniform** (SR-vs-far) hard instance
  forcing the lower bound that **matches** C1, making the characterization tight.
- **C3 — pin the tight dichotomy:** resolve (i)/(ii)/(iii) above; state the honest tight characterization;
  never present a gap as a dichotomy.

🔴 **NOT claimed (write as confident scope, §14):** no tester for **exact M-convexity recognition**
(deciding M-convexity of a given quadratic set function is co-NP-complete, B2 — we test SR, the
subcube-closed class, as a *standard/tolerant distribution* test, not exact recognition);
no result for the dropped "product-class unimodality" property; no `poly(n)` claim until C1 is proven;
no "tight" claim until C1 and C2 match (C3).

---

## §6. The hard sub-problems to attack (what the attacker must originate)

For each: **claim shape → what "done" means → the frozen risk/branch.** The orchestrator briefs/audits;
the attacker (codex-xhigh) originates the proofs. C0 and the de-risking sims are engineering you may run.

### C0 (Phase-0, cheap, do FIRST) — scoop/definition re-checks + a small-cube "local-handle lean"
- **Target:** (a) clear RED-1 / RED-2 (the scoop hunt; read 2502.16355's body for what the isoperimetric
  inequality says; confirm SR structural facts); (b) a **small-cube de-risking probe** (n ∈ {2,3,4}): is
  there a *local* statistic — computable from subcube-conditional samples (e.g. conditional pairwise
  negative-correlation / an NA-violation witness / a low-degree real-stability proxy) — whose value
  **separates** genuine SR distributions from adversarially-built **ε-far-from-SR** distributions? 🔴
  **The probe is a CANDIDATE local statistic, NOT the unbuilt C1 handle** — it does not presuppose C1
  exists; it is only a directional *lean* on whether a clean local handle is plausible (→ attack the
  tester) or absent (→ the handle may not exist; attack harder / consider the impossibility route).
  **Building the C1 handle is NOT a Phase-0 task.**
- **Done =** the scoop/definition checks resolved (or BLOCKED, reported) + a pre-registered sim with a
  clear separates-vs-doesn't read, audited. ≤ the Phase-0 budget; the full proof is the attack loop.
- **Honest feasibility seam (record it):** "ε-far from SR" requires a notion of distance to the SR set,
  which is **not obviously convex/tractable**. At small `n`, do **not** compute exact projection;
  instead build far instances by **perturbing an SR distribution to violate a specific certified
  inequality** (a named NA inequality, or a real-stability witness — a point where `g_μ` has a forbidden
  root) and **lower-bound the `ℓ₁` distance to SR by the violation margin** (state the lemma you rely on,
  or mark it as an assumption to be discharged). Pre-register that the candidate statistic should grow
  with the violation margin on far instances and stay ~0 on SR instances; **falsifier:** the statistic
  is large on genuine SR instances too (no separation) ⇒ the local handle is likely not clean ⇒ lean
  toward harder / impossibility.

### C1 (the load-bearing crux, R+) — local handle for SR + the SUBCOND tester
- **Target (Theorem A):** (1) a **local / isoperimetry-style inequality** for strong Rayleigh-ness on
  `{0,1}^n` (the analogue of the directed-isoperimetric inequality monotonicity enjoyed), and (2) a
  `poly(n, 1/ε)` SUBCOND tester whose acceptance/rejection is governed by that inequality, with a proven
  **upper bound**. Method-free: rebuild the isoperimetry → edge-tester bridge for the SR operator using
  closure-under-conditioning + NA + real stability, or **any other route**.
- **Done =** a full proof (the inequality + the tester + the upper-bound analysis, including soundness
  against non-SR distributions that pass marginal/pairwise statistics — CS3) surviving **3 adversarial
  audits with no FATAL**; OR a **proof that no `poly(n)` SUBCOND SR tester exists** (→ RED-3 /
  impossibility headline — note: a proof that no *local handle* exists is **not** RED-3, only YELLOW-a, §4).
  🔴 **The impossibility proof faces the SAME `K_audit = 3` adversarial bar** —
  it ends the `(R+)` line, so it is the *more* dangerous artifact to wave through; do not flip to the
  impossibility headline on an unaudited claim.
- **🔴 Frozen branch (NO-RETREAT, §15):** `(R+)` being *hard* (no handle found yet / over budget) is
  **not** a kill — escalate (web-Pro / fresh agent) and keep attacking. Switch to the impossibility
  headline ONLY on a *proof* that no `poly(n)` tester exists. Never deflate to "a non-tight first tester
  at RANDOM/APPROX" to dodge difficulty.

### C2 (the matching lower bound) — tightness via Yao-minimax planted-vs-uniform
- **Target (Theorem B):** a **planted-vs-uniform** distribution over instances — SR (planted) vs ε-far
  (or vice versa) — on which **every** SUBCOND tester needs `Ω̃(·)` queries **matching** C1's upper
  bound, via Yao's minimax. **Done =** the construction + the indistinguishability argument + the
  matching-exponent confirmation, audited clean. **Rigor bar (pre-committed):** a *matching* lower bound
  is the contribution; a **loose** lower bound (exponent below C1's upper bound) is a strictly weaker,
  possibly-not-SODA result and must be **labeled a gap, NOT "tight"** (§4 YELLOW-b, §5 C3). The "far"
  instances in the construction must be **provably ε-far from SR** (the #1 audit check — a planted
  instance that is secretly near-SR proves nothing).

### C3 (pin the tight dichotomy) — make the headline honest
- **Target:** resolve §5 (i)/(ii)/(iii); produce the **exact** tight statement (which quantity is
  `Θ̃(n)`, which is `Θ̃(√n)`, and whether the n-vs-√n shape is a *variant dichotomy* or a single tight
  bound). **Done =** a precise theorem statement whose upper and lower bounds **match**, audited; the
  "characterization" language is used only where matching bounds exist.

> **Priority:** the **tight characterization (C1 upper + C2 matching lower, pinned by C3)** is the
> headline; the impossibility route is the *other proven* resolution (RED-3), taken only on a proof. The
> #1 audit check throughout: **does a step secretly assume a local handle that was never established, or
> certify *product/NA* instead of *SR*?**

---

## §7. The escalation ladder

*(Standard section — playbook §1, slots filled. Engaged for C1/C2/C3.)*

```
[hard sub-problem: C1 local handle + SUBCOND SR tester; C2 matching planted-vs-uniform lower bound]
   │
   ├─(1) codex GPT-5.5-xhigh  ── multi-round attack ──┐
   │                                                  │ stall?
   │     stall = K_stall = 2 consecutive rounds with: │
   │       no new VERIFIED lemma, OR circular          │
   │       reasoning, OR a step that re-assumes a       │
   │       local/edge handle for SR already flagged     │
   │       unproven (B3), OR a tester that certifies     │
   │       product/NA not SR (CS3), OR a sustained drop  │
   │       in the confidence trend.                      │
   │                                                     ▼
   ├─(2) user-mediated web GPT-5.5-Pro ── method-free briefs, human relays each round ──┐
   │     (also, stuck on the SAME thread: spawn a FRESH-context attacker with a           │
   │      method-free brief — fresh agents leap past dead ends the thread is anchored on) │
   │                                                                                      ▼
   └─(3) converge OR conclude-open / (R+)↔impossibility on a PROOF ── §9 stop / §11 ──► human gate
```

- **Two tracked threads, not serialized:** C1 (the tester) is the primary attack; C2 (the matching
  lower bound) runs **in parallel** as its own thread with its own confidence trend in the ledger — the
  lower-bound construction is independently necessary for tightness and often informs the upper bound
  (the hard instances reveal what a tester must detect). Each thread independently follows this ladder.
- **Default to (1).** Route C1/C2 out immediately; do not burn orchestrator rounds proving them.
- **Escalate to (2) on the defined stall (`K_stall = 2`).** The 2026-07-09 deadline + a hot, fast-moving
  area make `K` tight.
- **Fresh-agent move** is first-class: if a thread keeps re-assuming a monotonicity-style local handle or
  anchoring on the 2502.16355 engine as if it transfers, spawn a fresh-context attacker with a
  method-free brief before/with escalating.
- **Economics:** web-Pro is slow + human-in-loop. Batch maximally; never spend a Pro round on what xhigh
  or an audit agent can do.
- **Transport (settle before the attack phase, not Phase 0):** invoke codex GPT-5.5-xhigh via the
  available codex interface (CLI/MCP if configured, else human-relayed like web-Pro); web GPT-5.5-Pro is
  always human-relayed. Phase 0 only *writes* the C1/C2 briefs — it does not send them.

---

## §8. The brief — freeze FACTS, free METHODS

*(Standard section — playbook §2.)* Every brief to the attacker has the same skeleton:

1. **The exact target** (a precise claim; no ambiguity about "done") — e.g. C1 / C2 as stated in §6.
2. **Frozen substrate** — proven/known results, labeled `P1…Pn`, "use freely, do not re-derive":
   the SR structural facts (closure under subcube conditioning, NA, real-stable characterization —
   confirmed in Phase-0 (c)); the directed-isoperimetry → edge-tester engine of 2502.16355 (as an
   *engine to adapt*, **not** as a transferring theorem); the `Õ(n/ε²)` SUBCOND marginal/equivalence
   subroutines of 2408.02347; the C0 de-risking lean.
3. **Refuted routes** — labeled `N1…Nn`, "do NOT attempt," each with the death reason (seed as they
   arise; e.g. if C0/early C1 kills "black-box plug-in of the monotonicity inequality," record it `N1`).
4. **Barriers in force** — `B1…Bn` (pre-seeded, §10): `B1` standard-model DPP testing has exp-in-dim
   lower bounds (2008.03650 — exact statement to be quoted/verified in Phase 0) ⇒ the SUBCOND tester must
   genuinely use conditional access; `B2` deciding
   M-convexity of a given quadratic set function is co-NP-complete (1704.02836) ⇒ target SR (subcube-closed) + tolerant/
   standard distribution testing, NOT exact recognition; `B3` **no known local/edge characterization or
   directed-isoperimetry for SR** ⇒ the handle must be built, the monotonicity bound shape is conjectural.
5. **The open question, posed method-agnostically:** "build a local/isoperimetric handle for SR and a
   `poly(n)` SUBCOND tester with a matching lower bound; use any route; **if no such handle / `poly(n)`
   tester can exist, prove that** (an impossibility / super-polynomial lower bound) instead."
6. **What we need back:** the full proof, OR exactly where it breaks; an updated confidence; a verdict.

🔴 **"Free methods" ≠ "no context."** Carry the substrate (the SR facts, the two engines, the
barriers). **Do not** prescribe the operator, mandate the 2502.16355 inequality as the route, or assert
an unproven "isoperimetric inequality for SR holds" / "monotonicity transfers" as fact (§1 traps).

---

## §9. The audit & rebattle loop (after every attacker reply)

*(Standard section — playbook §3–4.)*

- **Normal reply → 1 independent audit agent** (fresh, adversarial): "does a step secretly assume a
  *local/edge* handle for SR that was never proved? does the tester certify *product / pairwise-NA*
  rather than *SR* (CS3 — find a non-SR distribution that passes)? does the upper bound hide a blowup in
  `n` or `1/ε`? is the lower-bound 'far' instance **actually ε-far from SR**? does the
  indistinguishability argument actually hold under *subcube-conditional* (not just i.i.d.) queries?"
- **Major-progress / claimed-closure reply → 3 independent audit agents**, each fresh, adversarial,
  **blind to the others**; pool findings.
- **Classify:** **FATAL** (the tester accepts a far-from-SR distribution / the inequality is false / the
  lower-bound instances aren't far → claim dead or reformulate); **GAP** (a step asserted not proved →
  rebuttal brief); **MINOR** (wording / "state explicitly").
- **Rebattle:** fold GAPs/FATALs into a focused rebuttal brief; loop (repair → re-audit → repair).
- **Confidence trend (first-class signal):** a % per round with dates in the ledger; a sustained drop =
  **escalate / fresh-agent reset (attack harder)**, not another incremental round and **never a
  downgrade** (a drop is difficulty; per NO-RETREAT §15 it does not flip to a weaker venue/result — only
  a *proof* of impossibility does).

### Stop criteria — AI convergence (declare only when ALL hold)
1. The attacker explicitly claims closure (the tight characterization — C1 upper + C2 matching lower,
   pinned by C3 — OR a proven impossibility, with no further conditions).
2. ≥ `K_audit = 3` independent adversarial audits find **no FATAL**, **no non-SR distribution the tester
   accepts**, and **no near-SR instance in the lower-bound construction**.
3. Every residual is **verification debt** (a step to write out / a "state explicitly" fix) — not a new
   obstruction or unresolved GAP.

*(Note: `K_stall = 2` for escalation, §7, is a different constant from `K_audit = 3` here.)*

Then **STOP the AI loop** and hand to the human gate.

🔴 **"AI-verified" ≠ "proved."** Remaining work is mandatory and human: (a) human-expert verification of
the upper-bound proof, the isoperimetric inequality, and the lower-bound construction; (b) full formal
writeup; (c) independent human check of any AI-produced inequality/construction the result rests on
(esp. the SR local handle and the far-from-SR lower-bound instances — a negative/lower-bound claim is
not self-checking); (d) a final novelty/priority sweep (the area moves fast). **Assemble the handoff
dossier** into **`PROOF_REVIEW/`** for the gate-(b) human handoff.

---

## §10. Archiving — the orchestrator's bookkeeping duty (day-0 deliverable)

*(Standard section — playbook §5.)*

- **One append-only research-line ledger** — `docs/ledger_sr_subcond.md`. Sections:
  - frozen model / notation (`{0,1}^n`, `g_μ`, SR / real stability, the SUBCOND oracle, the testing
    task, `ε`-far);
  - **proven results** `P1…Pn` (each "use freely, do not re-derive") — seed with the confirmed SR
    structural facts once Phase-0 (c) verifies them;
  - **refuted routes** `N1…Nn` (each "do NOT attempt," with the killing reason);
  - **barriers** `B1…Bn` — pre-seeded: `B1` standard-model DPP testing exp-in-dim lower bound
    (2008.03650 — exact statement to verify/quote in Phase 0) ⇒ must use conditional access; `B2` deciding M-convexity of a given quadratic set
    function is co-NP-complete (1704.02836) ⇒ target SR + distribution-testing task, not exact
    recognition; `B3` **no known
    local/edge characterization / directed-isoperimetry for SR** ⇒ the handle must be built, the
    monotonicity bound shape is conjectural;
  - the **exact open problem** as currently reduced (start = C1, with C2 tracked in parallel, C3 pending);
  - a **confidence trend** with dates (seed it at Phase 0);
  - a **HEADLINE** line at top with current status.
  - 🔴 **Re-read the ledger + frozen artifacts before continuing — never work from memory.**
- **Per-round artifacts:** every brief / attacker reply / audit verdict / rebuttal — one file each,
  `docs/rounds/round{n}_{brief|response|audit}.md`.

---

## §11. Kill → pivot branch (kill criteria are *meant* to fire)

*(Standard section — playbook §6 + §0b no-retreat red line.)*

🔴 **Every kill here is proof-of-death, never difficulty (NO-RETREAT, §15):** RED-1 = a SUBCOND SR/DPP/
log-concavity tester *provably* exists in prior work; RED-2 = SR-testing *provably* collapses to a solved
property; RED-3 = SR is *proven* not `poly(n)`-SUBCOND-testable (→ the impossibility/barrier becomes the
headline, an equal-grade deliverable). "Hard / stuck / over budget" is **never** a trigger — it routes
to §7 escalation. When an evidence-backed kill genuinely fires:

1. **Record the kill** in the ledger (`N*`) + `docs/guide_amendments.md` (what died, the proof/evidence,
   who verified it).
2. **Assess the reachable resolution / pivot:**
   - **RED-3 → impossibility headline:** if no `poly(n)` SR tester can exist (a *proof*), the
     impossibility / super-polynomial SUBCOND lower bound is the result — NOT a pivot, the other face of
     the same question; owner-gate decides SODA (a strong barrier) vs more work.
   - **RED-1/RED-2 scoop/collapse:** if the gap is filled or the problem trivializes, pivot to a
     strictly-different angle — an **adjacent unstudied property in SUBCOND** the built substrate now
     reaches (e.g. another negative-dependence / log-concavity variant, or a different conditional
     oracle), or only the matching lower bound if a prior tester is non-tight. Re-run
     `own_work_corpus.py` before committing to a new line.
3. **This is a HUMAN-GATE decision.** Present the kill (with the *proof*/evidence) + the
   resolution/pivot + a rough budget; the owner chooses. Do not silently re-scope; do not grind a dead
   line.
4. If pivoting to a genuinely new line, open a new ledger; the repo/idea name is already stale (the
   unimodality half is dropped) — flag it.

---

## §12. De-risking simulations (internal only — SODA takes no experiments)

*(Standard section — playbook §7. Pure-theory venue: there is NO paper experiments section; these sims
are internal de-risking, and a clean plot is never a substitute for a proof.)*

**Adversarial input only.** A statistic that separates SR from far-from-SR on **random** instances is
**worthless** — the worst case is built by an adversary. Pre-register the expected trend + a falsifier
before running.

**(A) Phase-0 local-handle lean (C0).** On small cubes `n ∈ {2,3,4}`:
- **SR membership is checkable at small `n`:** test real stability of the multiaffine `g_μ` (or use the
  SR characterization) to enumerate/parametrize genuine SR distributions.
- **Far instances (adversarial):** perturb an SR distribution to **violate a specific certified
  inequality** (a named NA inequality, or introduce a forbidden root of `g_μ`); **lower-bound the `ℓ₁`
  distance to SR by the violation margin** (state the lemma relied on, or mark it an assumption to
  discharge — see §6 C0 feasibility seam). Do **not** assume exact projection-to-SR is tractable.
- **Candidate local statistic:** something computable from subcube-conditional samples — conditional
  pairwise negative correlations, an NA-violation witness, a low-degree real-stability proxy.
- **Pre-registered trend:** the statistic grows with the violation margin on far instances and stays
  ~0 on SR instances. **Falsifier:** it is large on genuine SR instances too (no separation) ⇒ the local
  handle is likely not clean ⇒ lean toward harder / impossibility (escalate per §15, do not downgrade).
- Fixed seeds; one regeneration script per figure into `derisk/results/`; have one fresh-context
  audit agent sanity-check the setup; freeze the lean in the ledger. **A lean is NOT a proof and NOT a
  kill** — it only directs the attack.

**(B) Per-theorem verification during the attack loop.** For C1/C2, exact small-cube checks: confirm the
proven inequality holds and the tester accepts SR / rejects the adversarial far instances at `n ∈ {2,3}`;
confirm the lower-bound instances are genuinely ε-far. Positive AND negative checks (the tester must
accept SR *and* reject far). Violations are logged + escalated, never tuned away.

---

## §13. Workflow = attack loop (not a linear pipeline)

```
screen (Phase 0: kill-scan incl. reading 2502.16355's isoperimetry body + confirming SR structural
        facts + the RED-1 scoop hunt; + C0 small-cube local-handle lean)
   → attack-loop on C1 (R+ tester: brief → codex-xhigh → audit → rebattle; escalate §7),
     C2 (matching lower bound) built in parallel, C3 pinning tightness as bounds emerge
        → if C1 *proven* impossible → RED-3: the impossibility/barrier becomes the headline  [human gate]
        → if C1 lives → finish the upper bound; close the C1↔C2 match (C3 tight statement)
   → converge (§9 stop) OR conclude-open
   → HUMAN GATE (AI-convergence handoff; SODA-strength / venue-step-down)
   → writing (venue-prompts/soda/, after the gate)
```

- **Before each milestone/round: enter plan mode.** Decompose into an ordered subtask checklist;
  execute straight through; do not re-confirm after each subtask.
- **Acceptance / verification style:** embed *expected shapes* (e.g. "the statistic separates",
  "exponent `< 1`", "upper = lower"), not exact constants; any randomized/sampled check repeated before
  pass/fail; every fix needs positive (works now) **and** negative (old failure gone) verification;
  frozen-results tables append-only.
- **Confidence trend as a first-class signal** (§9): a sustained drop ⇒ escalate / fresh-agent (attack
  harder), never a downgrade.
- **🎯 Per-gate paper-orientation subagent** (READ FIRST): judges SODA-submittability (is a **tight**
  characterization still leading, or has the result drifted to a non-tight first-tester / a general
  matroid-theory tangent / a tolerant-testing detour?) + drift + other problems (a step assuming an
  unproven local handle; certifying product not SR); correct course on its advice; log it in
  `PROJECT_STATE.md` + `DESIGN_DECISIONS.md`.
- **Progress discipline (MANDATORY):** maintain `PROJECT_STATE.md` + the ledger every round; decisions to
  `DESIGN_DECISIONS.md`. **When context grows long, re-read the ledger + `PROJECT_STATE.md` + frozen
  artifacts before continuing — never from memory** (memory is the source of number-drift, notation
  clashes, repeated work).
- **Escalation, not grind:** what won't prove out is not forced — escalate (§7); flip to the
  impossibility headline only on a proof (§11); never settle for a weaker venue out of difficulty (§15).

### Phase 0 deliverables (this session; then STOP at the human gate)
(i) repo scaffold — `PROJECT_STATE.md`, `DESIGN_DECISIONS.md`, `docs/guide_amendments.md` (append-only),
`docs/rounds/`, `lit/SCAN_REPORT.md`, `derisk/` (small-cube code; figures → `derisk/results/`),
`PROOF_REVIEW/` (empty stub), and the
ledger `docs/ledger_sr_subcond.md` **pre-seeded** per §10 (frozen model; `P*` empty until (c) confirms
the SR facts; `N*` empty; barriers `B1`–`B3`; open problem = C1 with C2 parallel, C3 pending; confidence
trend seeded; HEADLINE); (ii) literature kill-scan applying §4 — **including reading 2502.16355's
isoperimetry body, confirming the SR structural facts (special assignment (c)), and the RED-1 scoop
hunt** (+ one independent one-shot second-opinion subagent); (iii) **C0** small-cube local-handle lean
(separates vs doesn't, adversarial instances, the distance-margin seam handled honestly); (iv) a brief
assessment of which resolution the lean points toward (a *lean*, NOT a proof — a clean local handle
plausible → attack the tester; no separation → handle likely absent, attack harder / weigh the
impossibility route); (v) ready-to-send **C1 + C2 attack briefs** for codex-xhigh (do not run the loop);
(vi) a ≤15-line verdict (index; full reasoning un-truncated in `lit/SCAN_REPORT.md` + the ledger).
**Then STOP** — the human decides scope before the attack loop is run. (This Phase-0 stop is **not a
fourth gate**: it is the checkpoint where the §16 gates **(a) kill/pivot** — only if a RED fired — and
**(c) venue/scope** first fire; gate (b) AI-convergence is reached only later, after the attack loop.)

---

## §14. Paper Plan (SODA structure-clone — used only after the theorems converge + human gate)

Use `venue-prompts/soda/` in the writing phase (`1-results-selfcheck` → `2-writing-guide` →
`3-page-trim` → `4-pre-submission-check`). 🔴 **SODA = THEORY class** (per `2-writing-guide.md` step 1):
**full proofs are the default first-version product** (not a sketch-then-fill later), **whole-paper
length normally ~50–60 pages** (body ~10 + long proof appendix), **bibliography dense ~40–80+ entries**.
The failure mode is *too short / proofs only sketched / too few references*, NOT over-length.

- **Structure-clone target.** ⚠️ The SODA venue-prompt's deep-read profile is online-algorithms/caching
  (NSW dependent rounding SODA'25 arXiv:2301.08680; learning-augmented caching/MTS), **not distribution
  testing**. For *this* paper, **structure-clone an actual SUBCOND / distribution-testing theory paper**
  — the predecessor **monotonicity-in-SUBCOND (arXiv:2502.16355)** is the natural exemplar (same oracle,
  same isoperimetry-driven structure) — **verify it is fetchable + record its `.bbl` citation count and
  appendix length** as the density baseline, read its sections, and build a component-mapping table at
  writing time. (Optionally flag to the owner that a distribution-testing SODA star-paper profile could
  be added to `venue-prompts/_specialization-workflow.md` per the ~20-paper rule.)
- **Skeleton (SODA norm — verify against `2-writing-guide.md`):** §1 Introduction — **§1.1 Results**
  (formal: Thm A SUBCOND SR tester / upper bound; Thm B matching lower bound; the tight characterization
  / dichotomy statement) · **§1.2 Techniques** (the SR local/isoperimetric handle; the planted-vs-uniform
  adversary) · **§1.3 Related Work** (folded into the intro — SODA norm, NOT a late section) · §2
  Preliminaries (SR / real stability, the SUBCOND oracle, the testing task, `ε`-far, the SR structural
  facts) · §3 The local handle / isoperimetric inequality for SR · §4 The tester + upper-bound proof
  (key proof inline, full proof to appendix) · §5 The matching lower bound (adversary in the body) · §6
  the tight characterization / variant dichotomy (C3) · §7 Open Questions (optimal exponent; tolerant
  testing; other negative-dependence classes; other conditional oracles) · Appendices (full proofs,
  unlimited).
- **Page budget & format (SODA, verify current CFP):** **no page limit**; the **first ten pages after the
  title page must carry the merits** (material beyond read at committee discretion); **full proofs in the
  appendix and must be verifiable**; **references at the end** (aim
  ~40–80+, built by literature thread, not by page ratio — classic distribution testing; conditional-
  sampling models; SUBCOND line; SR / real-stability / negative-association toolkit; DPP testing; 1-D
  log-concavity). **2024+ lightweight double-blind** — anonymize from day 1, no first-person
  self-citation (verify the year's exact policy in the CFP).
- **Non-claims — INTERNAL honesty artifact, NOT a paper section** (reconcile with the SODA owner-rule:
  `2-writing-guide.md` 坑#1 **bans a defensive "Limitations" section**). Keep the list **only in
  `docs/NOT_CLAIMING.md`** and at writing time enforce each as a **precise positive scope statement
  inside the theorem/model definitions**: (1) the property is **SR** (stated as the setting — not "we do
  not do full M-concavity"); (2) **standard** (or explicitly tolerant) distribution testing in
  **SUBCOND** (stated as the model); (3) **"tight"** used ONLY where C1 and C2 match — if a gap remains,
  state the exponents and list the optimal exponent as an Open Question, never write "tight"; (4) the
  dropped unimodality half simply does not appear. Verbs: never "optimal" without the matching lower
  bound; "first SUBCOND tester for SR" only against the verified literature (SODA rejection trigger:
  non-SOTA comparison).
- **Title candidates:** "Testing Strong Rayleigh-ness in the Subcube-Conditioning Model"; "The
  Subcube-Conditioning Complexity of Strong Rayleigh Distributions"; "Isoperimetry for Strong Rayleigh
  Distributions and a Tight Tester."

---

## §15. Honesty rails (surfaced here, not buried)

- **Never fabricate** bounds, inequalities, constructions, or citations. Web/tool failure → list it, do
  not guess; a BLOCKED kill-scan (esp. the RED-1 scoop hunt or the SR-fact confirmation) or CFP check →
  **no GO**.
- 🔴 **"AI-verified" ≠ "proved"** (§9). Any closure the attack loop reaches is conditional until
  human-expert verification + a full formal writeup + independent human check of any AI-produced
  inequality/construction (esp. the SR local handle and the far-from-SR lower-bound instances). State
  this in the handoff and the paper's status.
- 🔴 **SODA AI-use disclosure compliance (verify the year's exact policy in the CFP).** SODA-27 requires
  disclosure of AI use beyond routine language polishing. Because this project's *mathematics is produced
  by an external solver* (codex-xhigh / web-Pro), the submission **must** (a) disclose that AI assistance
  per the CFP, and (b) ship only results whose **AI-produced substrate has been independently
  human-rebuilt and verified** (the §9 handoff). Do not submit an AI-produced proof/construction as if
  human-authored; do not omit the required disclosure. Settle the exact disclosure wording with the owner
  at the venue/scope gate (c).
- **Residual risks are elevated to kill criteria, not hidden** — the no-local-handle risk (YELLOW-a /
  RED-3), the scoop (RED-1), the definitional-collapse (RED-2), and the upper–lower gap (YELLOW-b) are
  all frozen above, not footnotes. (The idea's `residual_risk` three checks — ① is there a usable SR
  isoperimetry handle, ② can the bounds be made tight not gapped, ③ drop the unimodality half — are
  **exactly** C1, C2/C3, and the §0 scope decision.)
- **Adversarial-only de-risking** (§12): a "separates on random instances" plot proves nothing for a
  worst-case testing claim — build adversarial far-from-SR instances; the lower-bound construction must
  use **provably ε-far** instances.
- 🔴 **NO-RETREAT red line (target fixed ⇒ no difficulty-driven downgrade).** Once SODA + the tight-SR
  characterization headline are fixed, **difficulty / being stuck / time pressure are NEVER grounds to
  weaken the contribution or retarget to an easier venue (RANDOM/APPROX).** Hard ⇒ escalate the attack
  (codex-xhigh → web-Pro → fresh-context attacker) at full force — there is no retreat option. The
  contribution/target changes ONLY on **proof-of-death** — a *proven* impossibility (no `poly(n)` SR
  tester → the impossibility/barrier becomes an equal-grade SODA result, RED-3), a confirmed scoop
  (RED-1), a proven trivialization (RED-2), or a **proven** upper–lower gap that resists closing — and
  even then it is an **owner-gate** decision, never an agent downgrading to make the work easier.
  🔴 **"Proven un-closeable gap" has a concrete evidence bar — it is NOT "we ran many rounds and the
  bounds still don't match."** It requires either (i) a proof that the upper bound is *tight* (a matching
  `Ω̃` lower bound at the upper exponent is impossible — e.g. a faster tester is constructed, closing the
  gap *downward*), or (ii) a proof that the lower bound is *tight* (the upper bound cannot be improved),
  i.e. **a proof pinning the true complexity at one end of the gap** — so the "gap" is revealed to be the
  true tight answer for *one* of the two natural quantities (the §5-C3 variant-dichotomy outcome).
  Persisting difficulty in matching them is **difficulty → escalate (§7)**, never evidence of an
  un-closeable gap. A
  confidence-trend drop ⇒ attack harder, not downgrade. 🔴 **"A non-tight first SR tester / a `√n`
  separation for a sub-class, shipped to RANDOM/APPROX because tight was hard" is FORBIDDEN** — the
  RANDOM/APPROX outcome the idea's residual_risk names is permitted ONLY when the science *proves* the
  tight characterization unreachable, AND only at the owner's venue/scope gate (c).
- 🌐 **Answer-language rule:** unless the owner asks otherwise, the owner-facing conversation /
  summaries / verdict reports are in **Chinese**; artifacts (this guide, `PROJECT_STATE.md`, the ledger,
  `lit/SCAN_REPORT.md`, briefs, proofs, code) stay in their **working language (English)** — spoken to
  the human → Chinese; written to the archive / for submission → working language.

---

## §16. Risk Register / Decision Log / HUMAN INPUT

### Risk register (live; mirror into `PROJECT_STATE.md` / ledger)
1. **No usable local/isoperimetric handle exists for SR** (C1 has no foothold). *The single live-or-die
   headline risk* (idea residual_risk ①). Mitigation: de-risk via C0; **attack at full force**
   (NO-RETREAT — inability to find a handle is not proven impossibility); a *proof* of impossibility
   yields the RED-3 barrier result, an equal-grade SODA deliverable.
2. **A step secretly assumes a local handle / certifies product not SR** → a wrong "tester." Mitigation:
   the #1 audit check (§9); the boundary argument (§2/§3 CS1/CS3) names global-SR ≠ local-edge as
   load-bearing.
3. **Upper–lower gap (not tight)** — the SODA命门 unmet (idea residual_risk ②). Mitigation: C2/C3 push
   for matching bounds at full force; a **proven** un-closeable gap is the only thing that may, at the
   owner gate (c), step the venue down — never agent choice (§15).
4. **Scoop** (RED-1) — a SUBCOND SR/DPP/log-concavity tester already exists or a 2502.16355 follow-up
   extends the engine. Mitigation: Phase-0 scan special assignment (a); **move promptly** (deadline
   2026-07-09); scoop is a reason to attack fast, not to retarget (§15).
5. **Definitional collapse / triviality** (RED-2) — SR-testing reduces to product/equivalence or the
   class degenerates. Mitigation: C0 + the read of 2502.16355 + the SR-fact confirmation in Phase 0;
   surface the reduction as the finding if it fires.
6. **"Just mirror monotonicity" referee objection** (mechanical transfer). Mitigation: lead with the
   *built* SR local handle + why the monotonicity engine does NOT transfer black-box (CS1); never
   headline "we mirror 2502.16355."
7. **Distance-to-SR is intractable** even at small `n`, breaking the C0 de-risk. Mitigation: use the
   violation-margin lower bound on `ℓ₁` distance, not exact projection (§6 C0 / §12 seam); mark the
   relied-on lemma as an assumption to discharge.

### Decision log (seed)
- **Target venue = SODA** (owner-set 2026-06-20 at invocation; RANDOM/APPROX is the idea's *conditional
  fallback* venue — but only ever reachable via the owner's venue/scope gate (c) on proof-of-death, never
  by agent downgrade, §15).
- **Property = strong Rayleigh** (well-defined, subcube-closed); the **"product-class unimodality" half
  is DROPPED** (under-defined / likely trivial — fit reviewer).
- **Tight (matching) bounds are the contribution** — a poly gap is not a dichotomy (SODA命门).
- **Claude = orchestrator** for all the math (codex-xhigh → web-Pro); the small-cube de-risk sims are
  direct engineering.

### HUMAN INPUT checklist — three gates (do not fold into one end-of-Phase-0 stop)
- **(a) Kill / pivot gate:** fires ONLY on proof-of-death — RED-1 (*proven* scoop), RED-2 (*proven*
  trivialization), or RED-3 (SR *proven* not `poly(n)`-SUBCOND-testable → the impossibility/barrier
  becomes the headline) → present the proof + budget. 🔴 Difficulty alone never reaches this gate
  (NO-RETREAT, §15) — it routes to §7 escalation.
- **(b) AI-convergence → handoff gate:** when the attack loop converges (§9), approve handoff of a
  *still-conditional* result (the tight characterization, or the impossibility) to human verification
  (not "proved") — dossier in `PROOF_REVIEW/`. 🔴 **The SR local handle and the far-from-SR lower-bound
  instances are AI-produced and MUST be independently human-rebuilt before any "tight"/"impossible"
  claim** — an audited-clean inequality or lower bound can still hide a gap.
- **(c) Venue / scope gate:** confirm the SODA-27 CFP (no hard page limit / first-~10-pages-merits /
  appendix policy / double-blind / deadline `2026-07-09`) once re-verified; confirm the contribution is
  SODA-strength (a **tight** characterization leading) vs needs more work; **and — only on a *proven*
  obstruction (an un-closeable gap / non-tight result, per §15) — decide whether to step the venue down
  to RANDOM/APPROX.** This is the ONLY place that decision may be made, and only the owner makes it.
