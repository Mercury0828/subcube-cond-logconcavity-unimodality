# Round-8 audit — Pro's `Ω(√n/ε)` lower bound (§7) — independent agent, 2026-06-21

> Fresh-context adversarial audit; steps re-checked numerically + by inequality analysis; AFL (2408.02347)
> checked against the literature. **Verdict: the proof is CORRECT as argued. No FATAL. The one substantive
> issue is FRAMING/NOVELTY vs AFL (a GAP in presentation), plus MINOR write-up items.**

## Per-step verdict
- **(a) block farness — CORRECT** (loose). `D(p₊ᵅ)=−α` exact; `d_TV(p₊ᵅ,SR₂)≥α/2` valid (D 1-Lipschitz;
  true distance ≈0.184 for α=0.1 vs claimed 0.05).
- **(b) tensor farness / backward affinity recursion — CORRECT; THIS IS THE LOAD-BEARING STEP AND IT HOLDS.**
  The recursion does **not** illegitimately factorize affinity for correlated `Q`; it **peels one block**:
  `ρ(P,Q)=Σ_{x_<m}√(P_<m Q_<m)·ρ(p_m, Q(·|x_<m))`, using (1) `P` is a product (true by construction),
  (2) **SR closure** — `Q(·|x_<m)` is SR (conditioning) and `Q_<m` is SR (marginalization), and (3) per-block
  `sup_{SR 2-bit} ρ(p₊ᵅ,·) ≤ 1−α²/8` (numerically confirmed ≈0.979). Auditor stress-tested by maximizing
  `ρ(P,Q)` over correlated conditionally-SR `Q` — never exceeds `ρ(P,uniform)`. `1−ρ≥½d_TV²` standard. **No gap.**
- **(c) SUBCOND→iid simulation — CORRECT, exact.** `Pr(π=0)=½+2bα`; `law(X₂|X₁=0)=law(π)`; deterministic
  for fix-both; raw for fix-none. Never uses `b`. Products ⇒ one unconditional n-bit sample answers any
  multi-block subcube query; fresh sample per query ⇒ adaptive. (MINOR: a single query can span blocks —
  per-block description undersells but is fine.)
- **(d) χ² indistinguishability — CORRECT.** per-block inner product `1+16α²bb′`; `1+χ²=([(1+16α²)^q+
  (1−16α²)^q]/2)^m` matches brute force; `cosh` bound ⇒ `≤exp(128 m q² α⁴)`; `α²=Θ(ε/m)` ⇒ `q=o(√n/ε)`⇒χ²=o(1).
- **(e) AFL exact-simulation lemma — REAL** (2408.02347, APPROX/RANDOM 2024); the §7 simulation (c) is
  self-contained anyway (citation not load-bearing).
- **(f) 🔴 relation to AFL `Ω(√n/ε²)` — DUPLICATION / framing issue (the main finding).** The construction
  is **AFL's product-testing construction essentially verbatim** (same pairs, same hidden signs, same
  anti-product bias, `α ↔ ε/√n`). The `ε⁻¹` vs `ε⁻²` difference is a **distance-notion + α-scaling
  artifact** (distance to SR accumulated over `m` blocks vs distance to product), **NOT a strengthening** of
  AFL. Must be framed honestly.
- **(g) far-from-SR vs far-from-product — CORRECTLY bridged by (b), not conflated.** Step (b) lower-bounds
  distance to the **global SR class** (any correlated SR `Q`), via SR closure — products ⊊ SR, so this is
  the *stronger* statement, delivered correctly. YES instance (uniform) is SR. So it is honestly an
  SR-testing lower bound.

## Bottom line
**Is `Ω(√n/ε)` valid as argued? YES.** Every computational step checks; the affinity recursion is rigorous.
**The genuinely-SR content lives ENTIRELY in step (b)** (the closure-based far-from-SR upgrade); the
construction + χ² hardness are inherited product-testing hardness from AFL. **Classification: no FATAL, no
correctness GAP; one FRAMING GAP** (must cite AFL for the construction, state it is not a strengthening,
and make the SR-specific content (b) explicit) + MINOR write-up items (state the `m₊≥m/3` conditioning
consistently between (b) and (d); `α²=48ε/m<1/16` needs `m≳768ε`).
