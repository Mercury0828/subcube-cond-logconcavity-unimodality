# Round-16 — web GPT-5.5-Pro response (2026-06-22) — A6 closed; EXACT two-block reduction; entangled channel-blind family

> Owner-relayed. Three substantial results: (1) closes the A6 debt `I_i(g_s)=𝔇(g_s)`; (2) an **exact
> two-block reduction** making `NR(g_s)=d_TV(g_s,SR)=Θ(s^{−2})` fully rigorous; (3) 🔴 **a genuinely
> entangled sparse-paving family that defeats EVERY global channel** (`NR=2^{−Ω(n)}`) and all ≤6-coord
> conditionals — a much sharper R− near-counterexample (still NOT R−: an 8-coord excluded minor leaks on
> poly-fraction descendants). No R+/R−. Two parallel audits running. Bounds unchanged. **Reframes both sides.**

## §1 — A6 CLOSED: `I_i(g_s)=𝔇(g_s)` [referee backbone-verified]
Lemma 1.1: if both positive-prob `i`-conditionals of `μ` are SR, then `I_i(μ)=𝔇_d(μ)` — because for SR `σ`,
`𝔇(σ)=0` (sup includes `ν=σ`), so both correction terms in the localization formula
`I_i=𝔇_d(μ)−Σ_b Pr(X_i=b)𝔇_{d−1}(μ^{(i=b)})` vanish. `g_s`'s every deletion/contraction is SR ⟹
`I_i(g_s)=𝔇(g_s)` ∀i. **No comparator assumption needed.** (Resolves the round-15 audit's flag 1.)

## §2 — Theorem 2.1: EXACT two-block reduction [referee backbone-verified on n=4]
For `μ` `k`-homogeneous, permutation-invariant within blocks `A`(size `m`),`B`(size `ℓ`), `q=L(|X∩A|)`,
feasible `[a,b]=[max{0,k−ℓ},min{k,m}]`:
**`d_TV(μ,SR)=d_TV(q,PB_m[a,b])`** and **`𝔇(μ)=1−sup_{p∈PB_m[a,b]}ρ(q,p)²`** (EXACT TV + affinity).
Proof: (S1) restrict comparator to rank `k` (truncation preserves SR; TV↓, affinity↓-factor); (S2)
block-average over `S_A×S_B` (μ-fixing SR-preserving Markov kernel = symmetric exclusion ⟹ TV contracts,
affinity ↑); (S3) **block-exchangeable `k`-homog SR ⟺ count law PB** (gen poly = polarization of
`F_p(x,y)=Σp_j x^j y^{k−j}`; polarization preserves+reflects stability; `F_p` stable ⟺ `P_p(t)=Σp_j t^j`
real-rooted); (S4) within each cell both measures uniform ⟹ distances collapse to `q`. *(Referee: the S3
backbone — 2-block-exch SR ⟺ real-rooted count — confirmed on n=4, 7/7 cases MATCH.)* Upgrades two-orbit
real-rootedness from yes/no to **exact projection**.

## §3 — consequence: projected rank = exact two-block-symmetrized SR defect
For arbitrary `k`-homog `μ`, `|A|≤min{k,n−k}`: `d_TV(S_A μ,SR)=d_TV(L(|X∩A|),PB_{|A|})`. ⟹ the projected-rank
tester measures EXACTLY the SR defect surviving two-block symmetrization. **An entangled R− must be almost SR
after EVERY two-block symmetrization** (nonsymmetry alone is nowhere near enough).
For `g_s`: **`NR(g_s)=d_TV(g_s,SR)=d_TV(q_s,PB_{2s})=Θ(s^{−2})`**, `I_i(g_s)=Θ(s^{−4})`,
`(1/√800)√I_i ≤ NR(g_s) ≤ √I_i`. **Round-15 headline fully rigorous, no exponent correction.**

## §5 — 🔴 Theorem 5.1: a genuinely entangled, globally channel-blind sparse-paving family
`k=n/2`, `Ω=C([n],k)`, `N=C(n,n/2)`. Random sparse-paving matroid: `ξ_S~Ber(p)`, `p=1/4D` (`D=k(n−k)`),
`H={S: ξ_S=1, ξ_T=0 ∀T~S}` (independent set in Johnson `J(n,k)`); bases `=Ω∖H`; `μ_H` uniform.
- **`d_TV(μ_H,SR)≥n^{−C_0}`** (plant a fixed rank-4 8-element minor-minimal non-HPP `M_0` on a poly-fraction
  of distance-≥3 contexts; conditional aggregation).
- **`NR(μ_H)≤n^{O(1)}/√N=2^{−Ω(n)}`** — invisible to EVERY global monotone-channel rank statistic (identity
  `π_K^{μ_H}−Q̄_K=(|H|/(N−|H|))(Q̄_K−Q̄_{H,K})`; McDiarmid bounded-diff `D+1` + an `O(n²)`-log channel net
  ⟹ `H` pseudorandom against all channel kernels). So **every global covariance/PF certificate has
  `σ_min≤2·NR=2^{−Ω(n)}`** (super-poly ill-conditioned).
- **every ≤6-free-coord Boolean conditional is SR** (conditioning = a matroid minor; every ≤6-element
  matroid has HPP).
🔴 **Still NOT R−:** a fixed 8-coord non-SR minor `M_0` occurs on descendants of total prob `n^{−O(1)}` ⟹
obeys the **descendant** form of (36) via the excluded-minor mechanism. A SHARP near-counterexample: global
channels fail completely, ≤6-dim conditionals fail completely, **only descendant-excluded-minor rescues R+.**
*(✅ Literature VERIFIED by audit: "22 rank-4 8-element minimal non-HPP" REAL (Kummer–Sert 2111.09610: 32 on
≤8 elements = 10 rank-3/7 incl. Fano + 22 rank-4/8); "every ≤6-element matroid HPP" REAL (Wagner–Wei
0709.1269 / COSW; smallest non-HPP = Fano F_7). No hallucination.)*

## §6 — tensor amplification: `P_n=μ_H^{⊗R_n}` ⟹ `d_TV(P_n,SR)≥1−1/e` (constant-far), `NR(P_n)=D_n^{−ω(1)}`,
all ≤6-dim conditionals SR. A stronger global-blindness example than random-sign — homogeneous, matroidal,
sparse-paving, nonsymmetric. Still leaks fixed 8-dim obstructions ⟹ supports (36).

## §7 — REFRAMED targets
- **(R+) cut-or-minor removal lemma:** `𝔇(h)≥η ⟹` EITHER `max_A d_TV(L(|X∩A|),PB) ≥ (η/d)^C` (cut branch —
  the simpler SINGLE-block statistic, not a general Toeplitz σ_min search), OR a sample-guided descendant of
  inverse-poly probability has dimension `O(log(d/η))` and is inverse-poly-far from SR (small-minor branch,
  tested by learning that descendant). **Examples divide:** `g_s`→cut; sparse-paving→small-minor; product
  selectors→covariance; homogeneous→link. **Missing: a proof these exhaust all distributions.**
- **(R−) the precise object (45):** an ASYMPTOTIC sequence of minor-minimal non-HPP `ν_d` with every proper
  minor SR, `𝔇(ν_d)≥d^{−O(1)}`, `NR(ν_d)=d^{−ω(1)}` — a **pseudorandom excluded-minor family whose
  conditioning modulus degenerates with dimension**. Fixed-size classifications give abundance, NOT this.
  Plus an SR yes-ensemble with adaptive SUBCOND transcript indistinguishability for full R−.

## Status
PROVED (Pro, high confidence): A6 identity; exact two-block projection (TV+affinity); `NR(g_s)=d_TV(g_s,SR)
=Θ(s^{−2})`; the sparse-paving globally-channel-blind poly-far family + tensor amplification. NOT: the
cut-or-minor removal lemma; an asymptotic minor-minimal channel-blind obstruction; adaptive SUBCOND
indistinguishability; R+/R−. Bounds `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n/ε²)`. **Pro: "global channel
pseudorandomness is much easier than `g_s` suggested, even inside matroid measures. R+ may still hold not
because every obstruction leaks globally, but because every large obstruction has a two-block shadow OR a
poly-frequent excluded minor — that removal statement is the exact unresolved theorem."** Lean shifts toward
genuine balance.
