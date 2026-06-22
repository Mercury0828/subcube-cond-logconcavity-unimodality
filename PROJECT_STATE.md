# PROJECT_STATE — SR-SUBCOND

> Running state. **FROZEN 2026-06-22 for cold-start / GitHub push — read `RESEARCH_SUMMARY.md` FIRST**
> (authoritative resume doc), then `docs/ledger_sr_subcond.md`. When context grows long, re-read these +
> frozen artifacts before continuing — never from memory.

## ⏸ FROZEN STATE (2026-06-22)
**14 attack rounds done** (codex 1–7, web GPT-5.5-Pro 8–14, each audited + referee-verified). **No theorem;
lean R+ ~70/30.** Bounds `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n/ε²)`. Route = noisy-rank (SR ⟺ every monotone-channel
rank Poisson-binomial). **One open residual = the general higher-order rate (34).** **Resume = relay
`BRIEF_FOR_PRO.md` (round 14) to web GPT-5.5-Pro, paste reply back, audit.** 🔴 AI-disclosure red line
unresolved (orchestrator will NOT implement non-disclosure). Details: `RESEARCH_SUMMARY.md`.

## HEADLINE (historical — Phase 0)
Phase 0 (setup + kill-scan + C0 lean + briefs). Target **SODA 2027** (full-paper deadline 2026-07-09 AoE
— verify live). Headline TARGET (unproven): first `poly(n,1/ε)` SUBCOND tester for **strong Rayleigh-ness**
on `{0,1}^n` **with a matching lower bound** (TIGHT), OR a *proven* impossibility (RED-3). My role =
orchestrator / referee / archivist, NOT prover.

## Current phase / step
- **Attack loop — 7 rounds done (2026-06-21), CONSOLIDATED at a precisely-isolated open frontier.** codex
  GPT-5.5-xhigh/high + independent audits + my own de-risking. Still NOTHING proved; "AI-verified ≠ proved".
- **Established (verified):** the upper-bound handle landscape is mapped — N4 (covariance route tests only
  Rayleigh; `μ_4`), N5 (bounded-marginal handle incomplete; symmetric spread), N6 (single hidden character
  fails). A frozen-substrate ERROR (orthant Rayleigh ≠ SR) was caught & corrected (+ C0-code bug fixed).
- **🔴 THE CRUX (project research core, ledger §5 + §6):** *Can the symmetry of an evade-(i)+(ii)+far
  measure be BROKEN?* — symmetric N5 measures evade both (i) conditional covariances and (ii) bounded
  marginals, and are testable ONLY via (iii) the global rank statistic (symmetry-only). Is there a
  NON-symmetric `Ω(1)`-far-from-SR `μ` evading (i)+(ii)? **YES+lower bound ⟹ (B)/RED-3 impossibility;
  provably NO ⟹ (A) combined tester is complete ⟹ poly tester.** Both SODA-grade. **OPEN & hard.**
- **Confidence:** codex leans **70% toward (B)/impossibility** (off-orthant ill-conditioning + no
  non-symmetric compression) — but this is a lean, **NOT a proof**. Neither outcome proven.
- **Throughput ceiling hit this session:** codex times out on the hard long-reasoning rounds (construction
  / completeness proof); quick small-n engineering also hits compute limits (all-ℝ SR test is expensive; the
  symmetry-break probe was inconclusive/vacuous). Further progress needs sustained reasoning — **web-Pro
  (owner relay)** or a dedicated optimized construction-search — NOT more short autonomous rounds.

