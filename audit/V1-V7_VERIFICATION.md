# V1–V7 — Verification of the A-001 Auditor's External Claims

**Run:** 2026-08-16 · **Channel:** `WebSearch` with `allowed_domains` (per R1/R2 — `WebFetch` remains unusable for platform domains)
**Discharges:** `SESSION_HANDOFF.md` §6 and §8 item 3.

Per **Charter §6.2** and **R15a**, these claims were verified individually. They originated
from the A-001 auditor and were held as `PENDING VERIFICATION` — not adopted as fact. The
A-001 rejection never depended on them; it rested on an internally-confirmed contradiction.

---

## Source-grading note — a trap specific to this research

**A `vocal.media` URL is not automatically a primary source.** Vocal hosts user-written
articles, so `vocal.media/journal/…`, `/writers/…`, `/lifehack/…`, `/01/…` are *user content
published on the platform*, carrying no more authority than any blog. Only `vocal.media/resources/…`
and `help.vocal.media/…` are Vocal's own documentation.

The same applies to `simily.co/all-stories/…` and `forums.tapas.io`. Grades below reflect
this distinction. Restricting a search by domain constrains *who hosts* the page, not *who
wrote* it — this is R15a in a new form and should be treated as a standing rule.

---

## Results

| # | Claim | Verdict |
|---|---|---|
| **V1** | Vocal free tier pays ~$3.80/1k reads | ✅ **CONFIRMED** |
| **V2** | Simily live, paying ~$0.02/unique view | ✅ **CONFIRMED** (one caveat) |
| **V3** | Tapas banned AI since Jan 2023; premium gate 2,000 not 1,000 | ⚠️ **SPLIT — date confirmed, gate claim false (both parties wrong)** |
| **V4** | Ream Stories permits AI | ✅ **CONFIRMED — provisional** |
| **V5** | Pratilipi: ~10M readers, scale, AI policy | ⚠️ **PARTIAL — platform confirmed, AI policy still `UNKNOWN`** |
| **V6** | Vocal payout rail is Stripe; whether a hard block | ✅ **CONFIRMED — and it is a hard block, for Vocal only** |
| **V7** | Listverse pays $100/list via PayPal | ✅ **CONFIRMED — with a second rail the claim omitted** |

---

### V1 — Vocal free-tier read earnings · ✅ CONFIRMED

**Standard members earn ~$3.80 per 1,000 reads; Vocal+ ~$6.00 per 1,000** (Vocal+ $9.99/mo).
Source: `vocal.media/resources/step-6-maximize-your-earnings` and related official resource
pages. **Primary.**

The withdrawn closeout's claim — *"read earnings are Vocal+ only"* — is **definitively false**,
now confirmed externally as well as internally. Vocal's free-tier economics are **~3× better**
than the withdrawn text asserted: **~26,300 reads to net $100 at the standard rate**, not the
"16,700 reads/mo" figure the closeout paired with a Vocal+-only premise.

### V2 — Simily liveness and rate · ✅ CONFIRMED (caveat)

- **Rate: $20 per 1,000 reads**, stated on `simily.co`. The auditor's "~$0.02 per unique view"
  is the **same figure** expressed per-view. Both are right.
- **Payout: $10 minimum, processed via Tipalti** — *not* Stripe. See the cross-cutting finding.
- **Reads must come from subscribed members** to earn (Medium-like), so headline rate ≠ realised rate.
- **Liveness:** payments portal, contests, community guidelines, ToS and author application all
  live; a 2026 PitchBook company profile exists; 2025–2026 third-party references continue.

⚠️ **Caveat:** the root `simily.co/` page returns the title *"Under construction."* Sub-pages
are live and coherent, so this reads as a landing-page artifact rather than a dead platform —
but it is **not** fully resolved and should be re-checked directly when egress permits.

**$20/1k is ~5.3× Vocal's standard rate — 5,000 reads to $100 vs ~26,300.** This is the
single most economically significant number recovered by the whole A-001/V-series exercise,
and it was left unresolved after being self-identified as decisive. That negligence is exactly
what A-001 caught.

### V3 — Tapas · ⚠️ SPLIT VERDICT

**Date: CONFIRMED, and stronger than claimed.** As of **23 January 2023**, AI-generated
content is not allowed on Tapas — *"including comic and novel episodes, covers and banners… not
allowed in comics or novels in any capacity, including, but not limited to, covers, banners,
and text."* The ban covers **prose, not merely artwork**, despite the copyright rationale
being framed around images. Source: `help.tapas.io` Content and Community Guidelines and
`tapas.io/newsfeed/224`. **Primary.**

**Subscriber gate: BOTH PARTIES WRONG.** There is **no minimum subscriber count** for Premium
consideration — *"if you are on Tapas, there's no minimum subscriber count requirement."*
The Brain recorded a 1,000-subscriber gate; the auditor "corrected" it to 2,000. Neither
exists. **Charter §6.2 is vindicated in the most direct way available: the auditor was wrong,
and deferring to it would have imported a fresh error while feeling like a correction.**

⛔ **A third finding, unprompted:** `PROJECT_STATE.md` §5 records Tapas as *"OPEN with mandatory
tag (from Mar 2026)."* **No evidence of any March 2026 tagging policy was found**, and it is
contradicted by a standing ban documented since January 2023. That entry is marked
**UNSUPPORTED**. It sits inside already-withdrawn text, so nothing downstream depends on it —
but it must not be carried forward if §5 is ever mined for salvage.

### V4 — Ream Stories permits AI · ✅ CONFIRMED (provisional)

