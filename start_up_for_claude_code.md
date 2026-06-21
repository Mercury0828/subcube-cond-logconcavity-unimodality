# Start-up prompt — Phase 0 for `subcube-cond-logconcavity-unimodality` (SR-SUBCOND, target SODA)

Paste this whole message into a fresh Claude Code session opened in this project's repo. It runs
**Phase 0 only** and stops at the human gate.

---

You are starting a research project. **`guide.md` in this directory is your READ-ONLY project
constitution — read all of it first** (especially the **READ FIRST** box). Amend it only via
`docs/guide_amendments.md` (append-only); record decisions in `DESIGN_DECISIONS.md`, running state in
`PROJECT_STATE.md`, and the substantive research record in the per-line ledger `docs/ledger_sr_subcond.md`.

## Step 0 — Enter plan mode first
Read `guide.md` end to end, then **analyze the Phase-0 tasks, break them into an ordered subtask list,
and execute the whole list straight through** — do not start before planning, but once the list is set,
**do not stop to re-confirm after each subtask.**

## Your role — orchestrator / referee / archivist (NOT a solo prover)
This is a **pure-theory** paper (sublinear distribution testing). The **headline is a theorem**: the
**first** `poly(n,1/ε)` tester in the **subcube-conditioning (SUBCOND)** model on `{0,1}^n` for whether
an unknown distribution `μ` is **strongly Rayleigh (SR)** — the hypercube analogue of log-concavity,
closed under subcube conditioning — **with a matching lower bound** (a TIGHT characterization) — OR, as
the other *proven* resolution, an **impossibility / barrier** showing SR is not `poly(n)`-SUBCOND-
testable. That math is originated by an **external attacker**: **codex GPT-5.5-xhigh** by default,
escalating to **web GPT-5.5-Pro** (human-relayed) when stalled. **Your job:** structure **method-free
briefs** (freeze FACTS, free METHODS — guide §8); run **independent adversarial audits** with
fresh-context subagents (guide §9); classify FATAL/GAP/MINOR; maintain the **frozen ledger** (guide §10);
track the **confidence trend**; decide **escalate / continue / stop / pivot** (guide §7, §11). You must
**not** produce the frontier proof yourself and **not smuggle unproven implications into briefs** — in
particular, **never assert "a directed-isoperimetric inequality for SR holds," "SR has a local edge
characterization," or "the monotonicity tester transfers to SR"** — those are *exactly* what the attacker
must establish (guide §1, B3). The small-cube de-risking sims you may build directly (engineering) — but
**not the full proof, and the attack loop is NOT run in Phase 0.**

**Key constants (from guide §7/§9; copied here so this startup is self-contained):** escalation stall
trigger `K_stall = 2` (consecutive attacker rounds with no new VERIFIED lemma / circular reasoning /
re-assuming an unproven SR local handle / a tester that certifies product-NA-not-SR / a sustained
confidence drop) → escalate codex-xhigh → web-Pro / fresh agent; audits = **1** independent adversarial
agent per normal reply, **3** independent blind agents on a claimed-closure/major-progress reply;
AI-convergence stop needs **all** of: attacker claims closure + `K_audit = 3` audits find no FATAL / no
non-SR distribution the tester accepts / no near-SR lower-bound instance + every residual is mere
verification debt. (These are *not* run in Phase 0 — Phase 0 only writes the first briefs.)

## The crux + the resolutions (internalize before Phase 0)
- **The crux (C1):** monotonicity testing got its Θ̃(n) SUBCOND tester from a **local (edge)**
  characterization that a *directed*-isoperimetric inequality turns into a tester (Chakrabarty–Chen–
  Ristic–Seshadhri–Waingarten, STOC 2025, arXiv:2502.16355). **SR is a GLOBAL real-stability property
  with NO known local/edge characterization** → whether SR is even `poly(n)`-SUBCOND-testable is a
  genuine open question, and "mirror the monotonicity bound shape" is **conjectural**, not a transfer.
  C1 = build a usable local/isoperimetric handle for SR (or prove none exists). This is make-or-break.
- **Two *proven* resolutions, each potentially a result:** **(R+)** the tight SR characterization (C1
  upper bound + C2 matching lower bound, pinned by C3); **(R−/RED-3)** a *proof* that no `poly(n)` SR
  tester exists — an impossibility/barrier that is itself SODA-relevant. 🔴 Difficulty on (R+) ⇒ **attack
  harder** (escalate), never settle; the impossibility becomes the headline ONLY on a *proof*, at the
  owner gate.
