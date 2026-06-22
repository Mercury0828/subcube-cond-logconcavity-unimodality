# Round-11 — web GPT-5.5-Pro response (2026-06-21)

> Owner-relayed. **No proof/refutation of general UQHB**, but proves UQHB for the PRODUCT-children class,
> eliminates the easy refuter constructions, and confines the residual to a single named real-AG question.
> Audit + referee checks in `round11_audit.md`. "AI-verified ≠ proved." Leans **modestly R+**.

## §1 — Exact common-factor invariance (Theorem 1.1)
For SR `c` on disjoint coords: **`A(c⊗p)=A(p)`, `𝔇(c⊗p)=𝔇(p)`** (lower: `c⊗ν` SR, `ρ(c⊗p,c⊗ν)=ρ(p,ν)`;
upper: condition `Q` on `Y`, closure ⟹ `Q_{X|y}` SR, `ρ(c⊗p,Q) ≤ A(p)·ρ(c,q_Y) ≤ A(p)`). Hence
`Gap_λ(ca,cb)=Gap_λ(a,b)` and `Ξ_λ(ca,cb)=Ξ_λ(a,b)` (since `V(c)=0`). **Adding independent SR coords does
NOT worsen the UQHB ratio** — tensor padding is useless for a refuter. (Caveat: covers probabilistic
factorizations = disjoint-variable products; algebraic mixed-sign common factors after homogenization not
auto-covered.)

## §2 — 🎯 UNIFORM √-bound for PRODUCT children (Theorem 2.1)
For arbitrary Bernoulli-product children `a_p=∏(1−p_k+p_k z_k)`, `b_q=∏(1−q_k+q_k z_k)`, `h=(1−λ)a_p+λz_0 b_q`,
`s=λ(1−λ)`, `δ_k=p_k−q_k`:
**`Gap_λ(a_p,b_q) ≤ 2(d−1)·√(Ξ_λ(a_p,b_q))`** ⟹ **UQHB holds on the product class with α=1/2, P(d)=2(d−1).**
Proof ingredients: explicit projective witnesses **`Δ_{0k}(h)(1)=sδ_k`** and **`Δ_{rk}(h)=−s t δ_r δ_k`**
(`z_0=t∈[−1,1]`, other ordinary coords =1) ⟹ `Ξ ≥ s|δ_k|` and `Ξ ≥ s|δ_rδ_k|`; exact SR characterization
in-class (`h` SR ⟺ all `δ_k≥0` and ≤1 nonzero); construct a nearby compatible `h'` (keep the max-positive
discrepancy `δ_r`, erase the rest, modifying only the lighter selector branch) ⟹ `h'∈SR`; bound repair
`d_TV(h,h') ≤ w·Σ_J|δ_k| ≤ m√Ξ` (`w=min{λ,1−λ}`, `w|δ_k|≤√Ξ`); then `Gap=𝔇(h)≤1−ρ(h,h')²≤2d_TV ≤ 2m√Ξ`.

## §3 — product atoms harmless on any SR background (Cor 3.1)
`Gap_λ(ca_p,cb_q) ≤ 2(d−1)√(Ξ_λ(ca_p,cb_q))` for ANY SR `c` (DPP, spanning-tree, big tensor). **Tensor
padding does nothing.**

## §4 — perturbation continuity (Lemma 4.1)
`|𝔇(p)−𝔇(q)| ≤ 2√(2η)`, `|V(p)−V(q)| ≤ 2η` (`η=d_TV(p,q)`). ⟹ a `N^{−ω(1)}`-perturbation of an exactly
factored pair canNOT create an inverse-poly gap — a refuter's irreducible core must be genuinely
ill-conditioned (not a small perturbation of a nice tensor/common-factor model).

## §5 — what interlacer theory does/doesn't give
KPV (1212.6696): interlacer cone = preimage of the nonneg cone under the Wronskian map `h↦D_e f·h−f·D_e h`;
common factors factor out. Wagner–Wei (0709.1269): qualitative (nonpositive discriminant stays nonpositive),
**no repair-distance bound**; naive quantitative iteration loses a `√` per coordinate ⟹ `~2^{−d}` (useless).
No spectrahedral shortcut (projected-spectrahedral only for ternary; deg-3/4-var OPEN — Saunderson
1904.00491). Amenability of hyperbolicity cones gives an error bound but with a **cone/face-dependent
constant `κ` not poly in degree/dim** — and UQHB is exactly asking to keep `κ` from degenerating along a
sequence. **No theorem in the literature supplies the degree-uniform metric regularity.**

## §6 — the precise surviving obstruction
Residual restricted to: no independent common SR factor, genuinely nonproduct children, irreducible core
`dim→∞`. Sufficient fixed-child inequality: `inf_{s∈K_a}H²(b,s) ≤ poly(d)·Ξ_{1/2}(a,b)^α`, `K_a={s∈SR:
a+z_0 s stable}`. **Missing = a dimension-uniform normed right-inverse / error bound for the Wronskian map
defining `K_a` (after probability-mass normalization).** A refuter needs stable irreducible `(a_d,b_d)` with
`Gap ≥ d^{−O(1)}` but `Ξ = d^{−ω(1)}`, not within `d^{−ω(1)}` TV of a compatible tensor/common-factor model.

## §7 — conditional tester if the √-bound is global
Candidate `α=1/2, P=O(d)` ⟹ `γ=Θ(ε⁴/n⁴)` ⟹ tester **`Õ(n^{10}/ε^{10})`** queries; LB `Ω(max{√n/ε,1/ε²})`.
(Conditional: Thm 2.1 proves it only for product-child localized faces, not general SR.)

## Status
PROVED: common-factor invariance; the product-class √-UQHB (α=1/2, P=O(d)); perturbation continuity. NOT
proved: UQHB for general (irreducible nonproduct) children; an irreducible refuter; R+/R−. **Precise
surviving obstruction: do irreducible high-dimensional interlacer cones admit a polynomially-uniform
Hellinger error bound for their projective Wronskian inequalities?** Pro: high confidence in the theorems;
**leans modestly toward a global √-inequality (R+)**, but the irreducible near-singular case is uncontrolled
— where a counterexample would have to live.
