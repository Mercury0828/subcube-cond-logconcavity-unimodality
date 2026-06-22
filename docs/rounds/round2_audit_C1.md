# Round-2 Audit — C1 (independent symbolic verification of the parity counterexample, 2026-06-21)

> Fresh-context agent re-derived all four claims by exact symbolic computation (sympy, n=4,5,6) + hand
> analysis. **Supersedes the preliminary synthesis in `round2_response_C1.md`** (which leaned toward
> impossibility — the audit corrects that).

## Per-claim verdict: ALL CORRECT
- **C1 (g_n + uniform-product marginals): CORRECT.** Marginals on `|C|=3` all `1/8`, on `|C|=n−1` all
  `1/16`. Dropping ≥1 coord destroys the parity constraint → uniform.
- **C2 (closed-form tilted covariance): CORRECT** (matches brute force, n=5,6). **MINOR phrasing fix:**
  "`A∪{i,j}≠[n] ⟹ Cov=0`" is **per-pair**; a tilt missing exactly two coords `{k,l}` makes *that one*
  pair `(k,l)` visible. Headline unaffected: any field with `|A|≤n−3` gives Cov=0 for **all** pairs.
- **C3 (`≥1/8`-far from SR): CORRECT.** (i) per-face inequality `ν(00)ν(11)≤ν(01)ν(10)` is *necessary*
  for SR (conditioning-closure → 2-var SR ⇔ neg. correlation; rescaling preserves direction → holds for
  joint masses); (ii) per-face ℓ₁ `≥ a` (raising the off-diagonal costs `≥2a`); (iii) faces partition the
  cube → sums exactly → `‖μ_n−ν‖₁ ≥ 1/4`, `d_TV ≥ 1/8`. **No double-count.** Independently: `Δ_01<0` at
  `z=(2,2,0.1,0.1)` → `μ_n` is genuinely non-SR.
- **C4 (1-param full-support tilt detects): CORRECT.** `λ_k=δ` ⇒ `Cov→1/4`; at `δ=1/n²` (n=5) `Cov≈0.197`.
  Also: a single Boolean conditioning `X_B=t` (t even) gives `Cov(X_0,X_1|X_B=t)=+1/4`.

## Verdict: sparse-SUPPORT localization is genuinely REFUTED (airtight). 
But the **key strategic correction**:

### The obstruction is SUPPORT size, NOT parametric dimension
A **1-parameter** full-support field already detects `μ_n` with `Θ(1)` signal (C4). So `μ_n` refutes
*low-support* localization, **not** *low-parametric*. Reformulate the target as **low-PARAMETRIC
full-support** — that survives `μ_n`.

### `μ_n` and F2 are COMPLEMENTARY, not shared, blind spots → leans toward a poly tester
- `μ_n`: blind to sparse fields, **caught** by Boolean full-conditioning AND by a 1-param tilt.
- F2: caught by interior fields, **blind** to all Boolean conditional pairwise correlations.
- **No exhibited family defeats BOTH** {O(1)-param full-support tilt} and {bounded Boolean conditional
  pairwise covariance}. ⇒ the two primitives are individually insufficient but possibly **JOINTLY
  sufficient**. **Impossibility is NOT supported yet** (would require ONE family blind to both).

### `μ_n` is NOT a good lower-bound seed as-is
One full conditioning detects it (O(1) queries). A real SUBCOND lower bound needs a **hidden-random-parity**
planted family (random affine subspace / random target parity) so no fixed conditioning aligns with the
constraint and the detecting correlation is hidden among exp-many candidates.

## Round-3 recommendation (priority order; high-EV first)
1. **(Decisive, cheap) Prove/refute (T″):** do {bounded-set Boolean conditional pairwise covariances} +
   {O(1)-parameter full-support tilted pairwise covariances} **jointly** separate SR from ε-far — AND is
   each low-parametric tilted covariance **poly(n)-SUBCOND-estimable** (the P6 exp-sum must collapse for
   the `O(1)`-param structure)? C4 suggests the low-parametric reformulation holds → would convert the
   "refutation" into a corrected theorem + a poly tester. **Do this first.**
2. **Only if (1) fails** (a family blind to BOTH primitives is exhibited): build the hidden-random-parity
   planted family for the C2 lower bound. Plain `μ_n` is too easy.

→ **Round 3 = attack (T″) (low-parametric combined-statistic upper bound). C2 held.**