- 🔴 **The headline "Θ̃(n)-vs-Θ̃(√n) characterization" inherited from the idea is internally muddled** (it
  conflates an upper–lower *gap* with a *dichotomy*). **Pinning the precise tight statement is a
  deliverable (C3), not an assumption** (guide §5). Never write it as settled.

## Target venue + the constraints to keep in view from day 0
**Target: SODA** (fixed), headline = the **tight** SR characterization (fixed). **Deadline — SODA 2027
full paper `2026-07-09`** (AoE; verify against the live official SODA CFP at Phase 0 via the homepage in
`venues/conferences/soda.yaml`), Philadelphia 2027-01-24–27, CORE A*. 🔴 **NO-RETREAT red line (guide
§15):** **difficulty / being stuck / time pressure are NEVER grounds to weaken the contribution or
retarget to an easier venue (RANDOM/APPROX).** Hard ⇒ escalate the attack (codex-xhigh → web-Pro → fresh
agent) at full force; no retreat. The contribution/target changes ONLY on **proof-of-death** — a *proven*
impossibility (→ the RED-3 barrier, an equal-grade result), a confirmed scoop, a proven trivialization,
or a **proven** un-closeable upper–lower gap — and only as an **owner-gate** decision; never
self-downgrade. 🔴 **"Ship a non-tight first-tester / a `√n` separation at RANDOM/APPROX because tight was
hard" is FORBIDDEN** — the RANDOM/APPROX fallback the idea names is reachable ONLY on a *proven*
obstruction, AND only at the owner's venue/scope gate (c). (Scoop risk in a hot area is a reason to attack
*fast*, not to retarget.) Writing pipeline `venue-prompts/soda/` (4 stages) — used at the writing phase
only. Keep in view (SODA = **THEORY class**):
1. **No hard page limit; full proofs are the default first-version product** (not sketch-then-fill);
   the **first ~10 pages** convey the merits, **full proofs in the unlimited appendix**, **references not
   counted** (aim ~40–80+); whole-paper length normally **~50–60 pages**. Failure mode = *too short /
   proofs sketched / too few refs*, not over-length.
