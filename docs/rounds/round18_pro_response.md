# Round-18 (FINAL) — web GPT-5.5-Pro response (2026-06-22) — lemma NOT settled; new R+ evidence + paper-ready stack

> Owner-relayed, FINAL attack round. Pro did **not** prove/refute the energy-to-cut lemma, but: corrected
> the canonical statement, added a strong R+ evidence point (the entangled random-code family), settled
> MM-NR for binary/ternary matroids, and delivered the **paper-ready theorem stack A–G** + the canonical
> open problem. Referee-verified Lemma 2.3 + prefix-hash. Final lean (Pro) ~55/45 R+, low confidence.
> Bounds unchanged `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n/ε²)`.

## §1 — two corrections to the dichotomy
1. **The canonical conclusion must use the full `NR`, not deterministic cuts** (projected subset-ranks are a
   special — strictly weaker — monotone channel; the 3-bit example). So the open statement is **EC_NR**
   (energy-to-NOISY-RANK), not energy-to-cut.
2. **Minor-minimality is NOT formally equivalent to general EC.** EC ⟹ its minor-minimal special case
   (MM-NR), but proving only MM-NR does not control compatibility energy fragmented across many successive
   prefix levels. *(Corrects the round-18 brief's MM-cut⟺EC framing.)*

## §2 — 🔑 Theorem 2.1: entangled random-code stress test (strong R+ evidence) [referee-verified pieces]
A random code `C` (`M=2^{⌊n/64⌋}` uniform codewords, min distance `≥n/4`), `μ_C` uniform on `C`:
- `d_TV(μ_C,SR)≥1/8`, `𝔇≥1/64` (const-far; via SCP `Var_ν(f)≤n` for 1-Lipschitz `f` (Lemma 2.2) vs the
  bimodal code variance `>(9/64)δ²n²`);
- **`NR(μ_C)≤Cn²2^{−n/128}`** (exponentially global-channel-blind; Hoeffding over codewords + a 2n-param
  channel net, `π_K^{U_n}` is PB);
- **every conditional with `<n/4` free coords is a POINT MASS** (SR) — no small-arity witness at all;
- **YET a sample-guided prefix isolates exactly 2 codewords w.p. `≥1/(3e)`** (prefix hashing, `Z~Bin(M−1,
  2^{−t})`, `Pr(Z=1)≥1/2e` — referee-verified), exposing `L(|X∩A|)=½δ_0+½δ_a` with
  `d_TV(·,PB)≥1/6` (Lemma 2.3 — referee-verified, actually `~0.4`).
⟹ **a pure high-energy example (`𝓡_m=0, 𝓔_{>m}=𝔇` ∀`m<n/4`) on which EC succeeds DECISIVELY.** Plus a clean
restricted lower bound: adaptive global channel-rank queries (NO conditioning) need `2^{Ω(n)}` to distinguish
`μ_C` from `U_n` — **SUBCOND defeats it via prefix hashing** (conditioning is essential). **Global channel
pseudorandomness is NOT near an R− construction.**

## §3 — Theorem 3.1: MM-NR settled for binary & ternary matroids [literature under audit]
Binary minor-minimal non-HPP ⟺ `F_7,F_7*` (HPP⟺regular; `U_{2,4}` not binary). Ternary: HPP ⟺
sixth-root-of-unity matroid, finite excluded minors `≤8` elements. ⟹ `NR(μ_M)≥c_*>0` over the finite lists.
`Φ(F_7)=3/49 ⟹ CutDef(F_7)≥(1/245)^{3/2}`. *(The general HPP class has NO asymptotic excluded-minor theorem.)*

## §4 — DEFINITIVE PAPER-READY THEOREM STACK
- **A. Noisy-rank characterization:** `μ SR ⟺ π^μ_K∈PB ∀K`; `R_{μ,K}(t)=∏(1−s_i+s_it)·g_μ((1−r_i+r_it)/
  (1−s_i+s_it))` (Möbius UHP maps); `NR=0⟺SR`, `NR≤d_TV(μ,SR)`; estimable to `±τ` over ALL channels in
  `O((n log(n/τ)+log(1/δ))/τ²)` samples.
- **B. Exact two-block reduction:** `d_TV(μ,SR)=d_TV(q,PB_{|A|}[a,b])`, `𝔇=1−sup_{p∈PB[a,b]}ρ(q,p)²`.
- **C. Universal MEM:** `1−√(1−𝔇) ≤ d_TV(μ,SR) ≤ √𝔇`, hence `½𝔇 ≤ d_TV ≤ √𝔇`.
- **D. Exact multiscale + automatic minor branch:** `𝔇=𝓔_{>m}+𝓡_m`; `𝓡_m≥𝔇/2 ⟹` a random `m`-descendant
  is `𝔇/8`-far w.p. `≥𝔇/4`, poly-learnable for `m=Θ(log(d/𝔇))`.
- **E. `g_s`:** `NR(g_s)=d_TV(g_s,SR)=Θ(s^{−2})`, `I_i=𝔇=Θ(s^{−4})`, `NR=Θ(√I_i)`; interior channel; σ_min
  (not det) is the robust PF normalization.
- **F. Globally channel-blind sparse-paving:** `d_TV≥n^{−C_0}`, `NR=2^{−Ω(n)}`, all ≤6-coord conditionals
  SR ⟹ NO `d_TV(μ,SR)≤poly(n)·NR^α` globally; localization indispensable.
- **G. `PG(2,q)` cut-visible:** `Φ=3(q−1)²/(q²+q+1)² ⟹ CutDef=Ω(n^{−3/2})`.
- **§5 conditional tester** (assuming EC_NR, exp `C`): `Õ(2^m/ε⁶ + n(n/ε²)^{3C})=poly(n,1/ε)`.

## §6 — THE SINGLE OPEN PROBLEM (canonical)
> **Energy-to-noisy-rank removal (EC_NR).** `∃C`: `𝔇=𝔇(h)>0`, `m=Θ(log(d/𝔇))`, `𝓔_{>m}(h)≥𝔇/2 ⟹` a
> poly-query sample-guided prefix finds a face `F` with `NR(h|F)≥(𝔇/d)^C` w.p. `≥(𝔇/d)^C`.
> **MM-NR (pure case):** every proper positive conditional of `ν` SR `⟹ NR(ν)≥(𝔇(ν)/d)^C`?
R− counterexample target: every proper conditional SR, `𝔇(ν_d)≥d^{−O(1)}`, `NR(ν_d)=d^{−ω(1)}` (refutes the
R+ route; full R− also needs an SR yes-ensemble + adaptive SUBCOND transcript indistinguishability).

## §7 — Pro's honest final assessment
**Slight R+ lean ~55/45, low confidence.** Every concrete globally-pseudorandom obstruction found so far
(sparse-paving, random-code) is broken by adaptive prefix conditioning; but proving this ALWAYS happens needs
**a new polynomial removal theorem for compatibility failure, not another reformulation of real stability**.
Strongest UNCONDITIONAL message: **"Global statistics can be exponentially blind, while sample-guided
conditioning provably amplifies several qualitatively different SR obstructions."** The exact boundary is EC_NR.