## Next-session attack (teed up)
1. **(A) side:** try to PROVE the combined tester {(i) conditional covariances + (ii) bounded marginals +
   (iii) global weight/rank-type statistics} is COMPLETE — i.e. every evade-(i)+(ii)+far measure is
   "symmetric-like"/low-dim estimable. 2. **(B) side:** construct a NON-symmetric evade-(i)+(ii)+far measure
   (break N5's symmetry while preserving the properties) + a SUBCOND query lower bound. 3. Optimize the
   small-n search (sparse/structured perturbations; the multiplicative scheme; faster SR test) to settle
   existence empirically first.
- **🔴 Integrity hold (owner 2026-06-21 said "do not disclose AI"):** logged in `docs/guide_amendments.md`.
  I will continue the *research* but will **NOT** implement non-disclosure / present AI-produced math as
  human-authored at submission (violates §15 + academic integrity). Disclosure obligation RETAINED
  (`NOT_CLAIMING.md`, gate (c)); honest path = full human-rebuild of AI substrate + accurate brief
  disclosure per the real CFP. Unresolved with owner.

### (historical) Phase 0 — PASSED to attack loop
- **Phase 0** complete: NOT a proof/GO; scaffold + GREEN kill-scan + C0 lean + briefs done.
- Step status: A scaffold ✅ · B kill-scan ✅ (GREEN/NO-SCOOP; primary + 2nd-opinion; 3 special agents
  done) · C C0 lean ✅ (pre-registered, run, audited; fair order-4 S3 probe added) · D resolution lean ✅
  (→ ledger; leans harder/non-local + weigh impossibility) · E C1/C2 briefs ✅ (written, NOT sent) ·
  F verdict + paper-fit subagent + STOP (in progress).

## Kill-scan headline (GREEN)
- RED-1 scoop: **NO-SCOOP** (no SUBCOND/conditional tester for SR/DPP/log-concave/M-concave/NA exists;
  DPP tester 2008.03650 is i.i.d. with `Ω(2^{n/2}/ε²)` lower bound = the barrier SUBCOND escapes; 2502.16355
  has 3 forward-cites, none on SR). Independent second-opinion AGREES GREEN.
- 2502.16355 read: STOC 2025; Thm 3 directed-Talagrand `Ω(1/√log n)·dist₁`; edge-local; **no extension to
  SR given** → C1 must rebuild the bridge (B3).
- SR facts CONFIRMED vs BBL (0707.2340): closure / SR⇒NA(CNA+) / SR⇔real-stable (`P*` filled).
- B1 `Ω(2^{n/2}/ε²)` and B2 (QMCTP co-NP-complete) verified precisely.

## Frozen numbers / facts (paths)
- Model/notation frozen in `docs/ledger_sr_subcond.md` §1.
- Barriers B1–B3 seeded (`ledger §4`). `P*` substrate EMPTY until scan (c) confirms SR facts.
- Conjectured bound shape `Õ(n)` vs `Ω̃(√n)` is a **GAP not a dichotomy** as phrased — C3 to pin.

## Environment / tooling notes
- Repo was a bare scaffold (only guide.md / README.md / start_up). Created docs/, lit/, derisk/,
  PROOF_REVIEW/ this session.
- **Missing referenced resources (NOT fabricated):** `venues/conferences/soda.yaml`, `venue-prompts/soda/`
  (4-stage writing pipeline), `scripts/own_work_corpus.py`. → SODA CFP verified via live web instead;
  these are logged as Blocked/absent for the owner.
- Live web access: WORKING (kill-scan not blocked → GO permissible).

## TODO / pending-human
- Finish B (scan + CFP), C (C0 sim), D (lean), E (briefs), F (verdict).
- **Three human gates at the Phase-0 stop** (guide §16): (a) kill/pivot [only if a RED fired],
  (b) AI-convergence handoff [NOT yet — after attack loop], (c) venue/scope (confirm SODA-27 CFP +
  contribution strength + AI-use-disclosure plan).

## C0 lean (one line)
A clean LOW-ORDER local handle for SR looks **doubtful** (n=3 robust: the order-2 sign-constrained NA
handle is provably blind to interior-violation non-SR instances; n=4 / order-4 OPEN, search-limited).
A routing signal (attack harder / non-local / weigh impossibility), NOT a proof, NOT a downgrade (§15).

## Confidence trend
See `docs/ledger_sr_subcond.md` §6. Seeded 2026-06-20, pre-attack (unset).

## Paper-fit / drift check (F deliverable)
**To be a submittable SODA paper this still needs:** (1) the C1 SR local/structural handle + a `poly(n,1/ε)`
SUBCOND tester with a proven upper bound (or a *proven* impossibility); (2) the C2 matching lower bound on
provably-ε-far instances; (3) C3 pinning the *tight* statement (which quantity is `Θ̃(n)` vs `Θ̃(√n)`, or
the variant dichotomy) — "tight" only where bounds match; (4) independent **human rebuild** of the
AI-produced handle + far-from-SR instances ("AI-verified ≠ proved"); (5) the full ~50–60pp SODA writeup
(structure-clone 2502.16355), AI-use disclosure per the SODA-27 CFP, double-blind from day 1; (6) a final
novelty/priority re-sweep (hot area).
**Drift check:** independent paper-fit/drift subagent verdict = **ON-TRACK** — tight-characterization
headline still leading and honestly hedged (YES); no smuggled local-handle assumption in the briefs (NO);
CS3 product-not-SR risk flagged + demonstrated (NO un-flagged risk); C0 lean treated as a routing signal,
not a downgrade (YES). No course change. (One minor summary-wording fix already applied.)
