# Round-3 Response — C1 (codex GPT-5.5-xhigh, 2026-06-21) — MAJOR: substrate correction + route death

> Cleaned from `PROOF_REVIEW/codex_raw/round3_response_C1.raw.txt`. codex confidence 95%. Independent
> audit `round3_audit_C1.md` (running). **The orchestrator (referee) independently re-verified the core
> algebra** (below) — the result is solid modulo a literature cross-check on terminology.

## Verdict: (T″) FAILS — and it exposes a FROZEN-SUBSTRATE ERROR (the handle tested the WRONG property)
codex exhibits a constant-far-from-SR distribution invisible to **every positive external field** (hence
every Boolean conditioning and every mild/strong tilt — the entire covariance-handle class).

### The construction (REFEREE-VERIFIED)
`μ_4(S) = a_{|S|}/30`, `a=(1,2,2,2,1)`, i.e. `g_4(z)=1+2e_1+2e_2+2e_3+e_4` (symmetric, `g_4(1)=30`).
- **Rayleigh on ℝ₊ (positive-field covariances all ≤0):** for pair (1,2), `g_4=A+B(z_1+z_2)+Cz_1z_2`
  (`y=z_3,z=z_4`, `A=1+2y+2z+2yz`, `B=2+2y+2z+2yz`, `C=2+2y+2z+yz`). Then `Δ_12=B²−AC` (independent of
  `z_1,z_2`) and `AC−B² = −2−2y−2z−3yz−2y²z−2yz²−2y²z² < 0` on `ℝ₊²` ⟹ `Δ_12>0` ⟹ `Cov_{μ_4^λ}(X_1,X_2)≤0`
  for ALL positive fields. By symmetry, every pair. ✅ *(I re-expanded `AC−B²` by hand; exact match.)*
- **NOT real-stable (so NOT SR):** `g_4(t,t,t,t)=1+8t+12t²+8t³+t⁴`; `÷t²` ⟹ `(t+1/t)²+8(t+1/t)+10=0`,
  root `w=t+1/t=−4+√6≈−1.55 ∈ (−2,2)` ⟹ `t` complex (unit circle) ⟹ a root with `Im>0` in every
  coordinate ⟹ `g_4` not real stable. Equivalently `Δ_12<0` at the **real** point `(z_3,z_4)=(−1,−1)`. ✅
- **Constant-far from SR:** SR ⟹ `Δ_ij≥0` at ALL real points; `μ_4` has covariance numerator `+1/900` at
  `(−1,−1)`; the (quadratic) value is `≤8δ`-Lipschitz in TV `δ` ⟹ `d_TV(μ_4,SR) ≥ 1/7200`. Lift
  `μ_n=μ_4×Ber(1/2)^{⊗(n−4)}` stays far (marginalization preserves SR) and still invisible to all positive
  fields. ✅

### 🔴 THE FROZEN-SUBSTRATE ERROR (orchestrator's, now corrected)
The handle `P5`/`V(μ)=sup_{λ∈ℝ₊ⁿ}(Cov_{μ^λ})₊` and the criterion `P-SR`/`P3` as frozen
(`Δ_ij≥0 on ℝ₊ⁿ ⇔ SR`) were **WRONG**: `Δ_ij≥0` on the **positive orthant** is the **RAYLEIGH** property,
strictly weaker than **strongly Rayleigh** (= real stable = `Δ_ij≥0` on **all of ℝⁿ** / no upper-half-plane
roots). **Rayleigh ⊋ strongly Rayleigh**, and `μ_4` is an explicit Rayleigh-but-not-SR witness. The guide
§5 itself wrote the criterion on "`[0,1]^n`" (positive orthant) — the same imprecision. → logged in
`docs/guide_amendments.md`; literature cross-check pending (`round3_audit_C1.md`).

## Consequence: the covariance-handle route is DEAD for SR (N4)
No tester built on positive-external-field / Boolean-conditioning **pairwise covariances** can distinguish
SR from the Rayleigh-not-SR family. (T) / (T′) / (T″) all fail at the root: they certify *Rayleigh*, not
*SR*. CS3 was even sharper than we thought — not just "NA-not-SR" but "Rayleigh-not-SR" passes.

## BUT this is a REDIRECTION, not (yet) an impossibility — the new handle
🔴 `μ_4` is trivially **SUBCOND-testable by a DIFFERENT statistic**: condition away the product coords,
estimate the **O(1)-bit marginal**, and run a direct **real-stability (SR) test on that small marginal**
(decidable for fixed-size multiaffine polynomials). So the right handle is **"test real-stability of
conditional low-dimensional marginals,"** NOT pairwise covariances.
- `μ_4×Ber`: caught — its 4-bit marginal is non-SR. ✓
- `μ_n` (parity, round 2): all proper marginals are product (SR) ⟹ a *fixed* marginal SR-test misses it,
  but a marginal SR-test **after a Boolean conditioning** `X_B=t` catches it (conditional `{i,j}`-marginal
  is positively correlated). ✓ (needs deep conditioning + conditional marginal, not just unconditional.)
- ⟹ **(T‴) — the new target:** does `{ SR-test of the conditional marginal μ(X_W|X_T=ρ) : Boolean (T,ρ),
  |W|=O(1) or O(log n) }` separate SR from ε-far in `poly(n)` SUBCOND queries? I.e. is SR **locally
  testable on conditional marginals**: `d_TV(μ,SR) ≥ ε ⟹` some bounded conditional marginal is
  `Ω(poly)`-far from SR-on-`W`?
- Open obstruction to watch: a family that is far-from-SR but whose EVERY bounded conditional marginal is
  SR (a "spread-out" global violation). The audit is checking whether such a family is obvious.
