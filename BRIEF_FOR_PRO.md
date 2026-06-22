# Brief for web GPT-5.5-Pro — ROUND 14: the general higher-order noise-rank rate (34)
### (copy everything below the line and send as-is)

---

> Round-14, on your round-13 results. We **independently audited everything** (symbolic + 300k-sample
> numeric + literature): channel regularization (Thm 1.1), the **sharp** PB separation (Thm 2.1, exponent
> 3/2 confirmed sharp), the covariance witness (Thm 3.1), the **product-children NR-rate** (Thm 4.1), and
> the homogeneous-selector **search** theorem (Thm 5.1, your search-vs-bound downgrade is correct) — **all
> correct.** Two big things are now closed: **channel degeneracy** (regularization) and the **degree-2 PB
> obstruction** (Thm 2.1, sharp). The whole problem rests on extending this to higher order. We also bring
> one decisive new data point. **Full method freedom.**

## 1. 🔎 Decisive new evidence — the hardest known obstruction IS bounded-channel-visible

We ran the computation your §6 said was decisive, on **`μ_4`** (the round-3 Rayleigh-but-not-SR example,
symmetric on 4 bits, `g_4=1+2e_1+2e_2+2e_3+e_4`, `a=(1,2,2,2,1)/30` — it defeats the *entire* covariance /
`V` / interlacer route):
- **`μ_4`'s worst Boolean conditional pairwise covariance `= 0`** (it evades Thm 3.1 / the §3 covariance
  route, exactly as a Rayleigh measure should), **YET**
- a **bounded** monotone channel `(s,r)=(0.1, 0.55)` (both well inside `(0,1)`) gives noisy-rank PGF
  `(complex roots −1.90 ± 0.72 i)` → **not Poisson-binomial** → **`μ_4` is caught**, with a **constant**
  margin (not degenerate).

So the canonical *higher-order* (degree-≥3 PF) obstruction — invisible to all covariances — **is** exposed
by a bounded channel via the second branch of your (34). This is strong evidence the general (34) holds.

## 2. The exact target — prove the general (34)

> **(34) higher-order noise-rank rate.** `∃ α>0, poly P`: for every `d`-bit `h` and coordinate `i`,
> `I_i(h) ≥ η ⟹` EITHER a poly-likely sample-guided descendant has a positive Boolean conditional
> covariance `≥ poly(η/d)`, OR some **bounded** monotone channel `K` produces a noisy rank with
> `d_TV(π^h_K, PB) ≥ poly(η/d)` (a poly-large higher Toeplitz/Pólya-frequency minor).

Equivalently (cleanest sufficient form): **`I_i(h) ≥ η ⟹ NR(h) ≥ poly(η, 1/d)`** for arbitrary
(nonproduct, nonhomogeneous) stable children — the remaining case after Thms 3.1/4.1/5.1.

Prove (34) ⟹ **R+** with tester `Õ(n^{2+2a+2b}/ε^{2+4a})` (localize T4 → estimate `NR` over the regularized
bounded-channel box, Thm 3.1). Refute it (a *spread* nonproduct family whose higher-PF defect evades ALL
bounded channels — `NR = d^{−ω(1)}` while `I_i = Ω(1/poly)`, all projected ranks PB, evading Thms 6.1/7.2)
⟹ **R−** + a hard instance.

## 3. Audited assets (use freely)

- **(B1) Channel = stability-preserving Möbius substitution (Thm 1.1, r12).** The noisy-rank PGF is
  `g_μ` after coordinatewise UHP-self-maps + a real-stable prefactor, diagonalized. So a complex root of
  `g_μ` (the obstruction) maps to a complex root of the noisy-rank PGF — **and regularization (r13 Thm 1.1)
  makes the witnessing channel bounded.** The qualitative `L→∞` is gone.
- **(B2) Sharp degree-2 conversion (Thm 2.1).** `Φ(q)=4q_0q_2−q_1²>0 ⟹ d_TV(q,PB)≥(Φ/15)^{3/2}`. The needed
  higher-order analogue: **a complex root of the noisy-rank PGF at distance `δ` from ℝ ⟹ `d_TV(·,PB) ≥
  poly(δ)`** (a quantitative "real-rootedness vs Poisson-binomial" stability; `μ_4` shows `δ=Ω(1)` there).
- **(B3) Variational formula (T5).** `I_i(h)` = affinity loss from forcing the children's best stable
  approximations to be compatible — a *real* incompatibility. Connect it to the *complex root* the channel
  must expose (B1): the conflict between the two children's stable approximations should produce a
  bounded-channel restriction that is non-real-rooted with poly margin.
- **(B4) Spectral independence / local-to-global.** SR measures have spectral independence (not only
  homogeneous ones); the down-up / up-down machinery (your Thm 5.1 engine, ALOV) may localize a general
  global incompatibility to a low-dimensional link/conditional carrying a bounded-channel defect — the
  nonhomogeneous generalization of Thm 5.1.

## 4. Concrete angles (signposts — invent your own)

- **(R+) quantitative root→PB-defect:** prove B2's higher-order form — a degree-`d` PGF with a root at
  imaginary distance `δ` is `≥poly(δ)`-far from `PB` in TV (a Pólya-frequency / total-positivity stability
  bound) — then combine with B1 (regularized channel exposing the root) + B3 (the incompatibility forces a
  root at distance `poly(η)`).
- **(R+) general local-to-global for `NR`:** extend Thm 5.1 beyond homogeneous via spectral independence:
  `I_i(h)≥η ⟹` a poly-likely conditional/link has `NR ≥ poly(η/d)`.
- **(R+) channel from the incompatibility direction:** use the variational formula's two conflicting stable
  approximations to *construct* the bounded channel directly (as `μ_4`'s `(0.1,0.55)` was found), and bound
  the resulting noisy-rank defect below by `poly(η)`.
- **(R−)** a spread nonproduct stable-children family (evading 6.1/7.2, all projected ranks PB) whose every
  bounded-channel noisy rank is `d^{−ω(1)}`-close to PB — if the higher-PF defect can be "diluted" below
  any bounded channel's resolution.

## 5. Deliverable

Settle (34): a proof ⟹ R+ (tester complexity + best lower bound), or a bounded-channel-blind spread family
⟹ R−, or the furthest rigorous progress + the exact remaining gap. The `μ_4` data point suggests R+ is
within reach via a quantitative real-rootedness↔Poisson-binomial stability theorem — but go wherever the
math leads. Mark proved vs assumed; flag assumptions; honest confidence. (Human-verified later — keep
proofs explicit and checkable.)
