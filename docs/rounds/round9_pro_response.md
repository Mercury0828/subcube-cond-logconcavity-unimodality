# Round-9 — web GPT-5.5-Pro response (2026-06-21)

> Owner-relayed. **No proof/refutation of (L) yet**, but reduces the entire problem to ONE clean question
> (QHB), blocks the rare-hidden-face refutation strategy, and gives an explicit minor-minimal obstruction
> family. Audits + referee checks in `round9_audit*.md`. "AI-verified ≠ proved."

## §1 — strengthened rank test (projected subset ranks)
For every `A⊆[n]`, `|X∩A|` is Poisson-binomial under SR (projection closure). `RankDef(μ)=max_A
d_TV(L(|X∩A|),PB_{|A|}) ≤ d_TV(μ,SR)`; all `2^n` testable with `O((n+log1/δ)/τ²)` samples. (AESW theorem.)

## §2 — 🔑 Hellinger-defect telescoping + random-prefix localization (BLOCKS the rare-face strategy)
`A_d(p)=sup_{ν∈SR_d}ρ(p,ν)` (Bhattacharyya), `𝔇_d(p)=1−A_d(p)²`; `d_TV(p,SR)≥ε ⟹ 𝔇≥ε²`. One-coord
defect `I_i(p)=𝔇_d(p)−Σ_b p_b 𝔇_{d−1}(p^{(b)}) ≥ 0` (**Lemma 2.1**, via closure + Cauchy–Schwarz). Exact
telescoping `𝔇_n(p)=Σ_t E[I_{π_{t+1}}(p_t)]`. **Cor 2.2:** a random sample-guided prefix finds a face with
`I ≥ ε²/2n` w.p. `≥ ε²/2n`. ⟹ **an `Ω(1)`-far μ CANNOT hide all incompatibility on `n^{−ω(1)}`-probability
faces** — the rare-hidden-face refutation of (L) is dead. Remaining: convert `I_i` (affinity defect) into a
signed Rayleigh margin `V`.

## §3 — 🎯 QHB ⟹ R+ (the make-or-break, now precisely a real-stability gluing inequality)
> **(QHB)** `∃ α>0, poly P`: for every `d`-bit `h` and coord `i`, `I_i(h) ≤ P(d)·V(h)^α`.
**Thm 3.1:** QHB ⟹ poly-query SUBCOND SR tester, complexity `Õ(n²/ε² · (nP(n)/ε²)^{2/α})` (random
sample-guided prefix → V2 on the found face). **QHB HOLDS in d=2:** `d_TV(p,SR_2) ≤ 2V(p)` ⟹ `I_i ≤ 4V`.

## §4 — 🧩 explicit minor-minimal obstruction family `g_s` (non-SR, ALL proper conditionals SR)
`c_s=2√(1−1/s²)<2`, blocks `A,B` size `N=2s`, `E_k=e_k/C(N,k)`,
`g_s = [E_{s−1}^A E_{s+1}^B + c_s E_s^A E_s^B + E_{s+1}^A E_{s−1}^B]/(2+c_s)` on `4s` bits. **Thm 4.1
(7 properties, full proofs):** (1) not SR — diagonal `∝ x^{s−1}y^{s−1}(x²+c_s xy+y²)`, quadratic complex
(`c_s<2`); (2) **every proper Boolean conditional is SR** — contraction diagonal `=(√(s+1)x+√(s−1)y)²`,
deletion `=(√((s−1)/2s)x+√((s+1)/2s)y)²` (perfect squares, using `c_s s=2√(s²−1)`); (3) total rank `≡2s`
(Poisson-binomial); (4) `Θ(s^{−2})`-far from SR (upper via `c_s→2`; lower via a Toeplitz-minor eigenvalue
argument on the `A`-rank law + AESW); (5) `V(g_s) ≥ 3/(128 s⁴)`; (6) all conditional pairwise covariances
`≤0`; (7) `I_i(g_s) ≤ (64/3)·V(g_s)` — **satisfies LINEAR QHB** (evidence FOR QHB).

## §5 — tensoring: `d_TV(h^{⊗m},SR) ≥ 1−e^{−mδ²/2}` (Lem 5.1); `V(pq)=max{V(p),V(q)}` (Lem 5.2).
**Cor 5.3:** `μ_s=g_s^{⊗m_s}` (`m_s=6400s⁴`, `n_s=Θ(s⁵)`) is constant-far, PB total rank, all conditional
pairwise covariances `≤0`, and **every conditional with `<4s=Θ(n^{1/5})` free coords is SR** ⟹ a tester
inspecting only `o(n^{1/5})`-dim conditionals (or constant-density random restrictions) sees only SR. BUT
**NOT a counterexample to (L)** — the empty restriction has `V=Ω(n^{−4/5})` (inverse-poly), and the §1
projected-rank test catches it. (Obstructs *simplistic* L-alg, not L.)

## §6 — exact sufficient criterion to REFUTE (L)
Need `h_d` with (1) rank PB, (2) `δ_d>0`, (3) `M(h_d):=max_E V(h_d|E) = N_d^{−ω(1)}`, `N_d=Θ(d/δ_d²)`. Then
tensorize ⟹ (L) false. `g_s` misses (28) badly (`M(g_s)=Ω(N^{−4/5})`). A genuine refutation needs
increasingly ill-conditioned minor-minimal non-SR measures whose distance decays *polynomially* while
*every* normalized conditional Rayleigh violation decays *super-polynomially*.

## §7 — the remaining step = a QUANTITATIVE EXCLUDED-MINOR theorem
Wagner–Wei (arXiv:0709.1269) proved the EXACT zero-error gluing: if every 1-coord deletion/contraction is
SR, then one Rayleigh-difference `≥0` on all reals ⟹ parent SR. **QHB is its quantitative analogue** (no
known dimension-uniform `distance ≤ poly(d)·(neg margin)^α`). Minor-minimal non-HPP obstructions exist (22
eight-element matroids; +1218 nine-element; possibly infinitely many — arXiv:2111.09610, math/0202034).
Selector form: `h=½a(z)+½z₀b(z)`, both `z₀`-conditionals SR, `Δ_{0j}(h)=¼(b∂_j a−a∂_j b)` (projective
Wronskian). **QHB asks: can two SR polys be poly-far from every proper-position pair while all projective
Wronskians are super-poly small? No ⟹ R+; robust Yes (+PB rank) ⟹ the R− base object.**

## §8 — proved / not-proved / the exact gap
PROVED: §1 projected-rank universality; §2 telescoping + localization; QHB⟹R+ (Thm 3.1); QHB in d=2; the
`g_s` family (all 7 properties); tensoring lemmas; the §6 refutation criterion. NOT proved: QHB in general;
any weaker sufficient gluing theorem; a sequence meeting (28); adaptive SUBCOND indistinguishability.
**EXACT GAP: a dimension-uniform quantitative stability estimate connecting `I_i(h)` to projective Rayleigh
violations on `h` or poly-discoverable descendants.** Pro confidence: high on lemmas/family/tensor;
**genuinely DIVIDED on QHB** (low-dim + g_s support it; the abundance of minor-minimal HPP obstructions
leaves room for a badly-conditioned counterexample).
