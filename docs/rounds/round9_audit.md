# Round-9 audit — Pro's analytic claims (localization, QHB⟹R+, tensoring, refutation criterion) — 2026-06-21

> Independent adversarial agent + referee. The `g_s` algebraic core (non-SR parent; every 1-coord
> contraction/deletion a perfect square) was **referee-verified separately** (numeric, `derisk`). This
> audit covers the analytic claims. **No FATAL. Two GAPs, both = the precise normalization of `V`.**

## Verdicts
- **Claim A (strengthened projected-rank test): CORRECT.** Projection of SR is real-rooted ⟹ `|X∩A|`
  Poisson-binomial (ASW); `RankDef(μ) ≤ d_TV(μ,SR)`; union-bound sample complexity `O((n+log1/δ)/τ²)`
  right (reuse one sample batch; union over deviation events). MINOR: state the sample-reuse.
- **Claim B (localization theorem — the rare-face-blocker): ALL CORRECT.** B0 (`d_TV≥ε ⟹ 𝔇≥ε²`) ✓;
  B1(i) affinity factorization exact ✓; B1(ii) Cauchy–Schwarz right direction ✓; **B1(iii): the feared
  `q_b`-coupling is UNFOUNDED** — C–S eliminates `q_b` (`Σq_b=1`) *before* the `sup_ν`, so
  `A_d(p)² ≤ Σ_b p_b A_{d−1}(p^{(b)})²` cleanly ⟹ `I_i≥0` (needs `ν^{(b)}∈SR_{d−1}` by closure ✓); B2
  telescoping exact ✓; B3 Cor 2.2 reverse-Markov ✓. **CONCLUSION: an `Ω(1)`-far μ CANNOT hide all
  incompatibility on `n^{−ω(1)}`-path-probability faces — the rare-hidden-face refutation of (L) is dead.** ✓
- **Claim C (QHB⟹R+): reduction logic CORRECT** (inverse-poly `γ` ⟹ poly queries; completeness via
  `V=0` on SR faces). 🔴 **d=2 transfer: GAP** — `d_TV(p,SR_2)≤2V(p)` and `I_i=𝔇_2≤4V` hold *in form*
  (a single bilinear constraint admits linear transfer), but the **constant 2 and exponent α=1 depend on
  the exact (projective) normalization of `V`**, not pinned down. (d=2 is the only fully-verified QHB
  instance + base evidence — so the constant matters.)
- **Claim D: Lem 5.1 (tensor affinity `d_TV(h^{⊗m},SR)≥1−e^{−mδ²/2}`) CORRECT.** 🔴 **Lem 5.2
  (`V(pq)=max{V(p),V(q)}`): GAP** — `Δ_ij(pq)=q²Δ_ij(p)` for a `p`-pair ✓ and mixed pairs vanish ✓, BUT
  the equality needs `q²≤1` on `V`'s evaluation domain; SR is an *all-ℝⁿ* condition while the bound needs
  the *cube/projective* domain — **must confirm the cube-evaluated `V` faithfully certifies all-ℝⁿ
  stability AND `q²≤1` there.** Load-bearing for E1.
- **Claim E1 (refutation criterion): CORRECT conditional on Lem 5.2.** PB rank closed under tensoring ✓;
  `V=M` under tensoring needs the conditional Lem 5.2 (inherits the GAP).
- **Claim E2 (Wagner–Wei arXiv:0709.1269): CONFIRMED** — the exact local gluing iff (proper minors stable
  + `Δ_ij≥0` on all reals ⟹ parent stable) is real and correctly characterized; **QHB is fairly its
  quantitative analogue.** **E3:** no dimension-uniform quantitative version is known — **genuinely open.**

## 🔴 THE LINCHPIN (single most important item)
**Pin down the projective certificate `V` precisely and prove: (i) `V(g)=0 ⟺ SR` [established round-8], (ii)
the `q²≤1` cube-domain tensoring identity (Lem 5.2), (iii) the exact d=2 constant.** Both GAPs collapse to
this. Until done, the "d=2 + `g_s` ⟹ QHB plausible" evidence and the §6 refutation calculus are not airtight.

## Assessment of QHB (the make-or-break)
- **FOR QHB (⟹ R+):** holds in d=2; the explicit `g_s` minor-minimal family satisfies *linear* QHB.
- **AGAINST QHB (⟹ R−):** minor-minimal HPP obstructions are **abundant and irregular** (sporadic excluded
  minors; no known uniform modulus) — a dimension-uniform `I_i ≤ poly(d)·V^α` would be surprising.
- **Auditor's adversarial lean: QHB more likely FALSE at dimension-uniform strength (⟹ R−)**, possibly true
  in a weakened (d-dependent-exponent / family-restricted) form. **Pro leans DIVIDED.** Honest status:
  **genuinely OPEN.** Highest-value next step: (a) attempt a dimension-uniform QHB proof, OR (b) build the
  E1-refuter `h_d` from a known minor-minimal HPP obstruction (rank-4 sparse-paving 8-element matroids).
