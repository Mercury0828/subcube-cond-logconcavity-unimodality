# Literature Kill-Scan — SR-SUBCOND (Phase 0, 2026-06-20)

> Full, un-truncated reasoning (the ≤15-line verdict is only an index). Criteria FROZEN per guide §4.
> Live web access confirmed working → scan NOT blocked → a GO verdict is permissible. **Nothing here is
> "proved."** Citations carry real URLs; nothing asserted without a source; gaps marked BLOCKED, never
> guessed.

---

## 0. Overall verdict (this scan)
**GREEN — proceed.** The model+property pairing `(SUBCOND, strong Rayleigh)` is genuinely unoccupied
(RED-1 NO-SCOOP, high confidence). No RED-2 trivialization surfaced from the literature; the load-bearing
risk is **feasibility** (does a usable local/isoperimetric handle for SR exist — `B3`), which is the C0
lean + the attack loop's job, NOT a literature kill. Two non-blocking caveats: (i) exact SODA-27
double-blind / AI-disclosure CFP text is BLOCKED (SIAM 403); (ii) a final manual body-sweep of the 3
forward-citers of 2502.16355 is recommended before locking the scoop claim (none look threatening).

**Independent second-opinion subagent: AGREE-GREEN / NO-SCOOP.** After adversarial re-search it found no
conditional/SUBCOND tester for SR/DPP/log-concave/M-concave/NA (2020–2026), and **LOW trivial-reduction
risk** (SR ⊋ DPP ⊋ product, so SR-membership cannot reduce to product/uniformity testing). Two notes it
adds: (i) **arXiv:2511.22122 / ITCS 2026** "Interactive Proofs for Distribution Testing with Conditional
Oracles" (Biswas–Bun–Canonne–Sivakumar) — conditional-oracle + 2026 + Canonne, but does *label-invariant*
IP testing (SR is NOT label-invariant); cite as adjacent, not a scoop. (ii) **Lower-bound-overlap caveat
for C2:** ensure the SR lower bound does not merely re-derive the known product/equivalence `Ω(√n/ε²)`
(2408.02347) on a sub-instance — the hardness must come from SR-membership. *(Folded into the C2 brief.)*

---

## 1. Query log (engine = WebSearch unless noted; date 2026-06-20)

| # | query | top hits triaged | takeaway |
|---|---|---|---|
| Q1 | "subcube conditioning model distribution testing strongly Rayleigh negative dependence" | 2502.16355 (SUBCOND monotonicity); 2004.12496 (junta SUBCOND); 1911.07357 (uniformity SUBCOND); 2302.09013 (uniformity hypergrid SUBCOND); 0707.2340 (BBL neg-dependence) | SUBCOND active; no SR tester. |
| Q2 | "isoperimetric inequality strongly Rayleigh real stable negative association property testing" | 2504.17679 (Extremal neg-dependence & SR, 2025); 0707.2340 (BBL); **2011.09441 (Isoperimetric ineqs for real-valued fns → monotonicity testing, KMS-real)**; 1108.0687 (concentration of Lipschitz fns of SR measures) | No isoperimetric *handle for SR testing* exists; 2011.09441 is the KMS-real engine behind 2502.16355's Thm 3. |
| Q3 | "M-concave matroid distribution testing conditional sampling sublinear 2025 2026" | 2506.18444 (tight simulation via conditional samples); 1608.04759 / 1504.04103 (cond-sampling sublinear); ITCS 2026 Interactive-Proofs cond-oracle; 2503.12518 (mass estimation cond model) | **No M-concave/matroid tester in SUBCOND** → niche open. |
| Q4 | "arXiv 2408.02347 subcube conditioning equivalence product testing improved bounds" | 2408.02347 (Adar–Fischer–Levi, APPROX/RANDOM 2024): `Õ(n/ε²)` equivalence + product test | Engine `P4` confirmed (subroutines for marginals/equivalence). |
| Q5 | "SODA 2027 call for papers ... double blind ..." | PaperPilot, wikicfp, HyperAI, SIAM soda27 | Deadline 2026-07-09 AoE; Philadelphia Jan 24–27 2027; CORE A*. |
| Q6 | "arXiv 2008.03650 testing DPP lower bound NeurIPS 2020 exponential dimension" | 2008.03650 (Gatmiry–Aliakbarpour–Jegelka, NeurIPS 2020) | DPP testing, matching sample lower bound, i.i.d.; extends to log-submodular. |
| Q7 | "arXiv 2308.00089 testing log-concave lower bound; testing grainedness ITCS 2025" | 2308.00089 (New Lower Bounds for Testing Monotonicity & Log-Concavity, 1-D); ITCS 2025.26 grainedness (Canonne–Sen–Yang) | 1-D anchors; no hypercube/SUBCOND lift. |
| Q8 | "Iwamasa arXiv 1704.02836 deciding M-convexity quadratic set function co-NP-complete" | 1704.02836 (Iwamasa, DAM 238, 2018) | `B2` confirmed precisely (QMCTP co-NP-complete). |

