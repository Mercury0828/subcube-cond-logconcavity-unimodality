# DESIGN_DECISIONS — SR-SUBCOND

> Design decisions (not guide amendments — those go to `docs/guide_amendments.md`). Append-only in spirit;
> each entry dated with a reason.

## 2026-06-20 — Phase 0 setup

- **D1. Target venue = SODA** (owner-set at invocation). Headline = the **tight** SR characterization.
  RANDOM/APPROX is only a *conditional fallback* reachable solely via owner gate (c) on a **proven**
  obstruction — never an agent downgrade (guide §15 NO-RETREAT).
- **D2. Property = strong Rayleigh (SR)**, the subcube-closed real-stability class. The "product-class
  unimodality" half of the original idea is **DROPPED** (under-defined / likely trivial — fit reviewer).
  Repo/idea name `subcube-cond-logconcavity-unimodality` is therefore **stale** — flag on any pivot.
- **D3. Tight (matching) bounds are the contribution.** A poly upper–lower *gap* is NOT a dichotomy
  (the SODA命门). C3 pins the precise tight statement; "tight" used only where C1 and C2 match.
- **D4. Claude = orchestrator/referee/archivist for the math** (codex GPT-5.5-xhigh → web GPT-5.5-Pro the
  attacker). Small-cube de-risking sims (C0, §12) are direct engineering I may build.
- **D5. Missing referenced resources handled by NON-fabrication.** `venues/conferences/soda.yaml`,
  `venue-prompts/soda/`, `scripts/own_work_corpus.py` do not exist in the repo → verify SODA CFP via live
  web; log the absent writing-pipeline + own-work-dedup script for the owner rather than inventing them.
- **D6. Phase-0 scope discipline.** This session does setup + kill-scan + C0 lean + writes the C1/C2
  briefs, then STOPS at the human gate. The attack loop is NOT run; the briefs are NOT sent; no proof
  effort is sunk; no GO/convergence/theorem is declared.
- **D7. Language convention** (guide §15): owner-facing replies + verdict in **Chinese**; all archive
  artifacts (state, ledger, scan report, briefs, code) in **English**.
