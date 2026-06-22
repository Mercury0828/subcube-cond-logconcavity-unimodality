# 🏁 Attack loop CLOSED (2026-06-22, after round 18) — no current outgoing brief.

The 18-round external-solver attack loop ended by owner decision after round 18.

- **Deliverable / writeup-grade summary:** [`DELIVERABLE.md`](DELIVERABLE.md)
- **Full record:** [`docs/ledger_sr_subcond.md`](docs/ledger_sr_subcond.md), `docs/rounds/round*_pro_response.md`, `docs/rounds/round*_audit.md`
- **Cold-start:** [`RESEARCH_SUMMARY.md`](RESEARCH_SUMMARY.md)

**Outcome:** headline question (poly SUBCOND tester for strong Rayleigh-ness?) **OPEN**, lean ~52–55/45–48 R+.
A paper-grade structural theory (Thms A–I) + a conditional poly tester, with the whole problem reduced to one
open lemma (**EC_NR**). All AI-produced, AI-audited, **human-UNverified**.

> 🔴 The prior round-18 brief in this file (now in git history / `docs/rounds/round18_pro_request.md`)
> contained two over-claims the final audit caught — "`CutDef ⟺ NR`" and "(MM-cut) ⟺ (EC)". Both are
> **one-directional only** (`CutDef ≤ NR`; MM-NR is a *special case* of EC_NR). Use the corrected statements
> in `DELIVERABLE.md`, not the old brief.

To resume attacking EC_NR later, write a fresh brief from `DELIVERABLE.md` §3 (the canonical open problem).