Sources, by id, with URLs in §2/§4 below.

---

## 2. Threat-table verification (guide §4)

| paper | id / venue (verified) | what it actually does | verdict |
|---|---|---|---|
| Monotonicity in SUBCOND | **arXiv:2502.16355**, **STOC 2025** (ACM DOI 10.1145/3717823.3718297; submitted 2025-02-22) | `Θ̃(n/ε²)` monotonicity (Thm 1 up / Thm 2 low, tight), `Θ̃(√n/ε²)` monotone-uniformity (Thm 4 low matching CCKLW21 up); first directed-isoperimetry in distribution testing | **GREEN (engine).** No SR/log-concavity/neg-dependence extension (see §3). |
| Improved SUBCOND equivalence/product | **arXiv:2408.02347**, APPROX/RANDOM 2024 (Adar–Fischer–Levi) | `Õ(n/ε²)` equivalence + product test via subcube queries | **GREEN (subroutine, `P4`).** |
| Testing DPPs | **arXiv:2008.03650**, **NeurIPS 2020** (Gatmiry–Aliakbarpour–Jegelka) | DPP vs ε-far in `ℓ₁`; **Thm 2: any (ε,0.99)-tester needs `Ω(√N/ε²)=Ω(2^{n/2}/ε²)` i.i.d. samples**; hardness extends to log-submodular | **YELLOW→GREEN.** Standard i.i.d. model; exp-in-dim lower bound = exactly what SUBCOND bypasses. `B1` now **verified precisely** (not assumed). Does NOT give a SUBCOND tester. |
| 1-D discrete log-concavity / monotonicity lower bounds | **arXiv:2308.00089** | new `Ω` lower bounds for 1-D monotonicity & log-concavity testing (standard model) | **GREEN (1-D anchor).** No hypercube/SUBCOND version. |
| Testing grainedness | **ITCS 2025**, LIPIcs.ITCS.2025.26 (Canonne–Sen–Yang) | settles grainedness testing complexity; Huge-Object-Model uniformity application | **GREEN (genre precedent).** |
| Quadratic M-convexity recognition | **arXiv:1704.02836**, DAM 238 (2018), Iwamasa | **QMCTP — deciding if a given quadratic fn on `{0,1}^n` is M-convex — is co-NP-complete in general** (poly-time under a natural assumption; `O(n²)` algo there) | **GREEN (boundary, `B2`).** Justifies targeting SR distribution-*testing*, not exact recognition. |

---

## 3. Special-assignment subagent findings (independent, fresh-context)

### (a) RED-1 scoop hunt → **NO-SCOOP (high confidence)**
- Closest property-match: **2008.03650** DPP testing — but **standard i.i.d., NOT conditional/SUBCOND**.
- **2502.16355 has only 3 forward citations** (via Semantic Scholar API): "Testing Distributions against
  Bounded Distinguishers" (2026); **"Interactive Proofs for Distribution Testing with Conditional
  Oracles"** arXiv:2511.22122 / ITCS 2026 (pairwise-conditional IPs for label-invariant properties — NOT
  SR/DPP/log-concave); "On the Spectral Expansion of Monotone Subsets of the Hypercube" (APPROX/RANDOM
  2025 — "approximate FKG" for monotone sets, NOT a neg-dependence tester). **None extend the
  isoperimetry engine to SR / log-concavity / negative dependence.**
