# RESEARCH SUMMARY & COLD-START — SR-SUBCOND
### 🏁 Attack loop CLOSED 2026-06-22 (18 rounds). Read `DELIVERABLE.md` FIRST, then this.

> **如何冷启动（中文）：** **攻击循环已于 2026-06-22（round 18）按 owner 决定结束。** 先读
> **`DELIVERABLE.md`**（论文级总结 + 人工验证清单 + 诚实定位），再读 `docs/ledger_sr_subcond.md`（全程记录）。
> **结局**：头条问题（SR 是否有 poly SUBCOND tester）**仍开放**，置信度 **~52–55/45–48（真·五五开偏 R+）**。
> 但产出了一套**论文级结构理论（定理 A–I）+ 一个条件型 poly tester + 把整个问题约简成一条开放引理 EC_NR**。
> Round-18（最后一轮）：纠正了 MM-NR ⊊ EC_NR（二元/三元 MM-NR 不闭合 R+）；加了纠缠随机码 R+ 证据（全局
> 失明被前缀哈希打穿）。**全部由 AI 产出、AI 审计、未经人类验证**（`DELIVERABLE.md` 有 3 项必验清单）。
> 🔴 接下来全是 owner 的决定：①是否披露 AI（投稿前提）；②是否投入人工验证；③去向（诚实判断：诚实披露的
> arXiv 预印本，不是稳的 SODA）。🔴 "不披露 AI" 本编排者拒绝执行（违反 §15），披露义务保留、未解决。

---

## 1. The problem (fixed)
Determine the **subcube-conditioning (SUBCOND)** query complexity of **testing strong Rayleigh-ness (SR)**
on `{0,1}^n`. `μ` is SR iff its generating polynomial `g_μ(z)=Σ_S μ(S)∏_{i∈S}z_i` is real stable. Test:
accept SR `μ`; reject `μ` that are `ε`-far (`ℓ₁`/TV) from every SR distribution, using `poly(n,1/ε)`
subcube-conditional samples. Target venue **SODA** (deadline 2026-07-09 AoE); headline = a **tight**
characterization (R+ tight tester) OR a **proven impossibility** (R−). See `guide.md` (read-only constitution).

## 2. Current status (frozen 2026-06-22)
- **Phase 0 PASSED** (GREEN kill-scan: `(SUBCOND, SR)` is an open niche; no scoop). Then **14 rounds** of an
  external-solver attack loop: rounds 1–7 via codex GPT-5.5-xhigh (then transport got flaky), **rounds 8–14
  via web GPT-5.5-Pro (human-relayed by the owner)**, each round independently audited (1–2 fresh agents)
  + referee-verified (symbolic/numeric) by the orchestrator.
- **No theorem yet.** Bounds: **`Ω(max{√n/ε, 1/ε²}) ≤ Q_SR^SUBCOND(n,ε) ≤ O(2^n/ε²)`.**
- **Current lean: R+, ≈58–60/40 — genuinely open; the WHOLE problem is now ONE lemma.** Round-17 proved
  universal MEM (`½𝔇≤d_TV(μ,SR)≤√𝔇`, kills the degenerating-margin R− route) + an exact multiscale
  decomposition ⟹ **the low-dim minor branch is automatic** ⟹ **R+ ⟺ the energy-to-cut lemma** (high-dim
  compatibility energy ⟹ a poly-visible cut defect). `PG(2,q)` is cut-visible (R+ evidence). The audit's
  verdict: this is **consolidation, not a decisive shift — the energy-to-cut lemma is as hard as R+ ever was.**
- **Round 18 is written + sent (`BRIEF_FOR_PRO.md`), awaiting Pro's reply** — this is the resume point.
  ⚠️ **A genuine decision point has been reached (gate c): the problem has converged to one hard lemma; the
  rich conditional result may itself be the deliverable. See §7.**

