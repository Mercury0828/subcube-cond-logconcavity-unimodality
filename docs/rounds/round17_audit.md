# Round-17 audit — universal MEM + multiscale + minor-branch-automatic + PG(2,q) — 2026-06-22

> Independent fresh-context agent (300k-random Hellinger↔TV numeric + reverse-Markov + MEM bracket, all pass)
> + referee. **All claims CORRECT.** Lean ~58–60/40 R+ ("a modest, honest raise — consolidation, not a
> decisive shift"). The remaining lemma "carries essentially all the original R+ difficulty."

## Verdicts
- **Claim 1 (universal MEM `½𝔇≤d_TV(μ,SR)≤√𝔇`): CORRECT.** Both Hellinger↔TV directions standard +
  numerically verified. **Inf/sup bookkeeping is right** (upper: one affinity-optimal `ν*` witness; lower:
  `d_TV≥1−ρ` for EVERY SR `ν`). UNIVERSAL (no minor-minimality). Kills the `𝔇≥poly` + `d_TV(·,SR)=d^{−ω(1)}`
  R− route. 🔴 **Honestly NOT the bottleneck:** the tester observes `NR`/`CutDef`, not `d_TV(·,SR)`; the live
  R− object (`𝔇≥poly`, `NR=d^{−ω(1)}`) SURVIVES MEM. The real open ratio is `NR(ν)/𝔇(ν)^C`.
- **Claim 2 (exact multiscale `𝔇=𝓔_{>m}+𝓡_m`): CORRECT.** Telescoped localization identity (exact). *(Keep
  explicit: `I_i≥0` ⟺ conditioning doesn't decrease SR-affinity — the load-bearing monotonicity, true here.)*
- **Claim 3 (minor branch AUTOMATIC): CORRECT, conditional on truncation depth.** Reverse-Markov
  `Pr[Z≥𝔇/4]≥𝔇/4` ✓; on that event `d_TV(h_{d−m},SR)≥𝔇/8` (Thm 1.1); `m=O(log(d/𝔇)) ⟹ 2^m=poly` ⟹ learnable.
  *(MINOR caveat: this proves "IF residual energy sits at depth `O(log(d/𝔇))` it's caught" — the existence of
  a good `m` is itself the Branch-A boundary; don't over-claim "the minor branch always fires.")* This is
  where MEM is used LEGITIMATELY (at low dim you can brute-force-estimate `d_TV(·,SR)`).
- **Claim 4 (conditional R+ tester): CORRECT given (EC).** `ε`-far ⟹ `𝔇≥ε²` (MEM upper) ✓; exact cover
  `𝓔_{>m}+𝓡_m=𝔇` ⟹ one branch `≥𝔇/2` ✓; complexity poly given `τ,β,m`. **A real reduction, but a reframing
  — the energy-to-cut lemma carries all the original R+ difficulty.**
- **Claim 5 (minor-minimal=pure-high-energy; PG(2,q) cut-visible): CORRECT.** (5a) minor-minimal ⟹
  `𝓔_{>m}=𝔇, 𝓡_m=0` (pure Branch A) ✓. (5b) excluded-minor SIZE may be unbounded — genuine subtlety; *(flag:
  González D'León's `PG(2,q)` excluded minors are for **weak**-HPP ≠ ordinary HPP — do not silently
  transfer; but they ARE cut-visible so unbounded size ≠ cut-blind).* (5c)(5d) `PG(2,q)`: `J=|B∩L|∈{0,1,2}`,
  `Φ=3(q−1)²/(q²+q+1)²` exact ⟹ `CutDef=Ω(d^{−3/2})` — clean growing-obstruction R+ evidence. ✓

## 🔴 Single most important doubt (the whole ballgame)
**The energy-to-cut lemma (Branch A) is exactly the case where MEM gives NO help** (MEM bounds TV; the
obstruction hides in `NR`). Claims 1–3 discharge the TV-margin + low-dim difficulties precisely by relocating
ALL remaining hardness into Branch A (= the minor-minimal pure-high-energy case). **The sparse-paving family
(r16) is a standing warning that single-block shadow visibility is NOT automatic** (`NR=2^{−Ω(n)}` with poly
`𝔇`); `PG(2,q)` is one supporting example the other way. The lemma is neither proved nor refuted and is the
whole problem.

## Lean
**~58–60/40 R+** (up a few points): foundation rigorous, MEM removes the naive R− route, minor branch
discharged ⟹ fewer ways for R− to win. But **consolidation, not a decisive shift** — the energy-to-cut lemma
is as hard as R+ ever was, global blindness is cheap (sparse-paving), and the `NR/𝔇` asymptotic ratio is
untouched. **Round 18 = attack (EC)/(MM-cut): is cut-blindness compatible with minor-minimality?**
