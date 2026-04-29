---
file: README.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# PoC 04 — UI Vision

> Analyses banking UI screenshots using Claude Sonnet 4.6's vision capability to generate structured test scenarios for visible UI components.

**Status:** 🔴 Not Started | **Demo-Ready ETA:** 2026-05-06

---

## Purpose

New features often have no existing test cases and no test plan when they first land in QA. A QA engineer looking at a new screen must identify all testable elements from visual inspection alone. This PoC automates that visual analysis: upload a screenshot, get back a structured set of test scenarios covering functional, negative, boundary, accessibility, and compliance paths.

---

## How to Run

> **TODO (Gopi):** Fill in after Day 8 implementation.

```bash
cd poc-04-ui-vision/backend
# TODO: set ANTHROPIC_API_KEY in .env
# TODO: uvicorn main:app --reload
# Upload screenshot via frontend or POST to /api/analyse
```

---

## Demo Input

> **TODO (Gopi):** Create a synthetic banking UI mockup for the demo. Options:
> - Design a simple loan application form in Figma (free) and export as PNG
> - Use a generic banking UI template from a free mockup library
> - Build a simple HTML mockup and screenshot it
>
> Store the screenshot in `screenshots/`.

**Planned screen:** Synthetic loan application form with fields for customer name, loan amount, tenure, interest type, and submit button.

---

## Expected Output

> **TODO (Gopi):** Describe the expected JSON output structure.

- File: `outputs/scenarios_<screenshot_name>_<timestamp>.json`
- Fields per scenario: Scenario ID, Type, Description, Preconditions, Steps, Expected Result, Priority, Notes
- Minimum 5 scenarios per screenshot

---

## Status

| Component | Status |
|-----------|--------|
| Backend vision endpoint | 🔴 Not Started |
| Prompt integration (vision) | 🔴 Not Started |
| JSON output formatter | 🔴 Not Started |
| Frontend (screenshot upload) | 🔴 Not Started |
| Synthetic mockup screenshot | 🔴 Not Started |
| Demo video recorded | 🔴 Not Started |

---

## Vision Model Notes

- Claude Sonnet 4.6 supports image inputs via the Anthropic API (`image` content blocks)
- Max image size: check current Anthropic docs for limits
- Supported formats: PNG, JPEG, GIF, WebP
- **IMPORTANT:** Screenshots must be of synthetic mockups only — never real production screens

---

## Dependencies

- Python 3.11+ (`fastapi`, `anthropic`, `python-dotenv`, `Pillow` for image handling)
- Next.js 14 frontend (file upload component)

---

## Related Docs

- [ARCHITECTURE.md](./ARCHITECTURE.md) — component design
- [DEMO.md](./DEMO.md) — demo script and setup
- [docs/prompts/ui-vision-master.md](../docs/prompts/ui-vision-master.md) — master prompt
- [RISK.md](../RISK.md) — R-07 (vision misread risk)
