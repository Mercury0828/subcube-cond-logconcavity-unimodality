# Round-19 — FRESH context-clean GPT-5.5-Pro response (2026-06-22) — independent attack, SAME hard core

> A new, context-clean agent given the original problem + full freedom + prior work demoted to an optional
> appendix. **It did NOT escape the difficulty — it CONVERGED to the same hard core from an independent
> starting point (VC/Yatracos statistical learning theory), and independently reproduced the key structural
> phenomena — while adding two genuinely new/stronger positive results.** This is the decisive signal that
> the core difficulty is REAL and robust, not an artifact of the prior route's framing.

## NEW results (independent, stronger than the prior route)
1. **VC/Yatracos barrier (Prop 1):** `VCdim(A_{SR_n}) = 2^n − 1` (maximal). ⟹ global minimum-distance
   learning of an SR approximation is exponential — any poly tester MUST use conditioning/localization. *(A
   clean new barrier; independently confirms the prior route's "global statistics insufficient" via a totally
   different argument.)*
2. **🔑 Poly tester for ALL weighted binary-matroid basis laws (Thm 2):** `Õ(n³/ε⁴)` queries, arbitrary
   positive weights — STRONGER than the prior route's binary/ternary MM-NR (which was a non-closing special
   case). Mechanism: the binary-matroid SR class `{ν_{M,θ}}` has only `O(n²)` Yatracos dimension (binary
   matroids ↔ binary matrices + external fields) ⟹ learn a candidate + estimate TV distance (AFL-style
   SUBCOND TV estimator). Plus an `O(n² log)` exact membership test for *uniform* binary-matroid laws.
3. **b-block exact tester (Thm 3):** any fixed number of exchangeability blocks, `O(n^b/ε²)` — generalizes
   the prior two-block reduction and frames it as a tester.

## CONVERGENT results (independent reproductions of the prior route)
4. **Scale-free Rayleigh-violation certificate (Prop 4):** `𝔯(η)=max_{i<j,x} [Δ_ij/C(x)²]_+`, estimable in
   `Õ((d+log(1/δ))/τ²)` samples — essentially the prior route's projective certificate / noisy-rank, via the
   Rayleigh-difference directly.
5. **Explicit global-blind family (Prop 5):** constant-far from SR (`≥δ²/64`) yet `𝔯, NR = 2^{−Ω(n)}` (every
   unconditioned analytic/channel projection exponentially blind), instantly exposed by conditioning; + a `χ²`
   bound that unconditional samples need `2^{Ω(m)}`. *(Same phenomenon as the prior sparse-paving + random-code
   families, independent construction.)*
6. **🔑 The "exact missing theorem" (§6) = the SAME hard core.** The fresh agent independently reduces R+ to a
   **quantitative localization conjecture (15)** (`d_TV(μ,SR)≥ε ⟹` a sample-anchored prefix conditional has
   an estimable certificate `≥(ε/n)^C` w.p. `≥(ε/n)^C`) and a **proper-position repair inequality (16)**
   (`D_d(η) ≤ p_0 D_{d−1}(η_0) + p_1 D_{d−1}(η_1) + P(d)·Φ_i(η)^α`, coefficient 1 on the children, so it
   telescopes). **This is structurally identical to the prior route's EC_NR / energy-to-cut lemma.** The fresh
   agent: "No such polynomial-modulus proper-position repair theorem is presently established... a
   dimension-dependent Łojasiewicz bound exists abstractly but its exponent/constants can be exponential,
   which is precisely useless for the query question."
7. **§7 lower-bound requirements** = same characterization as the prior route (adaptive transcript
   indistinguishability; evades conditioning; nonbinary/large-coefficient-moduli; ill-conditioned through
   every accessible minor).

## 🎯 The decisive meta-signal
**Two independent AI attacks, from different mathematical starting points (noisy-rank/real-stability vs
VC/Yatracos learning theory), both (a) reproduced the global-blindness phenomenon, (b) proved the same
testable special cases, and (c) reduced the full problem to the SAME quantitative localization / proper-
position repair inequality — and both failed to prove it.** The natural tool (Łojasiewicz/semialgebraic error
bounds) gives exponential constants exactly at the barrier. This is strong evidence the core is GENUINELY HARD
and robust — not a local minimum of one framework. Bounds unchanged. Both still lean ~50–55/45 R+, low confidence.
