# Brief for web GPT-5.5-Pro — ROUND 9: the conditional-stability removal lemma (the make-or-break for R+)
### (copy everything below the line and send as-is)

---

> Round-9, building directly on your round-8 results. We **independently audited your round-8 reply
> (two separate adversarial checks, symbolic + literature)**: §1–§5 (rank universality, projective
> certificate, robust signed-witness tester, conditional aggregation, parity amplification) are all
> **verified correct, no errors**; your `Ω(√n/ε)` lower bound is **correct as argued** (one framing note
> below). Thank you — and you corrected two of our own mis-readings. The problem now reduces to **one
> precise lemma**. Proving it gives the poly-query tester (R+); refuting it (a construction hiding the
> amplifying face) gives the impossibility (R−). **Full method freedom as before** — if the right move is
> to attack neither and reframe, do that and tell us.

## 1. The state, after your round 8 (all VERIFIED — use freely)

Let `V(h)` be your projective certificate (`= max_{i<j, C⊆[n]∖{i,j}, x∈[−1,1]^{n−2}} [−Δ_{ij}(R_C h)(x)]_+`,
so `h` SR ⟺ `V(h)=0`). The verified building blocks:
- **(V1) Universal rank test.** For SR `μ`, `rank(μ)=|X|` is Poisson-binomial; `d_TV(μ,SR) ≥ d_TV(rank μ,
  PB_n)`, `O(n/τ²)`-sample estimable. (Necessary, not sufficient.)
- **(V2) Robust signed-witness tester (your Thm 3.1).** For any positive-probability conditional `h=μ(·|E)`
  of dimension `d`, `O((d log(d/γ)+log 1/δ)/γ²)` **samples** accept SR `h` and reject `V(h)≥γ`. So **a
  violation of inverse-poly margin at a single known subcube `E` is poly-query detectable.**
- **(V3) Conditional aggregation.** `d_TV(μ,SR) ≥ ¼ · E_{r∼μ_{F̄}}[ V(μ_r) ]` for any free-set `F`.
- **(V4) Amplification is real and necessary.** Dense parity `μ_T=2^{−m}(1+η(−1)^{|x|})` has global margin
  `V(g)=4η·4^{−m}` (exponentially small) yet is `Ω(η)`-far from SR, with a **constant** conditional margin
  `V(μ_r)=η/4` on a constant fraction of Boolean contexts `r`. So the witness lives in a conditional, and
  conditioning amplifies it — but the amplifying restriction must be *found*.
- **(V5) Lower bounds.** `Ω(√n/ε)` and `Ω(1/ε²)` (the former is, per our audit, the Adar–Fischer–Levi
  `2408.02347` anti-product construction with the distance measured to the global SR class via your
  closure step — correct, but it is *not* a strengthening of AFL's `Ω(√n/ε²)`; the SR-specific content is
  exactly the closure-based far-from-SR upgrade). Trivial upper bound `O(2^n/ε²)`.

## 2. THE TARGET — the conditional-stability removal lemma (prove ⇒ R+, refute ⇒ R−)

We need to convert the *necessity* facts (V1, V3) into a *sufficient, algorithmic* test. Precisely:

> **(L) Removal lemma (the make-or-break).** Is there a `poly(n,1/ε)`-query SUBCOND procedure and
> inverse-polynomial `γ(n,ε), β(n,ε)` such that: **if `d_TV(μ,SR) ≥ ε`, then with probability ≥ 2/3 the
> procedure outputs EITHER a certificate that `rank(μ)` is `≥γ`-far from `PB_n`, OR a positive-probability
> subcube `E` (a Boolean restriction) together with a pair `(i,j)` such that `V(μ(·|E)) ≥ γ`** — i.e. a
> bounded conditional whose signed certificate is inverse-poly-large?
> (Completeness: if `μ` is SR, no such certificate exists — guaranteed by V1, V2, V3.)

If (L) holds, then **(R+)**: run the rank test (V1) + the procedure of (L); when it returns a subcube `E`,
verify with the Thm-3.1 tester (V2). Total `poly(n,1/ε)` queries; soundness from (L), completeness from
V1/V2/V3. Done.

Two natural shapes for (L) — either suffices, and you may invent another:
- **(L-struct) a structural converse:** show that if `rank(μ)` is `o(γ)`-close to `PB_n` AND
  `E_{r}[V(μ(·|F=r))] ≤ o(γ)` for the restrictions in a `poly`-size, efficiently-samplable family `𝓕`,
  then `d_TV(μ,SR) = o(ε)`. (A quantitative converse to your aggregation V3, robust to a hierarchy of
  conditionings without the slack compounding.)
- **(L-alg) a random-restriction / search procedure:** a samplable restriction law (random subcube/junta
  of the right scale) such that a far-from-SR `μ` exhibits `V(μ(·|E)) ≥ γ` with inverse-poly probability —
  so random Boolean conditioning *finds* the amplifying face (as it does for parity). Show the margin
  survives at a discoverable scale.

The three known far-from-SR examples all already fit (L)'s dichotomy: **C-sym** → caught by the rank test
(V1); **μ_4** → constant *global* `V`; **dense parity** → constant *conditional* `V` on a constant fraction
of contexts. The open content is a theorem that these are *representative* — that far-from-SR always forces
either a rank-law violation or a poly-discoverable conditional certificate.

## 3. The other resolution — refute (L) ⇒ (R−)

Build full-support YES/NO ensembles with: every NO instance `Ω(1)`-far from SR; YES SR; and **every
adaptive `poly(n)`-query SUBCOND transcript has `o(1)` distinguishing advantage.** The hard part (V4):
the construction must **hide the amplifying face** — a far-from-SR `μ` whose conditional certificates
`V(μ(·|E))` are inverse-poly-large only on a `1/n^{ω(1)}` fraction of subcubes `E`, so no poly-query
adaptive search locates one, *and* whose rank law is `o(1)`-close to `PB_n`. (Dense parity fails this —
its amplifying faces are a constant fraction. You need them rare *and* adaptively unfindable.)

## 4. Deliverable + freedom

Prove **(L)** (⇒ a `poly(n,1/ε)` SUBCOND SR tester, R+ — and then please also give the best lower bound so
we can see how tight it is), **or** refute it via the hidden-face construction (⇒ R−), **or** show the
question needs a genuinely different idea and pinpoint exactly what. You have full freedom of method
(random restrictions / juntas, spectral / HDX, real-stability certificates, a smarter global statistic
beyond the rank law, communication / planted-distribution / SQ / learning-parity lower bounds — anything).
If our reduction to (L) is itself the wrong frame, say so and pivot.

**Return:** a proof of (L) with the resulting tester + its query complexity, OR the (R−) construction with
its indistinguishability proof, OR the furthest rigorous partial progress + the exact remaining gap; what
you used; assumed vs proved; honest confidence. (Everything will be independently human-verified — please
keep proofs explicit and checkable.)
