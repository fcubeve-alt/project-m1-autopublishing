# AUDIT CHARTER — Independent Decision Auditor

**Established:** 2026-08-15 · **First audit:** M-A (Class A conclusion)

---

## 1. Why this function exists

A negative mission conclusion closes an opportunity family. That decision has an asymmetry that makes it uniquely dangerous:

> **A false positive gets caught by the market. A false negative never gets caught at all.**

If we wrongly pursue a bad opportunity, reality corrects us — we spend, we fail, we learn. If we wrongly *close* a good opportunity, nothing ever contradicts us. The evidence of the mistake is a business that was never built. There is no feedback loop, so the error is permanent and invisible.

**Therefore: negative conclusions require a higher evidential standard than positive ones**, and an independent check before they are acted on.

## 2. Independence requirements

The Auditor must not be the Business Brain re-reading its own work. Independence means:

| Requirement | Implementation |
|---|---|
| **Fresh reasoning context** | Auditor runs as a separate agent with no memory of the Brain's deliberation |
| **No stake in the conclusion** | Auditor is explicitly instructed that its job is not to defend the existing answer |
| **Independent research** | Auditor must run its own searches, not re-read the Brain's |
| **Adversarial mandate** | Auditor is instructed to actively hunt falsifying evidence and counterexamples |
| **Own output** | Auditor writes its own report; the Brain does not edit it |

**The Brain must not pre-argue its case to the Auditor.** The audit brief states the claim neutrally and points at the artifacts; it does not rehearse the reasoning that produced it.

## 3. The two reviews

**Logic Review** — audits the *reasoning*: was the original question answered, was the sample adequate, was policy confused with economics, was existence confused with earnings, was `UNKNOWN` treated as negative, was discovery stopped early, was evidence cherry-picked, were counterexamples sought, did convenience or sunk work contaminate the conclusion.

**Evidence Audit** — audits the *facts*: independent search, an auditable platform matrix with sources and dates, explicit hunting for platforms and creators that would falsify the claim, and a justified sample-size argument.

## 4. Verdicts

| Verdict | Meaning | Consequence |
|---|---|---|
| **PASS** | Evidence sufficient; reasoning sound | Conclusion stands. Restore CONCLUDED |
| **PASS WITH CAVEATS** | Conclusion holds, but with stated limits or residual uncertainty | Conclusion stands **with the caveats written into it** |
| **INSUFFICIENT EVIDENCE** | Conclusion may be right, but is not adequately supported | **Conclusion does NOT stand.** Reopen the specified research |
| **REJECT CONCLUSION** | Evidence contradicts the conclusion | Reopen the mission; the Brain's finding is withdrawn |

**A mission stays `PENDING INDEPENDENT AUDIT` until a verdict is issued.** During that time its conclusion may not be relied on for downstream decisions.

## 5. Pre-committed response protocol

**Written before the verdict is known**, so that my response is a rule rather than a rationalisation. This is the same discipline as pre-committed kill criteria (R7): decide the response while the outcome is still genuinely uncertain.

### If PASS
- Restore M-A to `CONCLUDED`, annotated "independently audited."
- Record the audit as raising confidence, not as vindication.
- **Do not** treat a PASS as licence to relax evidence standards on the next mission.

### If PASS WITH CAVEATS
- Restore `CONCLUDED — WITH CAVEATS`, with each caveat written into `M-A_CLOSEOUT.md` itself, not filed separately where it will be forgotten.
- Any caveat naming an unexamined platform or category goes onto the **watchlist** with a re-check trigger.
- Where a caveat identifies a capability gap, apply R13: specify the cheapest unlock.

### If INSUFFICIENT EVIDENCE
- M-A becomes `REOPENED — EVIDENCE INCOMPLETE`. **The negative conclusion is withdrawn**, not softened.
- The Auditor's list of required work becomes the mission backlog, executed in its priority order.
- The `OUT_OF_SCOPE_REGISTER` and `WATCHLIST` are re-examined for anything filed on the strength of the unsupported conclusion.
- **I do not argue with this verdict.** Insufficient evidence is a statement about my work, not about the market.

### If REJECT CONCLUSION
- M-A reopens fully. The closeout is marked **withdrawn**, not deleted — the error and its cause stay in the record.
- Every downstream decision that leaned on the Class A finding is re-examined, specifically: the M-C charter's premise, M-P's charter, the `SCOPE_INTEGRITY_CHECK` class analysis, and the "economics predicted policy" heuristic in `OPERATING_RULES` R9 — which would be exactly the kind of elegant generalisation that survives because it is satisfying rather than because it is true.
- A post-mortem is written identifying which operating rule failed to catch the error, and a new rule is added.

## 6. Standing rules for the Auditor function

1. **Never audit your own reasoning and call it independent.**
2. **The Auditor may be wrong too.** Its findings are verified against primary sources before being acted on — deference to an auditor is the same failure as deference to a reviewer (governance model, `OPERATING_RULES` §0).
3. **Audit negative conclusions, not just positive ones.** The instinct is to scrutinise spending decisions. The asymmetry in §1 says closures deserve more scrutiny, not less.
4. **The audit does not block unrelated authorised work.** Only decisions that depend on the audited conclusion are held.

## 7. Audit register

| Audit | Subject | Status | Verdict |
|---|---|---|---|
| **A-001** | M-A — "Class A is closed or economically unattractive" | **IN PROGRESS** (opened 2026-08-15) | *pending* |
| **A-002** | M-C — "retail marketplaces are capability-blocked, mission dead" | **IN PROGRESS** (opened 2026-08-15) | *pending* |

## 8. Level discipline (added after A-002 was commissioned)

A-002 exposed a failure mode that A-001's framing did not cover: **a falsification at a narrow level propagating upward into a verdict on the whole enterprise.**

Every future negative conclusion must state **which level** the evidence reaches:

| Level | Claim | Remedy if falsified |
|---|---|---|
| **L1 Market** | A market exists at all | Abandon |
| **L2 Mission** | This mission's economic model can work | Owner scope decision |
| **L3 Channel** | This specific platform works for us | Change channel |
| **L4 Strategy** | This approach to discovery/distribution works | Change strategy |
| **L5 Experiment** | This specific configuration works | Change the experiment |

**Evidence reaches the level it actually tested, and no further.** Since L4/L5 remedies are cheap and abundant, mis-attributing an L5 falsification to L2 does not merely mislabel the finding — it silently discards every remedy that would have worked.

**Self-identified in advance of the audit:** the M-C evidence describes one configuration — *one unknown author, one new title, zero promotion, organic-only* — which is L5. The kill was applied at L2/L3. I do not think that propagation was independently supported, and I have said so in the audit brief rather than waiting to be caught.
