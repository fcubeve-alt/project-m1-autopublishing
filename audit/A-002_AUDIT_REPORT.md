# A-002 — INDEPENDENT AUDIT REPORT

**Subject:** M-C (Class C — retail publishing marketplaces, Amazon KDP and peers)
**Conclusion under audit:** "Retail marketplaces are capability-blocked; live marketplace data cannot be obtained through any compliant autonomous route, therefore the mission is dead."
**Auditor:** Independent Decision Auditor (fresh context, adversarial mandate)
**Audit opened:** 2026-08-16
**Status:** IN PROGRESS — written incrementally

---

## 0. Method and constraints

- Research channel: `WebSearch` (environment egress is allowlisted; `curl`/`WebFetch` do not reach general web domains).
- Every claim graded: **[PRIMARY]** (official platform/vendor/developer documentation), **[SECONDARY]** (practitioner, press, third-party analysis), **[UNVERIFIED]** (asserted, not confirmed).
- Evidence rows appended to `audit/A-002_EVIDENCE_MATRIX.csv` as found.
- A tool failure is a fact about the runtime, never about the market.

---

## 1. What the artifacts actually claim

Read in order: `M-C_CHARTER.md`, `M-C_EXPERIMENT_DESIGN.md`, `M-C_CLOSEOUT.md`, `DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md` §6a.

### 1.1 The kill's logical chain, as written

`M-C_CLOSEOUT.md` §4 states it as a four-row table. Restated as a syllogism:

1. Organic discovery is possible **in verifiably low-competition niches**. *(claimed evidenced)*
2. Verifying a niche requires BSR / review-count / publish-date data. *(claimed evidenced)*
3. We cannot obtain that data. *(claimed "verified impossible here")*
4. ⇒ Niche selection is a guess ⇒ expected hit rate is random ⇒ against a ~80%-earn-under-$100/month base rate, **kill**.

The closeout is careful in one respect and uncareful in three. Careful: §5 and §6 explicitly refuse a market verdict ("This is not a market verdict, and it must not be recorded as one") and §7 lists cheap reopen conditions. So the Brain did **not** intend an L1 claim, and said so.

### 1.2 Three problems visible **without any external research**

These are findings from the repository's own artifacts and require no web evidence to establish.

**(A) The kill is Amazon-shaped; the mission is not.**
`M-C_CHARTER.md` §2 defines M-C's scope as **eight** channels: Amazon KDP, Kobo Writing Life, Apple Books, Google Play Books, Barnes & Noble Press, Draft2Digital, Leanpub, Everand. Every piece of kill evidence is Amazon-specific: BSR is an Amazon metric, `kdp.amazon.com` is the tested-blocked host, "first page results" is Amazon search, the honeymoon/momentum claim is about Amazon's algorithm. **Seven of the eight in-scope channels are never mentioned in the closeout at all.** Leanpub and Everand in particular have materially different discovery models (Leanpub is author-driven/direct-audience; Everand is subscription). A mission with eight chartered channels was closed on evidence from one. That is an L3 finding recorded as an L2 kill, and it is visible on the face of the documents.

**(B) The mechanism was substituted between charter and closeout.**
`M-C_CHARTER.md` §4 names the central question as **discovery** ("Everything else is secondary"). Nowhere does the charter say the mechanism is *niche selection*. The closeout §4 asserts "M-C's mechanism is niche selection" — a mechanism introduced **in the kill document itself** — and then kills the mission for inability to execute that newly-named mechanism. Meanwhile the charter's own §3 evidence table names the two strongest empirical correlates of income as **catalogue size** and **email list ownership** (96% of highest-earning indie authors have a list vs 53% of low earners) — neither of which requires BSR data, and neither of which the closeout addresses. If catalogue and list are the strongest correlates on the Brain's own evidence, then a data channel supporting only *niche selection* is not the mission's binding constraint.

**(C) The closeout kills a probe the design document says was never run.**
`M-C_EXPERIMENT_DESIGN.md` sets out C-0 as a strong-kill/weak-go instrument at ~$0 marginal cost and ~30 minutes of Owner time, and states the design is **blocked at H1**, not falsified. `M-C_CLOSEOUT.md` §1 says the hypothesis was falsified "from the desk" instead — on **2 searches, 0 words**. So a mission with a designed, cheap, pre-committed-kill-criteria experiment was closed **without running it**, on secondary-source desk research, on the argument that the outcome is "predictable." The charter's §6 pre-committed kill trigger is "~0 impressions after **two** distinct metadata/category configurations over 30 days" — zero configurations were run. **The mission was killed without its own pre-committed kill criterion being met.**

