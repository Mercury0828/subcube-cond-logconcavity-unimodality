# Brief for web GPT-5.5-Pro — ROUND 10: prove or refute QHB (the quantitative excluded-minor inequality)
### (copy everything below the line and send as-is)

---

> Round-10, on your round-9 results. We **independently audited round 9** (symbolic + literature). The
> verdict: your **localization theorem (§2) is fully correct** — and it *rigorously kills* the
> "hide-the-witness-on-rare-faces" route to R−, which is a real result. Your **QHB ⟹ R+ reduction (§3) is
> a valid reduction.** Your **`g_s` family is verified** (we independently re-checked: the parent's
> diagonal quadratic has complex roots = non-SR, while every 1-coordinate contraction/deletion diagonal is
> a perfect square = SR — the minor-minimal property holds). **Wagner–Wei (0709.1269) is confirmed**, and
> QHB is fairly its quantitative analogue. So the entire problem now sits on **one inequality, QHB.** This
> brief asks you to settle it. **Full method freedom.**

## 0. Two normalization gaps to close first (the linchpin our audit flagged)

The single under-specified object is the projective certificate `V`. Please **pin it down precisely** and
prove the three facts everything rests on:
1. **`V(g)=0 ⟺ g` real stable** (you established this in round 8 — restate the exact definition/normalization
   used below).
2. **The d=2 constant:** `d_TV(p, SR_2) ≤ c·V(p)` with an explicit `c` (you used `2`), hence `I_i ≤ 4V` —
   make the constant rigorous under the pinned-down `V`.
3. **Tensoring `V(pq)=max{V(p),V(q)}` (Lemma 5.2):** the step `Δ_{ij}(pq)=q²Δ_{ij}(p)` needs `q²≤1` on
   `V`'s evaluation domain. SR is an *all-ℝⁿ* condition but your certificate evaluates on the *bounded cube*
   `[−1,1]` (via coefficient-reversal). Confirm the cube-evaluated `V` faithfully certifies all-ℝⁿ
   stability **and** `q²≤1` there, so Lemma 5.2 is exact. (This is load-bearing for the §6 refutation
   criterion — without it, the R− calculus wobbles.)

## 1. Verified state (use freely)

- **(W1) Strengthened rank test.** Every projected `|X∩A|` is Poisson-binomial under SR; `RankDef(μ)=
  max_A d_TV(L(|X∩A|),PB_{|A|}) ≤ d_TV(μ,SR)`, `O(n/τ²)`-estimable.
- **(W2) Localization (audited correct).** With `I_i(p)=𝔇_d(p)−Σ_b p_b 𝔇_{d−1}(p^{(b)}) ≥ 0`
  (`𝔇=1−sup_{SR}ρ²`), a random sample-guided prefix finds a face with `I ≥ ε²/2n` w.p. `≥ ε²/2n`.
  ⇒ **incompatibility cannot be hidden on `n^{−ω(1)}`-probability faces.**
- **(W3) QHB ⟹ R+ (audited valid).** `QHB: I_i(h) ≤ P(d)·V(h)^α` ⟹ a `poly(n,1/ε)`-query SUBCOND SR tester.
- **(W4) `g_s` (verified).** A minor-minimal non-SR family with every proper Boolean conditional SR,
  Poisson-binomial total rank, `Θ(s^{−2})`-far, `V ≥ 3/(128 s⁴)`, all conditional pairwise covariances
  `≤0`, satisfying *linear* QHB (`I_i ≤ (64/3)V`). Its tensor `μ_s` is constant-far with all
  `o(n^{1/5})`-dim conditionals SR — but NOT a (L)/QHB counterexample (`V=Ω(n^{−4/5})`).
- **(W5) Refutation criterion (§6).** A sequence `h_d` with PB rank, `δ_d>0`, and `M(h_d)=max_E V(h_d|E)=
  N_d^{−ω(1)}` (`N_d=Θ(d/δ_d²)`) ⟹ tensorize ⟹ refutes QHB/(L) (R−). `g_s` misses it (`M=Ω(N^{−4/5})`).
- **(W6) Wagner–Wei (0709.1269).** Qualitative iff: proper minors stable + `Δ_{ij}≥0` on all reals ⟹ parent
  stable. QHB is its quantitative (dimension-uniform) analogue, which is **not known**.

## 2. THE TARGET — settle QHB

> **(QHB)** `∃ α>0` and `poly P` such that for every `d`-bit distribution `h` and coordinate `i`,
> `I_i(h) ≤ P(d)·V(h)^α`.

Either:
- **(R+) PROVE QHB** — a dimension-uniform quantitative gluing/Hermite–Biehler inequality bounding the
  one-coordinate affinity incompatibility `I_i(h)` by a polynomial in the parent's projective Rayleigh
  margin `V(h)`. *(A weaker form still gives R+ as long as the resulting threshold `γ` in W3 stays
  inverse-poly — e.g. `α` and `P` may depend mildly on `d`; or it may suffice to prove the gluing for the
  selector form `h=½a(z)+½z₀b(z)`, `a,b∈SR_{d−1}`, where `Δ_{0j}(h)=¼(b∂_j a − a∂_j b)` is the projective
  Wronskian — your §7 reduction.)* Then state the tester's query complexity + the best matching lower
  bound, so we see how tight the characterization is.
- **(R−) REFUTE QHB** via W5 — exhibit `h_d` (PB rank, `δ_d`-far, `M(h_d)=N_d^{−ω(1)}`). The natural place
  to look is a **minor-minimal non-HPP obstruction**: take a known minor-minimal non-half-plane-property
  matroid (e.g. the rank-4 sparse-paving 8-element ones, or the Vámos-type / `V₈` family) or a weighted
  analogue, and check whether *every* conditional projective margin decays super-polynomially while the
  distance decays only polynomially. Then tensorize (needs §0.3 / Lemma 5.2) ⇒ R−. (For full R−, also give
  the adaptive-transcript SR-vs-NO indistinguishability — but even the W5 refuter alone settles QHB/(L).)

## 3. Our honest read + the divergence (do not let it bias you)

Our adversarial audit leans **QHB is more likely FALSE at dimension-uniform strength** (the minor-minimal
HPP obstruction structure is known to be sporadic/irregular, so a uniform modulus would be surprising) —
i.e. it leans **R−**. You (round 9) were **divided** (d=2 + `g_s` support QHB ⟹ R+). We flag this only so
you attack whichever way the math actually goes; **if a weakened-but-sufficient QHB holds, that is R+ and
equally welcome.** If the right move is to reframe (a different sufficient statistic, a different
lower-bound technique), do that.

## 4. Deliverable

Settle QHB: **a proof** (dimension-uniform or sufficient-weakened) ⇒ R+ with the tester complexity and the
best lower bound; **or a refuter** `h_d` (W5) ⇒ R− with (ideally) the indistinguishability; **or** the
furthest rigorous progress + the exact remaining gap. First close the §0 normalization items so d=2 and
`g_s` are airtight base evidence. Mark proved vs assumed; honest confidence. (All human-verified later —
keep proofs explicit and checkable.)
