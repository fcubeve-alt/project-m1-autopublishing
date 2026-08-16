# DEVELOPMENT_ENVIRONMENT_PREFLIGHT

Required by `Project_M_AI_Development_Environment_Preflight_Skills_Spec_v1.1` §2.
Produced by Session S-002, 2026-08-16. **No capability was installed. This is inspection and
recommendation only**, per Preflight §0.

---

## 1. Current agent and execution environment

| Item | Value |
|---|---|
| Coding agent | Claude Code, Claude Agent SDK harness |
| Model | `claude-opus-5` |
| Execution | managed remote container (Claude Code on the web), ephemeral |
| Platform | Linux 6.18.5, working dir `/home/user/project-m1-autopublishing` |
| Persistence | **none outside git** — container reclaimed after inactivity |
| Repo | `fcubeve-alt/project-m1-autopublishing`, branch `claude/session-handoff-reconstruction-dl6gwa` |
| Network | egress via agent proxy, restrictive policy (see §3) |

The ephemeral container is the mechanical reason S-001's work vanished: anything not
committed is destroyed. R10 exists to counter this.

---

## 2. Existing capabilities — inspected, not assumed

| Capability | Present | Notes |
|---|---|---|
| Web search | ✅ | verified with live queries returning Aug-2026 results |
| Web fetch — developer domains | ✅ | github.com verified |
| Web fetch — general web | ❌ | blocked by egress policy |
| Browser automation | ⚠️ present, **unusable for this project** | Chromium + Playwright preinstalled at `/opt/pw-browsers`, but target sites are egress-blocked |
| Git | ✅ | full local git |
| GitHub API | ✅ | GitHub MCP server (issues, PRs, contents, actions) |
| Scheduling / self-wake | ✅ | Routines / triggers / `send_later` available |
| Subagents | ✅ | available; not used — no fan-out need yet |
| Persistent project memory | ❌ | **no cross-session memory exists.** Git is currently the only durable memory |
| Structured task management | ⚠️ | ephemeral task tooling exists; durable state is `STATE/TASK_LEDGER.md` |
| Document handling | ✅ | docx/pdf/xlsx/pptx skills available; used to read the two specs |
| CI / test tooling | ❌ | none configured; nothing to test yet (no code, correctly) |

---

## 3. Network egress — the binding constraint

Measured, not assumed:

| Target | Method | Result |
|---|---|---|
| vocal.media | WebFetch | `EGRESS_BLOCKED` |
| help.medium.com | WebFetch | `EGRESS_BLOCKED` |
| www.royalroad.com | WebFetch | `EGRESS_BLOCKED` |
| substack.com | WebFetch | `EGRESS_BLOCKED` |
| vocal.media / medium / royalroad | curl | `CONNECT tunnel failed, response 403` |
| github.com | WebFetch | ✅ 200 |
| proxy status endpoint | curl | `enabled: true, selective: false, toolScoped: false` |

**Interpretation:** the environment runs a restrictive network policy permitting developer
infrastructure (GitHub, package registries) and the search backend, but not the open web. It
is an environment configured for *writing software*, while this project's Phase 0 is
*researching commercial platforms*.

**Consequence for the mission spec:** M1 §1 requires verifying "current official rules,
current monetization, current payment methods, AI-content policy…" — all of which live on
pages this environment cannot open. Search snippets can *quote* official pages, but that is
tier T2 evidence, not T1.

Do **not** work around this by disabling TLS verification or unsetting the proxy. The correct
paths are in §5.

---

## 4. Capability assessment (Preflight §3–§4 categories)

Format: recommendation · gap solved · risk.

### 4.1 Persistent project memory — `PROJECT-SPECIFIC`, defer
Real gap (no cross-session memory), but git already covers it and is auditable, exportable,
diffable and free. Preflight §3.1 says memory must not be the source of truth for git history
or spec. **Recommendation:** keep `STATE/` in git as memory. Reconsider only if repeated
repository re-scanning becomes a measured cost. *No install.*

### 4.2 Playwright browser testing — `REJECT for now`
P0 in the spec, but that presumes a product with user journeys. There is no code and no UI.
Already installed anyway. **Recommendation:** revisit when a Money OS surface exists.
Note it does **not** solve §3 — the egress block applies to the browser too.

### 4.3 Taskmaster AI / structured task management — `REJECT`
The spec flags it P1 *with security review required*, citing 2026 path/file-boundary and
credential issues. A markdown ledger in git provides the needed discipline at zero risk and
zero credential exposure. Preflight §3.3 explicitly says to avoid duplication when the
existing environment already gives equivalent discipline. **Recommendation:** do not install.

### 4.4 Firecrawl / web research and extraction — `ENABLE — highest-value candidate, Owner decision`
This directly addresses HG-01, the project's top blocker. It would restore official-source
verification and give structured Markdown/JSON extraction with provenance, which R2 requires.

Owner must review before enabling:
- **License:** AGPL-3.0 self-host, plus a hosted service — AGPL has real implications if
  self-hosted and integrated into a product; hosted service avoids that but sends target URLs
  to a third party.
- **Cost:** hosted usage is metered; caching required (Preflight §3.4).
- **Data exposure:** only public platform policy URLs would be sent — no credentials, no
  private data. That keeps it within the §3.4 prohibition.
- **Network:** it still needs egress. **If the environment's policy blocks the crawler's
  endpoint too, this does not help** — so option (a) below must be checked first.

### 4.5 Context7 / current documentation retrieval — `OPTIONAL, defer`
MIT, low risk, genuinely useful — but it serves *code library* documentation, and there is no
code. **Recommendation:** revisit at first implementation task.

### 4.6 Agent-Reach — `UNKNOWN — cannot assess`
Preflight §4.1 rates it P0 for autonomous business research. This session could not retrieve
current, verifiable information about it, and R2 forbids describing it from memory.
**Recommendation:** `UNKNOWN`; assess when official-source access exists. Do not install
anything matching the name without verifying the actual upstream repository — Preflight §3.1
warns that a capability category is not permission to install a similarly-named repo.

---

## 5. Recommended resolution for HG-01, in order of preference

1. **Widen the environment network policy** to allow the specific research domains needed.
   Cheapest, no new dependency, no license or data-flow question, no third party. This is the
   Reuse answer and should be tried first.
2. **Approve a research capability** (§4.4) if policy cannot be widened — but confirm its own
   egress works in this environment before committing to it.
3. **Proceed on T2/T3 evidence with the risk recorded** — acceptable only for candidate
   discovery, explicitly *not* for Top-5 selection, and every affected claim must stay tagged
   with its tier.

## 6. Rollback plan

Nothing was installed, so rollback is `git revert` of documentation commits. If a research
capability is later approved: keep it behind an adapter so the research layer is swappable
(Preflight §1 — reject dependencies that create architectural lock-in), pin the version,
route all fetches through one module, and keep raw retrieved evidence in `research/` so the
evidence base survives removal of the tool.

## 7. Smoke-test plan for any enabled capability

A capability counts as working only when it fetches a **named official policy page**
(e.g. Vocal's payout page, Medium's Partner Program page), returns text containing the
expected figures, and records URL + retrieval timestamp into the evidence log — thereby
promoting at least one T2 row to T1. Anything less does not solve HG-01.