### 1.3 The preflight contradiction

`DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md` §6a line 110 records **GitHub Actions as remote execution: AVAILABLE — UNUSED**, tested for GitHub reachability. Line 113 dismisses it for this purpose because "the marketplace data I actually lack is barred by platform terms, not by network reach."

That dismissal is a **category error stated in one sentence**: it treats "scraping is barred" and "no compliant route exists" as the same proposition. Scraping is one route. The dismissal never considers official APIs, licensed data vendors, public bibliographic APIs, or published bestseller lists — none of which are scraping, and all of which run fine from a runner with internet access. Charge 2 below tests whether any such route in fact exists.

---

## 2. CHARGE 1 — Level propagation (L1–L5)

*(pending)*

---

## 3. CHARGE 2 — The capability claim

**The claim under test:** "Live marketplace data (BSR, review counts, keyword volume) cannot be obtained through any compliant autonomous route from this environment."

The brief correctly decomposes this into (a) Amazon domains unreachable — tested, true; and (b) therefore no compliant route exists — asserted, untested. I tested (b).

### 3.1 The decisive finding: (b) is false, by direct test, in this container

I ran `curl` from inside this environment against candidate data hosts:

| Host | Result |
|---|---|
| `www.googleapis.com/books/v1/volumes` | **HTTP 429 with a well-formed Google API JSON body** |
| `openlibrary.org` | `000` (blocked) |
| `api.keepa.com` | `000` (blocked) |
| `webservices.amazon.com` | `000` (blocked) |
| `kdp.amazon.com` | `000` (blocked) — reproduces the Brain's test |

The 429 is not an egress failure. The body reads:

> `Quota exceeded for quota metric 'Queries' and limit 'Queries per day' of service 'books.googleapis.com' for consumer 'project_number:624717413613'`

That is the Google Books API **answering**. The container reached `books.googleapis.com`, was authenticated as the anonymous shared project, and was refused only on that shared project's per-day quota — a limit that a free API key removes by moving the caller to its own project. **A compliant, official, first-party book-data API is reachable from the exact container the Brain declared incapable of obtaining book-market data.** [PRIMARY — runtime test, reproducible]

This alone falsifies the sentence as written. The Brain tested `kdp.amazon.com`, found `000`, and generalised to "no compliant autonomous route." The generalisation was never tested and is wrong: the allowlist is narrow but not empty, and it contains at least one book-data API.

### 3.2 What Google Books actually answers — and what it does not

Grading honestly, because confirming one attribute confirms nothing else.

Google Books `volumes.list` needs **no authorization for public volume data** (a key is for quota and reporting only), and returns a volume list plus `totalItems`. [PRIMARY — `developers.google.com/books/docs/v1/using`]

Map that against the Brain's own three stated niche-verification inputs (`M-C_CLOSEOUT.md` §3):

| Input the Brain said it needed | Obtainable via Google Books? |
|---|---|
| **Most recent first-page publish date** ("2+ years old ⇒ demand without active publishers") | **Yes** — publication dates are core volume metadata |
| **Competition depth** for a keyword | **Partly** — `totalItems` gives a corpus-wide count; not Amazon's first-page ordering |
| **Review counts** | **No** — Amazon review counts are Amazon-specific |
| **BSR** | **No** |

So this route delivers **one of the Brain's two decision heuristics outright**, plus a competition-depth proxy, and delivers neither BSR nor Amazon review counts. That is a partial, not total, refutation — and I state it as partial. But the Brain's claim was **universal** ("any compliant autonomous route"), and a universal claim falls to one counterexample.

### 3.3 The other candidate routes, graded

