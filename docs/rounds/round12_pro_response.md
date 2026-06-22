# Round-12 — web GPT-5.5-Pro response (2026-06-21) — the OPENNESS RESET paid off

> Owner-relayed. Pro **abandoned the V/QHB/interlacer route** and found a cleaner R+ framework
> (monotone-noise rank ⟷ Poisson-binomial), plus TWO new R− obstructions. No R+/R− resolution yet, but a
> materially different + cleaner target. Bounds unchanged: `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n/ε²)`. Audit +
> referee checks in `round12_audit.md`. Leans **somewhat R+**. "AI-verified ≠ proved."

## §1 — 🔑 Theorem 1.1: monotone-noise rank characterization of SR [REFEREE-spot-verified]
For a monotone product channel `K` (`Pr(Y_i=1|X_i=0)=s_i`, `Pr(Y_i=1|X_i=1)=r_i`, `0≤s_i≤r_i≤1`), let
`π^μ_K=L_μ(|Y|)`. Then **`μ` SR ⟺ `π^μ_K ∈ PB_n` (Poisson-binomial) for EVERY `K`.** Forward: the channel
acts by Möbius maps `φ_i(y)=(1−r_i+r_i y)/(1−s_i+s_i y)` preserving the upper half-plane (`r_i>s_i`), so
real stability of `g_μ` ⟹ real stability of `g_{Kμ}` ⟹ the rank PGF `g_{Kμ}(t,…,t)` is real-rooted ⟹ PB.
Backward: any non-stable `g_μ` with bad root `z` ⟹ construct `K` (explicit `s_i,r_i=O(1/L)`) so the
noisy-rank polynomial has the upper-half-plane root `t` ⟹ not real-rooted ⟹ not PB. **Replaces the whole
`Δ_ij`/`V` machinery with 1-D rank-vs-PB tests.**

## §2–§3 — the defect `NR(μ)` is sound + estimable
`NR(μ)=sup_K d_TV(π^μ_K, PB_n)`; **`NR=0 ⟺ SR`** (Thm 1.1); **`NR(μ) ≤ d_TV(μ,SR)`** (channel + rank are
TV-contracting Markov kernels). **Estimable to additive `τ` over ALL channels in
`O((n log(n/τ)+log 1/δ)/τ²)` iid samples** (Rao–Blackwellized estimator `π̂_K=(1/m)Σ Q_{X^(ℓ),K}`, no
channel sampling; ℓ∞-net of the `2n`-param channel space + McDiarmid). Offline computation exp. So a
conditional `h` with `NR(h)≥τ` is poly-query rejectable (the new T3-analogue, no `V`).

## §4 — strictly STRONGER than projected ranks (T1) [REFEREE-VERIFIED numerically]
Explicit 3-bit `μ` (`100μ=(4,19,7,9,29,29,1,2)` over `000,100,010,110,001,101,011,111`): every projected
subset rank AND the total rank are Poisson-binomial (all discriminants `>0`), yet `μ` is not SR
(`Δ_{12}(g)(z_3)=(97−47z_3−29z_3²)/10000 < 0` at `z_3=2` — referee-verified exact). The thinning channel
`s=0, r=(.1,.7,1)` gives noisy-rank PGF `(2563+6868t+555t²+14t³)/10000` with complex roots `−19.63±9.50j`
(referee-verified) ⟹ not PB ⟹ caught. So `NR > 1.9e−6 > 0`. **Monotone channels detect strictly more than
`{L(|X∩A|)}`.**

## §5 — 🎯 a NEW R+ reduction (no V, no QHB, no interlacer cone)
T4 localization gives a face with `I_i(h) ≥ ε²/2n`; `I_i>0 ⟹ NR(h)>0` (Thm 1.1). The new bottleneck:
> **(Noise-rank removal)** `∃ α>0, poly P: I_i(h) ≤ P(d)·NR(h)^α` for all `h`?
If yes ⟹ poly tester `Õ(n²/ε²·(nP(n)/ε²)^{2/α})` (localize → estimate `NR` on the face). **Every rejecting
statistic is now a distance between a 1-D law on `{0,…,d}` and the Poisson-binomial family** — far cleaner
than interlacer-cone conditioning. (Pro: (44) "may conceal the same bad conditioning under more respectable
clothing," but it is a materially different, more probabilistic target.)

## §6 — Theorem 6.1: tangent rigidity at product measures (kills the Paninski R− route)
First-order SR perturbations of a full-support product law `π_p` have **standardized Fourier degree ≤ 2**
(no degree-≥3 terms; quadratic coeffs ≤0): `Δ_ij(F)≥0` on all reals + the limit ⟹ `∂_ij H ≤ 0` everywhere
⟹ (multiaffine bounded-above ⟹ constant) `∂_ij H` a nonpositive constant. ⟹ the tangent cone at a product
sits in an `O(n²)`-dim subspace (vs ambient `2^n−1`). **The "random high-degree SR perturbation of uniform"
lower-bound architecture cannot work to first order.**

## §7 — Theorem 7.2: homogeneous-selector incompatibility is locally discoverable (kills another R−)
For `k`-homogeneous SR children `π,σ` (common support), selector `h=½a+½z_0 b`: **`h` SR ⟺ `π=σ`** (proper
position ⟹ stochastic domination on an antichain ⟹ equality). And the down-up chain (spectral gap `≥1/k`
for homogeneous strongly-log-concave / SR) gives `E_{S∼σ↓}[1−ρ(π^S,σ^S)²] ≥ (1−ρ(π,σ)²)/k`, so a far
selector exposes an inverse-poly **link** discrepancy on a poly-likely face (SUBCOND-discoverable: condition
`X_0`, sample, delete a random element, condition on the link). **A hidden mismatch between homogeneous SR
children cannot give a super-poly lower bound.**

## §8 — status + the exact new bottleneck
PROVED: Thm 1.1 (channel characterization); Thm 3.1 (`NR` estimability); §4 strictness; Thm 6.1 (product
tangent rigidity); Thm 7.2 (homogeneous selector localization). NOT proved: the removal inequality (44);
a random-restriction theorem producing a face with inverse-poly `NR`; a far distribution with all
discoverable conditional `NR` super-poly-small; adaptive transcript indistinguishability; R+/R−.
**EXACT NEW BOTTLENECK (44): `I_i(h) ≥ η ⟹ NR(h) ≥ (η/poly(d))^{O(1)}`** — a robust projection from
multivariate SR incompatibility to a 1-D Poisson-binomial obstruction under an optimized monotone channel.
Pro confidence: high in Thms 1.1/3.1/6.1/7.2; moderate on (44); **leans somewhat R+** (every concrete
obstruction examined has a visible noisy-rank defect or is forced by expansion to reveal one).
