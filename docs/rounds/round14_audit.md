# Round-14 audit — Pro's root-route REFUTATION + PF-minor reframing — 2026-06-22

> Independent adversarial agent (reproduced the §2.2 counterexample, Thm 2.1 ratio, Thm 3.1 constant/regime,
> Thm 4.1 net+covariance; ASW confirmed) + referee. **All claims CORRECT.** Lean is more conservative than
> Pro's: **~52/48 R+ — genuinely open, marginal lean.**

## Verdicts
- **Thm 2.1 (universal root LB): CORRECT.** Each PB factor sits on segment `[1,z]` ⟹ `|P(z)|≥m(z)^d`;
  `|P(z)|≤2d_TV·R(z)^d`. **Exponential-in-d unavoidable** (LB `(m/R)^d`, `m/R=0.217<1` at `−1+i/2`; tight
  with §2.2). Root-depth alone ⇏ poly(1/d) PB-distance.
- **The refutation: CORRECT.** Channel `(1/10,9/10)` has mean ½ ⟹ Bin(d,½)↦PB + data-processing TV
  contraction ⟹ output stays `≤(3/2)4^{−d}` from PB with a root at `Im=160/401≈0.399`. **Survives a fixed
  nondegenerate interior channel.** μ_4 optimism correctly diagnosed as a **fixed-degree artifact**.
  Round-13 regularization is **one-way** (`NR=τ ⟹` bounded witness; NOT root⟹τ-bound).
- **Thm 3.1 (PF-minor sep): CORRECT (order); MINOR.** Honest constant is `2·k^{k/2+1}` (since `max_j|q_j−p_j|
  ≤2Δ`), not `k^{k/2+1}` — order right, constant ~2× optimistic, immaterial. ASW (PB ⟺ TN Toeplitz)
  confirmed. `k=O(log d/loglog d) ⟹ k^{k/2+1}=poly(d)` verified. `PF(q)≤d_TV` sound (lower-bound hierarchy).
- **Thm 4.1 (Ω(1)-far, NR=2^{−Ω(d)}): CORRECT + correctly NOT-R−.** Net `O(d²)` log-size + Hoeffding ⟹
  `sup_K d_TV≤O(d²2^{−d/2})` (modulo a standard, true Lipschitz-in-channel-params assertion). 🔴 The bad
  2-face `(+,−,−,+)` has **POSITIVE** covariance `+1/8` ⟹ round-13 §3 fires *on the descended conditional*
  ⟹ SUBCOND localization catches it ⟹ genuinely NOT R−. ⟹ "`I_i≥η⟹NR≥poly`" (descend then measure) is
  **strictly stronger** than global NR; descendant-search sees obstructions invisible to the parent.
- **Thm 5.1 + §5 "localizes the wrong quantity": CORRECT (kills the naive SCP route).** Hermon–Salez SCP
  Poincaré `≥1/m` localizes Hellinger `1−ρ²` — but `I_i` is disagreement with the *set of compatible pairs*,
  not Hellinger; compatible children can be far apart (Thm 5.1 fires even on SR parents); the **consistency
  problem** (per-face optima ≠ restrictions of one global optimum) blocks gluing; `g_s`/N5 rule out any
  per-face-independent-comparator argument. *(Caveat: refutes the naive route, not every spectral-indep variant.)*
- **Corrected §6 target: fair + strictly more attackable** (allows descent + uses normalized PF-minors, not
  root depth). **But (honest):** the route is **renamed, not reduced** — the open core ("compatibility-aware
  total positivity") is plausibly the SAME hardness the interlacer + root routes hit.

## 🔴 Single most important doubt (the auditor's)
The whole R+ program rests on the **unproven §6 conjecture**: every irreducible minor-minimal SR obstruction
with `I_i=Ω(1/poly)` carries an **inverse-poly normalized PF margin reachable through a bounded channel after
poly-discoverable descent**. The §2 family proves a *raw* normalized PF margin can be `4^{−d}` for a fixed `q`;
**there is currently NO mechanism** exempting incompatibility-forced obstructions from this exponential
smallness — only class-by-class evidence (product/homogeneous/μ_4). N5 (the repo's windows-search finding:
far-from-SR with all bounded-coord conditionals SR) is a live warning that low-order local statistics can be
globally blind.

## 🎯 Sharper R− characterization (fold into round 15)
An R− instance needs three ingredients: `I_i=Ω(1/poly)`; NO poly-discoverable positive-covariance descendant;
all bounded-channel PF minors super-poly-small. **`g_s`/N5 already supply two** (global SR-violation invisible
to all `≤k` conditionals). **The missing ingredient = a NON-SYMMETRIC lift that hides the rank statistic** —
because *symmetric* such families are poly-testable via the global rank sequence (the repo flags this). So the
R− target is now crisp: a non-symmetric `g_s`-lift whose rank statistic is SUBCOND-hidden.

## Lean
**~52/48 R+ (genuinely open).** Down from 70/30. Reasons: every proven *positive* mechanism covers only
special classes; two shortcuts (root-depth, SCP-Hellinger) refuted ⟹ the obstruction looks structural, not a
missing lemma; the R− side gained a credible (unbuilt) template (N5 + §2 exp-smallness + non-symmetric lift).
Above 50% only because μ_4 *is* caught with constant margin and no R− instance has actually been built (hiding
the global rank statistic from poly SUBCOND remains unsolved). **Decisive next step: settle `g_s` under the lift.**
