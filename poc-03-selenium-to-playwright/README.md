---
file: README.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# PoC 03 — Selenium → Playwright Converter

> Converts legacy Selenium WebDriver scripts (Python or Java) into modern, executable Playwright TypeScript scripts using Claude Sonnet 4.6.

**Status:** 🔴 Not Started | **Demo-Ready ETA:** 2026-05-05

---

## Purpose

Many banking QA teams maintain large Selenium test suites that need migration to Playwright for improved reliability, parallelism, and modern browser support. Manual migration is time-consuming and error-prone. This PoC automates the conversion, mapping Selenium APIs to Playwright equivalents and modernising patterns (explicit waits → auto-waiting, etc.).

---

## How to Run

> **TODO (Gopi):** Fill in after Day 7 implementation.

```bash
# Option A: FastAPI endpoint
cd poc-03-selenium-to-playwright/backend
# TODO: start server, POST script to /api/convert

# Option B: CLI (if simpler for PoC)
# TODO: python convert.py --input input/login_test.py --output output/login_test.ts
```

---

## Demo Input

> **TODO (Gopi):** Describe the synthetic Selenium script used for demo. Store in `input/`.

**Sample:** Synthetic Selenium Python test for a banking login + dashboard navigation (no real URLs or credentials).

---

## Expected Output

> **TODO (Gopi):** Describe the expected Playwright TypeScript output. Store in `output/`.

- File: `output/<original_name>.spec.ts`
- Framework: `@playwright/test`
- Verified runnable (no syntax errors, passes `npx playwright test --dry-run`)

---

## Conversion Scope (PoC)

| Pattern | Handled | Notes |
|---------|---------|-------|
| Basic element interactions (click, fill, get text) | 🔴 TODO | |
| Explicit waits → Playwright auto-waits | 🔴 TODO | |
| CSS/XPath selector conversion | 🔴 TODO | |
| Assertions (assertEqual → expect) | 🔴 TODO | |
| Setup/teardown → fixtures | 🔴 TODO | |
| iFrames, file uploads, alerts | 🔴 Out of scope for PoC | Flag in conversion notes |

---

## Status

| Component | Status |
|-----------|--------|
| Backend conversion endpoint | 🔴 Not Started |
| Prompt integration | 🔴 Not Started |
| Output validation (syntax check) | 🔴 Not Started |
| Sample input script | 🔴 Not Started |
| Demo video recorded | 🔴 Not Started |

---

## Dependencies

- Python 3.11+ (`fastapi`, `anthropic`, `python-dotenv`)
- Node.js 20+ + `@playwright/test` (for output validation)

---

## Related Docs

- [ARCHITECTURE.md](./ARCHITECTURE.md) — component design
- [DEMO.md](./DEMO.md) — demo script and setup
- [docs/prompts/selenium-to-pw-master.md](../docs/prompts/selenium-to-pw-master.md) — master prompt
- [RISK.md](../RISK.md) — R-06 (invalid script risk)
