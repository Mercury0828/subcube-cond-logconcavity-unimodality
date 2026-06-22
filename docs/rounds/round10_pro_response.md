# Round-10 — web GPT-5.5-Pro response (2026-06-21)

> Owner-relayed. **No proof/refutation of dimension-uniform QHB**, but CLOSES all 3 round-9 normalization
> GAPs, proves an exact variational formula for `I_i`, a nonuniform QHB in every fixed dimension, and
> reduces the whole problem to a single uniform-conditioning inequality (connected to interlacer cones).
> Audit + referee checks in `round10_audit.md`. "AI-verified ≠ proved."

## §0/§1 — `V` pinned + `V=0 ⟺ real stable` (closes round-9 GAP-1)
`V_d(g)=max_{i<j,C⊆[d]∖{i,j},x∈[−1,1]^{d−2}}[−Δ_{ij}(R_C g)(x)]_+`, `R_C g(z)=z^C g(w)` (`w_k=1/z_k` on C) =
gen-poly of the bit-flipped distribution, `|R_C g(x)|≤1` on the cube. Identity `Δ_{ij}(R_C g)(z)=
(∏_{k∈C}z_k²)Δ_{ij}(g)(w)`. **`V_d(g)=0 ⟺ g` real stable** (Brändén both directions; off-orthant witness
`r` flips coords `|r_k|>1` into the cube). Closes the all-real-vs-cube gap.

## §2 — exact d=2 constant (closes round-9 GAP-2) [referee-spot-checked]
`V_2(p)=(p_{00}p_{11}−p_{10}p_{01})_+`. Explicit mass transfer (to set det=0 at TV cost ≤2v) ⟹
**`d_TV(p,SR_2) ≤ 2V_2(p)`**, and (via `1−ρ²≤2d_TV`) **`I_i(p)=𝔇_2(p) ≤ 4V_2(p)`**. The round-9 constant 4 is
rigorous under (5).

## §3 — exact tensorization `V(pq)=max{V(p),V(q)}` (closes round-9 GAP-3) [referee-spot-checked]
`R_C(pq)=(R_{C∩A}p)(R_{C∩B}q)`; for a pair in A, `Δ_{ij}(R_C(pq))=(R_{C∩B}q)²Δ_{ij}(R_{C∩A}p)`, and
`|R_{C∩B}q|≤1` on the cube ⟹ `[−Δ]_+ ≤ V(p)`, equality at `C∩B=∅`, all-ones. Cross pairs vanish. **Lemma
5.2 now PROVEN** (the round-9 `q²≤1` worry resolved — the cube domain supplies it exactly).

## §4 — 🔑 EXACT variational formula for `I_i` (Theorem 4.1) [REFEREE-VERIFIED]
`h=(1−λ)a+λ z_i b`, `λ=Pr(X_i=1)`, `a,b` = conditionals. Compatibility set `C={(r,s)∈SR_{d−1}²:
r+z_i s real stable}` (branch-weight-independent). Then
**`I_i(h) = (1−λ)A(a)²+λA(b)² − max_{(r,s)∈C}[(1−λ)ρ(a,r)²+λρ(b,s)²]`** — the affinity loss from imposing
mutual compatibility on the children's best stable approximations. Consequences: if both children SR,
`I_i(h)=𝔇_d(h)` (so minor-minimal obstructions are the cleanest QHB tests); 🔴 **proving QHB only for
STABLE children does NOT give full QHB** (needs a projection-transfer inequality) — corrects a round-9
over-optimism.

## §5–§6 — nonuniform QHB in every fixed dimension (Theorem 5.1), and why it fails R+
`V_d`, `I_i` are continuous **semialgebraic** on the compact simplex; `V_d^{-1}(0)⊆I_i^{-1}(0)`; compact
semialgebraic **Łojasiewicz** ⟹ `I_i(h)^{N_d} ≤ K_d V_d(h)` (a Hölder modulus EXISTS in each fixed `d`).
🔴 BUT `N_d,K_d` depend on `d`: effective Łojasiewicz on a `2^d−1`-dim simplex gives `N_d ≤ 2^{2^{O(d)}}`,
so `V` could be doubly-exp small ⟹ useless for poly queries. **The bottleneck is DIMENSION-UNIFORMITY, not
existence.**

## §7 — 🎯 the exact uniform inequality now required (reduces to interlacer-cone conditioning)
`Gap_λ(a,b) ≤ poly(d)·Ξ_λ(a,b)^α` (a dimension-uniform weighted-Hellinger conditioning bound on
proper-position gluing), `Ξ_λ=V((1−λ)a+λz_0 b)`. Connects to: **Wagner–Wei** (0709.1269, exact zero-error
gluing) and **Kummer–Plaumann–Vinzant** (arXiv:1212.6696, interlacers of a hyperbolic poly form a convex
cone = linear slice of a nonneg-poly cone). Neither controls the cone's CONDITIONING uniformly as the
polynomial approaches singular/multiple-root/common-factor strata — that error bound is the gap. 🔴
**CORRECTION to our audit's R− lean:** sporadic excluded minors do NOT refute QHB (Thm 5.1 gives a Hölder
modulus in every fixed dim); **a refutation needs an ASYMPTOTIC sequence whose Hölder exponent → 0 (or
constant → super-poly).**

## §8 — W5 refutation criterion, sharpened
Tensorization now secure (Lem 5.2). To evade the STRENGTHENED rank test W1, need **every** projected
`|X∩A|` to be `N_d^{−ω(1)}`-close to PB (eqn 34), not just total rank (a single defective subset in one
factor persists in the tensor). PB total rank suffices only for the original L, not vs W1. And refuting
QHB/L still ≠ R− (needs the full adaptive-transcript lower bound).

## §9 — conditional R+ complexity `Õ(n²/ε² · (nP(n)/ε²)^{2/α})` (if uniform QHB holds); LB `Ω(max{√n/ε,1/ε²})`.

## §10 — status
PROVED: `V` normalization; `V=0⟺SR`; d=2 constants; exact tensorization; the variational formula; nonuniform
QHB in fixed `d`. NOT proved: dimension-independent `α`; poly bound on `K_d`; a refuting asymptotic family;
the tester; the adaptive impossibility. **EXACT GAP: does the compatibility set `C_d` satisfy the uniform
weighted-Hellinger bound `Gap_λ(a,b) ≤ poly(d)·Ξ_λ^α`?** Confidence: high on all normalization/tensor/
variational/semialgebraic results; **genuinely LOW on the uniform inequality** (fixed-dim rules out a cheap
obstruction; the surviving issue is a dimension-uniform conditioning theorem for proper-position gluing).
