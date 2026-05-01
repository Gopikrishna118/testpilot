---
file: HANDOFF.md
project: testpilot
session_end: 2026-05-01
sprint_day: D4 of 10
last_commit: 13cfda2
---

# HANDOFF — TestPilot Session Context

> Read this before doing anything. It contains the exact state of the codebase at
> end-of-session and the precise next action to take.

---

## Where We Are

**Sprint:** Day 4 of 10 complete | 2026-05-01
**Active work:** `poc-01-testcase-gen` — DONE, deployed, demo-ready
**Next work:** `poc-02-defect-creator` — start Day 5
**Git state:** Clean. Last commit `13cfda2` — "Add .python-version 3.11.9 and pin pythonVersion in render.yaml"

| Location | URL |
|----------|-----|
| GitHub | https://github.com/Gopikrishna118/testpilot |
| Render (live) | https://testpilot-wgpy.onrender.com |
| Local | http://localhost:8001 (run uvicorn from `poc-01-testcase-gen/backend/`) |

---

## poc-01 Status — Complete ✅

All backend files done and smoke-tested against real API:

| # | File | Status |
|---|------|--------|
| 1 | `shared/utils/sanitizer.py` | ✅ Done |
| 2 | `poc-01/backend/services/prompt_builder.py` | ✅ Done |
| 3 | `poc-01/backend/services/claude_client.py` | ✅ Done — mock removed, real key wired |
| 4 | `poc-01/backend/services/response_parser.py` | ✅ Done — 3-strategy extractor, 10-field schema |
| 5 | `poc-01/backend/services/excel_formatter.py` | ✅ Done — 10-column xlsx |
| 6 | `poc-01/backend/api/v1/endpoints/generate.py` | ✅ Done — POST /api/v1/generate |
| 7 | `poc-01/backend/api/v1/endpoints/download.py` | ✅ Done — GET /api/v1/download |
| 8 | `poc-01/backend/static/index.html` | ✅ Done — enterprise UI, dark navy/gold |
| 9 | `docs/prompts/testcase-gen-master.md` | ✅ Done — CRITICAL JSON rules, 10-field schema |
| 10 | Demo video | ✅ Recorded (90-second testcase-gen) |

**Local:** `uvicorn main:app --port 8001` from `poc-01-testcase-gen/backend/`
**Render:** https://testpilot-wgpy.onrender.com
**Health (Render):** https://testpilot-wgpy.onrender.com/api/v1/health
**Health (local):** http://localhost:8001/api/v1/health

---

## What Was Fixed on Day 4 (context for future debugging)

| Bug | Root Cause | Fix |
|-----|-----------|-----|
| 401 on first run | Stale/invalid `ANTHROPIC_API_KEY` in `.env` | Real key added to `.env` |
| 404 model not found | `CLAUDE_MODEL` env var had `claude-sonnet-4-6 → claude-sonnet-4-20250514` as literal string | Fixed to `claude-sonnet-4-6` |
| `_MODEL` hardcoded | `claude_client.py` had literal string instead of reading settings | Changed to `settings.claude_model` |
| JSON parse empty string | `_MAX_TOKENS=4096` truncated 8+ test case responses; also Claude adding preamble | Raised to 8192; added CRITICAL rules to prompt |
| Parser schema mismatch | Prompt used `test_steps`, parser required `steps` | Aligned parser to prompt schema |
| Download endpoint wrong path | Endpoint was in generate router (prefix `/generate`), so it was at `/api/v1/generate/download` not `/api/v1/download` | Moved to `endpoints/download.py`, registered separately |

---

## Day 5 — Next Action

**Goal:** Build `poc-02-defect-creator` backend — freetext defect description → JIRA ticket

### Step 1 — Read before writing

```
poc-02-defect-creator/backend/main.py
poc-02-defect-creator/backend/core/config.py
poc-02-defect-creator/backend/models/request.py
poc-02-defect-creator/backend/models/response.py
poc-02-defect-creator/backend/api/v1/endpoints/create.py
docs/prompts/defect-creator-master.md
```

Do NOT write code until you have read all scaffold files. The scaffold was written on Day 1
and may have stubs, TODOs, or class-based patterns that need updating (same pattern as poc-01 had).

### Step 2 — Service layer build order

1. `services/claude_client.py` — copy pattern from poc-01, same `complete()` signature
2. `services/prompt_builder.py` — load `defect-creator-master.md`, single framing (no input_type dropdown needed)
3. `services/response_parser.py` — Claude returns a JIRA-shaped JSON object, not an array
4. `services/jira_client.py` — NEW file; POST to JIRA REST API v3 (`/rest/api/3/issue`)
5. `api/v1/endpoints/create.py` — wire the chain: sanitize → prompt → Claude → parse → JIRA

### Step 3 — JIRA API notes

- Base URL from env: `JIRA_BASE_URL=https://<your-domain>.atlassian.net`
- Auth: `JIRA_EMAIL` + `JIRA_API_TOKEN` as HTTP Basic Auth
- Create issue endpoint: `POST /rest/api/3/issue`
- Required fields: `project.key`, `issuetype.name`, `summary`, `description` (Atlassian Document Format)
- For PoC: use `description` as plain text wrapped in ADF boilerplate (not full markdown)
- Return the created issue key (e.g. `QA-123`) and browse URL

### Step 4 — Prompt target

The Claude prompt for poc-02 should return:

```json
{
  "summary": "one-line JIRA title",
  "description": "full defect description in plain text",
  "priority": "High | Medium | Low",
  "labels": ["regression", "banking"],
  "components": ["Authentication"],
  "steps_to_reproduce": "numbered steps",
  "expected_result": "what should happen",
  "actual_result": "what happened instead",
  "environment": "browser/OS/build"
}
```

---

## Key Project Facts

| Fact | Value |
|------|-------|
| Local repo | `C:\Projects\testpilot` |
| GitHub | https://github.com/Gopikrishna118/testpilot |
| Render (poc-01 live) | https://testpilot-wgpy.onrender.com |
| poc-01 backend | `poc-01-testcase-gen/backend/` — fully deployed |
| poc-02 backend | `poc-02-defect-creator/backend/` — Day 5 target |
| Model | `claude-sonnet-4-6` (all PoCs) |
| Pitch target | Rajesh Kumar, QA Manager, 12 engineers, Day 10 (2026-05-08) |
| Security rule | All inputs are synthetic — sanitizer gate before every Claude call |
| `.env` | Must exist per PoC backend — never committed |
| `outputs/` | Gitignored — never commit generated xlsx files |
| Context files | `CLAUDE.md`, `HANDOFF.md`, `ROADMAP.md` |
