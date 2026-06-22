# RESEARCH SUMMARY & COLD-START — SR-SUBCOND
### Snapshot 2026-06-22 (through round 14). Read this first to resume.

> **如何冷启动（中文）：** 打开本文件 + `docs/ledger_sr_subcond.md`（详细记录）+ `guide.md`（只读宪法）。
> 当前进度：与 web GPT-5.5-Pro 的攻击循环已到 **round 15（已写好简报、待中转发送）**。下一步动作 =
> 把根目录 **`BRIEF_FOR_PRO.md`** 整段发给 web GPT-5.5-Pro，把它的完整回复贴回来，然后由编排者
> （Claude）派独立审计 + 复核 + 更新 ledger。
> 🔴 **Round-14 重要修正**：编排者提的 R+ 路线（"复根深度 ⟹ poly 的 PB 距离"）被 Pro 证伪（常数深度复根
> 可指数级接近 PB，连有界信道也救不了；μ_4 只因 4 阶固定才成立）。目标已改为**归一化 PF 子式**形式。置信度
> 从 70/30 降到 **~55–60/40（仍偏 R+，但更不确定）**。🔴 仍未闭合、未证明。🔴 owner 曾说"不披露 AI"——本编排
> 者拒绝执行该指令（违反 §15 + 学术诚信），披露义务保留，未与 owner 解决。

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
- **Current lean: MARGINAL R+, ≈52–58/42–48 — GENUINELY OPEN** (DOWN from 70/30; Pro says 55–60, independent
  audit says ~52/48). Round-14 refuted the root-depth R+ route AND the SCP-Hellinger route; the needed theorem
  is now a harder *compatibility-aware total-positivity localization* with NO known mechanism yet. The R−
  side has gained a credible (unbuilt) template: a non-symmetric `g_s`-lift hiding the rank statistic.
- **Round 15 is written + sent (`BRIEF_FOR_PRO.md`), awaiting Pro's reply** — this is the resume point.

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

## 5. 🎯 THE ONE OPEN RESIDUAL (corrected in round 14; what round 15 attacks)
> **(35) compatibility-aware PF/covariance localization.** `I_i(h) ≥ η ⟹` a poly-samplable descendant `F`
> (prob `≥(η/d)^C`) with EITHER (1) a Boolean conditional covariance `≥(η/d)^C`, OR (2) a bounded channel
> `K` with a Toeplitz minor of `q=π_K^{h|F}` of normalized magnitude `[−det M]_+/k^{k/2+1} ≥ (η/d)^C`
> (⟹ `d_TV(q,PB)≥(η/d)^C`, Thm 3.1). **Poly regime `k=O(log d/loglog d)`.**

- **NOTE the round-14 corrections:** (i) the ROOT formulation is DEAD (a constant-depth root can be
  `2^{−Ω(d)}`-PB-close, even through a bounded channel); the right object is a **normalized PF minor**, not
  root depth. (ii) GLOBAL `NR` alone is insufficient (there's an Ω(1)-far family with `NR=2^{−Ω(d)}`) —
  `I_i`-localization is essential. (iii) Spectral independence localizes Hellinger, not the compatibility
  gap; the needed theorem is **compatibility-aware total-positivity localization**.
- **Prove (35) ⟹ R+:** tester `Õ(n^{2+2a+2b}/ε^{2+4a})`. **Refute ⟹ R−:** an `I_i=Ω(1/poly)` family with no
  poly-discoverable positive-covariance descendant AND all bounded-channel PF minors `(η/d)^{ω(1)}`-small.
- **Candidate hard core = `g_s`** (non-SR parent, every proper Boolean conditional exactly SR). Decisive
  test: is `g_s`'s global obstruction caught by a bounded-channel PF minor with margin inverse-poly under
  the natural lift (R+), or does it decay `2^{−Ω(d)}` (R−)? *(Orchestrator should compute this — but
  remember the round-14 lesson: a single FIXED-dimension `g_s` computation does NOT establish an asymptotic
  rate.)*
- **Evidence: moderate R+** (product/covariance/homogeneous rates + the PF-minor hierarchy survive; the
  root route and the global-NR route are both ruled out as proof strategies).

## 6. HOW TO RESUME (exact next actions)
1. **Relay round 15:** send the entire root **`BRIEF_FOR_PRO.md`** (below the "send as-is" line) to web
   GPT-5.5-Pro (human relay). Paste Pro's full reply back to the orchestrator (Claude Code session).
2. **Orchestrator then:** archive the reply to `docs/rounds/round15_pro_response.md`; spawn 1–2 independent
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
