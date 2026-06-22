# RESEARCH SUMMARY & COLD-START — SR-SUBCOND
### Snapshot 2026-06-22 (through round 14). Read this first to resume.

> **如何冷启动（中文）：** 打开本文件 + `docs/ledger_sr_subcond.md`（详细记录）+ `guide.md`（只读宪法）。
> 当前进度：与 web GPT-5.5-Pro 的攻击循环已到 **round 16（已写好简报、待中转发送）**。下一步动作 =
> 把根目录 **`BRIEF_FOR_PRO.md`** 整段发给 web GPT-5.5-Pro，把它的完整回复贴回来，然后由编排者
> （Claude）派独立审计 + 复核 + 更新 ledger。
> 🔑 **Round-15**：候选硬核 `g_s`（非 SR、但每个真条件都 SR）被**有利解决**——`NR(g_s)=Θ(√I_i)`，被一个
> **完全内部的有界信道**抓住（已数值复核）；`g_s` 及其所有张量/填充/置换提升都被排除为 R−。证书也被修正：
> 正确对象是**负 Toeplitz 截面的 σ_min**（不是行列式，`g_s` 的行列式是 `e^{−Ω(s)}` 但 σ_min=Θ(s^{−2})）。
> 置信度回到 **~58–62/40**。🔴 **Round-14**：编排者提的"复根深度 ⟹ poly PB 距离"被 Pro 证伪（μ_4 只因 4 阶
> 固定才成立）。🔴 仍未闭合、未证明。🔴 owner 曾说"不披露 AI"——本编排者拒绝执行（违反 §15 + 学术诚信），
> 披露义务保留，未与 owner 解决。

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
- **Current lean: R+, ≈58–62/38–42 — genuinely open but the hard core resolved favorably.** Round-15 settled
  the candidate hard core `g_s` (`NR=Θ(√I_i)`, caught by a fully interior channel; all product lifts ruled out
  as R−) and corrected the certificate to **σ_min of a negative Toeplitz section** (Lemma 1.1). Round-14 had
  refuted the root-depth + SCP-Hellinger routes. The R+ pipeline is complete **modulo one localization theorem
  (36)**; the only remaining R− hope is a **genuinely entangled** obstruction (not a product lift).
- **Round 16 is written + sent (`BRIEF_FOR_PRO.md`), awaiting Pro's reply** — this is the resume point.

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

## 5. 🎯 THE ONE OPEN RESIDUAL (corrected in round 15; what round 16 attacks)
> **(36) compatibility-aware σ_min-localization.** `I_i(h) ≥ η ⟹` w.p. `≥(η/d)^C` a poly-samplable
> descendant `F` with EITHER (1) a Boolean conditional covariance `≥(η/d)^C`, OR (2) a bounded channel `K`
> whose rank law `q=π_K^{h|F}` has a **negative Toeplitz section `T` with `σ_min(T) ≥ (η/d)^C`**
> (⟹ `d_TV(q,PB)≥σ_min/2`, Lemma 1.1).

- **The corrections that produced this form:** (i) ROOT depth is dead (a constant-depth root can be
  `2^{−Ω(d)}`-PB-close, even through a bounded channel — round 14). (ii) The DETERMINANT normalization
  `[−det]/k^{k/2+1}` is also wrong (for `g_s` it's `e^{−Ω(s)}` while the rank law is `Θ(s^{−2})`-far from PB);
  the robust object is **`σ_min` of a negative Toeplitz section** (round 15, Lemma 1.1). (iii) GLOBAL `NR`
  alone is insufficient (an Ω(1)-far family has `NR=2^{−Ω(d)}`) — `I_i`-localization is essential. (iv)
  Spectral independence localizes Hellinger, not the compatibility gap.
- **Hard core `g_s` SETTLED (round 15):** `NR(g_s)=Θ(s^{−2})`, `I_i=Θ(s^{−4})` ⟹ `NR=Θ(√I_i)`, caught by a
  fully interior channel; `g_s` + all tensor/padded/permuted lifts ruled out as R−.
- **Prove (36) ⟹ R+:** tester `Õ(n^{2+2a+2b}/ε^{2+4a})`. **Refute ⟹ R−:** the only surviving hope is a
  **GENUINELY ENTANGLED** obstruction — `I_i=Ω(1/poly)`, all proper conditionals SR, the rank statistic
  SUBCOND-hidden by correlating the core with surrounding coords so NO product channel + descendant exposes
  a negative Toeplitz section with poly `σ_min` (a non-symmetric, rank-hidden core).
- **Evidence: R+ ~58–62/40** (the hard core + its product lifts are resolved favorably; root, global-NR, and
  determinant routes ruled out; the certificate is now clean/robust/estimable). Genuinely open.

## 6. HOW TO RESUME (exact next actions)
1. **Relay round 16:** send the entire root **`BRIEF_FOR_PRO.md`** (below the "send as-is" line) to web
   GPT-5.5-Pro (human relay). Paste Pro's full reply back to the orchestrator (Claude Code session).
2. **Orchestrator then:** archive the reply to `docs/rounds/round16_pro_response.md`; spawn 1–2 independent
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
