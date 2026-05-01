---
file: README.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# TestPilot — AI-Augmented QA Toolkit (PoC)

> Empowering Finastra QA engineers with Claude-powered automation — faster test cases, smarter defects, zero compliance risk.

✅ **Day 4 of 10** | Sprint: 2026-04-29 → 2026-05-08 | Owner: Gopi | Domain: Banking / Finastra

---

## What

TestPilot is a 4-PoC sprint demonstrating how Claude Sonnet 4.6 can augment QA workflows in a banking domain context.

| # | PoC | Description |
|---|-----|-------------|
| 1 | **Test Case Generator** | Converts Confluence/JIRA/BRD inputs into structured Excel test cases |
| 2 | **JIRA Defect Creator** | Generates structured JIRA bug tickets from freetext defect descriptions |
| 3 | **Selenium → Playwright** | Converts legacy Selenium scripts to modern Playwright equivalents |
| 4 | **UI Vision** | Analyzes banking UI screenshots and generates test scenarios |

---

## Why

> **TODO (Gopi):** Describe 3–5 sentences on the Finastra QA context — team size, current tooling pain points, sprint velocity pressure, and why AI-augmentation matters now. Example: "Our QA team of X engineers manually writes test cases for every sprint story, taking an average of Y hours per story. The current process for Z is..."

---

## Status

| PoC | Status | Demo-Ready |
|-----|--------|------------|
| poc-01-testcase-gen | ✅ Live — [deploy ↗](https://render.com/deploy?repo=https://github.com/Gopikrishna118/testpilot) | 2026-05-01 ✅ |
| poc-02-defect-creator | 🟡 In Progress (Day 5) | 2026-05-04 |
| poc-03-selenium-to-playwright | 🔴 Pending | 2026-05-05 |
| poc-04-ui-vision | 🔴 Pending | 2026-05-06 |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| AI Engine | Claude Sonnet 4.6 (Anthropic) |
| Backend | Python 3.11 + FastAPI |
| Frontend | Next.js 14 + TypeScript + Tailwind CSS |
| Output Formats | Excel (.xlsx), JSON, Playwright .ts scripts |
| Dev OS | Windows 11 |

---

## Quickstart

### PoC 01 — Test Case Generator (live ✅)

```bash
cd poc-01-testcase-gen/backend
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env                              # add ANTHROPIC_API_KEY
uvicorn main:app --reload --port 8001
# → open http://localhost:8001
```

Full instructions: [poc-01-testcase-gen/README.md](./poc-01-testcase-gen/README.md)

### Other PoCs (coming Days 5–8)

- PoC 02 — JIRA Defect Creator: [poc-02-defect-creator/README.md](./poc-02-defect-creator/README.md)
- PoC 03 — Selenium → Playwright: [poc-03-selenium-to-playwright/README.md](./poc-03-selenium-to-playwright/README.md)
- PoC 04 — UI Vision: [poc-04-ui-vision/README.md](./poc-04-ui-vision/README.md)

---

## Deploy to Render

PoC 01 is configured for one-click deployment via [`render.yaml`](./render.yaml).

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Gopikrishna118/testpilot)

**What deploys:** `poc-01-testcase-gen/backend` as a Python web service.

**Steps:**
1. Push this repo to GitHub
2. Click the button above (or go to Render → New → Web Service → connect repo)
3. Render reads `render.yaml` automatically
4. Set `ANTHROPIC_API_KEY` in the Render dashboard under Environment Variables
5. Deploy — the UI is live at `https://<service>.onrender.com`

**Notes:**
- Generated Excel files are written to `/tmp/outputs` (ephemeral — lost on restart). For persistence, add a Render Disk or S3 integration post-PoC.
- The free tier sleeps after 15 minutes of inactivity — use a paid instance for the demo.
- All other env vars (`CLAUDE_MODEL`, `OUTPUT_DIR`, `MAX_RETRIES`, `LOG_LEVEL`) are pre-set in `render.yaml`.

---

## Security

> **Synthetic data only. See [SECURITY.md](./SECURITY.md).**
>
> No real customer data, account numbers, PAN, Aadhaar, or Finastra production data is used in any PoC. All inputs are synthetically generated for demonstration purposes only.

---

## Further Reading

- [ROADMAP.md](./ROADMAP.md) — 10-day sprint plan
- [ARCHITECTURE.md](./ARCHITECTURE.md) — system design overview
- [SECURITY.md](./SECURITY.md) — compliance and data handling
- [RISK.md](./RISK.md) — risk register
- [METRICS.md](./METRICS.md) — success criteria and ROI template
- [DECISIONS.md](./DECISIONS.md) — architecture decision records
- [GLOSSARY.md](./GLOSSARY.md) — banking, QA, and AI terms
- [docs/pitch/PITCH-DECK.md](./docs/pitch/PITCH-DECK.md) — manager pitch

---

## License

See [LICENSE](./LICENSE) — Internal use only. Confidential. © 2026 Gopi / Finastra.

**Contact:** Gopi | QA Engineer | Finastra | gopikrishnamasanam229@gmail.com
