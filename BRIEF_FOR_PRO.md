# Brief for web GPT-5.5-Pro — ROUND 18: the energy-to-cut lemma (the single remaining R+ theorem)
### (copy everything below the line and send as-is)

---

> Round-18, on your round-17 results. We **independently verified** the two load-bearing computations: the
> universal MEM bracket `½𝔇≤d_TV(μ,SR)≤√𝔇` and the projective-plane cut defect
> `Φ(PG(2,q))=3(q−1)²/(q²+q+1)²` (exact, `q=2..8`) ⟹ `CutDef=Ω(d^{−3/2})`. Your multiscale decomposition
> `𝔇=𝓔_{>m}+𝓡_m` and the **automatic low-dimensional minor branch** are confirmed (audit running). This is
> a real collapse: **the entire R+ question is now one lemma.** Full method freedom — settle it (either way).

## 1. The single remaining theorem

> **(EC) Energy-to-cut lemma.** `∃ C`: for `m=O(log(d/D))`, `D=𝔇(h)`, if `𝓔_{>m}(h) ≥ D/2` (the
> compatibility defect lives at scales `> m` free coordinates), then a polynomial-query procedure finds, with
> probability `≥(D/d)^C`, a sample-guided prefix face `F` and a subset `A` of its free coordinates with
> `d_TV(L_{h|F}(|X∩A|), PB) ≥ (D/d)^C`.

You proved: the minor branch (`𝓡_m≥D/2`) is automatic; (EC) ⟹ **R+** with a `poly(n,1/ε)` tester. So
**(EC) holds ⟺ R+** (on this route), and its failure is the precise R− core.

## 2. 🎯 The crux, stated as cleanly as we can

By the multiscale identity, the hard case is a **minor-minimal** non-HPP obstruction: there every proper
minor is SR, so `𝓔_{>m}=𝔇`, `𝓡_m=0` — **pure high-energy**. So (EC) is equivalent to:

> **(MM-cut)** Does **minor-minimality + poly `𝔇`** FORCE a polynomially-visible cut/noise-rank defect?
> I.e. is there `C` with: `ν` minor-minimal non-HPP, `𝔇(ν)≥d^{−O(1)}` ⟹ `NR(ν) ≥ (𝔇(ν)/d)^C`
> (equivalently `CutDef(ν)≥(𝔇/d)^C`)?

The two known families pull in OPPOSITE directions and **this is the whole fight:**
- **`PG(2,q)`** is minor-minimal-flavored, growing, AND cut-visible (`Ω(d^{−3/2})`) — evidence (MM-cut) is TRUE.
- **the sparse-paving family** is cut-BLIND (`NR=2^{−Ω(n)}`) but **NOT minor-minimal** (its obstruction is a
  fixed 8-element planted minor; deleting outside it leaves a non-SR proper minor). So cut-blindness is
  achievable *only by hiding a small minor*, which minor-minimality forbids.

**So the exact question is: is cut-blindness COMPATIBLE with minor-minimality?** If pseudorandom global
cut-blindness inherently requires a *planted low-dimensional* obstruction (a proper non-SR minor), then
minor-minimality forbids it ⟹ (MM-cut) ⟹ **R+**. If you can make a *full-dimensional* minor-minimal
obstruction inherit the sparse-paving pseudorandomness, that is the **R−** core.

## 3. Both directions (signposts — invent your own)

- **(R+) prove (MM-cut).** Use the exact two-block reduction (A1): `CutDef(ν)≥` the best two-block-symmetrized
  SR defect. For a minor-minimal `ν`, every proper minor is SR — a very strong constraint. Does it force
  some block-`A` count law `L(|X∩A|)` to be poly-far from PB? The `PG(2,q)` computation (one line `L` exposes
  `Φ=Θ(d^{−1})`) is the template — is there a general "every minor-minimal non-HPP matroid has a flat/line/
  cocircuit whose intersection-count law is poly-far from PB"? (A structural matroid theorem: minimal HPP
  obstructions always carry a low-complexity certifying flat.)
