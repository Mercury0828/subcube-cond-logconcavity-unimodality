# Brief for web GPT-5.5-Pro — ROUND 15: compatibility-aware total-positivity localization
### (copy everything below the line and send as-is)

---

> Round-15, on your round-14 results. We **independently audited everything** (symbolic + numeric +
> literature) and **you are right**: we verified your exponentially-PB-close root family (`Q_d(−1+i/2)=0`
> with `d_TV(q^(d),Bin(d,½))≤(3/2)4^{−d}`, valid PGF, **and the same through the fixed bounded channel
> `(0.1,0.9)`** — confirmed at `d=4,8,16`). So our proposed "root-depth ⟹ poly PB-distance" route is dead;
> our `μ_4` optimism was an artifact of fixed degree. Your reframing to **normalized PF minors** and your
> identification that the obstruction is a **compatibility gap, not Hellinger** (Thm 5.1 §5) are the right
> diagnosis. We accept the corrected target. **Full method freedom — go wherever the math leads.**

## 1. The corrected target (your §6)

> **(35) compatibility-aware PF/covariance localization.** `∃ C`: for every `d`-bit selector `h` and coord
> `i`, `I_i(h) ≥ η ⟹` a poly-samplable descendant `F` (found w.p. `≥(η/d)^C`) such that EITHER
> (1) some Boolean conditional covariance is `≥(η/d)^C`, OR (2) for some **bounded** monotone channel `K`,
> `q=π_K^{h|F}` has a Toeplitz minor `M` (`T(q)_{ab}=q_{b−a}`) with `[−det M(q)]_+ / k(M)^{k/2+1} ≥ (η/d)^C`
> — whence `d_TV(q,PB) ≥ (η/d)^C` by your Thm 3.1.

Prove (35) ⟹ **R+** (tester `Õ(n^{2+2a+2b}/ε^{2+4a})`). Refute it (an `I_i=Ω(1/poly)` family with no
poly-discoverable positive-covariance descendant AND all bounded-channel PF minors `(η/d)^{ω(1)}`-small) ⟹
**R−** + a hard instance. The **poly regime is `k=O(log d/loglog d)`** (`k^{k/2+1}=poly(d)`): an
inverse-poly RAW negative minor of that order suffices.

## 2. The crux you isolated — localize *failure of compatibility*, not Hellinger

`I_i(h)` = affinity loss from forcing the two `X_i`-conditionals' best stable approximations to be
*compatible* (interlacing). Your Thm 5.1 (flip-swap, Hermon–Salez SCP Poincaré `≥1/m`) localizes ordinary
Hellinger `1−ρ(a,b)²` — which can be large even on SR parents (compatible children can be far apart). The
**consistency problem**: local affinity-optimal comparators need not be restrictions of *one* global
optimizer. So the missing theorem must localize the compatibility defect itself. **Two ways this could go:**

- **(R+) a single global compatible comparator that localizes.** The variational formula gives an
  affinity-optimal global compatible pair `(r,s)`; at least one of `a↔r`, `b↔s` has Hellinger `≥poly(η)`.
  Localize *that fixed* discrepancy by Thm 5.1 — the question is whether the local faces stay aligned with
  the *same* `(r,s)` (a covering/consistency bound over the compatible-pair polytope), or whether a second
  moment / overlap argument forces a poly-normalized covariance or PF minor on a poly-likely face.
- **(R−) the compatibility gap genuinely delocalizes.** A family where every proper face is compatible
  (covariance ≤0, PF minors PB) yet the parent is `η`-incompatible — the obstruction living *only* globally,
  below every bounded channel's resolution.

## 3. 🎯 The candidate hard core — `g_s` (please attack it directly)

You flagged `g_s`: a **non-SR parent every one of whose proper Boolean conditionals is exactly SR** (the
minor-minimal obstruction). This is the sharpest test of (35):
- **The decisive question:** is `g_s`'s global obstruction visible to a **bounded-channel noisy-rank PF
  minor** (a channel *mixes* coordinates, unlike a conditioning — that is exactly how `μ_4` was caught
  without any revealing conditional), and with a margin that is **inverse-poly in the dimension** as `g_s`
  is lifted/spread? Or does the channel margin decay `2^{−Ω(d)}` (like your §2 family), making a spread
  `g_s`-family the R− instance?
- A clean `NR(g_s)` rate (poly lower bound, uniform in the lift), or a proof it decays super-poly, likely
  **settles the whole problem.** `g_s` is small/explicit — give an exact `NR` (or PF-minor) computation and
  its asymptotics under the natural lift.
- **Sharp R− constraint (our audit):** an R− instance needs THREE ingredients — `I_i=Ω(1/poly)`, no
  poly-discoverable positive-covariance descendant, AND all bounded-channel PF minors super-poly-small.
  `g_s`/the minor-minimal family already supply the first two. The **missing ingredient is a NON-SYMMETRIC
  lift that hides the rank statistic** — because *symmetric* far-from-SR families with all bounded-coord
  conditionals SR are poly-testable via the global rank sequence. So: either (R+) prove every such
  obstruction still leaks an inv-poly PF minor through a bounded channel, or (R−) build the non-symmetric
  `g_s`-lift whose rank statistic is SUBCOND-hidden.

## 4. Audited assets (use freely)

- **(A1) PF-minor bound (Thm 3.1).** `det M(q)=−v<0 ⟹ d_TV(q,PB)≥v/k^{k/2+1}`; poly regime `k=O(log d/loglog d)`.
- **(A2) Channel regularization (r13 Thm 1.1, one-way).** Any defect `τ` has a bounded (`τ/d`-interior)
  channel witness keeping `Ω(τ)` — so WLOG work with bounded channels; but existence of a root ≠ a τ bound.
- **(A3) Covariance witness (r13 Thm 3.1).** Positive Boolean covariance `κ ⟹ NR≥(κ/15)^{3/2}` — the
  first alternative of (35).
- **(A4) Localization (T4).** `d_TV(μ,SR)≥ε ⟹ I_i(h)≥ε²/2n` on a poly-likely sample-guided face.
- **(A5) `g_s` proper-conditional SR-ness + Borcea–Brändén–Liggett** proper-position/domination structure.

## 5. Deliverable

Settle (35) — or `g_s` as its decisive special case. A proof ⟹ R+ (tester + best lower bound). A spread
`g_s`-type family evading all poly-discoverable covariance/PF descendants ⟹ R− + the hard instance. Or the
furthest rigorous progress + the exact remaining gap. If a different invariant settles SR-SUBCOND testing
more cleanly, take it. Mark proved vs assumed; flag assumptions; honest confidence. (Human-verified later —
keep proofs explicit and checkable; we will re-verify every construction numerically.)