- Other SUBCOND papers (2004.12496 junta, 1911.07357 uniformity, 2302.09013 hypergrid uniformity) target
  uniformity/junta, none SR/DPP/log-concave/neg-dependence.
- **No hit anywhere for a conditional/SUBCOND tester of SR, log-concavity, M-concavity, matroid, or NA.**
- BLOCKED: semanticscholar.org HTML page 404 (worked around via the API — coverage not lost).
- **Recommendation:** a final manual sweep of those 3 citing-paper bodies before locking the claim.

### (b) Read of 2502.16355 body (quote, don't paraphrase) — scopes what C1 must rebuild
- **Theorem 3 (real-valued directed Talagrand inequality), quoted:** "For any f:{−1,1}ⁿ→ℝ, we have
  𝐄ₓ[(∑_{i:xᵢ=−1}((f(x)−f(x⁽ⁱ⁾))⁺)²)^{1/2}] ≥ Ω(1/√log n)·dist₁(f)." Shape = root-sum-of-squared
  *positive* (directed, via `(·)⁺` over decreasing edges) edge-gradients lower-bounding `ℓ₁`
  distance-to-monotone, with constant **Ω(1/√log n)**. Generalizes KMS18 (2011.09441) to real-valued fns.
- **What is "local":** tester samples `x∼p`, `i∼[n]`, conditions on the 1-dim subcube `{x, x⁽ⁱ⁾}` (one
  free coordinate) and measures the **edge bias** (conditional mass leaning to the −1 endpoint). The
  isoperimetric inequality converts that local edge measurement into a global distance certificate.
- **Tightness + venue:** Thm 1 `Õ(n/ε²)` up, Thm 2 `Ω̃(n/ε²)` low ⇒ `Θ̃(n/ε²)` tight; Thm 4
  `Ω̃(√n/ε²)` monotone-uniformity matches CCKLW21's `Õ(√n/ε²)` ⇒ `Θ̃(√n/ε²)`. **STOC 2025** confirmed.
- **Extension remark:** **NONE found** for log-concavity / negative-dependence / global stability. The
  only stated open problem is internal (whether the `Ω(1/√log n)` loss in Thm 3 can be removed).
- **Bottom line:** monotonicity got the local→global bridge *for free* (Thm 3, KMS-type). **For SR, C1
  must rebuild that bridge from scratch** — derive an analogous directed-isoperimetric / local-to-global
  inequality whose local edge statistic certifies global `ℓ₁` distance to SR. The transfer is non-obvious
  and the paper provides no such extension. **This is exactly barrier `B3`.**

### (c) SR structural facts vs Borcea–Brändén–Liggett (arXiv:0707.2340; J. AMS 2009) — **CONFIRMED**
- **Def 2.9** (stable) / **Def 2.10**: "μ ∈ 𝔓ₙ is strongly Rayleigh if its generating polynomial g_μ is
  (real) stable." → Fact 3 (real-stable characterization) CONFIRMED.
- **Prop 2.1**: Rayleigh-closure under `∂^S`, positive translation, **specialization `f|_{zᵢ=αᵢ}`**, and
  positive scaling ⇒ subcube conditioning (set coord 0/1) + projection/marginalization preserved. §4 has
  the dedicated SR closure machinery (external fields, truncation). → **Fact 1 CONFIRMED** (substance);
  the exact §4 proposition *number* is BLOCKED (ar5iv render truncates at §2; PDF FlateDecode unreadable)
  — corroborated by Oveis Gharan SR lecture notes + arXiv:1602.05242. Do not cite a fabricated §4 number.
- **Thm 4.10**: "If f is strongly Rayleigh then μ_f is CNA+" (strongest NA, ⇒ NA). §4.2 "Stability
  Implies Negative Association." → **Fact 2 (SR ⇒ NA) CONFIRMED.**
- **NA necessary NOT sufficient for SR:** CONFIRMED via authoritative secondary sources (NA strictly
  contains SR); **no single named NA-but-not-SR counterexample with a theorem number located** in
  accessible primary text — flag for C2/CS3 use (the attacker may need to construct one; don't assume a
  canonical one exists in BBL).
