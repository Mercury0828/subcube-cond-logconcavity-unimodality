# Round-8 — web GPT-5.5-Pro response (2026-06-21)

> Pasted from the owner's relay. **NOT a resolution of R+/R−** (Pro is explicit); it gives bounds + new
> structural results + corrects two of our framing errors. Orchestrator audits + referee checks below /
> in `round8_audit*.md`. "AI-verified ≠ proved."

## Headline (Pro)
`Ω(max{1/ε², √n/ε}) ≤ Q_SR^SUBCOND(n,ε) ≤ O(2^n/ε²)`. Does NOT settle poly vs super-poly. Confidence:
high in the lemmas/lower bound; LOW on whether the answer is R+ or R−.

## §1 — 🔴 THE RANK STATISTIC IS UNIVERSAL (corrects our error)
For SR `μ`, `R_μ(t)=g_μ(t,…,t)=Σ_k Pr(|X|=k)t^k` is **real-rooted** (univariate restriction of a real
stable poly along `z_i↦t`), so **`rank(μ)=|X|` is Poisson-binomial — for EVERY SR `μ`, not only symmetric
ones.** Hence `d_TV(μ,SR) ≥ d_TV(rank(μ), PB_n)` (data processing) for ALL `μ`, and `rank(μ)` is
`O(n/τ²)`-sample estimable. Symmetry is needed only for *sufficiency* (BBL), not necessity. ⟹ **C-sym and
μ_4 are BOTH caught by the universal rank test** (their rank PGFs are non-real-rooted). [Referee-verified.]

## §2 — projective certificate (the off-orthant domain is COMPACTIFIABLE)
Coefficient-reversal `R_C` (flip bits in `C`, `C∩{i,j}=∅`): **`Δ_ij(R_C g)(z) = (∏_{k∈C}z_k²)·Δ_ij(g)(w)`**,
`w_k=z_k^{-1}` on `C`. Any real witness `Δ_ij(g)(r)<0` maps (flip `k` with `|r_k|>1`) to a witness in
`[−1,1]^{n−2}`. So `V(g):=max_{i<j,C,x∈[−1,1]^{n−2}}[−Δ_ij(R_C g)(x)]_+` satisfies **`g` real stable ⟺
`V(g)=0`**. (Our "off-orthant is intrinsically hard to estimate" was incomplete — the issue is *margin
size*, not domain reachability.)

## §3 — Theorem 3.1: a robust signed-witness tester (poly-query IF margin is inverse-poly)
`Δ_ij(R_C h)(x)=B(x)C₀(x)−A(x)D(x)`, all `A,B,C₀,D` are `[−1,1]`-bounded, `d`-Lipschitz. Grid+Hoeffding
with a union bound over `C(d,2)·2^{d−2}·O(d/γ)^{d−2}` items (only its **log** enters sample complexity):
**`O((d log(d/γ)+log(1/δ))/γ²)` samples** accept SR `h`, reject `V(h)≥γ`. Offline computation exponential.
Distance bound (8): `|Δ_ij(R_C h)(x)−Δ_ij(R_C ν)(x)| ≤ ‖h−ν‖₁`, giving `d_TV(h,SR) ≥ ½V(h)` (9) — converse FALSE.

## §4 — sharpened μ_4: `Δ_12(G_4)(−1,−1)=−1` ⟹ `V(g_{μ_4})≥1/900` ⟹ `d_TV(μ_4,SR)≥1/1800` (our 1/7200 valid but loose).

## §5 — Lemma 5.1 (conditional aggregation, SOUND direction):
`W_F(μ):=E_{r∼μ_{F̄}}[V(μ_r)]`. Then **`d_TV(μ,SR) ≥ ¼ W_F(μ)`**. (Conditioning + the signed tester
aggregate soundly.) Converse missing = the upper-bound problem.

## §6 — dense parity: exp-small global margin, constant farness
`μ_T=2^{−m}(1+η(−1)^{|x|})`: `Δ_ij(g)= −4η·4^{−m}∏_{k≠i,j}(1−z_k²)` ⟹ `V(g)=4η·4^{−m}` (EXP small), yet
constant-far: conditioning the other `m−2` bits gives a `+`-type pair table with `V(p⁺)=η/4`, so
`W_F=η/8` ⟹ `d_TV(μ_T,SR)≥η/32`. **SUBCOND amplifies the exp-small unnormalized violation to a normalized
`η/4` on rare faces.** ⟹ a lower bound must hide the *amplifying face*, not just an exp-variance moment.

## §7 — 🆕 NEW LOWER BOUND `Ω(√n/ε)` (anti-product blocks, Yao)
`n=2m` paired bits; YES = uniform `U`; NO = `⊗_t p_{b_t}^α`, random `b∈{±1}^m`,
`p_b^α(00)=p_b^α(11)=¼+bα`, `(01)=(10)=¼−bα`. (a) `D(p_+^α)=−α` ⟹ each `+` block is `α/2`-far from 2-bit
SR; (b) tensor farness via Bhattacharyya `ρ(P_b,Q)≤(1−α²/8)^{m_+(b)}` for ALL SR `Q` (suffix induction +
conditioning-closure), `m_+≥m/3` whp, `α²=48ε/m` ⟹ `d_TV(P_b,SR)≥ε`; (c) **exact SUBCOND→iid simulation**
(AFL: a subcube-conditioned block sample = one unconditional sample, parity trick, no knowledge of `b`);
(d) χ² mixture: `1+χ²(E_b P_b^{⊗q}, U^{⊗q}) ≤ exp(128 m q² α⁴)`, so `q=o(√m/ε)` fails. ⟹ `Ω(√n/ε)`.

## §8 — `Ω(1/ε²)` (two-bit `p^θ` vs `U₂`, KL `O(θ²)`/query, Pinsker; pad to all `n`).
## §9 — `O(2^n/ε²)` upper bound (learn empirical `μ̂` to `ε/4`, exp computation, distance to SR set).

## §10 — the EXACT remaining gap
For **R+**: a quantitative *conditional-stability removal lemma* — if `d_TV(μ,SR)≥ε` then either rank law
is inverse-poly-far from `PB_n`, OR a poly-query procedure finds a positive subcube `E` with `V(μ|E)≥γ`
(inverse-poly `β,γ`); ideally a random-restriction statement (27). Then Thm 3.1 tests `E`. For **R−**:
full-support YES/NO ensembles with every NO `Ω(1)`-far AND every adaptive poly-query SUBCOND transcript
`o(1)`-distinguishing — **must hide the amplifying face**, not just an unnormalized high-degree moment.
The three known examples (C-sym→rank; μ_4→constant global `V`; dense parity→constant pair-conditional `V`)
all fit the dichotomy; missing = a theorem that they are representative.

## Facts used / confidence (Pro)
Used F1 (Brändén all-real), F2 (closure incl. conditioning/projection/products), F5 (with the
universality correction), AFL exact simulation (arXiv:2408.02347). Independently checked μ_4 + parity.
Did NOT assume §4 of our brief. High confidence in: projective certificate, robust tester, Lemma 5.1,
parity separation, `Ω(max{1/ε²,√n/ε})` lower bound. LOW confidence on R+ vs R−.
