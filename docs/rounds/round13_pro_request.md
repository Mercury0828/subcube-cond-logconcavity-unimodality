# Round-13 brief — web GPT-5.5-Pro (pointer)

> **Canonical, copy-ready brief at repo root: [`BRIEF_FOR_PRO.md`](../../BRIEF_FOR_PRO.md)** (round-12 brief
> text = prior root content, recoverable from conversation/git; results in `round12_pro_response.md`).

## What this is
Round-13 = settle the single remaining quantitative crux of the round-12 noisy-rank route (audited clean,
`round12_audit.md`): **(NR-rate)** does a localized `I_i(h) ≥ η` yield a **bounded, non-degenerate**
monotone channel `K` (`L=poly`, params in `[η^{O(1)},1−η^{O(1)}]`) with noisy-rank defect `≥ poly(η)`, hence
`NR(h) ≥ poly(η,1/d)`? Prove ⟹ R+ poly tester; a bounded-channel-blind `η`-incompatible family (evading
Thms 6.1, 7.2, all projected ranks PB) ⟹ R−. The crux is precisely the channel-degeneracy rate (Thm 1.1's
root→channel is qualitative, `L→∞`). Audited toolbox (A1–A5) offered; angles (quantitative backward
construction; local-to-global for `NR`; low-degree exposure) as signposts; full method freedom.
