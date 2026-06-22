# Round-15 audit — g_s resolution + σ_min PF certificate — 2026-06-22

> Independent fresh-context agent (ASW/Edrei + Borcea–Brändén literature-confirmed; 20k-random-PB numeric +
> the g_s s=4..64 data). **All claims CORRECT.** Two honest flags (one verification-debt, one open math).
> Lean ~57/43 R+ (up from the round-14 audit's 52/48).

## Verdicts
- **Lemma 1.1 (σ_min spectral PF separation): CORRECT — incl. the crux (1a).** PB ⟺ real-rooted ⟺ the
  *semi-infinite* coefficient Toeplitz matrix is totally nonnegative (ASW/Edrei). A contiguous window
  `[q_{ℓ+j−i}]` with out-of-range entries `=0` is **literally a minor of that infinite TP array** (the tail
  zeros are honest entries, not a truncation artifact), so `det≥0` for PB — even when `L≫deg`. **Verified
  over 20,000 random PB laws, all sizes/offsets: min det = 0, never negative.** (1b) `σ_min=`Eckart–Young
  distance to nearest singular matrix; IVT gives a singular `S` on the `T(q)→T(p)` segment ⟹
  `σ_min(T(q))≤‖T(q)−T(p)‖_op`. (1c) finite section = compression of convolution-by-`(q−p)` ⟹ op-norm
  `≤‖q−p‖_1=2d_TV` (Young). Dimension-independent, robust, **no `k^{k/2}` loss.**
- **NR(g_s)=Θ(s^{−2}): CORRECT.** Exactly one negative eigenvalue at `L=⌊3π/2θ⌋−1`, `σ_min≥θ²/20≥1/20s²`
  (s=4..64); "keep A, zero B" is a product channel with rank law `q_s`; `ḡ_s`=polarization of
  `x^{s−1}y^{s−1}(x+y)²` is stable (Borcea–Brändén) ⟹ SR, `q̄=Bin(2,½)` PB; `d_TV=½tan²(θ/2)≤1/2s²` (machine
  precision). ⟹ `NR(g_s)∈[1/40s²,1/2s²]`.
- **NR(g_s)=Θ(√I_i): CORRECT, ONE dependency (see flag 1).** `d_TV²≤𝔇` standard; `1−ρ(q,q̄)²=Θ(s^{−4})`
  verified.
- **det→σ_min correction: CORRECT.** Continuant `det T_k=a_s^k sin((k+1)θ)/sinθ`; `|det T_{k*}|=e^{−Ω(s)}`
  (verified `−3e-10…−1.6e-179`); a `[−det]/k^{k/2+1}` clause gives `s^{−Ω(s)}` = a **false negative**, while
  `σ_min=Ω(s^{−2})` correctly reports poly distance. The r14 `(35)` clause (2) was genuinely mis-normalized
  (and the orchestrator propagated it in the r15 brief). Fixed.
- **g_s lifts NOT R−: CORRECT for PRODUCT lifts; entangled lifts OPEN (flag 2).** "keep block-A of one
  factor, zero the rest" reproduces `q_s` ⟹ padding/tensoring/copies/permutation don't hide it; the
  all-channel NR estimator costs `Õ(D/τ²)` (poly-net), so a permutation hides the block *computationally,
  not statistically*. (5d) does NOT rule out a *correlated/entangled* embedding — the surviving R− hope.
- **Corrected §7 target: fair + correctly normalized; ⟹ R+ CONDITIONALLY** (the antecedent — the
  compatibility-aware localization — is the unproven part).

## 🔎 Flag 1 (VERIFICATION DEBT — load-bearing): the `I_i(g_s)=𝔇(g_s)` identity
The headline `NR(g_s)=Θ(√I_i)` leans on `I_i(g_s)=𝔇(g_s)=1−sup_{ν SR}ρ(g_s,ν)²` for **every** coordinate `i`
— a step the auditor took from the project's affinity framework (round-10 variational formula T5) rather than
re-deriving. The spectral chain (Lemma 1.1, the `NR` rate, det→σ_min) is independently rock-solid; but if
`I_i` is a sup over *compatible-pair sets* and only *bounds* (not equals) `𝔇`, the exponent in `√I_i` could
shift. **Action: a fresh first-principles derivation of `I_i=𝔇` (folded into the round-16 brief) — this is
the next thing to nail down rigorously.** *(Does NOT affect the `NR(g_s)=Θ(s^{−2})` result, which is
unconditional; only the `I_i` linkage.)*

## 🎯 Flag 2 (OPEN MATH): the entangled obstruction (= the R− hope)
An `I_i=Ω(1/poly)` family, all proper conditionals SR, rank statistic SUBCOND-hidden by core↔environment
correlation so no product channel + descendant exposes a poly-`σ_min` negative Toeplitz section. **Not known
to exist; looks hard against sup-over-all-product-channels + poly descendants — but not excluded.** Where to
look (auditor): minor-minimal Rayleigh-not-SR families with hidden-subspace correlation (the ledger's
non-symmetric-spread RED-3 candidate); round-12 product-tangent-rigidity boundary.

## Lean
**~57/43 R+** (Pro says 58–62; audit slightly more conservative — the §7 antecedent is unproven and the
`I_i=𝔇` bridge is unverified by the auditor). The purpose-built hard core `g_s` is decisively caught + the
certificate is clean/robust + a propagated normalization error is fixed ⟹ a real raise; the general theorem
+ the entangled R− route keep it well short of decisive.
