# EVIDENCE_LOG

Provenance for every decision-relevant fact, per R2 and Preflight §3.4 ("track URL, retrieval
time and provenance for decision-relevant facts").

**Retrieval date for all entries below: 2026-08-16 (Session S-002).**
**Retrieval method: Web Search only.** Direct fetch of platform domains was blocked
(HG-01), so **no entry is tier T1.**

---

## Method and its limits

Queries were issued against a search backend that returns result links plus an extracted
summary. The extract sometimes quotes an official source (e.g. `support.substack.com`,
`inkitt.zendesk.com`) — those are recorded as **T2**, because the official page was *not*
opened and verified directly. Everything else is T3 (credible third party) or T4 (SEO
listicle / content-farm / plausibly AI-generated aggregator).

**Known weakness:** several source domains in the writing-monetization niche are themselves
low-quality or AI-generated content farms. Multiple T4 sources agreeing does **not** raise
confidence — they frequently copy one another, which is precisely how two dead platforms
(Kindle Vella, Radish) remain in circulation as live recommendations.

---

## Queries issued

| # | Query | Yield |
|---|---|---|
| 1 | Vocal Media creator payout program 2026 current rules | Vocal economics (T2/T3) |
| 2 | platforms that pay writers for original fiction and stories 2026 revenue share | candidate discovery (T4) |
| 3 | best paying writing platforms 2026 essays articles per view earnings | candidate discovery (T4) |
| 4 | serialized fiction platform writer earnings Royal Road Tapas Radish Inkitt | **Radish shutdown**; Tapas/Inkitt/Royal Road economics (T3) |
| 5 | newsletter subscription platform writers monetization Substack beehiiv Ghost Patreon 2026 payout | fee comparison (T3/T4) |
| 6 | Kindle Vella discontinued shut down Amazon official announcement | **Vella closure + Amazon statement** (T2/T3) |
| 7 | Medium Partner Program 2026 rules changes AI generated content policy earnings | **Medium AI ban** (T2/T3) |
| 8 | paid writing contests short story competitions 2026 cash prizes free entry | contest landscape (T3/T4) |
| 9 | Vocal Media AI generated content policy rules disclosure allowed | **NIL RESULT** — see below |
| 10 | Wattpad Webnovel Inkitt Tapas AI generated content policy 2026 prohibited | per-platform AI stances (T3) |
| 11 | Substack AI policy paid subscriptions Stripe supported countries writers payout | **Stripe country gating** (T2) |
| 12 | Ko-fi Buy Me a Coffee Patreon Ream Stories Laterpress writers payout Payoneer international | tipping fees (T4); nil on Ream/Laterpress/Payoneer |

---

## Facts by tier

### T2 — search extract attributing to an official source

| Fact | Attributed to | Use |
|---|---|---|
| Amazon: *"This was a difficult decision… Kindle Vella hasn't caught on as we'd hoped."* Timeline: announced 2024-10-28, new episodes stopped 2024-12-04, closed 2025-02-26 | Amazon statement, via GeekWire / Amazon customer-service page | Vella marked DEAD |
| Substack paid subscriptions are Stripe-gated; India, Brazil, Indonesia, Mexico, Malaysia, Thailand are exceptions; India requires direct Stripe invite as of 2024-05 | `support.substack.com` | HG-02 basis |
| Medium: AI-generated content not permitted to be paywalled, ineligible for Boost, non-compliance can mean Partner Program removal; undisclosed → Network Only, disclosed → General Distribution | Medium policy, via multiple reports | Medium likely disqualified |
| Inkitt offers an "AI-Assisted Content Label" | `inkitt.zendesk.com` help article | Disclosure-based model |
| Vocal: $3.80/1k views, $6.00/1k reads Vocal+, Vocal+ $9.99/mo, $35/$20 withdrawal minimum, Stripe payout, 600-word prose minimum, English only | `vocal.media` resources pages, via extract | Vocal economics |

### T3 — credible third-party reporting

- Radish Fiction shut down as of December 2025.
- Tapas: 70% ad revenue share; premium contracts carry digital exclusivity during monetization.
- Inkitt: contracted authors up to 100% of subscription revenue after fees; top performers up
  to ~$40k/yr; 6% royalties on ebook/audio adaptations.
- Royal Road: no direct monetization; audience-building platform.
- Wattpad: strongly discourages generative AI; AI editing/outlining/research tools at author
  discretion; Wattys 2026 rubrics reward human creativity.
- Webnovel: expanded AI writing toolkit launched February 2026.
- Substack: 10% fee plus Stripe processing ≈ 13–16% of gross.
- Story Unlikely contest: free entry, $3,000/$1,000/$750 + $250 reprint, ≤7,000 words,
  closing 2026-01-14 (**now stale**).
- Per-piece rates: Longreads from $500/essay and $0.50/word features; Craft $200/$100;
  Zizzle $250/$100; East of the Web $0.05/word; SFWA professional minimum $0.08/word.

### T4 — listicle / content-farm grade, discovery only

beehiiv and Ghost 0% revenue cut with flat monthly fees · Patreon 8–12% · Ko-fi 0%/5% ·
Buy Me a Coffee 5% · Contently $500–2,000 · ClearVoice $0.50/word · Verblio $0.15–0.40/word ·
LA Times travel $200/$350 · The Content Strategist $150–300 · Dreame/GoodNovel coin-unlock.

### T5 — name only, zero evidence

HubPages · NewsBreak creator program · (and any platform added later without a retrieval
record). Verify or drop; do not carry forward as if researched.

---

## Rejected claims

| Claim | Why rejected |
|---|---|
| "Wattpad Trust & Safety confirmed in a **March 2024 internal memo** that automated generation without disclosure was a top-five enforcement priority" | An internal memo is not a public source and cannot be verified. Plausibly fabricated by an AI-generated aggregator page. **Must not be repeated as fact.** |
| Listicle recommendations of Kindle Vella and Radish as live 2026 options | Directly contradicted by T2/T3 closure evidence |
| "FanStory: enter all cash-prize contests **free** with **upgraded membership**" | Self-contradictory as stated; needs verification before use |

---

## Nil results worth recording

- **Query 9 returned nothing about Vocal's AI policy.** The search backend returned YouTube,
  TikTok and Meta AI-disclosure material instead. Since Vocal is the spec's named template
  platform and otherwise the best-documented candidate, this is the **highest-priority
  unknown in the project**. Recorded as `UNKNOWN` per R2 — explicitly *not* inferred from
  other platforms' policies.
- No evidence retrieved for Ream Stories, Laterpress, or Payoneer creator-payout specifics.
- No AI policy retrieved for Substack, Dreame, or GoodNovel.

---

## What would upgrade this log to T1

Open and quote, with retrieval timestamps: Vocal's payout and content-policy pages · Medium's
Partner Program and AI policy pages · Substack's supported-countries page · Webnovel's and
Inkitt's author agreements · Tapas's premium contract terms · each shortlisted contest's
official rules page. All are blocked by HG-01; see `DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md` §5.