## 3. The research arc (how we got here)
1. **The original headline idea** (mirror the Θ̃(n) monotonicity-in-SUBCOND tester via a directed-isoperimetric
   inequality) was shown to need a *local handle for SR that does not exist* (B3). A frozen-substrate ERROR
   was caught & corrected mid-loop: **positive-orthant Rayleigh ≠ strongly Rayleigh** (Rayleigh ⊋ SR;
   real-stability needs `Δ_ij≥0` on ALL real `ℝⁿ`, not just `ℝ₊ⁿ`).
2. **Rounds 8–11 (web Pro)** built a clean structure: a projective certificate `V` (=0 ⟺ SR), a robust
   signed-witness tester, a **localization theorem**, a **variational formula** for the affinity defect, and
   reduced R+ to a **dimension-uniform interlacer-cone conditioning inequality (UQHB)** — proved for product
   children, but the general case hit a hard real-algebraic-geometry wall (no degree-uniform metric
   regularity for the Wronskian map; KPV/Saunderson/amenability are silent).
3. **Round 12 (an OPENNESS RESET — owner directive to maximize Pro's creative freedom)**: Pro **abandoned
   the V/QHB/interlacer route** and found a cleaner one (§4), and killed two R− routes.
4. **Round 13**: closed the channel-degeneracy worry + the degree-2 case, proved several class rates,
   and (referee finding) `μ_4` is caught by a bounded channel — the orchestrator over-extrapolated this to
   an R+ "root-depth ⟹ poly PB-distance" route.
5. **Round 14 (a CORRECTION)**: Pro **refuted that route** — a constant-depth complex root can be
   `2^{−Ω(d)}`-close to PB, even through a fixed bounded channel (`μ_4` worked only at fixed degree 4).
   Reframed the target to normalized **Pólya-frequency minors**, and showed (Thm 5.1 §5) that spectral
   independence localizes Hellinger discrepancy — the WRONG quantity; the real obstruction is the
   *compatibility gap* `I_i`. Lean down to ~55–60/40.

## 4. The current framework (web Pro, all audit-clean unless noted) — the noisy-rank route
- **(C1) Monotone-noise rank characterization.** For a monotone product channel `K` (per coord
  `Pr(Y_i=1|X_i=0)=s_i ≤ Pr(Y_i=1|X_i=1)=r_i`), `π^μ_K=Law(|Y|)`. **`μ` SR ⟺ `π^μ_K` is Poisson-binomial
  for EVERY `K`** (channel = stability-preserving Möbius maps). `NR(μ)=sup_K d_TV(π^μ_K,PB)`; `NR=0⟺SR`;
  `NR ≤ d_TV(μ,SR)`; **estimable in `Õ(n/τ²)` samples over ALL channels** (offline computation exponential).
- **(C2) Channel regularization.** `NR_δ(h) ≥ NR(h) − dδ` ⟹ any defect has a **bounded** (non-degenerate)
  channel witness (params `Ω(τ/d)` from `{0,1}`). *(Closed the only audit doubt.)*
- **(C3) Sharp degree-2 separation.** `Φ(q)=4q_0q_2−q_1² > 0 ⟹ d_TV(q,PB) ≥ (Φ/15)^{3/2}` (exponent 3/2 sharp).
- **(C4) Class rates (full `I_i → NR`):** positive covariance `κ ⟹ NR≥(κ/15)^{3/2}`; **product SR children
  `NR ≥ I₀³/poly(d)`** (α=1/3); homogeneous SR children — a SUBCOND-*search* witness (down-up gap ≥1/k).
- **(C5) Two R− routes killed:** product tangent rigidity (SR tangent at a product has Fourier degree ≤2 ⟹
  the Paninski high-degree-perturbation lower bound fails first-order); homogeneous-selector localization.
- **(C6) Lower bounds:** `Ω(√n/ε)` (anti-product blocks + exact SUBCOND→iid simulation, AFL 2408.02347;
  distance to SR via closure — honest framing: AFL's construction, SR-distance bookkeeping, NOT a
  strengthening) and `Ω(1/ε²)`.
- **(C7) The right higher-order object = normalized PF minors (round 14).** Root depth is NOT a valid
  certificate (a constant-depth root can be `2^{−Ω(d)}`-PB-close, even through a bounded channel). Use
  `PF(q)=sup_M[−det M(q)]_+/k^{k/2+1} ≤ d_TV(q,PB)` (Thm 3.1); poly regime `k=O(log d/loglog d)`. `μ_4`
  (caught by a bounded channel `(0.1,0.55)`, roots `−1.90±0.72i`) is real but only a FIXED-degree witness.
  Global `NR` alone is insufficient (an Ω(1)-far family has `NR=2^{−Ω(d)}`); `I_i`-localization is essential.
- **(C8) σ_min certificate + exact two-block reduction + the global-channel barrier (rounds 15–16).** The
  robust PF certificate is `σ_min` of a negative Toeplitz section, NOT a normalized determinant (Lemma 1.1).
  `d_TV(μ,SR)=d_TV(L(|X∩A|),PB[a,b])` exactly for block-exchangeable homogeneous `μ` (Thm 2.1) ⟹
  `NR(g_s)=Θ(√I_i)`. 🔴 **But a sparse-paving matroid family is poly-far from SR yet `NR=2^{−Ω(n)}` (global-
  channel-blind) with all ≤6-coord conditionals SR** — so NO global statistic suffices; the obstruction must
  be found by localization + an `O(log d)`-dim excluded-minor descendant. *(literature all verified real.)*

## 5. 🎯 THE OPEN RESIDUAL = a DICHOTOMY (sharpened in round 16; what round 17 attacks)
> **R+ ⟺ CUT-OR-MINOR REMOVAL LEMMA.** `𝔇(h) ≥ η ⟹` EITHER **(cut)** a block `A` with
> `d_TV(L_h(|X∩A|), PB) ≥ (η/d)^C` (an exact two-block-symmetrized SR shadow, r16 Thm 2.1), OR **(minor)** a
> sample-guided descendant of prob `≥(η/d)^C` of dimension `O(log(d/η))` that is `≥(η/d)^C`-far from SR.
> **R− ⟺ a DEGENERATING EXCLUDED-MINOR FAMILY.** asymptotic minor-minimal non-HPP `ν_d`, every proper minor
> SR, `𝔇(ν_d)≥d^{−O(1)}`, but `NR(ν_d)=d^{−ω(1)}` (+ adaptive SUBCOND indistinguishability).
> **Sharpest sub-question (MEM):** must a minor-minimal non-HPP obstruction's own SR-margin be `≥poly(η,1/d)`
> (⟹ minor branch fires ⟹ R+), or can it vanish while `𝔇` stays poly (⟹ R−)?

- **The route that's now DEAD:** the global-σ_min / global-channel route — the round-16 sparse-paving family
  is poly-far from SR yet `NR=2^{−Ω(n)}` (global-channel-blind) with all ≤6-coord conditionals SR. So global
  noisy-rank CANNOT suffice; `I_i`-localization + the descendant/excluded-minor mechanism is essential.
  *(This family IS a rigorous lower bound against all non-adaptive bounded-arity testers — a real result.)*

- **Prior dead ends (chronology):** root-depth (r14), normalized-determinant (r15), and global-σ_min/
  global-channel (r16 sparse-paving) routes are all ruled out as proof strategies; `g_s` + its product lifts
  ruled out as R− (r15). Each correction is in the round artifacts.
- **Prove the removal lemma ⟹ R+:** tester `Õ(n^{2+2a+2b}/ε^{2+4a})` + try to tighten `Ω(√n/ε)` using the
  sparse-paving family as a restricted-tester bound. **Build the degenerating excluded-minor family ⟹ R−.**
- **Evidence: R+ ~55–60/40 — genuinely open** (foundation rigorous; both forks crisp; the sparse-paving
  near-miss "tightens the noose but does not close it" — both audits).

## 6. HOW TO RESUME (exact next actions)
1. **Relay round 17:** send the entire root **`BRIEF_FOR_PRO.md`** (below the "send as-is" line) to web
   GPT-5.5-Pro (human relay). Paste Pro's full reply back to the orchestrator (Claude Code session).
2. **Orchestrator then:** archive the reply to `docs/rounds/round17_pro_response.md`; spawn 1–2 independent
   adversarial audit subagents (3 if Pro claims closure); referee-verify any construction/inequality
   (symbolic/numeric in `derisk/`); classify FATAL/GAP/MINOR; update `docs/ledger_sr_subcond.md` (confidence
   trend) + write the next brief. **Per-round artifact naming:** `round{N}_pro_request.md` (pointer to the
   root brief) / `round{N}_pro_response.md` / `round{N}_audit.md`.
3. **Brief discipline (guide §8):** freeze FACTS, free METHODS; flag our own claims as possibly-wrong; give
   Pro maximal creative latitude (owner directive). The root `BRIEF_FOR_PRO.md` is always the *current*
   outgoing brief (overwritten each round); prior briefs are recoverable from git history / round artifacts.
4. **Stop / gate criteria:** AI-convergence stop needs the attacker to claim closure + 3 blind audits find
   no FATAL + every residual is verification debt (guide §9). RED-3 (impossibility headline) needs a
   *proven* super-poly lower bound. Neither reached.

## 7. Three human gates (guide §16) — status
- **(a) kill/pivot:** NOT triggered (no proof-of-death; the R− lean is not a proof).
- **(b) AI-convergence handoff:** NOT reached (still attacking; no claimed closure).
- **(c) venue/scope:** SODA-27 deadline 2026-07-09 AoE confirmed (3 sources); the exact double-blind /
  **AI-use-disclosure** CFP text is BLOCKED (SIAM 403) → owner must verify. 🔴 If (34) proves unreachable,
  the *result-so-far* (the reduction + class rates + `Ω(√n/ε)` LB + conditional tester) is a strong but
  non-tight contribution — any venue step-down is an **owner-only** decision on proof-of-death (NO-RETREAT §15).

## 8. 🔴 Integrity (unresolved, must surface to owner)
The owner (2026-06-21) instructed "do not disclose AI." The orchestrator **declined**: the core math is
externally-solver-produced, so SODA's AI-use disclosure is required and presenting it as human-authored is
misconduct (guide §15). Logged in `docs/guide_amendments.md`. The honest path = **full human rebuild + verify
of all AI substrate** + accurate brief disclosure per the real CFP. "AI-verified ≠ proved" throughout.

## 9. File map
- `guide.md` — read-only constitution (problem, plan, gates).
- `docs/ledger_sr_subcond.md` — **the detailed append-only record** (frozen model `P*`, refuted routes
  `N1–N6`, barriers `B1–B3`, the full per-round confidence trend, the open problem).
- `BRIEF_FOR_PRO.md` (root) — current outgoing brief (round 14).
- `docs/rounds/round{N}_*` — per-round briefs / Pro responses / audits (rounds 1–7 codex internal; 8–14 web Pro).
- `docs/guide_amendments.md` — the substrate-error correction + the AI-disclosure conflict log.
- `lit/SCAN_REPORT.md` — the Phase-0 kill-scan.
- `derisk/` — small-cube verification code (`sr_core.py` real-stability test on all `ℝⁿ`; `windows_search.py`;
  numeric checks of the witnesses/examples); `derisk/results/`.
- `PROJECT_STATE.md`, `DESIGN_DECISIONS.md`, `docs/NOT_CLAIMING.md`, `PROOF_REVIEW/` (gate-(b) stub).
