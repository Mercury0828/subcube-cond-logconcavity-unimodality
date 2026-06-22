# Round-6 Response — C1/RED-3 (codex, high-effort, 2026-06-21)

> The off-orthant estimability crux. codex verdict: **(B) impossibility more likely, 70%.** Raw:
> `PROOF_REVIEW/codex_raw/round6_response_C1.raw.txt`. **A STRATEGY/INTUITION, not a proof** — the
> indistinguishability is asserted, not established (the hard core remains open).

## Thesis: off-orthant SR is an "exponentially ill-conditioned analytic-continuation problem"
SUBCOND gives Boolean-face conditionals = **bounded** statistics of the coefficient array. But
`Δ_ij(g)(x)` at `x∉[−1,1]^n` is a functional with weights `~∏|x_k|` (exp-growing). **Tiny high-degree
coefficient perturbations — invisible to poly-many bounded-face queries — can be amplified into a negative
off-orthant certificate** (far-from-SR). Symmetry escapes this (GWS collapses stability to the rank
polynomial, estimable via `|S|`-sampling); **non-symmetric measures appear to have no comparable
compression.**

## Lower-bound SKETCH (NOT proven — the indistinguishability is the open core)
- **YES ensemble:** a robust SR law + random low-visible perturbations keeping all queried Boolean-face
  conditionals SR-typical.
- **NO ensemble:** same visible Boolean statistics, but plant a **random high-degree signed perturbation**
  in the coefficient tensor — constant TV mass, creating some `(i,j,x)`, `|x_k|>1`, with `Δ_ij(g)(x)<0`
  (far from SR).
- **Why poly SUBCOND can't separate (ASSERTED):** a poly-query transcript probes poly-many subcubes;
  against a random high-degree planting the face restrictions look YES-typical; detecting the violation
  needs an exp-weighted off-orthant functional (exp variance).

## Referee classification: GAP (a strategy, not a theorem)
🔴 The sketch has the right *shape* but **does not prove**: (1) that the planted NO ensemble is
**constant-TV-far from SR** (the planting must achieve `Ω(1)` distance — needs the violation-margin →
distance lemma at an off-orthant point, with the exp weight handled); (2) the **indistinguishability**
(that NO and YES are statistically close under ALL adaptive poly-query SUBCOND transcripts — this is the
hard core of any lower bound and is only asserted); (3) that the planting keeps **all** cheap statistics
(covariances, bounded marginals, AND the weight/rank profile) YES-typical simultaneously (cf. round-5: no
explicit instance yet defeats all mechanisms). Making (1)–(3) rigorous = the RED-3 proof. UNPROVEN.

## Status
Evidence + codex now **lean toward (B)/impossibility** (codex 70%; the off-orthant barrier + N4 + N5 + the
no-compression-for-non-symmetric point all align). 🔴 **Still NOT RED-3** — RED-3 needs the *proven*
`n^{ω(1)}` lower bound (the indistinguishability), which is open. NO-RETREAT: round 7 attacks the rigorous
construction; (A) stays alive (it would need "a genuinely new structural theorem collapsing general
stability to bounded Boolean data" — codex's words — which nobody has).
