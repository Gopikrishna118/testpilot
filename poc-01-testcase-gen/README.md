# PoC 01 — Test Case Generator

> Converts Confluence pages, JIRA user stories, BRD sections, or freetext acceptance criteria into structured Excel test case suites using Claude Sonnet 4.6.

**Status:** ✅ Demo-Ready | **Last updated:** 2026-05-01

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_ORG/testpilot)

---

## What it does

QA engineers paste a user story or requirements fragment into the UI. Claude Sonnet 4.6 generates a structured test suite covering happy path, negative, boundary, and edge cases — formatted as a downloadable Excel file with 10 columns ready for JIRA/Zephyr import.

**Input types supported:**

| Type | Example |
|------|---------|
| JIRA Story | User story text + acceptance criteria |
| Confluence Page | Pasted page extract |
| BRD Section | Business requirements paragraph |
| Free Text | Plain English description |
| File Extract | Content from PDF/DOCX/XLSX |

**Output:** `testcases_<timestamp>.xlsx` with columns: Test ID · Module · Scenario · Preconditions · Test Steps · Expected Result · Priority · Test Type · Traceability · Notes

---

## Quickstart — Local

### Prerequisites

- Python 3.11+
- An Anthropic API key (`sk-ant-...`)

### 1. Set up the backend

```bash
cd poc-01-testcase-gen/backend

# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and set ANTHROPIC_API_KEY=sk-ant-...
```

### 2. Run the server

```bash
# From poc-01-testcase-gen/backend/
uvicorn main:app --reload --port 8001
```

### 3. Open the UI

Navigate to **http://localhost:8001**

The enterprise UI loads immediately. Paste your requirements text, select the input type, and click **Generate Test Cases**. Results appear as collapsible cards with stat counters. Click **Download Excel** to save the `.xlsx` file.

### 4. API endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/health` | Health check — returns model name and version |
| `POST` | `/api/v1/generate` | Generate test cases from requirements text |
| `POST` | `/api/v1/generate/debug` | Returns raw Claude response (no parsing) |
| `GET` | `/api/v1/download?path=<path>` | Download generated `.xlsx` file |
| `GET` | `/docs` | Interactive Swagger UI |

**Generate request body:**

```json
{
  "input_type": "jira",
  "content": "As a retail banking customer, I want to reset my password..."
}
```

**Generate response:**

```json
{
  "file_path": "/tmp/outputs/testcases_20260501_095856.xlsx",
  "count": 10,
  "message": "AI-GENERATED — requires human review before use."
}
```

---

## Deployment — Render

### One-click deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_ORG/testpilot)

This deploys `poc-01-testcase-gen/backend` as a Render web service using the [`render.yaml`](../render.yaml) at the repo root.

### Manual deploy steps

1. Fork or push this repo to GitHub
2. Go to [render.com](https://render.com) → **New → Web Service**
3. Connect your GitHub repo
4. Render auto-detects `render.yaml` — review the settings
5. Under **Environment Variables**, set `ANTHROPIC_API_KEY` to your key
6. Click **Deploy**

### Environment variables (Render)

| Variable | Value | Secret? |
|----------|-------|---------|
| `ANTHROPIC_API_KEY` | `sk-ant-...` | ✅ Yes — set in dashboard |
| `CLAUDE_MODEL` | `claude-sonnet-4-6` | No |
| `OUTPUT_DIR` | `/tmp/outputs` | No |
| `MAX_RETRIES` | `3` | No |
| `LOG_LEVEL` | `INFO` | No |
| `CORS_ORIGINS` | `["*"]` | No |

> **Note:** Render uses an ephemeral filesystem. Generated Excel files are written to `/tmp/outputs` and are available for the duration of the server process only. For persistent storage, wire up an S3 bucket or Render Disk (post-PoC).

---

## Security

- **Synthetic data only.** The PII sanitizer (`shared/utils/sanitizer.py`) blocks real PAN, Aadhaar, account numbers, email addresses, and phone numbers before any input reaches the Claude API.
- **Path traversal protection.** The `/api/v1/download` endpoint validates all file paths are inside the `outputs/` directory and restricts to `.xlsx` extension.
- See [SECURITY.md](../SECURITY.md) for the full compliance and data-handling policy.

---

## Component status

| Component | Status |
|-----------|--------|
| FastAPI backend | ✅ Complete |
| Claude integration (real API key) | ✅ Complete |
| PII sanitizer gate | ✅ Complete |
| Excel formatter (10 columns) | ✅ Complete |
| Enterprise UI | ✅ Complete |
| Download endpoint | ✅ Complete |
| Render deployment config | ✅ Complete |
| Demo video recorded | ✅ Complete |

---

## Related docs

- [ARCHITECTURE.md](./ARCHITECTURE.md) — component design
- [DEMO.md](./DEMO.md) — demo script and setup
- [docs/prompts/testcase-gen-master.md](../docs/prompts/testcase-gen-master.md) — master prompt (v1.0)
- [SECURITY.md](../SECURITY.md) — data handling rules
- [render.yaml](../render.yaml) — Render deployment config
