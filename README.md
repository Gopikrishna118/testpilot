---
file: README.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# QA-Forge — AI-Augmented QA Toolkit (PoC)

> Empowering Finastra QA engineers with Claude-powered automation — faster test cases, smarter defects, zero compliance risk.

🟡 **Day 1 of 10** | Sprint: 2026-04-29 → 2026-05-08 | Owner: Gopi | Domain: Banking / Finastra

---

## What

QA-Forge is a 4-PoC sprint demonstrating how Claude Sonnet 4.6 can augment QA workflows in a banking domain context.

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

| PoC | Status | Demo-Ready ETA |
|-----|--------|----------------|
| poc-01-testcase-gen | 🔴 Not Started | 2026-05-02 |
| poc-02-defect-creator | 🔴 Not Started | 2026-05-06 |
| poc-03-selenium-to-playwright | 🔴 Not Started | 2026-05-05 |
| poc-04-ui-vision | 🔴 Not Started | 2026-05-06 |

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

> **TODO (Gopi):** Add run commands once each PoC backend is implemented (Day 2+).

- PoC 01 — Test Case Generator: [poc-01-testcase-gen/README.md](./poc-01-testcase-gen/README.md)
- PoC 02 — JIRA Defect Creator: [poc-02-defect-creator/README.md](./poc-02-defect-creator/README.md)
- PoC 03 — Selenium → Playwright: [poc-03-selenium-to-playwright/README.md](./poc-03-selenium-to-playwright/README.md)
- PoC 04 — UI Vision: [poc-04-ui-vision/README.md](./poc-04-ui-vision/README.md)

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