A dedicated help article exists: *"Can I Post AI Art and Stories Written With AI on Ream?"*
(`help.reamstories.com/article/78`), and the retrieved text states that **regardless of an
author's use of AI, all content must abide by Ream's Content and Community Guidelines** — a
permissive, conditions-attached stance rather than a prohibition.

Separately confirmed: Ream contractually **prohibits use of author content for AI training**.

**Provisional** because only a partial extract was retrieved, not the full article. The
disposition (permitted-with-conditions) is clear; the exact conditions are not.

### V5 — Pratilipi · ⚠️ PARTIAL

**Platform and monetisation: CONFIRMED.** Multiple official mechanisms on
`english.pratilipi.com`: premium series, locked parts, coin unlocks, Superfan subscriptions,
virtual gifting (stickers cashed out). Concrete splits — of a ₹25 subscription, **42% to the
writer**, 28% Pratilipi, 30% payment platform; **36% of coin value** on unlocks. Eligibility
runs through a **Golden Badge**, one requirement being **200 followers**.

**AI policy: still `UNKNOWN`.** The only AI reference retrieved concerns Pratilipi using AI
for *translation into 20 languages* — which says nothing about whether AI-*authored* submissions
are permitted. Per R1, this `UNKNOWN` is **not** a negative verdict and Pratilipi stays
`UNRATED`, held open. The "~10M readers" scale figure was also not confirmed.

**This is the coverage gap A-001 identified: zero non-Anglophone-origin platforms had ever
been searched.** One search shows a large, genuinely multi-mechanism monetisation stack.

### V6 — Vocal payout rail · ✅ CONFIRMED (hard block, narrowly)

**Stripe is the only payout method on Vocal.** PayPal, Wise and other rails are not supported.
Stripe covers ~46–47 countries. Creators in unsupported countries **accrue earnings that cannot
be withdrawn**. Source: `vocal.media/resources/connecting-your-stripe-account`, plus a
`help.vocal.media` article on India specifically. **Primary.**

So the closeout was **right that this is a hard block — for Vocal.** Its error was treating it
as a Class-A-wide constraint (see below).

⚠️ **Unresolved discrepancy:** payout minimums are reported inconsistently — $35 standard /
$20 Vocal+ in one place, $20 standard in another. Recorded as `UNKNOWN`; it does not change
any decision at this stage.

### V7 — Listverse · ✅ CONFIRMED (plus an omission)

**$100 per accepted list, paid via PayPal *or Bitcoin*, in full minus PayPal fees, within 30
days of acceptance.** Source: `listverse.com` author guide + submission pages. **Primary.**
The auditor's claim named only PayPal; **the Bitcoin rail is a second, materially different
payout route** it omitted.

Requirements: native-level English · originality (not published anywhere) · verifiable
sourcing, no Wikipedia · **direct author submission only — "content submitted by a middle-man
or organization such as a content farm will be rejected."**

**AI policy: not stated.** The author guide's most recent retrieved version dates to 2019 and
predates the issue. The content-farm prohibition and originality clause are the live compliance
risk, not a named AI rule. Recorded `UNKNOWN`, not inferred either way.

---

## Cross-cutting finding — the payout-rail objection does not generalise

The withdrawn closeout treated **Stripe dependence as a Class-A-wide hard block**. The rails
are in fact platform-specific:

| Platform | Payout rail | Minimum |
|---|---|---|
| Vocal | **Stripe only** — ~46–47 countries, no alternative | $20/$35 (disputed) |
| Simily | **Tipalti** | $10 |
| Listverse | **PayPal or Bitcoin** | n/a — per accepted piece |
| Pratilipi | INR / in-platform, Google as payment platform | `UNKNOWN` |

**Consequence: H1 is not one gate, it is a per-platform question.** A country that fails
Stripe may still clear Tipalti, PayPal or Bitcoin. Generalising Vocal's rail constraint across
the class is the same error shape as R1 — a verified property of one option used as a verdict
on a category.

**This does not resolve H1** — the Owner's country of tax residence remains genuinely unknown
and unguessable (`PROJECT_STATE.md` §7). What changes is that H1 no longer blocks the *class*.
It blocks *Vocal specifically*, and each remaining candidate must be checked against its own rail.

## Consequences for M-A

M-A reopens with materially better economics than the withdrawn text described:

1. **Simily at $20/1k** — 5,000 subscriber-reads to $100, ~5.3× Vocal's standard rate.
2. **Vocal at $3.80/1k free tier** — ~3× better than the withdrawn claim, and no $9.99/mo
   subscription needed to earn at all.
3. **Ream permits AI** with conditions — a live candidate that was never searched.
4. **Pratilipi** — a large non-Anglophone-origin platform with a real monetisation stack,
   AI policy open.
5. **Listverse** — $100/piece on a non-Stripe rail, though the content-farm clause needs care.
6. **Tapas is genuinely closed** — the one place the withdrawn text was directionally right,
   for the wrong reason and with a fabricated subscriber gate.

**None of this reinstates any part of the withdrawn Class A finding** (handoff §10). If Class A
closes again it must close on new evidence with an evidenced R15b checklist attached.

## Residual unknowns — carried forward, not closed

| Item | Status |
|---|---|
| Simily root page "Under construction" | Re-check directly when egress permits |
| Simily AI policy | `UNKNOWN` — guidelines cover ownership/plagiarism, not AI |
| Pratilipi AI policy · reader-scale figure | `UNKNOWN` |
| Ream's exact AI conditions | Partial extract only |
| Listverse AI policy | Unstated; guide predates the issue |
| Vocal payout minimum ($20 vs $35) | Sources disagree |
| Tapas "Mar 2026 mandatory tag" claim | **UNSUPPORTED** — contradicted by the Jan 2023 ban |
