# Round-16 audit (TWO independent agents) — A6 + two-block theorem + sparse-paving R− family — 2026-06-22

> Two parallel fresh-context adversarial audits: (1) the algebraic theorems (A6, Thm 2.1, g_s exactness,
> cut-or-minor reframe); (2) the sparse-paving construction + **the load-bearing matroid-HPP literature**
> (WebSearch-verified). **All math CORRECT; ALL literature REAL (no hallucination).** Lean ~55–60/40 R+.

## AUDIT 1 — algebraic side
- **Claim 1 (A6: `I_i(g_s)=𝔇(g_s)`): CORRECT, genuinely closed.** `𝔇(σ)=0` for SR `σ` (sup attained at
  `ν=σ`); both localization correction terms vanish. *(MINOR: it's an arithmetic identity discharged, not a
  deep theorem — it relocates all content to `𝔇(g_s)`, which round-15 nailed.)*
- **Claim 2 (Thm 2.1 exact two-block reduction): CORRECT** — including the two most-doubted steps: the
  **"reflects-stability" polarization** is a genuine *iff* (Grace–Walsh–Szegő), and **completeness** holds
  (rank-truncation S1 + block-averaging S2 are WLOG reductions that only improve the comparator ⟹ the inf
  over ALL SR `ν` is attained within block-exchangeable rank-`k` SR = PB on the feasible interval). No gap.
- **Claim 3 (`NR(g_s)=d_TV(g_s,SR)=Θ(s^{−2})` EXACT): CORRECT** — `NR≤d_TV` by contraction, `≥` by the
  realizing "keep-A, zero-B" projection; the feared "another channel gives larger NR" is impossible. `I_i=
  Θ(s^{−4})`, `NR=Θ(√I_i)`. Round-15 headline rigorous, no exponent correction. *(MINOR: constant `√800`
  unchecked; Θ-exponents sound.)*
- **Claim 4 (cut-or-minor removal lemma, R+ reframe): GAP — fair target, NOT a theorem.** Correctly reduces
  the global alternative to a single-block rank statistic `d_TV(L(|X∩A|),PB)` (not a general Toeplitz σ_min);
  and (44) ALONE is provably false (sparse-paving). But the **small-minor branch** (a low-dim, inverse-poly-
  far, inverse-poly-likely descendant always exists when the cut branch fails) **+ exhaustiveness** are
  UNPROVEN. **R+ rests entirely on this.** Net: strengthens the foundation, doesn't advance the open problem.

## AUDIT 2 — sparse-paving R− family + matroid-HPP literature [🔴 ALL LITERATURE VERIFIED REAL]
- **Claim A (valid sparse-paving matroid): CORRECT.** non-bases = independent set in Johnson `J(n,k)`
  (Hamming dist ≥4 ⟺ Johnson dist ≥2); basis-exchange proof sound. ✔
- **Claim B (global channel-blindness `NR(μ_H)=2^{−Ω(n)}`): CORRECT (conclusion robust).** Identity (28) ✔;
  McDiarmid bounded-diff `D+1` ✔; `α=p(1−p)^D=Θ(1/D)` ✔. **B3 (uniform-over-channels net):** the template is
  right; stated constants loose, but **`√N=2^{Θ(n)}` swamps every poly(n) slack** ⟹ the `2^{−Ω(n)}` headline
  is insensitive to the constants. *(MINOR/GAP on net rigor, not the conclusion.)* ⟹ every global covariance/
  PF certificate has `σ_min≤2NR=2^{−Ω(n)}`.
- **Claim C (poly-far via planted `M_0`): CORRECT; 🔴 "22" is REAL.** **Kummer–Sert (arXiv:2111.09610, SIAM
  J. Discrete Math, doi:10.1137/22M1490648): 32 minor-minimal non-HPP matroids on ≤8 elements = 10 rank-3 on
  7 (incl. Fano + relaxations + duals) + 22 rank-4 sparse-paving on 8** (P_8, relaxations, coextension of
  P_7, dual). `32−10=22`. **Exactly Pro's claim.** Packing/conditional-aggregation sound ⟹ `d_TV(μ_H,SR)≥n^{−C_0}`.
- **Claim D (≤6-coord conditionals SR): CORRECT; 🔴 literature REAL.** **"Every ≤6-element matroid has HPP"
  (Wagner–Wei 0709.1269 / COSW / Kummer–Sert); smallest non-HPP = Fano F_7 (7 elements).** HPP minor+dual
  closed; conditioning = a minor ⟹ every ≤6-free-coord conditional SR. Threshold is EXACTLY as needed (all
  ≤6 HPP, first failure 7, rank-4 failure 8). ✔
- **Claim E (tensor amplification + NOT-yet-R−): CORRECT, incl. the honest negative.** `d_TV(P_n,SR)≥1−1/e`
  (SR-products ⊆ SR ⟹ the comparator inequality goes the right way; affinity multiplicative) ✔;
  `NR(P_n)≤R_n NR(μ_H)` (PB closed under convolution) ✔. 🔴 **Correctly NOT-yet-R−:** `M_0`'s margin
  `V(ν_0)=Θ(1)` is CONSTANT in `n`, leaks on poly-fraction descendants ⟹ obeys the descendant form of (36).
  A true R− needs an **asymptotic excluded-minor family whose conditioning modulus degenerates in `d`** (a
  fixed-size classification cannot supply it) **+ adaptive SUBCOND transcript indistinguishability** for the
  yes-ensemble. ✔
- **Hallucinated literature: NONE.** Every matroid claim checks out.

## Net assessment (both audits)
**Round 16 STRENGTHENS the foundation (now fully rigorous: A6, exact two-block reduction, `g_s=Θ(√I_i)`) and
CLARIFIES both sides into dual, precise targets — but does not advance the open problem.** The sparse-paving
family is a **rigorous, literature-grounded lower bound against all non-adaptive bounded-arity testers** (a
real result) and **the most promising R− lead**, but is "**one genuine conceptual step — not bookkeeping —
away from a true impossibility theorem.**" R+ ⟺ the cut-or-minor removal lemma; R− ⟺ a degenerating-margin
pseudorandom excluded-minor family. **Lean ~55–60/40 R+ ("the construction tightens the noose but does not
close it") — holds, with firmer ground + crisper forks.**