2. **2024+ lightweight double-blind** — anonymize from day 1, no first-person self-citation (verify the
   year's exact policy in the CFP).
3. ⚠️ The SODA venue-prompt's star-paper profile is online-algorithms/caching, **NOT distribution
   testing** — at writing time structure-clone an actual SUBCOND/testing paper (the monotonicity
   predecessor 2502.16355 is the natural exemplar; guide §14).
4. **No standalone Limitations section** — keep the non-claims list **only in `docs/NOT_CLAIMING.md`**
   (an internal honesty artifact, NOT a paper section) and at writing time fold each as a precise
   *positive* scope statement into the model/theorem statements (guide §14;
   `venue-prompts/soda/2-writing-guide.md` 坑#1).

## This session does Phase 0 ONLY, then STOP at the human gate
Phase 0 = (A) repo scaffold + ledger, (B) literature kill-scan **incl. reading 2502.16355's
isoperimetry body, confirming the SR structural facts, and the RED-1 scoop hunt**, (C) C0 small-cube
local-handle lean, (D) which resolution the lean points toward, (E) ready-to-send C1 + C2 attack briefs,
(F) verdict. **Do not run the attack loop, do not sink proof effort.** Stop at the human gate.

### A. Repository scaffold + ledger (day-0 deliverables)
Create `PROJECT_STATE.md`, `DESIGN_DECISIONS.md`, `docs/guide_amendments.md` (append-only),
`docs/rounds/`, `lit/SCAN_REPORT.md`, `derisk/` (small-cube code), `PROOF_REVIEW/` (empty stub).
**Create the ledger `docs/ledger_sr_subcond.md` pre-seeded** per guide §10: frozen model/notation
(`{0,1}^n`, generating polynomial `g_μ`, SR / real stability, the SUBCOND oracle, the testing task,
`ε`-far); `P*` empty (fill once the SR structural facts are confirmed in (B/c)); `N*` empty; barriers
`B1` (standard-model DPP testing has exp-in-dim lower bounds, arXiv:2008.03650 ⇒ the SUBCOND tester must
genuinely use conditional access), `B2` (deciding M-convexity of a given quadratic set function is
co-NP-complete, arXiv:1704.02836 ⇒ target SR (subcube-closed) + the distribution-testing task, NOT exact
recognition), `B3` (**no known
local/edge characterization or directed-isoperimetry for SR** ⇒ the handle must be built; the
monotonicity bound shape is conjectural); exact open problem = C1 (with C2 in parallel, C3 pending);
confidence trend seeded with today's date; a HEADLINE status line. Use a project venv/conda for any code;
do not touch the system environment.

### B. Literature kill-scan (guide §4 — criteria FROZEN, do not soften)
**🔴 Requires live web/tool access.** No web retrieval → the kill-scan is **BLOCKED** → you **cannot**
issue verdicts or any GO → **escalate to the human and STOP; do not fabricate citation contents; do not
proceed to a GO** (same for the CFP check). Run the §4 mandatory coverage (queries + sources); log
**every query + hit** in `lit/SCAN_REPORT.md` (full reasoning, un-truncated — the verdict is only a
15-line index); maintain a concern table; issue GREEN/YELLOW/RED per §4 + one independent one-shot
second-opinion subagent. Three special-assignment subagents (depth-cap each ≤1 page, yes/no/uncertain;
the moment a full proof is needed, STOP and record "post-Phase-0"):
- (a) hunt **only** for the RED-1 scoop — any **SUBCOND/conditional** tester for SR / DPP / log-concavity
  / strong-log-concavity / M-concavity / negative-dependence on the cube, or a 2502.16355 follow-up that
  extends the directed-isoperimetry engine to SR;
- (b) **read arXiv:2502.16355's body** — extract *precisely* what the directed-isoperimetric inequality
  says, what is "local" about it, and any author remark on extension beyond monotonicity (this scopes
  what C1 must rebuild); **quote, don't paraphrase**;
- (c) **confirm the SR structural facts** to be frozen as substrate `P*` (closure under subcube
  conditioning; negative association; real-stable-polynomial characterization) against an authoritative
  source (Borcea–Brändén; Anari / Oveis Gharan), so the substrate is not folklore.
If a PDF won't open, **exhaust free routes** (ar5iv/HTML, author pages, Semantic Scholar) then mark
BLOCKED — do not guess. Paywalled/unreachable → list under "Blocked items" and continue. **Absence of a
closing result is itself a logged finding. Phase 0 must NEVER declare AI-convergence or a proven
theorem** — convergence is human gate (b).

### C. C0 — small-cube local-handle lean (cheap; after scaffold)
Per guide §6 C0 / §12(A): on `n ∈ {2,3,4}`, probe whether a **candidate local statistic** (computable
from subcube-conditional samples — conditional pairwise negative correlations / an NA-violation witness /
a low-degree real-stability proxy) **separates** genuine SR distributions from **adversarially-built
ε-far-from-SR** distributions. 🔴 **The probe is a CANDIDATE statistic, NOT the unbuilt C1 handle** — it
does not presuppose C1 exists; it is only a directional *lean*. **Adversarial instances, not random** (a
clean random-input plot proves nothing). 🔴 **Honest distance seam:** "ε-far from SR" needs a distance to
the SR set, which is **not obviously tractable** — do NOT compute exact projection; build far instances
by **perturbing an SR distribution to violate a specific certified inequality** (a named NA inequality, or
a forbidden root of `g_μ`) and **lower-bound the `ℓ₁` distance to SR by the violation margin** (state the
lemma relied on, or mark it an assumption to discharge). Pre-register the expected trend + a falsifier
(falsifier: the statistic is large on genuine SR instances too ⇒ no clean local handle ⇒ lean toward
harder/impossibility); fixed seeds; freeze in the ledger. Have one fresh-context audit agent sanity-check
the setup. **Do NOT attempt the full proof — that is the attack loop, next session.**

### D. Which resolution does the lean point toward? (assessment only, NOT the proof)
Briefly assess (write to the ledger) whether a clean local handle looks **plausible** (lean → attack the
C1 tester first) or **absent** (lean → the handle may not exist; the attack loop must escalate hard and
weigh the impossibility route). This is a *lean*, not a theorem. 🔴 A lean toward "no separation" is
**NOT** RED-3 (RED-3 needs a *proof* that no `poly(n)` tester exists, guide §15) — note it and that the
attack loop still attacks C1 at full force while building C2 in parallel; do not pre-flag a retreat on a
mere lean.

### E. C1 + C2 attack briefs (set up, do NOT run the loop)
Write `docs/rounds/round1_brief_C1.md` (the local handle + the SUBCOND SR tester / upper bound) and
`docs/rounds/round1_brief_C2.md` (the Yao-minimax planted-vs-uniform matching lower bound) for codex-xhigh
(guide §6/§8): exact target; frozen substrate (`P*` = the confirmed SR facts + the C0 lean + the two
engines 2502.16355 / 2408.02347 as *engines to adapt, NOT transferring theorems*); refuted routes (none
yet); barriers (`B1`–`B3`); the open question posed method-agnostically ("build a local handle + a
`poly(n)` SUBCOND SR tester with a matching lower bound; any route; **if no such handle/tester can exist,
prove that** instead"); what we need back. These are the first things the *next* session (post-gate) will
send. **Do not run the attack now.** Do not assert in the brief that the monotonicity inequality
transfers (guide §1 trap).

### F. Verdict report (then STOP at the human gate)
Write a ≤15-line summary (an INDEX — full reasoning stays un-truncated in `lit/SCAN_REPORT.md` + the
ledger): GREEN/YELLOW/RED per §4 (esp. the RED-1 scoop result; the 2502.16355 isoperimetry-body read; the
SR-fact confirmation); the C0 lean (does a local statistic separate SR from far-from-SR?); which
resolution the lean points toward ((R+) tester vs the impossibility route — a *lean*); blocked items; and
the **exact human decisions now required** — the **three gates** (guide §16): (a) kill/pivot,
(b) AI-convergence handoff [not yet], (c) venue/scope. **Append one line:** "to be a submittable SODA
paper this still needs: ___ ; drift check: ___" and record it in `PROJECT_STATE.md`.

## Operating rules
- **Highly autonomous — minimize interrupting the human.** Once Phase 0 is broken into subtasks, run the
  list straight through. **Stop to ask the human ONLY at** the three gates (kill/pivot; AI-convergence
  handoff; venue/scope), an irreversible/outward action, or a true blocker (missing critical info you
  cannot proceed without). **Never** pause after each subtask to ask "next I'll do X — continue?" —
  default to continuing until the Phase-0 human gate. Escalate-in-report.
- **You are the referee, not the prover.** Do not try to prove C1/C2 yourself; set up the briefs and the
  audits; route the math out (codex-xhigh) in the *next* session per the ladder.
- **Never fabricate** — no invented bounds, inequalities, constructions, or citations. Web failure → list
  + continue; BLOCKED scan/CFP → no GO. Do not assert "monotonicity transfers to SR" or "an isoperimetric
  inequality for SR holds" — those are the attacker's to prove.
- **Pre-register before measuring** (C0); mismatch → diagnose, record honestly. Never shape-force.
- **Progress discipline:** update `PROJECT_STATE.md` + `docs/ledger_sr_subcond.md` every step (progress /
  frozen results & numbers + paths / current step / TODO + pending-human / confidence trend). **When
  context grows long, re-read the ledger + `PROJECT_STATE.md` + frozen artifacts before continuing —
  never from memory.**
- 🔴 **"AI-verified" ≠ "proved."** Nothing the loop produces is "proved" until human-expert verification +
  a full formal writeup + independent human check of any AI-produced inequality/construction (esp. the SR
  local handle and the far-from-SR lower-bound instances). Say so in every handoff. **And: SODA-27
  requires AI-use disclosure beyond routine polishing — since the math here is produced by an external
  solver, the eventual submission must disclose that per the CFP and ship only human-rebuilt substrate
  (guide §15); flag this for the owner at the venue/scope gate.**
- 🔴 **NO-RETREAT:** difficulty ⇒ escalate, never downgrade the contribution or retarget to RANDOM/APPROX;
  only a proof-of-death (proven impossibility → RED-3, confirmed scoop, proven trivialization, or a proven
  un-closeable gap) + owner gate may change the target/contribution (guide §15).
- **🎯 Paper-first, not open-ended research.** The point is a SODA-submittable paper (a **tight** SR
  characterization leading). Phase-0's verdict applies that lens, and **every later gate runs an
  independent "paper-fit / drift" subagent** (guide READ FIRST + §13) that judges submittability + drift
  (esp. "has it drifted to a non-tight first-tester / general matroid theory / a tolerant-testing detour?
  does a step assume an unproven local handle? does the tester certify product not SR?") + other problems,
  and corrects the route on its advice.
- 🌐 **Answer-language rule:** unless the owner asks otherwise, give the owner all **conversational
  replies / the verdict report / the ≤15-line summary in Chinese**. Artifacts (`PROJECT_STATE.md`, the
  ledger, `lit/SCAN_REPORT.md`, briefs, proofs, code) stay in their **working language (English)** —
  spoken-to-the-human → Chinese; written-to-the-archive / for-submission → working language.
- End with the ≤15-line verdict (in Chinese) and the explicit list of pending human decisions (the three
  gates), then **STOP**.
