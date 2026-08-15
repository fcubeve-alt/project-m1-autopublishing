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

## 2. Network capability — corrected 2026-08-15 after a direct test

**Earlier claim (WITHDRAWN):** "Outbound HTTPS to external hosts is denied by this session's egress policy."

That was **inferred from eight `WebFetch` failures and it was wrong.** A Reviewer challenged it; a direct `curl` test settled it. Egress is an **allowlist**, not a blanket block:

| Host | Result |
|---|---|
| `api.github.com` | **200 — reachable** |
| `raw.githubusercontent.com` | **301 — reachable** |
| `pypi.org` | **200 — reachable** |
| `registry.npmjs.org` | **200 — reachable** |
| `www.google.com` | 000 — blocked |
| `kdp.amazon.com` | 000 — blocked |
| `vocal.media` | 000 — blocked |
| `api.firecrawl.dev` | 000 — blocked |

**Corrected finding:** GitHub and the package registries are reachable; general web hosts are not. `WebFetch` fails on all general web hosts, and `WebSearch` (which routes outside this container) remains the working research channel.

**What this changes for the capability review:**

- **Firecrawl and Agent-Reach remain correctly REJECTED**, but for the accurate reason: `api.firecrawl.dev` is unreachable, so a *hosted* crawler genuinely cannot be called from this container. The earlier reasoning ("everything is blocked") happened to reach the right verdict from a false premise, which is not the same as being right.
- **A capability I had missed now exists: GitHub Actions.** GitHub is fully reachable, and Actions runners execute on GitHub's infrastructure with unrestricted internet access. That is a legitimate remote execution path for research or monitoring — not a circumvention of any security control, simply a different machine doing the fetching. Recorded as **AVAILABLE — UNUSED** (see §7).
- **MCP servers do not share the container's network path.** The GitHub MCP server functioned normally. Any future remote MCP research server would need testing on its own terms rather than assuming the container's limits apply.

**Process lesson, now binding as `OPERATING_RULES.md` R2:** never characterise a capability limit from a sample of failures. One `curl` loop settles what a paragraph of inference cannot, and an inferred limit that goes untested will propagate into every document built on it — as this one did.

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

## 6a. Capability Recovery Audit (2026-08-15)

Required by `OPERATING_RULES.md` R2. Every verdict marked **TESTED** or **INFERRED**.

| Capability | Verdict | Basis |
|---|---|---|
| `WebFetch` to general web hosts | **UNAVAILABLE** | **TESTED** — 8/8 `EGRESS_BLOCKED` |
| `WebSearch` (incl. `allowed_domains`) | **AVAILABLE — primary research channel** | **TESTED** — verified against 10+ official domains |
| Direct HTTPS to GitHub | **AVAILABLE** | **TESTED** — `curl` 200/301 |
| Direct HTTPS to package registries | **AVAILABLE** | **TESTED** — `curl` 200 |
| Hosted crawler APIs (Firecrawl class) | **UNAVAILABLE** | **TESTED** — `api.firecrawl.dev` 000 |
| Agent-Reach | **UNAVAILABLE** | **INFERRED** — runs in-container over blocked egress. Not separately tested; the inference is narrow and rests on a tested fact |
| Playwright / browser automation | **UNAVAILABLE for external sites** | **INFERRED** from the tested allowlist |
| MCP servers | **AVAILABLE — separate network path** | **TESTED** — GitHub MCP functioned |
| **GitHub Actions as remote execution** | **AVAILABLE — UNUSED** | **TESTED** (GitHub reachable) + **INFERRED** (runner internet access is standard) |
| Amazon marketplace data (BSR, keywords) | **UNAVAILABLE** | **TESTED** — `kdp.amazon.com` blocked. Note: scraping would breach Amazon's terms and is barred by `COMPLIANCE_POLICY.md` regardless of reachability |

**On the GitHub Actions path — deliberately not used yet.** It could legitimately fetch public pages for research or monitoring. It is not being adopted in C1 because: (a) it is infrastructure, and `BUILD_VS_NO_BUILD.md` defers building until revenue justifies it; (b) it would not solve the binding constraint, since the marketplace data I actually lack is barred by platform terms, not by network reach. It is recorded so that a future cycle needing source-monitoring for the re-issue cadence starts from a known-available path rather than re-deriving it.

## 7. Recommendation to the Owner

The Preflight spec was written for an environment with open outbound access. **This environment does not have one, and that gap is the most consequential technical fact in the project.** It is not a blocker for Cycle 1 — the strategy was chosen to fit the available evidence channel — but it does mean:

1. Real-time marketplace intelligence (rank, keyword, competitor depth) is unobtainable here.
2. Automated source-monitoring for the re-issue cadence — the natural Phase-2 build — is impossible until egress opens.
3. If this business scales, an environment with a defined allow-list (Amazon, official policy domains, the chosen sales rails) would be the highest-leverage infrastructure change available.

**No action is requested now.** Recorded so the constraint is visible when it starts costing money rather than being discovered again later.
