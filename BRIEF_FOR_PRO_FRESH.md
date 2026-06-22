# Fresh brief for a NEW (context-clean) GPT-5.5-Pro — testing strong Rayleigh distributions with subcube conditioning
### (copy everything below the line and send as-is to a fresh agent)

---

We want to pin down the query complexity of a property-testing problem. We are deliberately giving you a
**clean slate**: the complete problem, **no prescribed method**, and — only at the very end, clearly optional
— a short note on what a previous attempt established, which **you are free to ignore entirely**. We are
specifically hoping for a fresh angle, so please attack the problem however you see fit before (if ever)
looking at the appendix.

## The problem

A distribution `μ` over `{0,1}^n` (equivalently, over subsets of `[n]`). Its **generating polynomial** is
the multiaffine polynomial
`g_μ(z_1,…,z_n) = Σ_{S⊆[n]} μ(S) ∏_{i∈S} z_i`.
`μ` is **strongly Rayleigh (SR)** iff `g_μ` is *real stable*: it has no zero `z∈ℂ^n` with `Im z_i > 0` for
all `i`. SR is the canonical class of "strongly negatively dependent" distributions — it contains
determinantal/DPP measures, uniform spanning-tree edge sets, random-cluster/exclusion measures, product
measures, and is closed under conditioning, marginalization, symmetrization, and truncation to a fixed size.

**Access model — subcube conditioning (SUBCOND).** A single query specifies a subcube of `{0,1}^n` (fix an
arbitrary subset of coordinates to chosen 0/1 values, leave the rest free); the oracle returns one i.i.d.
sample from `μ` *conditioned* on that subcube, provided the subcube has positive probability. (Unconditional
samples are the special case of fixing nothing.)

**Testing task.** Given `ε>0` and SUBCOND access to an unknown `μ`, distinguish with probability `≥ 2/3`:
- **YES:** `μ` is SR; versus
- **NO:** `μ` is `ε`-far (in total variation / `ℓ_1`) from *every* SR distribution on `{0,1}^n`.

**The question.** Is there a tester using **`poly(n, 1/ε)`** queries?
- If **yes**, give the tester — and, ideally, a matching lower bound, for a *tight* characterization.
- If **no**, prove it: a super-polynomial query lower bound (an impossibility).
- Either direction, or the furthest rigorous progress with the exact remaining gap, is valuable.

## What we're looking for

- **Total method freedom.** Direct tester, a different invariant or certificate, a reduction to/from another
  testing problem, a Yao-minimax lower-bound construction, an information-theoretic argument — anything.
  Bring whatever machinery you think fits (real-stability/geometry of polynomials, matroid theory, negative
  association, high-dimensional expansion / spectral independence, coding theory, Fourier analysis, …).
- **A genuinely fresh perspective is the point.** A prior multi-round attempt is summarized in the appendix;
  we deliberately keep it out of the way so it doesn't anchor you. If you can reframe or solve the problem
  by a route that ignores it, that is exactly what we want.
- Mark clearly what is **proved** vs **conjectured/assumed**; keep constructions and proofs explicit and
  checkable (we re-verify everything numerically and by independent review). Honest confidence at the end.

## The only quantitative anchors (audited, safe to assume)

`Ω(max{√n/ε, 1/ε²}) ≤ Q_SR^SUBCOND(n,ε) ≤ O(2^n/ε²)`.
The lower bound is a routine adaptation of a known SUBCOND product/equivalence-testing bound (Adar–Fischer–
Levi, arXiv:2408.02347); the upper bound is the trivial "learn the whole distribution." **The gap between
`poly(n,1/ε)` and `2^n` is wide open** — that gap is the whole question.

---

## Appendix (OPTIONAL — you may skip this entirely)

> Included only so you needn't rediscover basics. **You are explicitly encouraged to discard this framing
> and find your own.** None of it is required; some of it may even be the wrong lens.

A previous extended attempt established the following (all independently re-derived/verified at our end,
though not yet by a human referee):

1. **A rank reformulation.** Apply any "monotone product channel" `K` to a sample (flip each output bit with
   coordinate-dependent probabilities `Pr(Y_i=1|X_i=0)=s_i ≤ Pr(Y_i=1|X_i=1)=r_i`). Then **`μ` is SR iff for
   every such `K` the output Hamming weight `|Y|` is a Poisson-binomial law** (a sum of independent
   Bernoullis ⟺ real-rooted PGF). Define `NR(μ)=sup_K d_TV(Law|Y|, Poisson-binomial)`; `NR(μ)=0 ⟺ SR`, and
   `NR(μ)≤d_TV(μ,SR)`, and `NR` is estimable from `poly(n,1/τ)` samples.
2. **Two-block exactness.** For a `k`-homogeneous measure symmetric within two coordinate blocks `A,B`, the
   SR-distance equals exactly the TV-distance of the law of `|X∩A|` to the Poisson-binomial class.
3. **An affinity bracket.** With `𝔇(μ)=1−sup_{ν SR}ρ(μ,ν)²` (`ρ`=Hellinger affinity):
   `½𝔇(μ) ≤ d_TV(μ,SR) ≤ √𝔇(μ)`.
4. **Global blindness vs conditioning.** There exist measures that are `Ω(1)`-far from SR yet have
   `NR=2^{−Ω(n)}` (every *global* monotone-channel rank statistic is exponentially close to Poisson-binomial)
   — so no global statistic alone can test SR; *adaptive conditioning seems essential*. Yet on every concrete
   such "global-blind" family found so far, a sample-guided **prefix conditioning** does expose the defect.
5. **Where it stalled.** The attempt reduced "is there a `poly` tester?" to a single clean conjecture: if the
   SR-defect of `μ` is concentrated at *high-dimensional* conditionals (not visible in any low-dimensional
   descendant), must some bounded-complexity conditional + monotone channel still expose an inverse-poly
   noisy-rank defect? It could neither prove nor refute this. The hard core is **matroid basis measures**
   (`μ_M` is SR ⟺ matroid `M` has the "half-plane property"); the key unknown is whether a *minor-minimal*
   non-SR matroid (every proper minor SR) can hide its defect from all bounded-complexity conditional/channel
   statistics — related to whether half-plane-property excluded minors can have unbounded size with vanishing
   detectable margin.

Treat 1–5 as **leads, not constraints**. If your instinct is to attack the testing question by a completely
different route — a clean lower-bound construction, a different reduction, an upper bound that never mentions
"noisy rank" — please follow it. We would rather have an independent line of attack than a continuation of
this one.
