# Round-14 — web GPT-5.5-Pro response (2026-06-22) — REFUTES the root-depth R+ route; corrects the target

> Owner-relayed. **Pro refutes the orchestrator's proposed R+ angle** (the "complex-root depth ⟹ poly
> PB-distance" implication) — a genuine correction of a round-13/14 over-extrapolation. Reframes the target
> to a normalized PF-minor formulation. Neither R+ nor R− settled. Audit + referee checks below. Lean
> downgraded to **moderate R+ (~55–60/40)**.

## 🔴 HEADLINE CORRECTION (orchestrator was wrong)
The round-14 brief pushed "a noisy-rank PGF with a complex root at imaginary distance `δ ⟹ d_TV(·,PB) ≥
poly(δ)`" as the main R+ route, justified by the `μ_4` finding. **Pro proves this FALSE** uniformly in `d`.
`μ_4` worked ONLY because its degree is fixed at 4 (a constant-degree coefficient vector has a fixed
distance from PB). The implication fails for growing degree — **even through a fixed bounded channel.**

## §2 — A constant-depth complex root can be `2^{−Ω(d)}`-close to PB [REFEREE-VERIFIED]
- **Thm 2.1 (universal root lower bound):** `Q(z)=0 ⟹ d_TV(q,PB_d) ≥ ½(m(z)/R(z))^d`, `m(z)=`dist(0,
  segment `[1,z]`), `R(z)=max{1,|z|}` — necessarily **exponential** in `d`.
- **§2.2 counterexample:** `Q_d=Bin(d,½)` PGF + a tiny degree-≤2 perturbation `E_d=(t−1)(u_d t+v_d)` chosen
  so `Q_d(ζ)=0` at `ζ=−1+i/2` (constant imaginary part ½), with `d_TV(q^(d),Bin(d,½)) ≤ (3/2)4^{−d}`.
- **§2.3:** the same family, fed through the **fixed interior channel `(s,r)=(1/10,9/10)`** (mean ½ ⟹ maps
  fair bits to fair bits), keeps a root at `Im t_0=160/401≈0.399` and PB-distance still `≤(3/2)4^{−d}`.
- *(Referee: confirmed at d=4,8,16 — `Q_d(ζ)=0`, valid PGF, `d_TV≤(3/2)4^{−d}` (2.8e-3, 1.1e-5, 1.6e-10);
  bounded-channel root `φ(t_0)=ζ` exact, PB-close preserved. d≥32 hits float floor. **Pro's refutation
  holds.**)*
- **Consequence:** round-13 regularization is **one-way** (`NR=τ ⟹` a `τ/d`-bounded channel keeps `Ω(τ)`);
  it does NOT turn "a complex root exists" into a poly lower bound on `τ`.

## §3 — The correct objects: normalized Pólya-frequency (PF) minors
- **Thm 3.1 (robust PF-minor separation):** a `k×k` Toeplitz minor `M(q)` (`T(q)_{ab}=q_{b−a}`) with
  `det M(q)=−v<0 ⟹ d_TV(q,PB_d) ≥ v/k^{k/2+1}` (Hadamard + multilinearity; PB ⟹ totally nonneg Toeplitz).
- `PF(q):=sup_M [−det M(q)]_+/k^{k/2+1} ≤ d_TV(q,PB_d)`. A complete hierarchy (`q∉PB ⟹` some minor <0), but
  the normalized magnitude can be tiny (the §2 family: every negative minor `≤(3/2)4^{−d}`).
- **Key regime:** if `k=O(log d/loglog d)` then `k^{k/2+1}=poly(d)` ⟹ a negative minor of that order with
  inverse-poly RAW magnitude suffices for a poly tester.

## §4 — Global noisy-rank distance can be exponentially weak (but this is NOT R−)
- **Thm 4.1:** a random-sign full-support `μ_d` with `d_TV(μ_d,SR) ≥ 1/1280` yet `NR(μ_d) ≤ Cd²2^{−d/2}`
  (every GLOBAL noisy-rank statistic exp-close to PB). ⟹ no dimension-uniform `d_TV(μ,SR) ≤ poly(d)·NR^α`.
- **NOT an R− construction (§4.3):** random 2-faces expose constant positive covariance ⟹ SUBCOND catches
  it trivially via localization. **The point: arbitrary GLOBAL distance from SR does not force poly
  noisy-rank distance — `I_i`-localization is essential.** The "clean form" `I_i≥η ⟹ NR(h)≥poly` is
  STRICTLY STRONGER than the descendant-search form of (34) (a descendant can be visible even when the
  current face has exp-small global NR).

## §5 — Why spectral independence alone cannot prove (34)
- **Thm 5.1 (flip-swap localization):** Hermon–Salez SCP ⟹ Poincaré `≥1/m` ⟹ a random flip/swap face has
  `E[1−ρ(a^F,b^F)²] ≥ D(a,b)/2mM`. **But this localizes ordinary Hellinger discrepancy** `1−ρ(a,b)²`.
- 🔑 `I_i` is NOT Hellinger between children — it's disagreement with the **SET of compatible pairs**. A
  compatible selector can have far-apart children (products). Local affinity-optimal comparators need not be
  restrictions of ONE global optimizer (the **consistency problem**), witnessed by `g_s` (non-SR parent,
  every proper Boolean conditional exactly SR). ⟹ **the missing theorem must localize failure-of-
  compatibility itself, not raw Hellinger variation.**

## §6 — The corrected higher-order target (replaces the root formulation)
> `I_i(h)≥η ⟹` a poly-samplable descendant `F` (prob `≥(η/d)^C`) with EITHER (1) a Boolean conditional
> covariance `≥(η/d)^C`, OR (2) a bounded channel `K` with a Toeplitz minor of `q=π_K^{h|F}` satisfying
> `[−det M(q)]_+/k^{k/2+1} ≥ (η/d)^C` (⟹ `d_TV(q,PB)≥(η/d)^C` by Thm 3.1).
Known examples fit (product→covariance; homogeneous→link categorical; `μ_4`→fixed-order PF; high-freq→
covariance after deep conditioning; `g_s`→global inv-poly obstruction w/ stable proper conditionals).
**Unknown: whether every irreducible minor-minimal obstruction carries an inv-poly normalized PF margin.**

## §7 — query complexity unchanged. Bounds `Ω(max{√n/ε,1/ε²}) ≤ Q ≤ O(2^n/ε²)`.

## Status
PROVED: the root counterexample (exp PB-close, even through a bounded channel); root→PB necessarily exp in
`d`; the PF-minor bound `v/k^{k/2+1}`; the Ω(1)-far-but-`NR=2^{−Ω(d)}` random-sign family; flip-swap
localizes Hellinger only. NOT: `I_i≥η ⟹ NR≥poly`; the descendant dichotomy (34); a compatibility-aware
total-positivity localization; R+/R−. **Pro: "moderately inclined toward R+; the proof now needs a
compatibility-aware total-positivity localization theorem, NOT a generic quantitative real-rootedness
theorem."**
