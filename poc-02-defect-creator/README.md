---
file: README.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# PoC 02 — JIRA Defect Creator

> Converts freetext defect descriptions into complete, structured JIRA bug tickets and creates them via the JIRA REST API using Claude Sonnet 4.6.

**Status:** 🔴 Not Started | **Demo-Ready ETA:** 2026-05-06

---

## Purpose

QA engineers often raise JIRA defects under time pressure, resulting in incomplete tickets that require multiple back-and-forth clarifications with developers. This PoC takes a 2–3 sentence defect description in plain English and generates a fully structured JIRA ticket (summary, description, steps to reproduce, severity, priority, labels, component) — then creates it in JIRA via REST API.

---

## How to Run

> **TODO (Gopi):** Fill in after Day 5 implementation.

```bash
# 1. Navigate to backend
cd poc-02-defect-creator/backend

# 2. Set environment variables
# TODO: export ANTHROPIC_API_KEY=your_key
# TODO: export JIRA_BASE_URL=https://your-sandbox.atlassian.net
# TODO: export JIRA_API_TOKEN=your_jira_api_token
# TODO: export JIRA_EMAIL=your_email
# TODO: export JIRA_PROJECT_KEY=QA

# 3. Run FastAPI server
# TODO: uvicorn main:app --reload
```

---

## Demo Input

> **TODO (Gopi):** Describe the synthetic payment failure defect used for demos. Store in `samples/`.

**Sample input:** Synthetic description of a payment processing failure during NEFT transfer (no real transaction data).

---

## Expected Output

> **TODO (Gopi):** Describe the expected JIRA ticket fields and the API response.

- JSON payload to JIRA REST API
- Created ticket URL returned to frontend
- Fields: Summary, Description, Steps to Reproduce, Expected/Actual, Severity, Priority, Labels, Component

---

## Status

| Component | Status |
|-----------|--------|
| Backend FastAPI skeleton | 🔴 Not Started |
| Prompt integration | 🔴 Not Started |
| JIRA REST API integration | 🔴 Not Started |
| JIRA sandbox setup | 🔴 Not Started |
| Error handling + auth | 🔴 Not Started |
| Demo video recorded | 🔴 Not Started |

---

## Dependencies

> **TODO (Gopi):** Confirm versions on Day 5.

- Python 3.11+
- `fastapi` — web framework
- `anthropic` — Claude SDK
- `httpx` or `requests` — JIRA REST API calls
- `python-dotenv` — env var loading
- JIRA sandbox / cloud instance (Atlassian free tier works for PoC)

---

## JIRA Setup Notes

> **TODO (Gopi):** Before Day 5, create a free Jira Software Cloud instance at atlassian.com. Create a project with key `QA`. Generate an API token from your Atlassian account settings.

---

## Related Docs

- [ARCHITECTURE.md](./ARCHITECTURE.md) — component design
- [DEMO.md](./DEMO.md) — demo script and setup
- [docs/prompts/defect-creator-master.md](../docs/prompts/defect-creator-master.md) — master prompt
- [SECURITY.md](../SECURITY.md) — data handling rules
- [RISK.md](../RISK.md) — R-05 (JIRA API auth risk)
