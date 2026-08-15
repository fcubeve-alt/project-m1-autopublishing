# A0001 — Publication Package

**Status:** Draft v0.9 — awaiting Human Editorial Gate (H2)
**Prepared:** 2026-08-15

The Owner should not need to author anything below. Everything is ready to paste into the KDP upload form.

---

## Listing details

| Field | Value |
|---|---|
| **Title** | The AI Disclosure Handbook |
| **Subtitle** | What Creators and Sellers Must Declare in 2026 |
| **Edition** | August 2026 Edition |
| **Author** | `UNKNOWN` — Owner decides. Real name or a consistent publishing name. See note below |
| **Language** | English |
| **List price** | **$6.99 USD** (70% royalty band, $2.99–$12.99 as of 2026-07-07) → **$4.89 net per sale** |
| **Royalty option** | **70%** |
| **KDP Select** | **NO — do not enroll.** Non-exclusive by decision D0003 |
| **Territories** | All |
| **ISBN** | Not required for Kindle eBooks |
| **DRM** | Recommended: No |

### Note on author name
This is the one metadata field the AI should not decide. It is a personal and reputational choice, and a regulatory-adjacent title benefits from a name the Owner is willing to stand behind — which is also what the EU AI Act's editorial-responsibility provision contemplates. Raised at H2.

---

## AI content disclosure — KDP upload form

**Declare: YES — contains AI-generated content.**

| Component | Declaration |
|---|---|
| **Text** | **AI-generated** |
| **Images** | AI-generated `[if the cover is AI-produced]` / Not AI-generated `[if typographic]` — confirm before upload |
| **Translations** | None |

Per `COMPLIANCE_POLICY.md` §2, we declare AI-generated rather than relying on the AI-assisted carve-out, even though human editorial review occurs. Where the boundary is arguable, we disclose. A book about disclosure that under-discloses would be indefensible.

---

## Categories

Select 2–3 at upload. Suggested, in priority order:

1. Business & Money › Small Business & Entrepreneurship › Home-Based Business
2. Computers & Technology › Business Technology › Software (or nearest AI/technology-in-business category)
3. Business & Money › Business Life › Business Ethics *(or a law/compliance category if a closer fit exists)*

Exact category trees shift and could not be verified from this environment (`kdp.amazon.com` egress-blocked). **Confirm live options at upload and record which were chosen** — category choice is a primary variable in the day-21 discovery diagnosis.

---

## Keywords (7 slots)

1. `AI disclosure rules`
2. `AI content compliance`
3. `EU AI Act Article 50`
4. `Etsy AI policy sellers`
5. `KDP AI generated content`
6. `AI transparency requirements 2026`
7. `AI compliance guide creators`

Deliberately weighted toward **specific, recent, high-intent phrases** rather than broad terms like "artificial intelligence." Broad terms are unwinnable for an unknown title; specific recent phrases are where the recency thesis (D0004) actually cashes out.

---

## Book description

> **Most of what you have read about AI disclosure rules is wrong. Here is what the platforms actually say.**
>
> On 2 August 2026, the EU AI Act's transparency obligations became binding law, carrying penalties of up to €15 million or 3% of global turnover. Platform rules shifted around the same date. If you use AI in commercial work — selling on Etsy, publishing on Amazon, posting to YouTube, writing for money — your obligations changed, and the freely available advice about them does not agree with itself.
>
> While compiling this book, three widely repeated claims turned out to be flatly contradicted by the platforms' own material. One of them — the belief that disclosing AI on YouTube costs you monetisation — is causing creators to take real risk in order to avoid an imaginary one.
>
> **The AI Disclosure Handbook** is a dated, sourced, plain-language reference to what you must actually declare, and where.
>
> Inside:
>
> - The distinction between AI-**generated** and AI-**assisted** that decides most of your obligations — and why it means different things on different platforms
> - A cross-platform decision table you can read in two minutes
> - Platform-by-platform chapters: Amazon KDP, Etsy, YouTube, Medium, Royal Road, and direct sales
> - Why four major platforms organise their rules around four different concepts — how it was made, the seller's role, whether it looks real, and which tier of assistance — so no definition travels
> - The EU AI Act's Article 50 for non-lawyers: which obligations are yours, which belong to your AI tool's provider, the editorial-responsibility carve-out, and the 2 December 2026 deadline
> - The Amazon image metadata requirement almost nobody knows about
> - How to keep a disclosure record that would survive a challenge
> - A documented list of corrections to claims circulating online, each checked against the source
>
> **Every claim carries its effective date and its source**, marked Official, Reported, or Unknown. Where the answer is genuinely unsettled, this book says so instead of guessing — because a compliance guide that pretends to certainty it does not have is worse than no guide at all.
>
> This is not legal advice. It is the reference you read before deciding whether you need any.
>
> **A note on length:** this is a dense reference of roughly 8,000 words — about 40 pages — not a padded business book. It is built to be looked things up in, and priced accordingly.
>
> *August 2026 Edition. Compiled 15 August 2026.*

---

## Cover — PRODUCED ✅

**File:** `cover.png` (1600×2560, Kindle's recommended 1:1.6 ratio)
**Source:** `make_cover.py` — regenerate after the author name is set
**Thumbnail check:** `cover_thumbnail_check.png` (160×256). Title and the gold **AUGUST 2026 EDITION** block both remain legible at Amazon search-result size.

**Design rationale.** The cover states the book's actual differentiator rather than asserting authority it has not earned: the evidence-grade key (`[Official]` / `[Reported]` / `[Unknown]`) appears on the front, and the edition date sits in a high-contrast gold block sized to survive thumbnail scaling. A buyer can verify that promise in the free sample before paying — which is the mechanism that makes the accountability claim credible (`A0001_BUYER_INTENT.md` §3b).

**Compliance:** no photorealistic people (avoids Amazon's `contains-synthetic-performer` IPTC requirement entirely), no brand marks or platform logos, no purchased or templated design assets, no artist-name prompting. Typography is DejaVu (free/open licence).

**Outstanding:** `AUTHOR NAME` is a placeholder — set `AUTHOR_NAME` and re-run `make_cover.py` once the Owner decides (H2).

### Original brief (retained for reference)

**Design:** original typographic design. No purchased or templated design, no stock layout.
**Content:** title, subtitle, edition date prominent, author name.
**Prohibited:** photorealistic AI-generated people (would trigger the `contains-synthetic-performer` IPTC requirement); platform logos, brand marks or trade dress; any "in the style of" prompting against a named living artist.
**Requirement:** the **August 2026 Edition** date must be legible at thumbnail size. Recency is the product's core differentiator; if a buyer cannot see the date in search results, the differentiator is invisible at exactly the moment it matters.

---

## Pre-publication checklist

- [ ] Human Editorial Gate (H2) — APPROVE / REVISE / REJECT
- [ ] Author name decided
- [ ] All sources re-verified within 48h of upload *(critical — this is a recency product; a stale claim at launch destroys the premise)*
- [ ] Compliance pass against `COMPLIANCE_POLICY.md`
- [x] **Cover produced** — `cover.png`, thumbnail-verified
- [ ] Author name set in `make_cover.py`, cover regenerated
- [ ] Manuscript converted to Kindle format
- [ ] KDP account + tax interview complete (H1)
- [ ] AI disclosure set correctly at upload
- [ ] KDP Select **not** enrolled
- [ ] Categories chosen and **recorded** for later diagnosis
- [ ] Publish (H3)
