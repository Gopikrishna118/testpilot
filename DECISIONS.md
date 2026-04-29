---
file: DECISIONS.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# DECISIONS — Architecture Decision Records (ADRs)

> Use this log to record every significant technical or process decision made during the PoC sprint. Future-you (and your manager) will thank you.

---

## ADR Template

```
### ADR-XXX: <Title>
- **Date:** YYYY-MM-DD
- **Status:** Proposed | Accepted | Deprecated | Superseded by ADR-YYY
- **Context:** Why was this decision needed? What problem does it solve?
- **Decision:** What was decided?
- **Tradeoff Gained:** What benefit does this choice provide?
- **Tradeoff Lost:** What did we give up?
- **Consequences:** What follow-up actions or constraints does this create?
```

---

## ADR-001: Use Claude Sonnet 4.6 as Default Model

- **Date:** 2026-04-29
- **Status:** Accepted
- **Context:** The 4-PoC sprint requires an AI model capable of structured text generation, code conversion, and vision analysis. Cost and latency matter for a live demo. Two viable options are Claude Opus 4.7 (more capable, higher cost) and Claude Sonnet 4.6 (strong capability, ~5x cheaper per token).
- **Decision:** Default to Claude Sonnet 4.6 for all PoCs. Escalate to Claude Opus 4.7 only for architecture review sessions or pre-release audit tasks where complex multi-file reasoning is needed.
- **Tradeoff Gained:** ~5x cost reduction vs Opus 4.7; faster response latency improves live demo experience; sufficient capability for all 4 PoC use cases.
- **Tradeoff Lost:** Slightly weaker on complex multi-file reasoning and nuanced ambiguous instructions compared to Opus 4.7.
- **Consequences:** Document any case during the sprint where Sonnet 4.6 output was insufficient and required switching to Opus 4.7. These cases inform the production model selection recommendation.

---

## ADR-002: Excel-Only Output — No Database in PoC

- **Date:** 2026-04-29
- **Status:** Accepted
- **Context:** PoC demo needs the simplest possible output format. Banking QA teams universally use Excel for test case management (ALM, manual spreadsheets). Introducing a database layer adds infrastructure complexity without adding demo value during a 10-day sprint.
- **Decision:** All PoC outputs are Excel (.xlsx), CSV, or JSON files written to the local `outputs/` directory. No database, no persistence layer, no auth system.
- **Tradeoff Gained:** Zero infrastructure to spin up; easy to share outputs with stakeholders during pitch; QA-familiar format; no migration risk during demo.
- **Tradeoff Lost:** No historical analytics, no multi-user state, no output versioning. Can't show usage trends.
- **Consequences:** Production version will need a proper persistence layer (PostgreSQL or similar). Document the migration path from file-based to DB-backed output as part of the production proposal. Reference this ADR in the pitch when asked "why no database?"

---

## ADR-003: Synthetic Data Only for PoC

- **Date:** 2026-04-29
- **Status:** Accepted
- **Context:** Banking compliance posture and pending InfoSec approval mean we cannot use real customer data, real Finastra production data, or real JIRA/Confluence content in any PoC input. Using personal Claude Pro account further restricts what data is appropriate to send to external APIs.
- **Decision:** All inputs across all 4 PoCs use synthetically generated banking data only. Synthetic data must be clearly labeled. A sanitization layer validates inputs before any API call.
- **Tradeoff Gained:** Bypasses InfoSec review delay that would otherwise block the PoC sprint; safe for personal Claude Pro account; demonstrates security-conscious engineering posture to manager.
- **Tradeoff Lost:** Demo data is slightly less realistic than production scenarios; some edge cases present in real data may not be covered.
- **Consequences:** The pitch must explicitly state that the production version routes through an InfoSec-approved API gateway (e.g., Bedrock). Synthetic data examples must be realistic enough to be convincing. See `shared/synthetic-data/` for approved sample inputs.

---

## Future ADRs (TODO Gopi)

> Add ADRs here as decisions are made during the sprint. Suggested topics:
> - ADR-004: Production deployment approach (Bedrock vs. Anthropic Enterprise vs. other)
> - ADR-005: JIRA API authentication strategy (OAuth vs. API token for PoC)
> - ADR-006: Frontend framework selection rationale (if questioned)
> - ADR-007: Prompt versioning strategy
