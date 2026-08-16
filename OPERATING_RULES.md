# OPERATING_RULES

Binding rules distilled from the two governing `.docx` specifications. This file is a
**convenience index, not an authority**. Where this file and a `.docx` disagree, the `.docx`
wins.

**Authority order** (from Preflight spec §0):
Project M Master Specification → verified existing repository/code → Capability Specification
→ individual tool defaults/prompts.

---

## R1 — Research before code

- Phase 0 is research and feasibility. **Do not start by coding** (M1 spec §1).
- Do not build a large autonomous publishing stack until the §12 deliverables show a viable
  path (M1 §12).
- For any meaningful new subsystem, produce an architecture decision memo first; answer
  explicitly **Reuse / Extend / Buy / Build** (Preflight §1).
- No Skill/MCP install without reviewing permissions, cost, license, data exposure,
  maintenance and rollback (Preflight §0).

## R2 — Evidence discipline (hardest rule)

- **Unknown must be written `UNKNOWN` and researched. Do not fill gaps with model memory**
  (M1 §2).
- Verify *current* official rules. **Do not rely on old "top writing sites" lists** (M1 §1).
  — Confirmed necessary: such lists currently recommend Kindle Vella and Radish, both dead.
- Record URL, retrieval time and provenance for decision-relevant facts (Preflight §3.4).
- Record evidence freshness/date per platform (M1 §2).

### Evidence tiers used in this repo

| Tier | Meaning | Usable for Top-5 selection? |
|---|---|---|
| **T1** | Official platform page, retrieved and quoted, with date | ✅ yes |
| **T2** | Search extract explicitly attributing a figure to an official source | ⚠️ provisional only |
| **T3** | Credible third-party reporting (trade press, established blog) | ❌ background only |
| **T4** | SEO listicle / content-farm / likely AI-generated aggregator | ❌ candidate discovery only |
| **T5** | Name recalled with **zero** retrieved evidence | ❌ must be verified or dropped |

## R3 — Legality and honesty

Prohibited without exception (M1 §7):
fake identity · false address · borrowed financial accounts · CAPTCHA bypass · policy evasion
· deceptive AI disclosure.

- Escalate only the **minimum** human-bound step (KYC, payment ownership, CAPTCHA, phone
  verification, contractual acceptance).
- If automated publishing is prohibited, prepare the full package for human posting. Lack of
  automation is **not** grounds to abandon a profitable platform.
- Do not expose internal credentials or private data to external crawling services
  (Preflight §3.4).
- Never commit provider API keys to task/config files (Preflight §3.3).

## R4 — Editorial pipeline

Research/Idea → Outline → Draft → Critic/Editor → Rewrite → Originality/Copyright Check →
Platform Compliance Check → AI Disclosure Check → Final Draft.

- AI must self-review **before** asking a human to review.
- **Human Editorial Gate is required before publishing substantive content** (initial mode).
- Gate outcomes: APPROVE → publish where allowed · REVISE → revise and resubmit ·
  REJECT → do not publish, record reason as learning evidence.

## R5 — Content assets and cross-posting

- Treat each work as a reusable asset, but **never assume one work may be cross-posted
  everywhere.** Determine per platform: exclusivity, first-publication requirement,
  previously-published allowance, syndication/canonical rules, contest originality rules.

## R6 — Economics

- Success is **first lawful, attributable external revenue** with low human intervention —
  not "the system published content" (M1 §13).
- Optimize realized economic value, not article count (M1 §9).
- Log **human minutes** at every human-mediated step, so automation can later be justified
  economically (M1 §18).
- Ledger fields: platform · asset ID · cost · human minutes · publication date · reads ·
  engagement · followers · tips · winnings · subscription revenue · affiliate/licensing ·
  payout received · realized net profit · time-to-first-revenue · hypothesis (M1 §9).

## R7 — Architecture constraints (Phase 1)

- **Do NOT make Anthropic API access a required dependency** for the first revenue experiment
  (M1 §14).
- Writer is a **replaceable provider boundary**. Initial provider:
  `CLAUDE_MANUAL_SUBSCRIPTION`. Changing provider must not require redesigning research,
  compliance, publishing, analytics, ledger or iteration logic (M1 §15).
- Writing Jobs must be portable (Markdown/JSON), usable by a human-mediated Claude workflow
  today and an API provider later without changing business logic (M1 §16).
- **Do not build a multi-model tournament before first revenue** (M1 §17).
- **Automation Upgrade Gate** (M1 §19): propose API automation only after (1) a platform path
  is viable, (2) real engagement/revenue signal exists, (3) cost is justified, (4) it
  materially reduces human effort or raises profitable throughput. *First prove the money
  loop, then automate the proven loop.*

## R8 — Mandatory self-iteration

Observe → Research → Hypothesize → Prioritize → Create → Review → Publish → Measure →
Diagnose → Keep/Improve/Kill → Reallocate → Repeat.

The AI must kill low-value paths, scale validated ones, and challenge its own prior
assumptions. **The Owner must not be required to invent the next task** (M1 §10).

## R9 — Capability resolution ladder (when blocked)

1. Use existing local capability → 2. Check Project M Shared Capability Registry →
3. Search current Skills/MCP/API/CLI/SDK/open-source/SaaS →
4. Compare reuse/buy/build (cost, reliability, security, permissions, maintenance) →
5. Prefer a mature reusable solution → 6. Build only if nothing suitable exists →
7. Escalate to Owner **only** for irreducible human authority/actions.

> **Access failure is not research failure.** Seek legitimate alternative access methods and
> current sources.

## R10 — Session continuity (added by S-002)

Not from the specs — added because its absence cost a full session.

- `SESSION_HANDOFF.md` and `STATE/TASK_LEDGER.md` must be **updated and committed before a
  session ends**. Uncommitted state does not exist.
- Every task gets an ID, a status, and — when blocked — a named blocker.
- Never claim a checkpoint that is not reconstructible from committed files.
