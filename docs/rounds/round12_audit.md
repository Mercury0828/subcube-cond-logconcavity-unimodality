# Round-12 audit — Pro's noisy-rank framework (Thms 1.1/3.1/6.1/7.2) + "does it escape the wall?" — 2026-06-21

> Independent adversarial agent (sympy + literature) + referee. **Thms 1.1, 3.1, 6.1, 7.2 ALL CORRECT.**
> The §4 strictness example was referee-verified separately. **Claim 6 (escape) = GAP: partial escape, not
> proven full.** Lean: **cautiously R+.**

## Verdicts
- **Thm 1.1 (monotone-noise rank characterization): CORRECT.** (1b) `Im φ_i·|1−s_i+s_i y|²=(r_i−s_i)Im y`
  (symbolic) ⟹ `φ_i` UHP-self-map; stability preserved under coordinatewise UHP-substitution + mult by the
  real-stable factors `(1−s_i+s_i y)` (BBL/Borcea–Brändén closure). (1c) real-rooted nonneg PGF ⟺ PB (ASW).
  (1d) `(1−r_i+r_i t)/(1−s_i+s_i t)=z_i` holds *identically* (symbolic). (1e) `0<s_i<r_i<1` for large `L`.
  (1f) `Im t=L>0` genuine UHP root. *(Structural note: backward construction uses `b_i>0 ∀i` = the correct
  negation of real stability — a root in the open product UHP, one `ξ<min_i(a_i−1)/b_i` serving all coords.)*
- **Thm 3.1 (`NR` estimable): CORRECT.** `E‖π̂_K−π^μ_K‖₁ ≤ √((n+1)/m)` (unbiased + `ΣVar(Q_k)≤ΣE Q_k=1`);
  McDiarmid `c_ℓ=1/m`; net `(Cn/τ)^{2n}` (log `O(n log(n/τ))`); `d_TV(Q_{x,K},Q_{x,K'})≤n‖K−K'‖∞`. MINOR:
  state explicitly that the *empirical* `π̂_K` is `n`-Lipschitz in `K` (avg of Lipschitz `Q_{x,K}`) so the
  net→all sup transfers — it holds. `Õ(n/τ²)` tester accepting SR / rejecting `NR≥τ`.
- **Strictness (§4): CORRECT logic.** deterministic `K∈{(0,0),(0,1),(1,1)}` reproduce `|X∩A|` ⟹ `NR ≥` every
  projected-rank defect; the verified 3-bit example has all projected ranks PB but a thinning channel
  catches it ⟹ `NR` strictly dominates the T1 family.
- **Thm 6.1 (product tangent rigidity): CORRECT.** `F` stable ⟺ `g` stable (affine map, Jacobian `1/σ_i>0`).
  `Δ_ij(1+tH)` has `t`-coefficient **exactly `−∂_ij H`** (symbolic), `t²` term `o(t)` ⟹ `∂_ij H ≤ 0` on `ℝ`;
  multiaffine bounded-above ⟹ constant ⟹ `H` degree ≤2, quadratic coeffs ≤0. **Validly kills the first-order
  Paninski R− route** (linear test gets no first-order signal).
- **Thm 7.2 (homogeneous-selector localization): CORRECT.** (5a) BBL proper-position ⟹ stochastic domination
  on the level-`k` antichain ⟹ `π=σ` — confirmed (BBL's order for Pemantle's conjectures). (5b) down-up gap
  `≥1/k` for `k`-homogeneous SLC/SR (ALOV "Log-concave polynomials II"; Cryan–Guo–Mousa) + the Dirichlet-form
  identity `ℰ(f)=E_S Var_{π^S}f`, `f=√(σ/π)`, Poincaré ⟹ `E_{S∼σ↓}[1−ρ(π^S,σ^S)²] ≥ (1−ρ)²/k`. **Validly
  kills the homogeneous-selector R− route** (far selector ⟹ inverse-poly link discrepancy, SUBCOND-findable).

## 🔴 Claim 6 (escape the interlacer wall?) — GAP: PARTIAL, not proven full
The new bottleneck **(44) `I_i(h)≥η ⟹ NR(h)≥(η/poly(d))^{O(1)}`** is **structurally different** from UQHB:
`NR` is a *channel optimization* (sup over a `2n`-param box of an explicit TV functional), not a worst-case
conditioning of the interlacer cone `V`. The backward construction (root→channel) suggests one can *read off*
a good channel from a localized incompatibility direction. **BUT it is QUALITATIVE** (`L→∞`, so `s_i,r_i→0`,
degenerate channel): whether a localized `I_i(h)≥η` gives a **poly-bounded** `NR` (vs a signal that collapses
as the channel degenerates) is **unproven** — the bad conditioning may re-enter as the **channel-degeneracy /
TV-collapse rate**. So (44) is fresher and more attackable, but NOT yet proven strictly easier. **Not a
relabel; not a settled escape.**

## Single most important doubt + next step
**The quantitative `η→NR` rate, independent of channel degeneracy.** Decisive next question: does a localized
`I_i(h)≥η` yield a **BOUNDED-magnitude** channel (`L=poly`, `s_i,r_i∈[1/poly, 1−1/poly]`) with `NR(h)≥poly(η)`?
If yes ⟹ R+; if the incompatibility can only be exposed by degenerate (`L→∞`) channels with vanishing TV ⟹ the
wall resurfaces. **Lean: cautiously R+** — the framework is solid and both R− routes are dead; the risk is
concentrated entirely in this rate.
