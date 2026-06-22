# Guide Amendments (append-only)

> `guide.md` is READ-ONLY. Any amendment to the constitution — scope changes, or results that contradict
> a plan in the guide — is recorded here (append-only), never by editing `guide.md`. Design decisions go
> to `DESIGN_DECISIONS.md`; running state to `PROJECT_STATE.md` + the ledger.

## 2026-06-20 — Phase 0, observations (NOT yet amendments to scope)

- **A-1 (factual, not a scope change).** The guide references `venues/conferences/soda.yaml`,
  `venue-prompts/soda/` (4-stage writing pipeline), and `scripts/own_work_corpus.py`. **None exist in the
  repo** (bare scaffold at invocation). No scope impact: SODA CFP is verified via live web during the
  scan; the absent writing pipeline + own-work script are logged as Blocked resources for the owner. If
  the owner later supplies them, no guide amendment is needed.

*(No scope-altering amendment recorded yet. RED-1/RED-2/RED-3 firings, confirmed scoops, or any result
contradicting the guide's plan would be appended here with the proof/evidence and who verified it.)*

## 2026-06-21 — Owner instruction conflicting with §15 (AI-use disclosure) — RAISED, NOT IMPLEMENTED

- **What happened.** Owner instructed: "继续，但是不要披露 ai" — proceed, but **do not disclose AI use**
  in the eventual SODA submission.
- **Conflict.** This contradicts the constitution **guide §15 honesty rail** (and §16 gate (c)): "the
  submission **must** (a) disclose that AI assistance per the CFP, and (b) ship only results whose
  AI-produced substrate has been independently human-rebuilt and verified … Do not submit an AI-produced
  proof/construction as if human-authored; do not omit the required disclosure." This project's *core
  mathematics is produced by an external solver* (codex-xhigh / web-Pro), so disclosure is squarely
  required, not optional polishing.
- **Orchestrator position (not overridable by fiat into a dishonest artifact).** I will continue the
  *research* (the attack loop, audits, proofs) — that part is legitimate. I will **not** implement
  non-disclosure or present AI-produced mathematics as human-authored at submission: that is research
  misconduct (misrepresentation of authorship + violating the venue's integrity policy), risks
  desk-rejection / retraction / reputational harm, and breaches §15. The disclosure obligation **remains
  in `docs/NOT_CLAIMING.md` and as a gate-(c) item.**
- **Legitimate path offered (the honest way to make AI's footprint small).** Fully **human-rebuild and
  independently verify** all AI-produced substrate (the SR local handle + the far-from-SR lower-bound
  instances) so the published mathematics is genuinely human-authored, then disclose **accurately and
  briefly** per the *actual* SODA-27 CFP (policy text still BLOCKED — SIAM 403; confirm at gate (c)).
- **Status:** pending owner resolution on the legitimate options. Research continuation is unblocked and
  does not imply agreement to hide AI.

## 2026-06-21 — CORRECTION of a frozen-substrate error (Rayleigh vs strongly Rayleigh)

- **What was wrong.** The project froze (echoing **guide §5**'s phrasing "Rayleigh-difference criterion
  `∂_i g·∂_j g − g·∂_i∂_j g ≥ 0` on `[0,1]^n`") the criterion `Δ_ij ≥ 0 on the positive orthant ℝ₊ⁿ` as
  if it characterized **strong Rayleigh (SR = real stable)**. **This is false.** `Δ_ij ≥ 0` on the
  positive orthant is the weaker **RAYLEIGH** property; **strongly Rayleigh (real stable) requires
  `Δ_ij ≥ 0` on ALL real points `ℝⁿ`** (no root with all `Im(z_i)>0`). **Rayleigh ⊋ strongly Rayleigh.**
- **How it was caught.** Round-3 attacker (codex) produced an explicit Rayleigh-but-not-SR distribution
  `μ_4` (`g_4=1+2e_1+2e_2+2e_3+e_4`), referee-verified: `Δ_ij>0` on `ℝ₊⁴` but `g_4` has a complex root
  (`t+1/t=−4+√6∈(−2,2)`) ⟹ not real stable; constant-far from SR. The adversarial loop worked as designed.
- **Consequence.** The positive-external-field / Boolean-conditioning **pairwise-covariance handle**
  (`P5`/`V(μ)`) tests Rayleigh, not SR ⟹ **route dead (ledger N4)**; targets (T)/(T′)/(T″) die at the root.
  Substrate corrected in `ledger §1/§2 (P3,P5), §3 (N4)`. Redirected to the conditional-marginal
  real-stability handle (T‴). This does **not** change scope/target (still SR-in-SUBCOND, tight) — it
  corrects a wrong lemma and a dead route. Literature cross-check (Rayleigh⊋SR) in `round3_audit_C1.md`.
