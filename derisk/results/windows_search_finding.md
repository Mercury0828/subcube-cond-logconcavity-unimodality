# Windows search finding (round-4 de-risk, 2026-06-21) — (T‴) bounded-marginal handle is INCOMPLETE

> Engineering de-risk (not a proof). Reproduce: `python derisk/windows_search.py` (seed 20260621).
> Symmetric/exchangeable reduction via Grace–Walsh–Szegő.

## Setup
A symmetric measure with rank weights `a=(a_0..a_n)` is SR ⇔ `P(t)=Σ_k C(n,k) a_k t^k` is **real-rooted**.
A bounded conditional marginal (condition Boolean `(T,ρ)`, project to `w≤k` coords) is SR ⇔ a corresponding
`≤k`-degree polynomial is real-rooted. The **full** bounded-marginal test
(`all_bounded_marginals_real_rooted`, all conditionings × all projections `w≤k`) was used.

## Finding: a far-from-SR symmetric measure with EVERY ≤k-coord conditional marginal SR
**Verified example (n=6, k=4):** `a = [0.5085, 0.78987, 1.0, 0.93066, 0.53687, 0.2272, 0.05883]`.
- Global `P(t)=Σ C(6,k) a_k t^k` has **complex roots `−3.178 ± 1.131 i`** ⟹ **NOT real-rooted ⟹ not SR**
  (robustly: `|Im|≈1.13`).
- **Every** bounded conditional+projected marginal with `w≤4` coords is **real-rooted (SR)** — including all
  unconditioned project-to-2/3/4 marginals. (Independently re-checked.)
Many more found across `n∈{6,8,10,12}`, `k∈{2,3,4}`, 3 generators (`max|Im root|` up to ~600).

## Consequence (records as N5)
🔴 **The bounded-marginal real-stability handle (T‴) is INCOMPLETE for any fixed `k`:** there are
far-from-SR measures all of whose `≤k`-coordinate conditional marginals are SR. The SR-violation is
genuinely **global/spread** (visible only in the degree-`n` rank polynomial). So "test all bounded
conditional marginals" does NOT yield a complete SR tester.

## 🔴 Crucial caveat — this is NOT (yet) a SUBCOND lower bound
These witnesses are **symmetric** ⟹ determined by `n+1` rank numbers ⟹ **SUBCOND estimates the whole rank
sequence trivially** (sample, count `|S|`) and tests global real-rootedness directly. So **symmetric
measures remain poly-SUBCOND-testable** via the *global rank statistic*. The search refutes the
**bounded-marginal handle**, not SR-SUBCOND-testability.

## Where this points (the refined dichotomy)
- Covariance handle: dead (N4, `μ_4`). Bounded-marginal handle: dead/incomplete (N5, here).
- **(A) survives only via a GLOBAL low-dimensional statistic** (for symmetric measures: the rank sequence).
  Open: does a `poly(n)`-dimensional SR-determining statistic exist for **general (non-symmetric)** measures?
- **(B)/RED-3 candidate (now better supported):** a **non-symmetric** "spread off-orthant violation"
  hidden from every `poly(n)`-query SUBCOND statistic (the symmetric route can't give this — symmetric is
  low-dim). This is the leading impossibility lead; needs a non-symmetric construction + indistinguishability.
