# Round-13 — web GPT-5.5-Pro response (2026-06-21) — channel degeneracy SOLVED + class rates

> Owner-relayed. **Resolves the audit's main doubt (channel degeneracy)** + proves the NR-rate for several
> classes. No general NR-rate yet; residual sharpened to a higher-order local-to-global statement. Bounds
> unchanged `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n/ε²)`. Audit + referee checks in `round13_audit.md`. Leans R+.

## §1 — 🔑 Theorem 1.1: channel regularization (KILLS the degeneracy doubt)
`NR_δ(h):=sup_{δ≤s_i≤r_i≤1−δ} d_TV(π^h_K,PB) ≥ NR(h) − dδ`. Proof: post-process each output bit (keep w.p.
`1−2δ`, replace by a fair bit w.p. `2δ`) ⟹ params `∈[δ,1−δ]`, each coord changes w.p. `≤δ` ⟹ rank-law TV
`≤dδ`. ⟹ if `NR(h)=τ`, a channel with params `Ω(τ/d)` from `{0,1}` (and slopes `0` or `≥τ/8d`) retains
`⅞τ` defect. **So a defect visible only at degenerate (`L→∞`) channels cannot hide a poly defect — the
"single most important doubt" is resolved.**

## §2 — Theorem 2.1: sharp quadratic PB separation [REFEREE-VERIFIED]
For `q` on `{0,1,2}`, `Φ(q):=4q_0q_2−q_1²`: `Φ>0 ⟹ d_TV(q,PB) ≥ (Φ/15)^{3/2}`. Proof via Schur's
degree-3 inequality (`e_1³+9e_3≥4e_1e_2`) ⟹ `Φ(u)_+^{3/2} ≤ 9 u_{≥3}` for any PB `u`; `q_{≥3}=0` + TV
contraction. **Exponent 3/2 SHARP** (`Bin(3,p)|_{≤2}`: `Φ~3p²`, `d_TV~p³`). *(Referee: lower bound holds
with margin ≥95×; `Φ=κ` for the §3 channel checked exactly.)*

## §3 — Theorem 3.1: positive covariance ⟹ bounded noisy-rank witness
`Cov(U,V)=κ>0 ⟹ NR(h) ≥ (κ/15)^{3/2}`, via the slope-½ channel `s_U=(1−p)/2, r_U=1−p/2` (E U'=½),
`Cov(U',V')=κ/4`, rank law `q_0=q_2=¼+κ/4, q_1=½−κ/2` ⟹ `Φ(q)=κ` (referee-verified) ⟹ Thm 2.1. Bounded
witness via Thm 1.1. *(Insufficient alone: Rayleigh-but-not-SR `h` can have NO positive Boolean conditional
covariance.)*

## §4 — Theorem 4.1: complete NR-rate for PRODUCT SR children
`h=(1−λ)a_p+λz_0 b_q`: **`NR(h) ≥ I₀(h)³/(8·15^{3/2}(d−1)³)`** i.e. `I₀ ≤ 2√15·(d−1)·NR^{1/3}` (α=1/3).
Via the product √-bound `I₀ ≤ 2(d−1)√κ` (round-11 engine, `κ=max_{u<v}Cov_h(X_u,X_v)_+`) + Thm 3.1. Bounded
witness with margin `Ω(I₀³/(d·m³))`.

## §5 — Theorem 5.1: homogeneous SR children — a SUBCOND-SEARCH witness
If `I₀(h)≥η`: w.p. `≥η/2k`, a sample-guided `(k−1)`-link `S` yields a *balanced link selector* `h_S^*` +
bounded channel `K_S` with `d_TV(π^{h_S^*}_{K_S},PB) ≥ (η/120k)^{3/2}`. Engine: down-up gap `≥1/k` (ALOV)
+ Thm 2.1 (link channel ⟹ `Φ=t/2`, `t=d_TV(π^S,σ^S)≥η/4k`). SUBCOND-implementable in `Õ(mk³/η³)` queries.
🔴 **Honest limitation (Pro-flagged):** `h_S^*` is SYNTHESIZED by querying the two branches separately +
mixing; it need NOT equal the natural conditional of `h`. So this is a **SUBCOND-search** theorem (gives the
bounded witness algorithmically for this class), **not literally a lower bound on `NR(h)`**.

## §6 — settled / not + the precise residual
SETTLED: the **bounded-channel clause** (regularization, Thm 1.1); the rate for positive-covariance,
product-children, and homogeneous-children regimes. **NOT settled:** arbitrary irreducible nonproduct
nonhomogeneous proper-position incompatibility. Positive covariance insufficient (Rayleigh-not-SR).
**The precise missing theorem (34):**
> `I_i(h)≥η ⟹` EITHER a poly-likely descendant has positive covariance of size `poly(η/d)`, OR a bounded
> channel produces a **negative higher Toeplitz / Pólya-frequency minor** with poly-normalized magnitude.
Thm 2.1 handles the first quadratic PB obstruction; **missing = its higher-order analogue tied
quantitatively to SR gluing incompatibility.**

## 🔎 REFEREE FINDING (orchestrator, 2026-06-21) — the hardest example IS caught by a bounded channel
Direct test of the residual (34) on `μ_4` (the round-3 Rayleigh-but-not-SR example, which defeats the
ENTIRE covariance/interlacer route): `μ_4`'s **worst Boolean conditional pairwise covariance = 0** (evades
Thm 3.1's §3 covariance route, as expected for a Rayleigh measure) — **YET a BOUNDED symmetric channel
`(s,r)=(0.1,0.55)`** (both well inside `(0,1)`) gives a noisy-rank polynomial with **complex roots
`−1.901±0.715j`** ⟹ not Poisson-binomial ⟹ `μ_4` is **caught**. So the canonical higher-order
(Rayleigh-not-SR) obstruction — invisible to all covariances/`V` — IS exposed by a bounded channel via a
higher PB/Toeplitz-minor defect (the second branch of (34)), with a CONSTANT margin (not degenerate).
**Strong concrete evidence the higher-order local-to-global (34) holds, i.e. for R+.**

## §7 — if a general rate `NR≥c·I_i^a/d^b` holds ⟹ tester `Õ(c^{-2} n^{2+2a+2b}/ε^{2+4a})`.
## Status
PROVED: regularization; sharp PB separation; covariance/product/homogeneous rates. NOT: the general
higher-order rate (34); adaptive transcript indistinguishability; R+/R−. Pro confidence: high in
regularization + PB separation + class rates; uncertain on the general rate. **"Endpoint degeneracy is
SOLVED; the only surviving obstruction is higher-order quantitative separation from the PB family."** Leans R+.
