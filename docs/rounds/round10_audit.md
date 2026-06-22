# Round-10 audit — Pro's QHB normalization + variational formula + Łojasiewicz + reduction — 2026-06-21

> Independent adversarial agent (SymPy + literature) + referee. **All claims CORRECT.** The problem is
> cleanly + correctly reduced to one dimension-uniform inequality; both Pro and this audit lean **weakly
> R+** but agree it is genuinely OPEN.

## Verdicts (all CORRECT)
- **Claim 1 (d=2 constant `I_i≤4V₂`): CORRECT.** `V₂=(p₀₀p₁₁−p₁₀p₀₁)₊`; transfer feasibility + new det=0
  verified symbolically. **MINOR (phrasing):** a *single* transfer is NOT ≤2v (counterexample
  `p=(0.9,0,0.05,0.05)`); the bound needs **min of the two transfers** (the two group-sums total 1 ⟹
  max≥½ ⟹ min-cost ≤2v). State "take the cheaper of the two."
- **Claim 2 (tensorization `V(pq)=max{V,V}`): CORRECT** (symbolic). The `q²≤1` is legitimate: `R_C` permutes
  nonneg coeffs summing to 1 ⟹ `|R_C q|≤1` on the cube. Equality attained at `C∩B=∅`, all-ones.
- **Claim 3 (variational formula Thm 4.1): CORRECT** (all sub-steps symbolic; the `q*` Pythagorean max
  verified). 🔴 The correction **"QHB for stable children ≠ full QHB" is VALID and important** — the
  stable-children case only constrains the diagonal `(r,s)=(a,b)`; full QHB needs control of *suboptimal*
  compatible `(r,s)` (a genuine projection/transfer inequality).
- **Claim 4 (nonuniform fixed-d Łojasiewicz QHB): CORRECT, d-DEPENDENT.** `V_d,I_i` continuous
  semialgebraic on the compact simplex (incl. zero-prob branches via the unnormalized `Φ_m`);
  `V_d^{-1}(0)⊆I_i^{-1}(0)`; compact-semialgebraic Łojasiewicz ⟹ `I_i^{N_d}≤K_d V_d`. **Effective bound
  confirmed doubly-exponential** (`(8d)^{2(n+7)}`, `n=2^d−1` ⟹ `N_d≤2^{2^{O(d)}}`) — **fatal to a poly-query
  tester this route**; Pro correctly does NOT claim a tester.
- **Claim 5 (reduction + obstruction analysis): CORRECT.** 5a reduction to a dimension-uniform Hölder bound
  `Gap_λ ≤ poly(d)·Ξ_λ^α` is the right crux. **5b KPV (1212.6696) CONFIRMED** — interlacers of a hyperbolic
  poly form a convex cone (linear slice of the nonnegativity cone); **no conditioning modulus** (qualitative
  only); "neither WW nor KPV gives a uniform modulus" is fair. **5c CORRECTION VALID:** fixed-d / sporadic
  excluded minors cannot refute QHB (a Hölder modulus exists in each fixed `d`); **R− needs an ASYMPTOTIC
  family with `α_d→0` or `K_d` super-poly.** **5d CORRECT:** evading the strengthened W1 needs ALL projected
  ranks `|X∩A|` PB-close (a defective factor persists under tensoring, Claim 2).

## Single most important doubt
The whole result reduces to the **dimension-uniform interlacer-cone conditioning inequality (5a)** — exactly
where the literature is silent (KPV: convex structure, no modulus; Łojasiewicz: provably doubly-exp in `d`).
**No proof and no clear strategy for uniformity yet.** Everything proven (Claims 1–4) is fixed-d or
per-factor; none constrains the `d→∞` behavior of `α_d`.

## R+ vs R− (audit's assessment)
**Leaning WEAKLY R+ (uniform QHB more likely TRUE), but UNRESOLVED.** For R+: tensorization is *exactly*
multiplicative (no cross-factor degradation), d=2 clean with explicit constant, the structural decomposition
is tight. Against settling: the only known general modulus (Łojasiewicz) is doubly-exp; KPV/WW give no
uniform conditioning ⟹ a degenerating asymptotic family (Hölder exp→0) is NOT excluded. **Verdict: plausibly
true; the load-bearing (5a) is unproven — do NOT claim QHB established.**
