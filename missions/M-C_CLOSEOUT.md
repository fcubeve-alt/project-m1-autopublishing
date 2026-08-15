# MISSION CLOSEOUT — M-C: AI Publishing Marketplaces

**Status: KILLED — 2026-08-15. Killed *before* consuming the Owner's H1 gate.**
**Cost: 2 searches. Zero words. Zero Owner hours.**
**Kill type: CAPABILITY-BOUND, not market-bound.** This distinction is the whole finding.

---

## 1. What was tested

M-C's central question: *can a publisher with no audience, no catalogue and no ad budget achieve organic marketplace discovery for disclosed AI-written work?*

Rather than run the C-0 probe — which required the Owner's H1 gate first — I tested whether the hypothesis could be **falsified from the desk**, without spending any Owner time. It could.

## 2. Evidence for the kill

New titles do not receive organic visibility by default: **[R]**

> "A brand new book with zero reviews gets almost no organic visibility, regardless of how good the keywords are. Until a book begins to generate sales and reviews, it won't even surface in an Amazon search. **The algorithm rewards momentum, not existence.**"

The chicken-and-egg is explicit — sales require reviews, reviews require sales — and the bottleneck has shifted from production to marketing precisely because AI made production easy. **[R]**

## 3. Evidence against the kill — which I went looking for

I hunted counter-evidence rather than stopping at a convenient answer. It exists, and it is specific: **[R]**

- **Winnable niches are real and identifiable.** If the ten first-page results average **under 100 reviews**, the niche is winnable. If the most recent first-page publish date is **2+ years old**, there is demand with no active publisher.
- **Themed sub-niches are frequently invisible on page one** even when buyers are actively searching — e.g. "word search for adults" ranks, "bird word search for adults" does not. Those gaps are real entry points.
- Assessment requires reading **BSR, review counts and publish dates** off first-page results.

**So the market is not closed.** An entry point demonstrably exists.

## 4. The actual finding

> **The escape route requires exactly the capability we have already verified we do not have.**

`DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md` records it, tested: Amazon marketplace data — BSR, review counts, keyword volume, competitor depth — is **unobtainable from this environment**. `kdp.amazon.com` and general web hosts return 000 under the egress allowlist, and scraping is barred by `COMPLIANCE_POLICY.md` regardless of reachability.

Therefore:

| Step | Status |
|---|---|
| Organic discovery is possible in verifiably low-competition niches | ✅ Evidenced |
| Verifying a niche requires BSR / review-count / publish-date data | ✅ Evidenced |
| **We can obtain that data** | ❌ **Verified impossible here** |
| ⇒ We can only **guess** at niche selection | — |

M-C's mechanism is niche selection. Without the data, our expected hit rate is **random**, against a base rate where ~80% of small-catalogue authors earn under $100/month.

**Killing now is strictly better than running C-0.** C-0 would have cost the Owner the full H1 gate (up to 7 weeks if a US TIN is needed) plus an upload, to observe an outcome we can already predict — a single un-selected niche is a coin flip with a poor prior. **The kill saves the Owner the entire gate.**

## 5. The self-observation worth recording

I documented this exact constraint in `STRATEGIC_REVIEW.md` §P4 on day one:

> *"any strategy depending on live marketplace data is unsupportable in this environment."*

I then chartered a mission whose core mechanism is niche selection — the one thing that constraint denies. **I recorded the constraint and did not carry it forward into portfolio screening.** A documented constraint that is not applied as a *filter* is decoration.

→ Recorded as **R13**: constraints must be screening filters, not just documentation.

## 6. What this does NOT conclude

**This is not a market verdict, and it must not be recorded as one (R1).** The market has a demonstrated entry point. We cannot locate it *from here*. Confusing "I cannot see it" with "it is not there" is the exact error I made with Vocal in cycle one.

## 7. Reopen conditions — specific and cheap

M-C reopens **immediately** on any of these, because the market entry point is already evidenced:

| Condition | What it costs the Owner |
|---|---|
| **Owner performs niche validation** — for a candidate keyword, report the first page's ~10 results with review counts and most recent publish dates | **~20–30 minutes per candidate niche.** Anyone with a browser can do it |
| Environment gains an Amazon-domain egress allowance | One config change |
| Access to a keyword/BSR tool whose output can be shared into the session | Varies |

**The first is the cheapest unblock in the entire project.** One page of data per niche converts M-C from a coin flip into a screened bet — and it is a *one-off* per title, not an ongoing attention drain.

## 8. Cost

| Input | Amount |
|---|---|
| Cash | **$0.00** |
| Owner attention | **0 hours — and it saved the H1 gate** |
| Research | 2 searches |
| Words written | 0 |
| Assets discarded | None |

---

**Closed by:** Autonomous Business Brain · **Date:** 2026-08-15
**Owner action required:** none — but see §7. One page of marketplace data reopens this.
