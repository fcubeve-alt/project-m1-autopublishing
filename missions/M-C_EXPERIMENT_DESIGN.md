# M-C EXPERIMENT DESIGN — testing the core question at the lowest possible cost

**Date:** 2026-08-15 · **Status:** design only. **No production authorised.** Blocked at H1.

---

## The problem with the obvious plan

M-C's central question is:

> Can a publisher with no audience, no catalogue and no ad budget achieve **organic marketplace discovery** for disclosed AI-written work?

The obvious way to test it is to write a genre-correct novel (60–80k words) and list it. That plan has a bad shape:

- It requires the **largest production commitment in the project so far** to test a hypothesis the evidence says usually fails (~80% of authors with 1–3 books earn under $100/month).
- If it returns zero, we will have spent a novel to learn something about **metadata and categories**.
- It conflates two questions — *does Amazon surface a new title at all?* and *is this a good book?* — and answers neither cleanly.

M-C won the charter **by default**, when M-P's pre-committed trigger fired. Winning by default is not justification, and the counterfactual test is still owed at the production commitment point (R7). Before committing a novel, it is worth asking whether the core question can be answered for materially less.

## Separating the two questions

| Question | What it measures | What it needs |
|---|---|---|
| **C-0 — Discovery** | Does Amazon surface a *new listing from an unknown seller* at all? Measured in **impressions**, not sales | **A listing.** Largely a function of category and keyword placement, not prose quality |
| **C-1/C-3 — Product** | Will buyers choose *this* work and pay? | **A good product** in a category with real demand |

**C-0 gates everything.** If a new listing gets ~zero impressions across two metadata configurations, no quality of writing rescues it, and M-C dies by its own pre-committed kill criterion. So C-0 should be tested **first, and as cheaply as possible.**

## The cheapest available C-0 instrument

**A0001 already exists**: ~9,000 words, 73 `[Official]` claims, cover produced and thumbnail-verified, full publication package, categories and keywords drafted. Marginal production cost to list it: **zero**.

**Is this sunk-cost reasoning?** The distinction matters, so I will state it explicitly. R7 forbids continuing a project *because* work was already done. That is not the argument here. The argument is:

- C-0 is a question worth answering, chosen **before** considering which asset to use;
- C-0 needs *a listing*, not *a good book*;
- among available instruments, A0001 is the cheapest by a wide margin.

Choosing the cheapest instrument for an independently-justified test is forward-looking. **If A0001 did not exist, the correct move would be to write the smallest publishable thing — not a novel.** That it already exists is convenient, not causal.

**A0001 remains a poor revenue bet** — it failed on artifact and budget-context grounds, and nothing here reverses that. It is being proposed as a **measuring instrument**, not as the business.

## The confound, stated honestly

A0001 is **non-fiction in a crowded category**. M-C's eventual product is likely **fiction**. Discovery dynamics differ between them — category competition, keyword behaviour and browse patterns are not the same.

**So a C-0 result from A0001 transfers asymmetrically:**

| Result | What it tells us | Confidence |
|---|---|---|
| **Zero impressions** | Amazon does not surface unknown-seller listings without external signal. Applies to *any* category | **High** — a floor-level failure is not category-specific |
| **Meaningful impressions** | Discovery is reachable in *this* category | **Low transfer** to fiction. Would need re-testing per category |

The asymmetry is what makes the probe worth running: **it is a strong kill signal and a weak go signal.** That is exactly the right shape for a first test — cheap to fail, and a pass merely earns the right to spend more.

## Proposed sequence

```
H1 cleared (Owner)
   │
   ├─► C-0 PROBE — list A0001, $0 marginal cost
   │      ├─ ~zero impressions after 2 metadata configs / 30 days
   │      │     └─► M-C KILLED by its own criterion. No novel written.
   │      └─ meaningful impressions
   │            └─► C-0 passes for non-fiction. Re-run counterfactual test,
   │                then decide whether to commit to a genre-correct work
   │
   └─► (Any sales A0001 makes are incidental, not the point)
```

**Cost of the kill branch: one upload, ~30 minutes of Owner time, $0.** Versus a 60–80k word novel to learn the same thing.

## Owner-facing conditions

Two things must be true before this runs, and neither is mine to decide:

1. **H1** — payout setup. Blocking.
2. **H2** — editorial approval of A0001, including whether the Owner is willing to have it published under their name given it is explicitly *not* our strongest product. A legitimate refusal; if so, the C-0 instrument becomes "the smallest publishable original work," and the probe costs more but the logic is unchanged.

## What this design deliberately does not do

- **Does not authorise production.** No novel, no new asset.
- **Does not rehabilitate A0001** as a revenue product. It failed that test and remains failed.
- **Does not treat a C-0 pass as validation.** It would only buy the right to run the counterfactual test again with better information.

## Status

**Blocked at H1.** No further agent work on M-C is useful until payout geography is known — genre selection ahead of a possible C-0 kill would be work performed on an experiment that may never run.
