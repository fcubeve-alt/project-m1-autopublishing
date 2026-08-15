# DEVELOPMENT ENVIRONMENT PREFLIGHT

**Date:** 2026-08-15
**Required by:** `Project_M_AI_Development_Environment_Preflight_Skills_Spec_v1.1` §2

## 1. Environment inventory

| Item | Value |
|---|---|
| Agent | Claude Code (Claude Agent SDK), remote managed execution environment |
| Container | Ephemeral. Repo cloned fresh at start; **reclaimed after inactivity — uncommitted work is lost** |
| Platform | Linux 6.18.5, primary dir `/home/user/project-m1-autopublishing` |
| Repo | `fcubeve-alt/project-m1-autopublishing`, branch `claude/ai-publishing-business-a3o9om` |
| Working tools | Read/Write/Edit, Bash, Glob, Grep, `WebSearch`, task list, git, GitHub MCP |
| Package registries | Reachable (npm, PyPI, crates, Go proxy — in `noProxy`) |

## 2. Network capability — the decisive finding

**Outbound HTTPS to external hosts is denied by this session's egress policy.**

`WebFetch` returned `EGRESS_BLOCKED` for **every** host attempted:

`kdp.amazon.com` · `help.medium.com` · `policy.medium.com` · `www.royalroad.com` · `vocal.media` · `gumroad.com` · `authorsguild.org` · `en.wikipedia.org`

Proxy status confirms `enabled: true`, `selective: false`, with no listed relay failures — these are policy denials, not TLS or configuration faults. The proxy README states such denials must be reported rather than retried or routed around, and that instruction is being followed. **No attempt was made to circumvent the policy.**

**Consequence:** the entire fetch/crawl/browse capability tier in the Preflight spec is non-executable here.

**Working alternative found:** `WebSearch` with `allowed_domains` scoping does reach and extract from primary sources. Verified against Medium Help Center, KDP Help, Royal Road's official policy blog, Substack Support and beehiiv Support. This is now the documented house research method, and its limitation is recorded honestly: it returns search-engine-mediated extracts, not the full page, so it is weaker than direct retrieval for exhaustive terms review.

**Second-order consequence:** any strategy depending on live marketplace data (Amazon BSR, keyword volume, competitor catalogue depth) is unsupportable in this environment. The content strategy was chosen to depend on regulatory and policy recency instead — evidence `WebSearch` supplies well. See `STRATEGIC_REVIEW.md` §P4.

## 3. Capability evaluations

| Capability | Spec priority | Gap solved | Cost / license | Decision |
|---|---|---|---|---|
| Playwright | P0 | Browser E2E | MIT, free | **REJECT** — cannot reach external hosts; no app under test; brief §7 forbids disallowed account automation |
| Context7 | P0 | Current library docs | MIT | **REJECT** — no code being written |
| Agent-Reach | P0 (research) | Cross-platform reachability | MIT | **REJECT** — its core value is the exact thing egress policy denies |
| Firecrawl | P2 | Structured web extraction | AGPL-3.0 / hosted | **REJECT** — non-functional here; AGPL would additionally need review |
| Persistent memory MCP | P1 | Cross-session continuity | varies | **REJECT — already solved.** The git repo is project-scoped, searchable, exportable, secret-free memory. A second store would split the source of truth |
| Taskmaster AI | P1 | Task discipline | MIT | **REJECT** — duplicates the session task list; spec §3.3 itself warns on duplication and credential/path issues |
| Last30Days EN/CN | P1 | Trend signals | MIT / CN unverified | **REJECT for now** — depends on outbound platform access. Re-evaluate if egress opens |
| PraisonAI | Optional | Multi-agent orchestration | MIT | **REJECT** — architecture theatre for a one-asset business |
| LiveKit Agents | Project-specific | Realtime voice | Apache-2.0 | **NOT APPLICABLE** |
| OpenMontage | Project-specific | Agentic video | AGPLv3 | **DEFER** — Phase 3 at earliest; AGPL needs architecture/legal review |

**Nothing is being installed.** Per Capability Resolution Ladder step 1, existing capabilities cover the actual work.

## 4. Secrets, security, cost

- **Secrets:** none required, none stored, none committed. No API keys, no credentials, no MCP servers added. Owner account credentials never leave the Owner's possession — the AI never holds platform logins.
- **Attack surface:** unchanged. No new dependency, no install script executed, no MCP server enabled.
- **Cost:** **$0.00 committed.** No paid service. Only prospective spend is the $20 Draft2Digital account fee, gated on demonstrated sales (`HUMAN_GATES.md`).
- **Rollback:** trivial — the repository is documents and data. `git revert` is the complete rollback plan.

## 5. Smoke tests performed

| Test | Result |
|---|---|
| `WebSearch` general | ✅ Returns dated 2026 results |
| `WebSearch` + `allowed_domains` against official help centres | ✅ Extracted primary-source policy text from Medium, KDP, Royal Road, Substack, beehiiv |
| `WebFetch` any external host | ❌ `EGRESS_BLOCKED` — 8/8 hosts. Recorded, not circumvented |
| Proxy status endpoint | ✅ `enabled: true`, `selective: false`, no relay failures |
| Git read/write, branch state | ✅ On `claude/ai-publishing-business-a3o9om` |
| `.docx` extraction (stdlib zipfile + ElementTree) | ✅ Both source documents read in full, no dependency added |

## 6. Definition of Done — status

| Criterion | Status |
|---|---|
| Environment inventory exists | ✅ |
| All capability categories evaluated | ✅ All 10 |
| Duplicate tools rejected | ✅ Memory MCP and Taskmaster rejected as duplicates |
| Permissions/costs/licenses/rollback documented | ✅ |
| Secrets strategy defined | ✅ No secrets required or stored |
| Install/config reproducible | ✅ Trivially — nothing installed |
| Smoke tests prove enabled capabilities work | ✅ |
| Master Spec remains highest authority | ✅ |

## 7. Recommendation to the Owner

The Preflight spec was written for an environment with open outbound access. **This environment does not have one, and that gap is the most consequential technical fact in the project.** It is not a blocker for Cycle 1 — the strategy was chosen to fit the available evidence channel — but it does mean:

1. Real-time marketplace intelligence (rank, keyword, competitor depth) is unobtainable here.
2. Automated source-monitoring for the re-issue cadence — the natural Phase-2 build — is impossible until egress opens.
3. If this business scales, an environment with a defined allow-list (Amazon, official policy domains, the chosen sales rails) would be the highest-leverage infrastructure change available.

**No action is requested now.** Recorded so the constraint is visible when it starts costing money rather than being discovered again later.
