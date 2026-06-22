# Round-18 FINAL audit — new results + paper-readiness — 2026-06-22

> Independent fresh-context auditor; ALL matroid/coding literature WebSearched; the 4 numerics re-derived.
> **No hallucinated literature, no FATAL.** Several GAPs that matter for the writeup. Final lean ~52/48 R+.

## Verdicts
- **Claim 1 (dichotomy corrections): CORRECT — and they invalidate prior over-claims.** (1a) `CutDef ≤ NR`
  always (a deterministic projected cut is a degenerate monotone channel) and can be STRICT ⟹ **EC_NR**
  (noisy-rank) is the right canonical conclusion, not energy-to-cut. (1b) MM-NR is a SPECIAL CASE of EC_NR;
  the converse is NOT automatic (energy fragments across the prefix tree). 🔴 **The round-18 brief's
  "equivalently CutDef" and "(MM-cut)⟺(EC)" language was an OVER-CLAIM — Pro correctly breaks it. Consequence:
  a MM-NR-only theorem (incl. binary/ternary, Claim 3) does NOT close R+.**
- **Claim 2 (random-code stress test Thm 2.1): CORRECT — genuine R+ evidence.** (2a) GV min-distance
  `2α=1/32<1−H₂(¼)=0.189` ✓. (2c) SCP correctly invoked (SR⟹SCP, Pemantle–Peres; `Var_ν(f)≤n` even more
  robust than claimed). (2d) the `n²` vs `n` variance separation is correct ⟹ `d_TV(μ_C,SR)≥1/8`. (2e)
  prefix-hash `Pr(Z=1)≥1/2e` ✓ (referee-verified). 🔴 **GAP (2b): the mesh-Lipschitz / channel-net
  discretization step is a BLACK BOX** — almost certainly true (derivatives `O(n)`), but a human must write it
  (load-bearing for both Thm 2.1 AND Thm A estimability).
- **Claim 3 (binary/ternary MM-NR): CORRECT; literature REAL.** Binary HPP⟺regular, excluded minors
  `F_7,F_7*` (`U_{2,4}` not binary) — Tutte + COSW ✓. Ternary HPP⟺sixth-root-of-unity, excluded minors
  `{F_7⁻,(F_7⁻)*,P_8}` all ≤8 elements (`P_8`=exactly 8) — **the "≤8" claim is TRUE, not hallucinated.**
  Finite list ⟹ uniform `c_*>0`. 🔴 **Precision fix: scope the ternary statement to "within ternary"**
  (search summaries blurred "√6̄1 excluded minors" with the larger "minimal non-HPP" list).
- **Claim 4 (theorem stack A–G + tester): PAPER-READY, no FATAL.** Tester correctly labeled CONDITIONAL on
  EC_NR; `Ω(√n/ε)` honestly framed as AFL bookkeeping. GAP (4b): the estimability `O(n log(n/τ)/τ²)` needs
  the same mesh-Lipschitz lemma as (2b). **Must purge the "CutDef⟺NR" / "(MM-cut)⟺(EC)" equivalences
  throughout before submission.**
- **Claim 5 (honest assessment): HONEST.** ~55/45 defensible (audit: ~50–55). 🔴 **Single most important
  doubt (5c): prefix-hashing is EXAMPLE-SPECIFIC — it works because the random code has SPARSE, WELL-SEPARATED
  support (hash `log M` coords ⟹ isolate O(1) codewords); a general minor-minimal obstruction can have dense
  exponential support where no prefix isolates O(1) points. It does NOT obviously generalize to EC_NR.**

## Final lean: R+ ~52/48, LOW confidence
Marginally below Pro's 55/45 — the MM-NR/EC_NR gap is wider than round-18 first admitted, and the
generalization doubt is unresolved. Still slightly R+ because no R− instance survives and every concrete
obstruction empirically breaks under adaptive conditioning. **The honest band across the project: ~50–55/45–50,
genuinely open.** (Trajectory 70→58→55→52 = honest deflation as each near-miss failed to close it.)

## 🔴 TOP 3 a human MUST re-verify before any submission
1. **The mesh-Lipschitz / channel-net discretization lemma** — load-bearing for Thm 2.1 (NR pseudorandomness)
   AND Thm A (estimability). One analytic step; if the Lipschitz constant isn't poly(n), two theorems break.
2. **Scope the ternary excluded-minor list to "within ternary"** ({F_7⁻,(F_7⁻)*,P_8}); cross-check the
   Kummer–Sert table DIRECTLY (not search summaries — they blurred two lists).
3. **Purge every "CutDef⟺NR" and "(MM-cut)⟺(EC)" equivalence**; restate as the one-directional inclusions;
   confirm the conditional tester depends on EC_**NR**.

## 🔴 NOT safe to claim
- MM-NR (binary/ternary) does NOT close or nearly-close R+ (special case only).
- `CutDef` and `NR` are NOT equivalent (NR strictly stronger).
- The random-code technique is NOT a general method toward EC_NR (example-specific).
- Keep `Ω(√n/ε)` labeled as AFL-construction bookkeeping.
