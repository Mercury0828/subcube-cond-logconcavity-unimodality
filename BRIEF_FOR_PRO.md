# Brief for web GPT-5.5-Pro — ROUND 17: the cut-or-minor removal lemma (R+) vs a degenerating excluded-minor family (R−)
### (copy everything below the line and send as-is)

---

> Round-17, on your round-16 results. We ran **two independent audits** (algebraic + a literature audit with
> web search). **Everything checks out and all your matroid literature is REAL** (Kummer–Sert: 32
> minor-minimal non-HPP on ≤8 elements = 10 rank-3/7 incl. Fano + **22 rank-4/8 sparse-paving**; "every
> ≤6-element matroid has HPP", smallest non-HPP = Fano `F_7` — Wagner–Wei/COSW). Your A6 closure, the
> **exact two-block reduction** (`d_TV(μ,SR)=d_TV(q,PB[a,b])`, making `NR(g_s)=d_TV(g_s,SR)=Θ(√I_i)`
> rigorous), and the **globally channel-blind sparse-paving family** (`NR=2^{−Ω(n)}`, poly-far, all ≤6-coord
> conditionals SR) are all confirmed. You've reduced the entire problem to two dual statements. **This is
> likely the decisive round. Full method freedom — settle one side.**

## 1. The problem is now exactly this dichotomy

Your two-block theorem killed the global-σ_min route (the sparse-paving family is global-channel-blind yet
poly-far). What survives is:

> **R+ ⟺ CUT-OR-MINOR REMOVAL LEMMA.** `∃ C`: if `𝔇(h) ≥ η` then EITHER
> **(cut)** some block `A` has `d_TV(L_h(|X∩A|), PB) ≥ (η/d)^C` (an exact two-block-symmetrized SR shadow),
> OR **(minor)** a sample-guided descendant of probability `≥(η/d)^C` has dimension `O(log(d/η))` and is
> `≥(η/d)^C`-far from SR.

> **R− ⟺ a DEGENERATING EXCLUDED-MINOR FAMILY.** an asymptotic sequence of minor-minimal non-HPP measures
> `ν_d` with every proper minor SR, `𝔇(ν_d) ≥ d^{−O(1)}`, but **`NR(ν_d) = d^{−ω(1)}`** — equivalently (by
> your §3) every two-block shadow is `d^{−ω(1)}`-close to PB AND no `O(log d)`-dim descendant is more than
> `d^{−ω(1)}`-far from SR (+ adaptive SUBCOND transcript indistinguishability for the SR yes-ensemble).

The sparse-paving family is the near-miss: it nails `NR=2^{−Ω(n)}` and global blindness, but its excluded
minor `M_0` is **fixed (8 elements, margin `V(ν_0)=Θ(1)`)**, so it leaks on `O(1)`-dim descendants — the
minor branch fires. **The whole question is whether the excluded-minor margin can be forced to vanish.**

## 2. 🎯 The single sharpest sub-question (please target this)

> **(MEM, "minimal excluded-minor margin")** For a minor-minimal non-HPP measure `ν` on `d` coordinates with
> compatibility defect `𝔇(ν) ≥ η`, must its **own** SR-distance (= its excluded-minor margin, since every
> proper minor is SR) be `≥ poly(η, 1/d)`? Equivalently: can a minor-minimal non-HPP matroid measure be
> **`d^{−ω(1)}`-close to SR while `𝔇 ≥ d^{−O(1)}`**?

- If **MEM holds (margin ≥ poly)** ⟹ the **minor branch always fires** on the minimal excluded minor itself
  (a descendant of inverse-poly probability and dimension = its support size) ⟹ **R+** (you still must bound
  the minor's *dimension* — see §3 — but `g_s`/`M_0` both have small minimal excluded minors).
- If **MEM fails** (a sequence of minor-minimal non-HPP measures with vanishing margin but poly `𝔇`) ⟹
  **R−** candidate core.

This is a clean matroid/real-stability question: **how does the SR-margin of a minor-minimal non-HPP
obstruction scale with its dimension?** The Kummer–Sert classification is fixed-size (constant margin); the
**asymptotic** margin is the unknown. The exact two-block constraint (your §3: the obstruction must survive
EVERY two-block symmetrization) is the lever — does it force a poly margin, or can a growing excluded minor
satisfy it with vanishing margin?

## 3. Both directions (signposts — invent your own)

- **(R+ / prove the removal lemma)** show: `𝔇(h)≥η ⟹` either a two-block shadow `≥poly` (cut), or a
  poly-likely **low-dimensional** (`O(log(d/η))`) descendant that is poly-far from SR (minor). The minor
  branch needs BOTH (i) MEM (the excluded minor has poly margin) AND (ii) a **dimension/discovery bound**
  (the minimal excluded minor has support `O(log(d/η))` and is hit by a sample-guided descendant with
  prob `(η/d)^C`). Is there a width/branchwidth-style bound on minimal non-HPP excluded minors? (Matroid
  minor theory: are minimal excluded minors for HPP of bounded size, or can they grow?)
- **(R− / build the degenerating family)** push the sparse-paving construction so the planted obstruction is
  an excluded minor of GROWING size `ω(log d)` with margin `d^{−ω(1)}` (so no `O(log d)`-dim descendant
  catches it), while keeping `𝔇 ≥ d^{−O(1)}` (some two-block shadow or affinity defect stays poly) and all
  proper minors SR. The tension: growing the excluded minor while *shrinking* its margin but *keeping* `𝔇`
  poly — does some inequality forbid this? If not, instantiate it (a pseudorandom non-HPP matroid sequence).
- **(structural)** is `𝔇(ν) = Θ(`some power of the excluded-minor margin`)` for minor-minimal obstructions
  (as for `g_s`, where `𝔇=Θ(margin²)`)? If `𝔇` and the margin are polynomially related for ALL
  minor-minimal obstructions, MEM holds and R+ follows.

## 4. Audited assets (use freely)

- **(A1) Exact two-block reduction (r16 Thm 2.1).** `d_TV(μ,SR)=d_TV(q,PB[a,b])`; the obstruction must
  survive every two-block symmetrization.
- **(A2) A6 (r16).** if both `i`-conditionals SR then `I_i=𝔇`; for minor-minimal obstructions `I_i=𝔇` ∀i.
- **(A3) `g_s` (r15–16).** `NR=d_TV(g_s,SR)=Θ(s^{−2})=Θ(√I_i)`; the cut-branch witness, small excluded minor.
- **(A4) sparse-paving family (r16).** the global-channel-blind near-miss; the minor-branch witness, fixed
  excluded minor `M_0` (margin `Θ(1)`).
- **(A5) HPP literature.** Kummer–Sert 2111.09610 (minimal non-HPP ≤8 elts); Wagner–Wei 0709.1269 (≤6 ⟹ HPP);
  COSW (Fano = smallest non-HPP). HPP minor- and dual-closed.

## 5. Deliverable

Settle the dichotomy — ideally via **MEM**. A proof that minor-minimal non-HPP obstructions have poly margin
+ bounded support ⟹ the removal lemma ⟹ **R+** (a `poly(n,1/ε)` tester + the best lower bound; try to
tighten `Ω(√n/ε)` using the sparse-paving family as a restricted-tester bound). A degenerating excluded-minor
family ⟹ **R−** + the hard instance + its query lower bound. Or the furthest rigorous progress + the exact
remaining gap. Mark proved vs assumed; flag assumptions; honest confidence. (Human-verified later — keep
proofs explicit and checkable; we re-verify every construction numerically.)
