# derisk/ — C0 small-cube local-handle lean (internal de-risking only)

> SODA takes NO experiments. This is **adversarial de-risking** (guide §6 C0 / §12), never a paper
> section. A clean plot is NEVER a substitute for a proof. The output is a directional **lean**, not a
> proof and not a kill (guide §6: a lean only directs the attack).

## What this probes (the load-bearing question, B3)
Does a **candidate local statistic** — computable from subcube-conditional samples — **separate** genuine
strong-Rayleigh (SR) distributions from **adversarially-built ε-far-from-SR** distributions, on small
cubes `n ∈ {2,3,4}`? A clean separation ⇒ a local handle is *plausible* (lean: attack the C1 tester). No
separation ⇒ the handle is likely absent (lean: attack harder / weigh the impossibility route).

🔴 The candidate statistic is **NOT** the unbuilt C1 handle — it does not presuppose C1 exists.

## Files
- `preregistration.md` — the pre-registered hypotheses + falsifier, frozen BEFORE measuring.
- `sr_core.py` — SR membership test (Brändén multiaffine Rayleigh-difference criterion), the two honest
  distance-to-SR lower-bound lemmas (C0-L1, C0-L2), the candidate statistics, and the F1/F2 far families.
- `run_c0.py` — runs the pre-registered experiment with FIXED seeds; writes `results/`.
- `results/` — regenerated figures/tables (one regeneration command each).

## Reproduce
```
python derisk/run_c0.py          # fixed seeds; writes results/c0_results.json + summary
```
Runtime note: pure-Python; the full run (incl. the n=4 order-4 S3 search at budget 120000) takes a few
minutes. `results/c0_results.json` is frozen from that run. **The n=4 genuine (non-tensored) F2 search is
search-limited (count 0): random perturbations of the uniform product rarely achieve full conditional
negative correlation AND non-SR at n=4 — a limitation, NOT evidence such instances are absent.** The
robust, audited signal is at n=3 (see `docs/ledger_sr_subcond.md §7` + `docs/rounds/round0_C0_audit.md`).

## Honest distance seam (guide §6 C0)
"ε-far from SR" needs a distance to the SR set, which is NOT obviously tractable. We do **NOT** compute
exact projection. We build far instances by perturbing an SR distribution to **violate a named certified
inequality** and **lower-bound the ℓ₁ distance to SR by the violation margin** via two stated lemmas
(C0-L1 from SR⇒pairwise-negative-correlation `P2`; C0-L2 from SR⇒Rayleigh-difference≥0 `P3`). Both
lemmas are stated in `preregistration.md` and rely only on confirmed substrate; the Lipschitz constants
are computed explicitly, not assumed.
