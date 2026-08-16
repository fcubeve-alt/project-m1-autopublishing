# A-002 POST-MORTEM — the M-C capability-bound kill

**Written:** 2026-08-16 · **Required by:** `AUDIT_CHARTER.md` §5, REJECT CONCLUSION protocol —
*"a post-mortem is written identifying which operating rule failed to catch the error, and a new
rule is added."*

---

## 1. What happened

M-C (Class C, retail publishing marketplaces) was killed on 2026-08-15 for 2 searches and 0 words,
recorded as **CAPABILITY-BOUND** — the strongest possible form of closure, because it asserts
impossibility rather than unattractiveness.

Audit A-002 returned **REJECT CONCLUSION**. All three clauses of the kill failed independently.

## 2. Root cause

**The root cause of A-001 was:** *verifying one attribute of a candidate created false confidence
in every other attribute of that candidate.*

**The root cause here is different, and worse:**

> **A tested fact was widened into an untested universal, and the universal was then used to close
> a mission — with no step in between at which the widening was itself checked.**

The tested fact was real: `kdp.amazon.com` returns `000` from this container. The universal was
*"live marketplace data cannot be obtained through any compliant autonomous route."* Those are not
the same claim, and the distance between them was never examined. One counterexample was enough to
destroy the universal, and it was available from inside the same container, in one `curl`.

**The specific logical move was a category error**, preserved verbatim in `docs/DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md`
§6a line 113: *"the marketplace data I actually lack is barred by platform terms, not by network
reach."* This treats **"scraping is barred"** as synonymous with **"no compliant route exists."**
An official, ToS-governed API is not scraping. The sentence is load-bearing for the entire kill,
and it is a definitional confusion, not an evidential gap.

## 3. Which rules failed, and how

| Rule | Should have caught | Why it did not |
|---|---|---|
| **R1** — evidence unavailable ≠ opportunity does not exist | The whole kill | R1 is written about **platforms** ("an option scored on absent evidence must be scored `UNRATED`"). The kill was about a **data input**, so R1 was never felt to apply. The error shape was identical; the vocabulary was not |
| **R2** — capability recovery loop, never downgrade on inference | Clause 2 | R2's ladder was **run and passed** in C1 — it is what discovered GitHub Actions. Then §6a **dismissed its own finding** in the next sentence. R2 mandates *finding* the path; nothing obliged me to *use* what it found |
| **R12** — a blocked action is not a stopped system | Clause 3 | R12 was applied to the *system* (am I idle?) and not to the *mission* (is this family closed?). It stopped one level too high |
| **R13** — a documented constraint not used as a filter is decoration | Clause 1 | Inverted here: the constraint was used as a filter **too aggressively**, on a class it had never been tested against |
| **R14** — negative conclusions require independent audit | — | ✅ **R14 worked.** This is the rule that caught it. It is the reason M-C was `PROVISIONAL` rather than closed, and the reason this document exists |
| **R15** — grades belong to claims, not rows | Charge 3 | R15 was written *after* M-C was killed, so it could not have applied retroactively. Had it existed, the `[R]` grade on the niche heuristics would have been graded per claim and exposed as vendor folklore |

**The honest summary: R14 is the only rule that functioned.** Every other rule either did not apply
in its own vocabulary, or was satisfied at the wrong altitude. The audit function is currently
carrying the entire error-detection load, which is not a stable design.

## 4. Three failures that required no research at all

The most uncomfortable part of the finding. These were visible in our own committed files:

1. **Seven of eight chartered channels were never mentioned.** `M-C_CHARTER.md` §2 charters Amazon
   KDP, Kobo, Apple Books, Google Play Books, Barnes & Noble Press, Draft2Digital, Leanpub and
   Everand. The closeout discusses Amazon. **Channel-level evidence was recorded as a mission-level kill.**
2. **The kill mechanism was substituted between charter and closeout.** The charter's central
   question is **discovery**; *"M-C's mechanism is niche selection"* first appears in the **kill
   document**. The thing that was killed is not the thing that was chartered.
3. **The pre-committed kill criterion never fired.** `M-C_CHARTER.md` §6 required ~0 impressions
   after **two** distinct metadata/category configurations over 30 days. **Zero were run.** The
   experiment design records C-0 as *blocked at H1* — blocked, not falsified.

Point 3 is the sharpest. **Pre-committed kill criteria exist precisely so that a mission cannot be
killed on a feeling.** The criterion was written, then bypassed, and the bypass was invisible
because the kill document was internally coherent.

## 5. The new rule

**R16 — A kill must fire its own trigger, at the level its evidence reaches.** Added to
`OPERATING_RULES.md`.

## 6. What this does not license

The verdict rejects the *reasoning*, not the mission's economics. `M1_OPPORTUNITY_FAMILIES.md` §50
— *open but crowded, median outcome failure, structural dependence on catalogue scale* — is
untouched and may still be right. **M-C may still be a poor use of the next unit of capital.**

Declining it on **economics** is available to the Owner at any time and requires none of the
remediation backlog. What is no longer available is recording it as **impossible**.

## 7. What survives from the killed analysis

Carried forward so the remediation does not re-derive it:

- KDP's own reports genuinely are private to the account holder — no competitor BSR there.
- PA-API / Creators API eligibility genuinely is gated on qualifying referral sales (10 in 30 days
  for Creators; access revoked after 30 consecutive days without). A real chicken-and-egg for an
  account with no audience.
- **Scraping is correctly ruled out and stays ruled out.** `COMPLIANCE_POLICY.md` is not the error.
- Pessimism about the naive zero-promotion configuration is well-founded.

## 8. Verification status of the auditor's own findings

Per **Charter §6.2**, the auditor is not deferred to. Status:

| Finding | Brain verification |
|---|---|
| `googleapis.com` reachable from container | ✅ **Independently retested.** Confirmed reachable — **and more qualified than a bare "reachable"**: anonymous quota is **zero**, so a key is required before data returns. `openlibrary.org` is blocked, so reachability does not generalise. Recorded in preflight §6a |
| Amazon publishes BSR as an API field | ⏳ Unverified by the Brain. **Gap:** whether the post-deprecation Creators API retains it (report §6) |
| Keepa / Rainforest ToS-compliance of *their* collection | ⏳ **Unverified — and it is the strongest ground a rebuilt kill could stand on** |
| Document-internal findings (§4 above) | ✅ **Verified directly against our own committed files.** These need no external source and are the most robust part of the verdict |

**The verdict does not depend on the unverified rows.** It rests on the container-reachable
counterexample plus the document-internal findings, both of which are confirmed.
