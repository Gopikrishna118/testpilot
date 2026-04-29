---
file: README.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# PoC 01 — Test Case Generator

> Converts Confluence pages, JIRA user stories, BRD sections, or freetext acceptance criteria into structured Excel test case suites using Claude Sonnet 4.6.

**Status:** 🔴 Not Started | **Demo-Ready ETA:** 2026-05-02

---

## Purpose

QA engineers at Finastra spend significant time manually writing test cases from user stories. This PoC automates the first-draft generation, producing a structured Excel file with Test ID, Scenario, Preconditions, Steps, Expected Result, Priority, and Traceability — ready for human review and refinement.

---

## Supported Input Types

| Input Type | Description | Status |
|------------|-------------|--------|
| JIRA user story (paste) | Paste story text + acceptance criteria | 🔴 TODO |
| Confluence page (paste) | Paste page content | 🔴 TODO |
| BRD section (paste) | Paste Business Requirements Document section | 🔴 TODO |
| Freetext | Plain English description of the feature | 🔴 TODO |

---

## How to Run

> **TODO (Gopi):** Fill in after Day 2 implementation.

```bash
# 1. Navigate to backend
cd poc-01-testcase-gen/backend

# 2. Activate virtual environment
# TODO: add venv setup instructions

# 3. Set environment variable
# TODO: export ANTHROPIC_API_KEY=your_key

# 4. Run FastAPI server
# TODO: uvicorn main:app --reload

# 5. Open frontend
# TODO: cd ../frontend && npm run dev
```

---

## Demo Input

> **TODO (Gopi):** Describe the synthetic user story used for demos. Store the actual input file in `samples/`.

**Sample story:** Synthetic KYC onboarding story for a new retail banking customer (no real data).

---

## Expected Output

> **TODO (Gopi):** Describe the expected Excel output after Day 2 implementation.

- File: `outputs/testcases_<timestamp>.xlsx`
- Columns: Test ID | Module | Scenario | Preconditions | Test Steps | Expected Result | Priority | Test Type | Traceability | Notes
- Minimum 8 test cases per run

---

## Status

| Component | Status |
|-----------|--------|
| Backend FastAPI skeleton | 🔴 Not Started |
| Prompt integration | 🔴 Not Started |
| Excel output formatter | 🔴 Not Started |
| Frontend UI | 🔴 Not Started |
| Error handling | 🔴 Not Started |
| Demo video recorded | 🔴 Not Started |

---

## Dependencies

> **TODO (Gopi):** Confirm versions on Day 2.

- Python 3.11+
- `fastapi` — web framework
- `anthropic` — Claude SDK
- `openpyxl` — Excel file generation
- `python-dotenv` — env var loading
- Node.js 20+ + Next.js 14 (frontend)

---

## Related Docs

- [ARCHITECTURE.md](./ARCHITECTURE.md) — component design
- [DEMO.md](./DEMO.md) — demo script and setup
- [docs/prompts/testcase-gen-master.md](../docs/prompts/testcase-gen-master.md) — master prompt
- [SECURITY.md](../SECURITY.md) — data handling rules
