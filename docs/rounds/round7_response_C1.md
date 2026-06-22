# Round-7 — C1/RED-3: single hidden-character construction FAILS (referee analysis + de-risk, 2026-06-21)

> codex round-7 (the construction) timed out (transport). This is the **orchestrator's** referee analysis
> + a small-n de-risk (`derisk` ad-hoc check). Result: the natural single-hidden-character RED-3 candidate
> is **not** a valid hard instance.

## The candidate and why it fails
`NO = uniform + ε·χ_T`, `χ_T(x)=(−1)^{Σ_{i∈T}x_i}`, random parity `T`. Verified (n=6, ε=0.6,
`T={0,1,2}` and `{0,1,2,3}`):
- `is_sr(μ_T)=False` (far from SR), and the **non-SR-ness lives entirely in the `T`-marginal**
  (`marginal-on-T is_sr=False`); every marginal NOT ⊇ `T` is exactly **uniform** (invisible). ✓ as designed.
- 🔴 **BUT `rayleigh_margin(μ_T) < 0`** (hugely negative) — `μ_T` is **non-Rayleigh** (ON-orthant
  violation), so it is **caught by conditional pairwise covariances** (mechanism (i)), not an off-orthant
  `μ_4`-style violation.

**Caught either way (combined tester):**
- `|T|=O(1)`: a tester checking all `C(n,O(1))=poly(n)` bounded marginals finds the `T`-marginal non-SR. (ii)
- `|T|` large: condition all-but-2 coords; the free pair `{i,j}` has `Cov≠0` iff `{i,j}⊆T`; `~(n/|T|)²=poly`
  random conditionings hit a `T`-pair. (i)

⟹ **`N6`: a single hidden character is not a valid SUBCOND lower-bound instance.**

## The crux this leaves (precisely stated — the project's open research core)
Every concrete candidate is caught by the **combined tester** {conditional pairwise covariances (i)} +
{bounded conditional marginals (ii)} + {global rank statistic, symmetric case}. The make-or-break:
> **Is there an `Ω(1)`-far-from-SR, NON-symmetric `μ` that is CONDITIONALLY RAYLEIGH (evades (i)) AND has
> all `O(1)` conditional marginals SR (evades (ii))?** — i.e. a `μ_4`-style OFF-ORTHANT violation SPREAD
> over `ω(1)` coordinates.
- **YES + lower bound ⟹ (B)/RED-3.** **Provably NO ⟹ the combined tester is complete ⟹ (A) poly tester.**
- **Unresolved after 7 rounds.** codex leans 70% toward "cannot evade both" for non-symmetric `μ`
  (⟹ impossibility) but it is **NOT proven**. This is a hard, genuinely-open theory question — the actual
  SODA-grade core. Neither a clever completeness proof for the combined tester nor an evade-both construction
  has been produced; it needs sustained attacker work (codex throughput-limited this session; web-Pro = owner relay).