- **(R+ alt) bound the excluded-minor support.** If every minimal non-HPP excluded minor has support
  `O(log(d/𝔇))` (or even `poly`), the minor branch already catches it. Is there ANY support bound for HPP
  excluded minors (even quasi-poly)? (You noted weak-HPP has unbounded `PG(2,q)` excluded minors — but those
  ARE cut-visible, so unbounded support need not mean cut-blind.)
- **(R−) make a minor-minimal cut-blind family.** Force the sparse-paving pseudorandomness to be
  full-dimensional and minor-minimal: a non-HPP matroid `ν_d` with every proper minor SR, `𝔇≥d^{−O(1)}`,
  `d_TV(ν_d,SR)≥½d^{−O(1)}` (MEM), yet `CutDef(ν_d)=d^{−ω(1)}` (every flat/block count law `d^{−ω(1)}`-close
  to PB). The tension: minor-minimality means the obstruction is "spread" over all of `[d]` (no proper minor
  witnesses it), but cut-blindness means no `O(1)`-arity flat witnesses it either — is that combination
  realizable, or self-contradictory? Resolve it.

## 4. Audited assets (use freely)

- **(A1) Exact two-block reduction (r16).** `d_TV(μ,SR)=d_TV(L(|X∩A|),PB[a,b])`; `CutDef(ν)` lower-bounds it.
- **(A2) Universal MEM (r17).** `½𝔇≤d_TV(μ,SR)≤√𝔇`. (A3) **multiscale** `𝔇=𝓔_{>m}+𝓡_m`; minor branch automatic.
- **(A4) sharp PB separation (r13).** `Φ(q)=4q_0q_2−q_1²>0 ⟹ d_TV(q,PB)≥(Φ/15)^{3/2}` — the cut-defect engine.
- **(A5) `PG(2,q)` cut-visible (r17):** `CutDef=Ω(d^{−3/2})`. **sparse-paving (r16):** cut-blind but not
  minor-minimal. **HPP lit:** Kummer–Sert; Wagner–Wei (≤6⟹HPP); González D'León (weak-HPP `PG(2,q)` minors).

## 5. Deliverable — this is the FINAL attack round; resolve it OR give us the definitive writeup

We are concluding the attack loop after this round, so please optimize for one of two outcomes:

**(a) Settle (MM-cut)/(EC).** A proof (minor-minimality + poly `𝔇` ⟹ poly `NR`) ⟹ **R+** (`poly(n,1/ε)`
tester + the best lower bound; try to tighten `Ω(√n/ε)` via the sparse-paving restricted-tester bound). A
full-dimensional minor-minimal cut-blind family ⟹ **R−** core (+ an SR yes-ensemble + adaptive SUBCOND
transcript indistinguishability). Either way, give the complete argument.

**(b) If you cannot fully settle it, produce the DEFINITIVE WRITEUP-READY summary** — because this corpus
will become a paper. Specifically: (i) the cleanest self-contained statements of the established theorems
(noisy-rank characterization, exact two-block reduction, universal MEM, the multiscale decomposition + the
automatic minor branch, `g_s=Θ(√I_i)`, the conditional `poly(n,1/ε)` tester, the sparse-paving `2^{−Ω(n)}`
restricted-tester lower bound, `PG(2,q)` cut-visibility); (ii) the single open problem (EC/MM-cut) stated as
cleanly and canonically as possible, with your honest assessment of its difficulty and which way it likely
resolves; (iii) any additional structural result that strengthens the *conditional* paper (e.g. more
obstruction families shown cut-visible, a partial energy-to-cut bound for a natural subclass, a tightened
constant). Mark proved vs assumed; flag every assumption; honest confidence. (All of this will be
human-verified before any submission and is disclosed as AI-assisted — keep proofs explicit and checkable;
we re-verify every construction numerically.)
