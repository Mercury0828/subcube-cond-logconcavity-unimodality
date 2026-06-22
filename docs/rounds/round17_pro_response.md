# Round-17 — web GPT-5.5-Pro response (2026-06-22) — MEM universal; minor branch AUTOMATIC; R+ ⟺ ONE lemma

> Owner-relayed. **Collapses the dichotomy to a single open statement.** MEM holds universally (kills the
> degenerating-margin R− route) but is honestly flagged as NOT the bottleneck; an exact multiscale
> decomposition makes the low-dim minor branch AUTOMATIC; so R+ ⟺ one "energy-to-cut" lemma. PG(2,q) (a
> growing obstruction) is cut-visible. Referee-verified the two key computations. Lean R+ ~58–62/40.

## §1 — 🔑 MEM is UNIVERSAL (Theorem 1.1) [referee-verified]
For EVERY distribution: **`½𝔇(μ) ≤ d_TV(μ,SR) ≤ √𝔇(μ)`** (via `1−ρ≤d_TV≤√(1−ρ²)` + `1−√(1−x)≥x/2`).
⟹ **`𝔇(ν_d)≥d^{−O(1)}` and `d_TV(ν_d,SR)=d^{−ω(1)}` is IMPOSSIBLE** — the "degenerating excluded-minor
margin" R− route is DEAD. `g_s`'s `𝔇=Θ(d_TV²)` is the extreme Hellinger side of this universal interval.
🔴 **But MEM is NOT the bottleneck:** the margin in MEM is the full coefficient-space `d_TV(ν,SR)`, which the
algorithm does NOT observe — it sees `CutDef(ν)=max_A d_TV(L(|X∩A|),PB)` and `NR(ν)`. (My MEM framing was the
wrong sharpest-question.)

## §2 — the corrected R− target: poly-FAR but observable-shadow-degenerate
A surviving R− core (8/24): minor-minimal non-HPP `ν_d`, every proper minor SR, `𝔇(ν_d)≥d^{−O(1)}`,
`d_TV(ν_d,SR)≥½d^{−O(1)}` (**poly-far, not super-poly-close!**), but `NR(ν_d)=d^{−ω(1)}` (the observable
two-block/channel shadow degenerates). The open ratio is `NR(ν)/𝔇(ν)^C`, NOT `d_TV(ν,SR)/𝔇(ν)`.

## §3 — 🔑 EXACT multiscale decomposition (Theorem 3.1)
`𝔇(h) = 𝓔_{>m}(h) + 𝓡_m(h)`, where `𝓔_{>m}=Σ_{t=0}^{d−m−1} E[J_t]` (defect expended above scale `m`,
`J_t=I_{π_{t+1}}(h_t)` along a random prefix) and `𝓡_m=E[𝔇(h_{d−m})]` (defect surviving into a random
`m`-dim descendant). Nonnegative, sum to `𝔇(h)`. (Telescoping the localization identity `E[𝔇(h_{t+1})|h_t,i]
=𝔇(h_t)−I_i(h_t)`.)

## §4 — 🔑 the minor branch is AUTOMATIC ⟹ R+ ⟺ ONE lemma
From Thm 3.1, either **Branch A** `𝓔_{>m}≥𝔇/2` ⟹ a poly-discoverable `I_i`-witness at scale `>m`
(`Pr[J_t≥𝔇/4d]≥𝔇/4d`); or **Branch B** `𝓡_m≥𝔇/2` ⟹ a random `m`-dim descendant is `𝔇/8`-far from SR
w.p. `≥𝔇/4` (Thm 1.1) — **already the low-dim minor branch, poly-discoverable for `m=O(log(d/𝔇))`** (learn
the `m`-bit conditional in `O(2^m/𝔇²)=poly` samples). **So the ONLY unproved branch is:**
> **(Energy-to-cut lemma)** for `m=O(log(d/D))`, `𝓔_{>m}(h)≥D/2 ⟹` a poly-query procedure finds (w.p.
> `(D/d)^{O(1)}`) a prefix face `F` + subset `A` with `d_TV(L_{h|F}(|X∩A|),PB)≥(D/d)^{O(1)}`.
This lemma ⟹ **R+** tester `Õ(2^m/ε⁶ + n/βτ²)=poly(n,1/ε)` (§5).

## §6 — minor-minimal obstructions = the PURE high-energy case
For minor-minimal `ν`: `I_i(ν)=𝔇(ν)` ∀i, and `𝓔_{>m}(ν)=𝔇(ν)`, `𝓡_m(ν)=0` ∀`m<d` (once any coord fixed,
SR). So a proof of the energy-to-cut lemma for minor-minimal measures rules out the most concentrated R−
core. **The dimension issue is genuinely open:** HPP excluded-minor size may be UNBOUNDED — in weak-HPP,
`PG(2,q)` are ALL excluded minors (González D'León); so "all minimal obstructions are 8 points in disguise"
is a poor assumption. (Kummer–Sert finite-size only; Kummer–Sawall 2402.01272 no bounded-support theorem.)

## §7 — `PG(2,q)` (growing obstruction) is CUT-VISIBLE [referee-verified] ⟹ R+ evidence
`μ_q` = uniform rank-3 bases of `PG(2,q)`, `d=q²+q+1`. For a line `L`, `J=|B∩L|∈{0,1,2}`; Choe–Wagner counts
`A=(q+1)q³/2, B=(q+1)q³(q−1)/2, C=(q+1)q³(q−1)²/6`. **`Φ=4p_0p_2−p_1²=3(q−1)²/(q²+q+1)²`** (referee-verified
exact, q=2..8) ⟹ (round-13 sharp PB sep) `CutDef ≥ (Φ/15)^{3/2}=Ω(q^{−3})=Ω(d^{−3/2})`. A growing family
whose high-dim HPP-failure is exposed by ONE line's two-block defect.

## §8 — full R− still also needs an SR yes-ensemble + adaptive SUBCOND transcript indistinguishability.

## Status
PROVED (Pro high-confidence; referee-verified MEM + PG(2,q)): universal MEM `½𝔇≤d_TV≤√𝔇`; exact multiscale
`𝔇=𝓔_{>m}+𝓡_m`; the minor branch automatic + poly-discoverable; `PG(2,q)` cut-visible `Ω(d^{−3/2})`. NOT
(Pro LOW-confidence): the **energy-to-cut lemma** (high-dim compatibility energy ⟹ poly-visible cut defect)
— now the SINGLE exact remaining R+ theorem; a poly-far/shadow-degenerate minor-minimal R− family; bounded
HPP-excluded-minor support; adaptive SUBCOND indistinguishability; R+/R−. Bounds unchanged. **The whole
problem = does high-dimensional compatibility energy force a polynomially visible cut defect?**
