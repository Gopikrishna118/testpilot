# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Summary

TestPilot is a 10-day PoC sprint (2026-04-29 → 2026-05-08) demonstrating Claude Sonnet 4.6 augmenting QA workflows in a banking domain. It consists of 4 independent PoC tools, each with its own FastAPI backend and Next.js 14 frontend, sharing common utilities.

| PoC | What it does |
|-----|-------------|
| `poc-01-testcase-gen` | Confluence/JIRA/BRD text → structured Excel test cases |
| `poc-02-defect-creator` | Freetext defect description → JIRA ticket via REST API |
| `poc-03-selenium-to-playwright` | Legacy Selenium scripts → Playwright TypeScript |
| `poc-04-ui-vision` | Banking UI screenshots → JSON test scenarios (vision API) |

---

## Current Sprint Status

**Sprint:** Day 4 of 10 | 2026-05-02

### Day 1 — Done (2026-04-29)
- 46 files scaffolded across all 4 PoCs + `shared/`
- Repo renamed `qa-forge` → `testpilot` across all docs
- Commits: `d2186ae` (initial scaffold), `086ff9b` (rename)

### Day 2 — Done (2026-04-30)
- Security bundle: `SECURITY.md` (OWASP ASVS / NIST / DPDP), `THREAT_MODEL.md` (STRIDE), `DATA_HANDLING.md`, `.env.example`
- `poc-01` backend skeleton: FastAPI layered structure (`api/`, `core/`, `services/`, `models/`), health endpoint, sanitizer, Claude client, Excel formatter
- `project-knowledge/` bundle created for Claude Project migration (12 files)
- Commits: `885d593` (Day 2 baseline), `820e134` (project-knowledge)

### Day 3 — Done (2026-05-01)
- `shared/utils/sanitizer.py` — 7-pattern PII detect + redact, Luhn check, overlap resolution
- `poc-01/backend/services/prompt_builder.py` — module-level load, 5 input-type framings
- `poc-01/backend/services/claude_client.py` — `complete()`, 3-attempt backoff, selective retry; API key via pydantic-settings
- `poc-01/backend/services/response_parser.py` — fence-strip, schema validation, `risk_level` normalisation
- `poc-01/backend/services/excel_formatter.py` — 6-col xlsx, risk colouring, auto-fit widths
- `poc-01/backend/api/v1/endpoints/generate.py` — E2E wired; all 3 input types smoke-tested ✅
- Fixed: `anthropic` bumped to `>=0.40.0` (httpx compat); `CORS_ORIGINS` JSON format in `.env.example`
- Commits: `5ef94df` (5/7 checkpoint), `fee2ba4` (Day 3 complete)

### Day 4 — Done (2026-05-01)
- Mock removed from `claude_client.py`; real `ANTHROPIC_API_KEY` wired in `.env` ✅
- Fixed `CLAUDE_MODEL` env var (had display string `→ claude-sonnet-4-20250514` baked in) ✅
- Fixed `_MAX_TOKENS` 4096 → 8192 (was truncating 8+ test case responses) ✅
- Prompt hardened: CRITICAL JSON-only output rules + anti-hallucination guard alignment ✅
- `response_parser.py` — 3-strategy fence extractor, raw-response logging, `test_steps` schema aligned to master prompt ✅
- `excel_formatter.py` — expanded from 6 to 10 columns matching full prompt schema ✅
- Enterprise UI (`static/index.html`) — dark navy/gold, two-column, stat cards, collapsible test case cards ✅
- `GET /api/v1/download` endpoint — path-traversal guard, xlsx-only, `FileResponse` ✅
- `outputs/` added to `.gitignore`, removed from git history ✅
- Demo video recorded (90-second testcase-gen) ✅
- Commits: `c5b598e` (Day 4 main), `831d57d` (outputs gitignored)

### Day 5 — Next (2026-05-02)
- First task: Build poc-02 JIRA defect creator — start with backend scaffold
- Read `poc-02-defect-creator/backend/` scaffold files before writing anything
- Wire `services/claude_client.py` → `services/jira_client.py` → POST `/api/v1/create`
- Reuse shared sanitizer pattern from poc-01

---

## Development Commands

Each PoC backend follows the same pattern (substitute `poc-01-testcase-gen` as needed):

```bash
# Backend (Python)
cd poc-01-testcase-gen/backend
python -m venv .venv && source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # then fill in ANTHROPIC_API_KEY
uvicorn main:app --reload

# Frontend (Next.js)
cd poc-01-testcase-gen/frontend
npm install
npm run dev

# Lint / type-check
cd poc-01-testcase-gen/frontend
npm run lint
npx tsc --noEmit
```

`.env` variables used by every backend:

```
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-sonnet-4-6
OUTPUT_DIR=./outputs
MAX_RETRIES=2
```

---

## Architecture

### Shared data flow (all PoCs)

```
User input → shared/utils/sanitizer (PII scrub) → Prompt builder
  → Claude Sonnet 4.6 (Anthropic SDK) → Response parser → Output formatter
  → outputs/<name>_<timestamp>.(xlsx|json|ts)
```

**The sanitizer must run before every Anthropic API call.** See `SECURITY.md §5` for the regex rules it enforces (PAN, Aadhaar, Indian account numbers, email, phone, card).

### Planned file layout per PoC backend

```
backend/
  main.py                    # FastAPI app, CORS
  config.py                  # Env vars, model name, output path
  routers/generate.py        # POST /api/generate
  services/
    prompt_builder.py        # Injects input into master prompt template
    claude_client.py         # Anthropic SDK wrapper + retry/backoff
    response_parser.py       # Extracts JSON from Claude response
    excel_formatter.py       # JSON → .xlsx via openpyxl  (PoC-01 only)
```

### Shared utilities (`shared/utils/`)

| Module | Purpose |
|--------|---------|
| `sanitizer.py` | PII regex scrubbing — mandatory gate before any API call |
| `logger.py` | Structured logging (request, response, errors) |
| `error_handler.py` | Anthropic API error codes + exponential backoff retry |
| `config.py` | Central env-var loading |

### Prompts (`docs/prompts/`)

Each PoC has one versioned master prompt file (`testcase-gen-master.md`, `defect-creator-master.md`, `selenium-to-pw-master.md`, `ui-vision-master.md`). The prompt builder reads these at runtime and injects user input. When iterating on prompts, update the file and bump the version in the frontmatter.

---

## Key Constraints

- **Synthetic data only.** Never pass real customer data, PAN, Aadhaar, account numbers, or internal Finastra content to the API. See `SECURITY.md` for the full list.
- **Model:** `claude-sonnet-4-6` is the default (ADR-001). Escalate to `claude-opus-4-7` only for complex multi-file reasoning tasks.
- **No database in PoC** (ADR-002). All outputs are files written to `outputs/`. Production persistence is out of scope for this sprint.
- **No cloud infra.** All PoCs run locally. Production routing through an InfoSec-approved gateway (Bedrock or Anthropic Enterprise) is a post-PoC requirement (see `DECISIONS.md` ADR-004 TODO).
- **`.env` must never be committed.** It is in `.gitignore`. Check before every push.

---

## Tech Stack Versions

| Layer | Version |
|-------|---------|
| Python | 3.11.x |
| FastAPI | 0.111+ |
| `anthropic` SDK | 0.28+ |
| Node.js | 20.x LTS |
| Next.js | 14.x (App Router) |
| TypeScript | 5.x strict mode |
| Tailwind CSS | 3.x |
| `openpyxl` | for Excel output (PoC-01) |