| Route | What it actually exposes | Eligibility / cost | Grade | Verdict on the route |
|---|---|---|---|---|
| **Amazon PA-API 5.0** | **BSR directly** — `BrowseNodeInfo.WebsiteSalesRank` (website rank) and per-node `BrowseNodes.SalesRank` | Requires an Associates account **with qualifying referral sales**; access revoked after 30 consecutive days without qualified sales | PRIMARY | **BSR is officially exposed, not scrape-only** — but gated behind sales the account does not have. A real chicken-and-egg |
| **Amazon Creators API** | Successor to PA-API. **PA-API was deprecated 2026-05-15 and no longer accepts new customers** | Documented as **10 qualifying sales in the past 30 days** | PRIMARY | Route exists under a new name; the Brain checked neither the old nor the new one |
| **Keepa API** | Vendor docs state price histories, product data, offers, deals, **best seller lists**, category lookup, product search, token-priced | Paid subscription. **No Associates-sales gate** | PRIMARY (product exists & scope) / UNVERIFIED (whether review counts are a field; whether the vendor's own collection is Amazon-ToS-compliant) | Genuine candidate. `api.keepa.com` is blocked from this container — but this is precisely what the **GitHub Actions** path in preflight §6a exists to solve |
| **Rainforest API (Traject Data)** | Bestsellers endpoint, review data (star ratings, counts, text), search, category pages; free trial of 100 requests | Paid, no eligibility gate | PRIMARY (capability) / UNVERIFIED (compliance of vendor-side collection) | Candidate, with an honest compliance question the Brain would have been right to raise — but never raised, because it never looked |
| **Google Books API** | Titles, publish dates, publishers, categories, `totalItems` | Free, no auth for public data | PRIMARY | **Reachable from this container today.** See §3.1 |
| **KDP's own reports** | Dashboard / Sales & Royalties / Historical / Month-to-Date — **the account holder's own orders, royalties, KENP reads only** | Account holder | PRIMARY | **Supports the Brain.** KDP gives you *your* numbers, not competitors'. This sub-route is genuinely a dead end |
| **OpenLibrary / ISBNdb / WorldCat** | Bibliographic | — | UNVERIFIED | `openlibrary.org` returns `000` from this container. Not checked further |
| **Published bestseller lists (e.g. NYT Books API)** | — | — | **UNVERIFIED** | Search returned no primary links. **I record no finding.** A tool returning nothing is not evidence of absence |

### 3.4 The GitHub Actions dismissal

Preflight §6a records GitHub Actions as **AVAILABLE — UNUSED** with runner internet access, then dismisses it because "the marketplace data I actually lack is barred by platform terms, not by network reach."

That reasoning fails on the evidence above. The data is **not** uniformly barred by platform terms:

- Google Books is an official public API with no bar at all.
- Amazon's own PA-API/Creators API **publishes BSR as a documented field** — Amazon is not withholding rank data by policy, it is gating it on Associates sales.
- Keepa and Rainforest are commercial products sold openly for this purpose.

"Scraping is barred" is true. "No compliant route exists" does not follow from it, and §6a is where the two were merged into one sentence. The dismissal is a **category error**, and it is the single load-bearing sentence in the whole kill.

### 3.5 What survives of the Brain's capability claim

I will not overstate this. Two parts of the Brain's position survive intact:

1. **Amazon-specific BSR and review counts are genuinely hard for this project right now.** PA-API/Creators require qualifying sales the account cannot have; `api.keepa.com` and Amazon hosts are blocked from the container; KDP's own reports show only your own sales. That is a real, non-trivial constraint, honestly identified.
2. **Scraping is correctly ruled out** and should stay ruled out.

What does **not** survive is the leap from those facts to "no compliant autonomous route exists, therefore the mission is dead." The correct statement is: *"the most convenient route is blocked; three unblocked-or-purchasable routes exist and were not examined; one of them answers from this container today."* That is a **data-acquisition task**, which is exactly what the brief says collapses the capability-bound kill.

---

## 4. CHARGE 3 — The discovery heuristics

### 4.1 "New titles get almost no organic visibility" — the kill's evidential core

The closeout §2 quotes: *"A brand new book with zero reviews gets almost no organic visibility… it won't even surface in an Amazon search. The algorithm rewards momentum, not existence."* [SECONDARY, uncited]

I hunted counter-evidence as instructed. What I found does **not** vindicate the naive "honeymoon boost" story either — I report it as it is.

**(i) Amazon's own documentation contradicts the strong form.** [PRIMARY — `kdp.amazon.com/en_US/help/topic/G201648140`]
KDP's Sales Ranking page states that rank "takes previous sales into account, as well as recent sales," and — decisively — that **"one sale of a very popular book may not influence its rank much at all, but one sale of a lower volume book may significantly improve that book's rank."**

That is Amazon stating that in a low-volume category, *minimal* sales move rank materially. It is the exact mechanism a low-competition niche strategy relies on, confirmed by the platform, and it is inconsistent with an algorithm that "rewards momentum, not existence" in the absolute sense the kill needs.

**(ii) New titles have dedicated ranked surfaces.** [PRIMARY — `amazon.com/gp/new-releases/books` and per-category paths]
Amazon operates New Releases lists ("the best-selling new & future releases in X") across the book taxonomy — `/gp/new-releases/books`, `/books/10134` (Genre Literature & Fiction), `/digital-text/154606011` (Kindle eBooks), and so on. On these surfaces a new title competes against a **new-release cohort**, not the all-time backlist. That is a structural advantage for exactly the configuration the Brain declared hopeless. Related: the **#1 New Release badge** is awarded to the top-selling new release in a category within the first 90 days, with the definition of "new release" varying by category and the award updated hourly [SECONDARY — Amazon Seller Forums, user-generated]. Because Amazon's book taxonomy is very fine-grained, this is reachable at low absolute sales in a narrow category — a standard launch tactic, and an L4/L5 remedy.

**(iii) The honeymoon period: the counter-hypothesis is real but weaker than the brief hoped — and it still contradicts the kill.** [SECONDARY]
I searched specifically for the new-release window. The honest state of the evidence is that the *automatic 30-day visibility boost* is **not supported** — several seller-side sources call it a myth outright. The corrected account is a **cold-start sampling window**: Amazon serves a new listing impressions in order to test shopper response, then sustains or withdraws them based on conversion. Aggregate data from Helium 10 and Jungle Scout is cited for a ~30–45 day evaluation phase.

I will not overstate this, so note two limits: these sources are Amazon-seller-general (largely physical products), **not** book-specific, and the transfer to KDP is unverified; and "conditional sampling" is a long way from "new books get discovered."

But the point that matters is this: **C-0's metric is impressions.** The cold-start account says new listings *do* receive sampled impressions. The Brain's evidence says a new title "won't even surface." Those are direct contradictions **at exactly the metric the pre-committed experiment was designed to measure** — and they are the same grade of source. The Brain adopted one side of a contested secondary literature, without searching for the other side, and killed a mission on it.

### 4.2 "First page averaging under ~100 ratings ⇒ winnable" — DOWNGRADE TO FOLKLORE

The heuristic is real in the sense that it is widely repeated. It is not real in the sense of being calibrated.

Searching the practitioner literature returns the threshold in mutually inconsistent forms — "under 100 reviews," "fewer than 2000 reviews on average," "50–200 reviews each," "BSR above 50,000," "fewer than 10,000 search results" — spanning **more than an order of magnitude** for the same decision. No primary source, no controlled study, no published hit-rate. And the sources are overwhelmingly content marketing for the niche-research tools (BookBeam, Publisher Rocket, Seller Sprite) that the article then recommends the reader buy. That is a conflict of interest on top of the absence of evidence.

**Grade: [SECONDARY, uncalibrated, vendor-conflicted].** Not decision-grade.

### 4.3 "Most recent first-page publish date 2+ years old ⇒ demand without active publishers" — SIGN CONTESTED, DIRECT COUNTEREXAMPLE

This is the sharpest finding of Charge 3. The **same class of source** the Brain drew the heuristic from asserts the **opposite sign**:

- The good demand signal is described as *ten successful books in the niche published **within** the last 2 years*;
- and the desirable first page is *top-10 titles published within the last 2–3 years*;
- with the explicit statement that *"the lack of recent titles on the first page combined with older publication dates would suggest **declining demand or a shifting market — the opposite of what you'd want**."*

The Brain read an aged first page as *opportunity*. This literature reads the same observation as *a dying niche*. Both are secondary, neither is evidenced. **A heuristic whose sign is unresolved within its own source literature is not a heuristic; it is a narrative attached to a coin flip.**

### 4.4 The consequence for the kill — this is the part that matters

The kill's chain was: *niche verification requires data → we cannot get the data → selection is random → kill.*

Charge 3 breaks the chain one link earlier than Charge 2 does. Even granting for argument that the data were unobtainable, the thresholds that data would have been compared against are:

- uncalibrated (§4.2), and
- of **contested direction** (§4.3).

So possessing the data would not have converted "a coin flip into a screened bet," as the closeout §7 claims. It would have converted a coin flip into a coin flip with numbers next to it. The Brain killed a mission for lack of an input whose decision rule it had never validated — and graded the rule `[R]` (researched) rather than as the vendor-marketing folklore it is.

### 4.5 A capability finding that emerged from Charge 3

`KDP Book Trends Data` [PRIMARY — `kdp.amazon.com/en_US/help/topic/G3WC49TM63DUM4VW`] is an aggregate count of customers who engaged with a title over the most recent 30 days (via categories, Look Inside, customer reviews, search results), updated daily — and it is **displayed in search results and on detail pages**, i.e. it is a public demand signal on *other people's* titles, not merely a private report on your own. That is a competition/demand proxy that requires neither BSR nor review counts. It goes to Charge 2's question "whether KDP itself surfaces category/competition data," and the answer is: **partly yes**, and the Brain did not look.

---

## 5. Verdict

*(pending)*

---

## 6. INCOMPLETE — what remains

*(pending)*
