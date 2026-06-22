# SR-SUBCOND — DELIVERABLE (consolidated 2026-06-22, after 18 attack rounds)
### Status: attack loop CLOSED (owner decision). This is the writeup-grade summary. NOT a finished paper.

> 🔴 **Three standing caveats, all unresolved, all the owner's to settle before anything leaves this repo:**
> (1) **Every theorem below was produced by an external AI (GPT-5.5-Pro) and audited by other AI agents — NONE
> human-verified.** "AI-verified ≠ proved." (2) **AI-authorship must be disclosed** (the orchestrator declined
> the owner's "do not disclose AI" instruction; an honest disclosure is a precondition for any submission).
> (3) The headline question (poly tester for SR? or impossibility?) is **OPEN** — lean ~52–55/45–48, genuinely
> undecided.

---

## 1. The result in one paragraph
We introduce the **noisy-rank** invariant for testing strong Rayleigh-ness (SR) in the subcube-conditioning
(SUBCOND) model on `{0,1}^n`: `μ` is SR iff, under every monotone product channel, the output Hamming weight
is Poisson-binomial. We prove an exact two-block reduction, a universal affinity–TV bracket, and an exact
multiscale decomposition that **discharges the low-dimensional half of a testing dichotomy**. We show
**global statistics can be exponentially blind to SR-defect** (an Ω(1)-far measure with `NR=2^{−Ω(n)}`), yet
**adaptive sample-guided conditioning provably amplifies several qualitatively different obstructions**
(`g_s`, projective planes `PG(2,q)`, binary/ternary minimal obstructions, and an entangled random-code
family). The existence of a `poly(n,1/ε)` tester reduces to **one** clean open problem — an
**energy-to-noisy-rank removal lemma (EC_NR)** — for which we give a conditional tester and matching evidence
on both sides.

## 2. The theorem stack (paper skeleton) — each is AI-produced, audit-clean, human-UNverified
- **Thm A (noisy-rank characterization).** `μ∈SR ⟺ ∀K: π^μ_K∈PB`, via `R_{μ,K}(t)=∏_i(1−s_i+s_it)·
  g_μ((1−r_i+r_it)/(1−s_i+s_it))` (coordinatewise Möbius UHP self-maps). `NR(μ):=sup_K d_TV(π^μ_K,PB)`;
  `NR=0⟺SR`; `NR≤d_TV(μ,SR)`; estimable to `±τ` over ALL channels in `O((n log(n/τ)+log(1/δ))/τ²)` samples.
  ⚠️ estimability needs the **mesh-Lipschitz lemma** (verify item #1).
- **Thm B (exact two-block reduction).** block-exchangeable `k`-homog `μ`: `d_TV(μ,SR)=d_TV(q,PB_{|A|}[a,b])`,
  `𝔇(μ)=1−sup_{p∈PB[a,b]}ρ(q,p)²`. (Upgrades two-orbit real-rootedness to an exact projection.)
- **Thm C (universal MEM).** `1−√(1−𝔇) ≤ d_TV(μ,SR) ≤ √𝔇`, hence `½𝔇 ≤ d_TV ≤ √𝔇`, every `μ`.
- **Thm D (multiscale + automatic minor branch).** `𝔇=𝓔_{>m}+𝓡_m`; if `𝓡_m≥𝔇/2` a random `m`-descendant
  is `𝔇/8`-far from SR w.p. `≥𝔇/4`, poly-learnable for `m=Θ(log(d/𝔇))`. **⟹ the low-dim branch is free.**
- **Thm E (`g_s`).** `NR(g_s)=d_TV(g_s,SR)=Θ(s^{−2})`, `I_i=𝔇=Θ(s^{−4})`, `NR=Θ(√I_i)`; interior-channel
  witness; `σ_min` (not determinant) is the robust Pólya-frequency normalization.
- **Thm F (global blindness ⟹ localization indispensable).** a homogeneous sparse-paving family with
  `d_TV(μ,SR)≥n^{−C_0}` yet `NR=2^{−Ω(n)}` and all ≤6-coord conditionals SR ⟹ **no** `d_TV(μ,SR)≤poly(n)·
  NR^α` holds globally. (Uses Kummer–Sert's 22 rank-4/8-element minimal non-HPP matroids.)
- **Thm G (`PG(2,q)` cut-visible).** `Φ=3(q−1)²/(q²+q+1)² ⟹ CutDef=Ω(n^{−3/2})` (a growing obstruction
  caught by one line's two-block defect).
- **Thm H (entangled random-code stress test).** an Ω(1)-far measure with `NR=2^{−Ω(n)}` and EVERY `<n/4`-coord
  conditional a point mass, yet a sample-guided prefix isolates 2 codewords ⟹ a constant cut defect. **Shows
  global channel pseudorandomness is NOT near an R− construction** + a clean `2^{Ω(n)}` lower bound for the
  no-conditioning restricted oracle (conditioning is essential).
- **Thm I (binary/ternary MM-NR).** minor-minimal non-HPP **binary** matroids = `{F_7,F_7*}`; **within
  ternary** = `{F_7⁻,(F_7⁻)*,P_8}` (≤8 elements) ⟹ `NR≥c_*>0`. ⚠️ scope to "within ternary" (verify item #2).
- **Lower bounds.** `Ω(√n/ε)` (AFL anti-product construction + SR-distance bookkeeping — **NOT a new
  technique; frame honestly**) and `Ω(1/ε²)`. **No matching upper bound** (the tester is conditional).
- **Conditional tester (assuming EC_NR, exp `C`).** `Õ(2^m/ε⁶ + n(n/ε²)^{3C})=poly(n,1/ε)`.

## 3. The ONE open problem (canonical)
> **EC_NR (energy-to-noisy-rank removal).** `∃C`: `𝔇=𝔇(h)>0`, `m=Θ(log(d/𝔇))`, `𝓔_{>m}(h)≥𝔇/2 ⟹` a
> poly-query sample-guided prefix finds a face `F` with `NR(h|F)≥(𝔇/d)^C` w.p. `≥(𝔇/d)^C`.
> Special case **MM-NR:** every proper positive conditional of `ν` SR `⟹ NR(ν)≥(𝔇(ν)/d)^C`?
**EC_NR ⟺ R+ on this route.** R− core = a family with every proper conditional SR, `𝔇≥d^{−O(1)}`,
`NR=d^{−ω(1)}` (+ for a full lower bound: an SR yes-ensemble + adaptive SUBCOND transcript indistinguishability).
🔴 **MM-NR ⊊ EC_NR** (NOT equivalent — energy fragments across the prefix tree); the binary/ternary MM-NR
result does **not** close R+. The remaining gap needs a NEW removal theorem, not a reformulation of stability;
the prefix-hashing technique is **example-specific** (works for sparse, well-separated support only).

## 4. 🔴 Human-verification checklist (BEFORE any submission)
1. **Write the mesh-Lipschitz / channel-net discretization lemma** (load-bearing for Thm A estimability AND
   Thm F/H NR-pseudorandomness; currently a black box — if the channel-param Lipschitz constant isn't
   poly(n), those break).
2. **Cross-check the ternary excluded-minor list directly in Kummer–Sert** (scope to "within ternary":
   `{F_7⁻,(F_7⁻)*,P_8}`; do not transfer a "√6̄1 excluded minors" list as "minimal non-HPP" wholesale).
3. **Purge every "CutDef ⟺ NR" / "(MM-cut) ⟺ (EC)" equivalence** from all drafts; they are one-directional
   (`CutDef≤NR`; MM-NR is a special case). Confirm the tester depends on EC_**NR**.
4. **Reconstruct each of Thms A–I from first principles** — the whole corpus is AI-produced and unverified.
5. **Re-confirm the `Ω(√n/ε)` lower bound** is correctly attributed to AFL (2408.02347) + honest about the
   SR-distance bookkeeping being the only added step.

## 5. Honest scope assessment (orchestrator)
- **As-is: a strong arXiv preprint / 2nd-tier-venue submission, NOT a confident SODA paper.** It is a
  *structural theory + a conditional tester + partial/restricted lower bounds* for a niche testing problem —
  no tight characterization, no resolved complexity. SODA wants a resolved question or a clearly novel
  technique; a conditional result on `(SUBCOND, SR)` is borderline at best, and only if the structural theory
  (Thms A–D, F, H) is judged independently compelling.
- **If EC_NR were proved (≈25–35% within a few more rounds, optimistically): a genuine SODA-grade result**
  (first poly SUBCOND SR tester) — but then the full human reconstruction (item #4) is mandatory and large.
- **Best honest framing of the contribution:** "A noisy-rank theory of strong-Rayleigh testing: global
  blindness vs conditioning amplification, reducing the testability of SR to one removal lemma." Thms B and H
  and the global-blindness/localization dichotomy (F+D) are the most independently interesting pieces.
- **Realistic path:** human-verify Thms A–H (weeks), post an honest AI-disclosed preprint stating EC_NR as
  the open problem, and only target SODA if a human cracks EC_NR or a reviewer-grade reviewer finds the
  structural theory strong enough on its own.
