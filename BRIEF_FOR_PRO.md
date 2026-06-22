# Brief for web GPT-5.5-Pro — ROUND 16: the general compatibility-aware σ_min-localization (or an entangled R−)
### (copy everything below the line and send as-is)

---

> Round-16, on your round-15 results. We **independently audited + numerically verified** the decisive
> `g_s` computation: the centered Toeplitz eigenvalue formula `λ_j=2a_s(cosθ_s+cos(jπ/(L+1)))` is exact,
> there is **exactly one negative eigenvalue** with `σ_min≥θ_s²/20`, and at `k*=⌊π/θ_s⌋` the determinant is
> `e^{−Ω(s)}` (`−4e-8…−9e-122` for `s=4..64`) while `σ_min=Θ(s^{−2})` — so your **σ_min correction is
> decisively right** and `NR(g_s)=Θ(√I_i(g_s))` with a fully interior channel. The hard core is **not**
> bounded-channel-blind, and its product lifts are not R−. We accept the corrected certificate and target.
> Two big shortcuts (root-depth, SCP-Hellinger) and one big candidate (`g_s`+lifts) are now closed. **Full
> method freedom — settle it.**

## 1. The state in one line

The R+ pipeline is complete **modulo one localization theorem**, now correctly normalized:

> **(36) compatibility-aware σ_min-localization.** `∃ C`: `I_i(h) ≥ η ⟹` w.p. `≥(η/d)^C` a poly-samplable
> descendant `F` has EITHER (1) a positive Boolean conditional covariance `≥(η/d)^C` (→ R13 covariance→NR),
> OR (2) a **bounded** monotone channel `K` whose noisy-rank law `q=π_K^{h|F}` has a **negative Toeplitz
> section `T` with `σ_min(T) ≥ (η/d)^C`** (→ Lemma 1.1: `d_TV(q,PB)≥σ_min/2`).

Prove (36) ⟹ **R+**, tester `Õ(n^{2+2a+2b}/ε^{2+4a})` (T4 localizes `I_i≥ε²/2n`; estimate covariance / learn
the rank law to `τ=(η/d)^C` and test the section's `σ_min`). Refute (36) ⟹ **R−** + a hard instance.

## 2. The two honest directions — please push BOTH

### (R+) prove (36). The structure you built points here:
- **(A) the affinity-optimal global comparator + a σ_min second-moment bound.** The variational formula
  gives a global compatible pair `(r,s)` with `1−ρ(h,·)²≥I_i`; at least one child-vs-comparator Hellinger
  is `≥poly(η)`. Flip-swap (Thm 5.1) localizes *that fixed* discrepancy — the open step is to convert a
  localized Hellinger/covariance signal into a **negative Toeplitz section with poly σ_min** on a
  poly-likely descendant (Lemma 1.1 is the bridge; `g_s` is the worked example where the bump
  `(a, 2a cosθ, a)` becomes a poly-σ_min tridiagonal section). Does a localized incompatibility always
  imprint a **near-singular-but-sign-flipped** consecutive Toeplitz window on some bounded-channel rank law?
- **(B) a structure theorem for minor-minimal obstructions.** `g_s` is THE minor-minimal obstruction (all
  proper conditionals SR). If every minor-minimal SR obstruction has, like `g_s`, a 3-term (or `O(1)`-band)
  rank bump under some bounded channel — giving a banded Toeplitz section with `σ_min=poly` — then (36)
  follows by reduction to the minor-minimal core. **Is the minor-minimal obstruction essentially unique /
  `g_s`-like (a localized near-singular Toeplitz band), or is there a genuinely different one?**

### (R−) the only surviving hope — a GENUINELY ENTANGLED obstruction:
Build (or rule out) an `h` with `I_i=Ω(1/poly)`, every proper Boolean conditional SR, and the rank
statistic **SUBCOND-hidden**: the obstruction core is *correlated* with the surrounding coordinates so that
**no product channel** (and no poly-discoverable descendant) leaves a negative Toeplitz section with poly
`σ_min`. Your §6 shows product lifts of `g_s` fail (a fixed product channel recovers `q_s`); the question is
whether **entangling** the core with its environment can suppress every product-channel rank law to within
`(η/d)^{ω(1)}` of PB while keeping all proper conditionals SR. The audit's sharpest framing: a *non-symmetric*
core whose `|Y|`-statistic is blind to all coordinate-independent channels. **Does the all-channel +
descendant machinery provably prevent this (⟹ R+), or is there an adaptivity/correlation gadget that defeats
every fixed product channel (⟹ R−)?**

## 3. Audited assets (use freely)

- **(A1) Lemma 1.1 (σ_min spectral PF separation, r15).** `det T<0 ∧ σ_min(T)≥τ ⟹ d_TV(q,PB)≥τ/2`;
  dimension-independent, robust to `‖q̂−q‖_1<τ`. **This replaces the (mis-normalized) determinant clause.**
- **(A2) `g_s` solved (r15).** `NR=Θ(s^{−2})`, `I_i=Θ(s^{−4})`, `NR=Θ(√I_i)`; interior channel margin
  `Θ(s^{−3})`; the rank bump `(a_s, 2a_s cosθ_s, a_s)` → tridiagonal Toeplitz, one negative eigenvalue.
- **(A3) Covariance→NR (r13).** positive covariance `κ ⟹ NR≥(κ/15)^{3/2}` — alternative (1) of (36).
- **(A4) Localization T4 + flip-swap Thm 5.1** (Hermon–Salez SCP Poincaré `≥1/m`) localizes Hellinger — the
  engine to upgrade into σ_min/covariance.
- **(A5) product lifts of `g_s` are NOT R−** (r15 §6); the all-channel NR estimator's cost is `log`(channel net).
- **(A6) one verification-debt item to nail rigorously:** the identity `I_i(g_s)=𝔇(g_s)=1−sup_{ν SR}ρ(g_s,ν)²`
  for every `i` (the bridge from `NR`/`d_TV` to the affinity quantity, underlying the headline `NR=Θ(√I_i)`).
  Our audit flagged this as the one load-bearing step not yet re-derived from first principles — please give
  an explicit derivation (or correct it: if `I_i` only *bounds* `𝔇`, state the exact relation and how it
  changes the exponent). The unconditional `NR(g_s)=Θ(s^{−2})` is not in question; only the `I_i` linkage.

## 4. Deliverable

Settle (36): a proof ⟹ **R+** (tester complexity + the best lower bound, ideally tightening `Ω(√n/ε)`), or a
genuinely entangled `η`-incompatible family with all proper conditionals SR and every bounded-channel rank
law `(η/d)^{ω(1)}`-close to PB ⟹ **R−** + the hard instance + its query lower bound. Or the furthest rigorous
progress + the exact remaining gap. If a cleaner invariant settles SR-SUBCOND testing, take it. Mark proved
vs assumed; flag assumptions; honest confidence. (Human-verified later — keep proofs explicit and checkable;
we re-verify every construction numerically.)
