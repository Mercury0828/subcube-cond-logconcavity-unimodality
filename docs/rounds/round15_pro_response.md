# Round-15 — web GPT-5.5-Pro response (2026-06-22) — g_s SETTLED (supports R+); PF certificate corrected to σ_min

> Owner-relayed. **Settles the candidate hard core `g_s` favorably for R+** + corrects round-14's PF-minor
> normalization (`k^{k/2+1}` determinant → `σ_min` of a negative Toeplitz section). General theorem still
> open. Bounds unchanged. Audit + referee checks below. Lean back UP to **~58–62/40**.

## 🔑 HEADLINE: `g_s` is NOT bounded-channel-blind
**`NR(g_s)=Θ(s^{−2})`, `I_i(g_s)=Θ(s^{−4})` ⟹ `NR(g_s)=Θ(√I_i(g_s))`** (clean square-root rate). An explicit
**fully INTERIOR** channel (endpoint margin `Θ(s^{−3})`) exposes `d_TV(π_K^{g_s},PB)=Ω(s^{−2})=Ω(√I_i)` with
descendant `F=∅`, witness prob 1, channel magnitude `O(s³)`. **No covariance witness needed.** ⟹ the
minor-minimal obstruction (non-SR parent, all proper conditionals SR) is decisively caught — R+ on the hard core.

## §1 — Lemma 1.1 (spectral PF separation) [REFEREE-VERIFIED structure]
For the consecutive Toeplitz section `T_{ℓ,k}(q)=[q_{ℓ+j−i}]`: if `det T<0` and `σ_min(T)≥τ` then
`d_TV(q,PB) ≥ τ/2` (dimension-independent). Proof: PB ⟹ `det T(p)≥0`; the segment `(1−t)T(q)+tT(p)` crosses
a singular matrix ⟹ `σ_min(T(q)) ≤ ‖T(q)−T(p)‖_op ≤ ‖q−p‖_1 = 2d_TV` (Young). **Statistically robust** (no
`k^{k/2}` loss; an empirical `q̂` with `‖q̂−q‖_1<τ` keeps `det<0`).

## §2 — exact `NR(g_s)` rate [REFEREE-VERIFIED]
`g_s` (blocks `A,B` size `2s`, `θ_s=arcsin(1/s)`, `c_s=2cosθ_s`). The `K_A=|X∩A|` law is 3-point:
`q_s(s−1)=a_s, q_s(s)=2a_s cosθ_s, q_s(s+1)=a_s`, `a_s=1/(2(1+cosθ_s))`. **`1/40s² ≤ NR(g_s) ≤ ½tan²(θ_s/2) ≤
1/2s²`.** LOWER: centered tridiagonal Toeplitz section (size `L≈3πs/2`), eigenvalues `λ_j=2a_s(cosθ_s+
cos(jπ/(L+1)))` — **exactly one negative**, `σ_min≥θ_s²/20≥1/20s²` ⟹ Lemma 1.1. *(Referee: eigenvalue
formula EXACT, exactly 1 negative eigenvalue, `σ_min≥θ²/20` confirmed at s=4..64.)* UPPER: SR comparator
`ḡ_s` (`c_s→2`, = polarization of `x^{s−1}y^{s−1}(x+y)²`, stable) with `d_TV(g_s,ḡ_s)=½tan²(θ_s/2)`.

## §3 — `I_i(g_s)=Θ(s^{−4})` ⟹ `NR(g_s)=Θ(√I_i)`. (every 1-coord del/contraction SR ⟹ `I_i=𝔇(g_s)`.)

## §4 — explicit interior channel: `(s_j,r_j)=(δ,1−δ)` on `A`, `(δ,δ)` on `B`, `δ=1/320s³`. Couple to the
boundary channel (each bit flips w.p. `≤δ`) ⟹ `‖q_s^δ−q_s‖_1≤1/40s²` ⟹ `σ_min(T(q_s^δ))≥1/40s²` ⟹
`d_TV(q_s^δ,PB)≥1/80s²=Ω(√I_i)`, endpoint margin `δ=Ω(I_i^{3/4})`.

## §5 — 🔧 CORRECTION: determinant magnitude is the WRONG normalization [REFEREE-VERIFIED]
Continuant: `det T_k(q_s)=a_s^k sin((k+1)θ_s)/sinθ_s`; first negative at `k*=⌊π/θ_s⌋=Θ(s)`, where
**`|det T_{k*}|=e^{−Ω(s)}`** (referee: `-4e-8,-9e-16,...,-9e-122` for s=4..64). So round-14's `[−det]/k^{k/2+1}
≥(η/d)^C` clause gives `s^{−Ω(s)}` (super-poly small) **even though the rank law is `Ω(s^{−2})`-far from PB**
and a larger section has `σ_min=Ω(s^{−2})`. A determinant multiplies ALL singular values ⟹ can be exp-small
while the matrix is poly-far from singular. **The robust certificate is `σ_min` of a negative Toeplitz
section, NOT a poly-normalized determinant.** *(This corrects a flaw the orchestrator propagated from r14.)*

## §6 — `g_s` lifts still leak the witness ⟹ NOT R−
For `g_s⊗ν` (any `ν` on disjoint coords): apply the `g_s` channel + zero the `ν`-coords ⟹ output rank law
still `q_s` ⟹ same certificate, distance `1/40s²` from EVERY PB law. So **independent padding, tensoring,
many copies, arbitrary permutation do NOT hide the obstruction** (the all-channel NR estimator searches
coordinate-dependent channels; cost = log of the channel net). E.g. `μ_s=g_s^{⊗Θ(s⁴)}` (`D=Θ(s⁵)`,
constant-far) is detected in `Õ(D/τ²)=Õ(D^{9/5})` samples. **A genuinely hard lift must ENTANGLE the core**
so no product channel can suppress the surrounding coords and recover a spectrally robust Toeplitz violation.

## §7 — the corrected general target (replaces (35)) ⟹ R+
> `I_i(h)≥η ⟹` w.p. `≥(η/d)^C` a poly-samplable descendant has EITHER (1) positive conditional covariance
> `≥(η/d)^C`, OR (2) a bounded-channel noisy-rank law with a **negative Toeplitz section at operator-norm
> distance `≥(η/d)^C` from singularity** (`det T<0, σ_min(T)≥(η/d)^C`).
(1)→r13 covariance theorem; (2)→Lemma 1.1; learn rank law `O(d/τ²)`; T4 supplies the face. ⟹ poly tester.

## Status
PROVED: `g_s` asymptotics (`NR=Θ(s^{−2})`, `I_i=Θ(s^{−4})`, `NR=Θ(√I_i)`); interior channel; Lemma 1.1
(σ_min certificate); `g_s` tensor/padded/permuted lifts ruled out as R−. CORRECTED: σ_min not determinant.
NOT: the general compatibility-aware localization; a **genuinely entangled** obstruction evading all product
channels + descendants; R+/R−. Bounds `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n/ε²)`. **Pro: high confidence in the
`g_s` results + the spectral PF lemma; general localization genuinely open; but `g_s` + lifts ruled out as R−.**