- **Rayleigh-difference (Def 2.5):** `∂ᵢf·∂ⱼf ≥ ∂ᵢ∂ⱼf·f` on `ℝ₊ⁿ` — a **global analytic** condition on
  the positive orthant, **NOT a SUBCOND-observable local handle** (guide §5 caution). Turning it into a
  local statistic is precisely C1's burden.

---

## 4. SODA-27 CFP check (guide gate (c) input)
- **Deadline: 2026-07-09 23:59:59 AoE (UTC-12)** — confirmed across PaperPilot, wikicfp #194835, HyperAI.
- **Conference:** Philadelphia, PA, **Jan 24–27, 2027**; CORE A* / CCF A.
- **Format:** no page limit; "full version" submission encouraged (corroborated from SODA general
  guidance) — full proofs the default product; first ~10 pages carry the merits; references at end.
- **Double-blind:** SODA is (lightweight) double-blind in recent years (purpose statement located), but
  the **exact SODA-27 anonymization + generative-AI disclosure policy text is BLOCKED** — SIAM site
  returns HTTP 403 to automated fetch. **→ Owner must verify the official SODA-27 CFP at gate (c)**
  (anonymize from day 1 regardless; AI-use disclosure is load-bearing since the math is externally
  solver-produced — guide §15).

---

## 5. Concern table
| concern | severity | status |
|---|---|---|
| RED-1 scoop (SUBCOND SR/DPP/log-concave tester exists) | would-be-fatal | **CLEARED — NO-SCOOP** (sweep 3 forward-citers to lock) |
| RED-2 trivialization (SR-SUBCOND collapses to a solved property) | would-be-fatal | no literature evidence; C0 + the SR-fact read give no collapse signal — re-checked at C0 |
| `B1` exp-in-dim DPP lower bound (load-bearing, "verify don't assume") | needed for framing | **VERIFIED** `Ω(2^{n/2}/ε²)`, i.i.d. (2008.03650 Thm 2) |
| `B2` M-convexity hardness precise statement | needed for scope | **VERIFIED** (1704.02836: QMCTP co-NP-complete) |
| `B3` no local handle for SR | THE live risk | confirmed *as an open problem* (2502.16355 gives no extension); C0 leans, attack loop resolves — NOT a literature kill |
| SODA-27 double-blind / AI policy exact text | gate-(c) admin | BLOCKED (SIAM 403) → owner verifies |
| own-work dedup script `scripts/own_work_corpus.py` absent | admin | script missing from repo; guide §0 already adjudicated soft-overlap (caching ≠ distribution testing) → proceed |

---

## 6. Blocked items (exhausted free routes; never guessed)
- SODA-27 official CFP text (double-blind anonymization detail + generative-AI disclosure) — SIAM.org
  HTTP 403 to WebFetch. Deadline/format corroborated elsewhere; policy text deferred to owner gate (c).
- BBL §4 exact closure-proposition *number* — ar5iv truncation + PDF FlateDecode; substance confirmed.
- A named "NA-but-not-SR" counterexample with a theorem number — not in accessible primary text.
- `venues/conferences/soda.yaml`, `venue-prompts/soda/`, `scripts/own_work_corpus.py` — referenced by the
  guide but absent from the repo (not fabricated; logged for owner).

---

## 7. Verdict rationale (why GREEN, not YELLOW/RED)
- **Not RED-1:** no SUBCOND/conditional tester for SR/DPP/log-concavity/M-concavity/NA exists; the one DPP
  tester is i.i.d. with an exp-in-dim lower bound (the very barrier SUBCOND escapes).
- **Not RED-2:** no literature reduction of SR-SUBCOND to a solved property; SR facts confirm SR ⊋ product
  / ⊋ DPP and NA-necessary-not-sufficient, so a product/equivalence tester does NOT certify SR (CS3 alive).
- **Not RED-3:** no impossibility proof exists (and RED-3 needs a *proof*, not a difficulty lean).
- **GREEN:** the area is hot and the engines (2502.16355 isoperimetry bridge, 2408.02347 marginal
  subroutines) + the confirmed SR substrate strengthen the attack. The single live risk is `B3` (feasibility
  of a local handle) — routed to C0 + the attack loop under NO-RETREAT (§15), not a kill.
