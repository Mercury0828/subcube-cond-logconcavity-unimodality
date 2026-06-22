# Round-11 audit — Pro's common-factor invariance + product-class √-UQHB + perturbation continuity — 2026-06-21

> Independent adversarial agent (analytic + literature) + referee numeric check + referee resolution of the
> flagged doubt. **All claims CORRECT.** Witnesses numerically verified (`Δ_{0k}(1)=sδ_k`, `Δ_{rk}=−stδ_rδ_k`,
> exact). R+/R− lean: **cautiously R+** (both Pro and audit).

## Verdicts (all CORRECT)
- **Claim 1 — common-factor invariance (Thm 1.1): CORRECT.** Lower (`c⊗ν` SR, `ρ` factorizes) + upper
  (condition `Q` on `Y`, closure ⟹ `Q_{X|y}` SR, `ρ(c⊗p,Q)=Σ_y√(c q_Y)ρ(p,Q_{X|y}) ≤ A(p)ρ(c,q_Y) ≤ A(p)`)
  both rigorous; the only external input ("conditioning preserves SR") is a true BBL closure property.
- **Claim 2 — product-class √-UQHB (Thm 2.1): CORRECT** (`Gap_λ ≤ 2(d−1)√Ξ`, α=½, P=2(d−1)).
  - witnesses (2a) `Δ_{0k}(1)=sδ_k`, (2b) `Δ_{rk}=−stδ_rδ_k` — analytically re-derived + **referee-numeric-verified exactly**.
  - **(2d) repair SR-ness CONFIRMED:** `h'=c·g`, `c=∏_{k≠r}(1−p_k+p_k z_k)` (stable affine product),
    `g=(1−λ)(1−p_r+p_r z_r)+λ z_0(1−q_r+q_r z_r)` 2-bit with Wagner–Wei discriminant `βγ−αξ=sδ_r ≥0` ⟹
    `h'∈SR`. **MINOR (fixable):** the all-`δ_k<0` case (no positive `δ_r`) is not stated — fix: collapse
    all coords, `h'=c'·[(1−λ)+λz_0]` trivially SR.
  - **(2e) cost chain CONFIRMED:** `w²≤s`; δ_k<0 ⟹ `Ξ≥s|δ_k|` (raw `−Δ_{0k}(1)`); δ_k>0 ⟹ bilinear
    witness `Ξ≥sδ_rδ_k≥sδ_k²` (`δ_r≥δ_k`); both ⟹ `w|δ_k|≤√Ξ` (uses `|δ_k|≤1`, MINOR omission);
    `d_TV(h,h')≤w Σ|δ_k|≤m√Ξ`; `Gap=𝔇(h)≤1−ρ(h,h')²≤2d_TV≤2m√Ξ`.
- **Claim 3 — perturbation continuity (Lem 4.1): CORRECT.** `|𝔇(p)−𝔇(q)|≤2√(2η)` (A 1-Lipschitz in
  Hellinger); `|V(p)−V(q)|≤2η` (Δ bounded-domain Lipschitz; "constant ≤2η" is loose wording, substance OK).
- **Claim 4 — literature: FAIR on all 4.** KPV (1212.6696): interlacer cone = convex, linear slice of the
  nonnegativity cone (Vámos ⟹ SOS relaxation not always exact). Saunderson (1904.00491): projected-
  spectrahedrality of interlacer/derivative cones OPEN beyond ternary. **Hyperbolicity cones ARE amenable**
  (Lourenço–Roshchina–Saunderson) ⟹ a Hölder error bound `dist(x,F)≤κ dist(x,K)` exists, **but `κ` not
  poly in degree/dimension** — exactly the missing uniformity. "No degree-uniform Wronskian-map metric
  regularity on irreducible cones" is a FAIR characterization of the gap.
- **Claim 5 — R+/R−: cautiously R+.** Refuter-elimination sound (tensor-padding killed by Claim 1;
  small-perturbation killed by Claim 3, both verified). No explicit degenerating family found. Product
  √-bound is constructive. **R+ the safer bet, but a lean, not a proof.**

## 🔴 The flagged doubt (V-normalization) — RESOLVED by the referee
The audit's single doubt: does `Ξ=V(h)` dominate the *raw* witnesses `s|δ_k|`, `sδ_rδ_k` (no shrinking
denominator)? **Resolved:** Pro's round-10 definition (5) is `V_d(g)=max_{i<j,C,x∈[−1,1]^{d−2}}
[−Δ_{ij}(R_C g)(x)]_+` — the **raw** max of the positive part of `−Δ`, **no normalizing denominator** ("projective"
refers to the coordinate-reversal `R_C`, not a division). The witnesses live at cube points (`Δ_{0k}` at
all-ones; `Δ_{rk}` at `z_0=1`, others `=1`), so `V(h) ≥ s|δ_k|` and `V(h) ≥ sδ_rδ_k` hold directly. ⟹ the
cost chain is sound; α=½, P=2(d−1) stand. (Two MINOR write-up gaps remain: the all-`δ_k<0` case; the
implicit `|δ_k|≤1`.)

## Net
Round-11 product-class UQHB + invariance + continuity are **audit-confirmed**. Easy refuters dead. The
residual (irreducible near-singular interlacer-cone degree-uniform metric regularity) is genuinely open;
amenability gives existence of the modulus but not the needed dimension-uniformity. Lean: R+.
