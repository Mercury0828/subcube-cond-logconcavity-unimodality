# NOT_CLAIMING — internal honesty artifact (NOT a paper section)

> Per guide §14 + `venue-prompts/soda/2-writing-guide.md` 坑#1: SODA bans a defensive "Limitations"
> section. This list stays INTERNAL; at writing time each item is folded as a **precise positive scope
> statement** into the model/theorem definitions, never as a standalone caveat.

1. **Property = strong Rayleigh (SR)**, the subcube-closed real-stability class — stated as *the setting*.
   NOT a tester for **exact M-convexity recognition** (deciding M-convexity of a given quadratic set
   function is co-NP-complete, `B2`/arXiv:1704.02836). We test SR as a *distribution* property, not exact
   recognition.
2. **Model = subcube-conditioning (SUBCOND)** distribution testing on `{0,1}^n`; **standard** testing by
   default (any move to *tolerant* testing is a logged scope change, stated as the model).
3. **"Tight" is used ONLY where C1 (upper) and C2 (lower) match.** If a gap remains, state the exponents
   and list the optimal exponent as an Open Question — never write "tight"/"optimal" without the matching
   bound.
4. **The dropped "product-class unimodality" half simply does not appear** (no negative framing needed).
5. **No `poly(n)` claim until C1 is proven; no "first SUBCOND tester for SR" claim except against the
   verified literature** (SODA rejection trigger = non-SOTA comparison).
6. **"AI-verified ≠ proved":** any result the external-solver attack loop reaches is conditional until
   independent human verification + full formal writeup (guide §9/§15). The SR local handle and the
   far-from-SR lower-bound instances especially must be human-rebuilt before any "tight"/"impossible"
   claim. The eventual SODA submission must disclose AI use per the CFP.
