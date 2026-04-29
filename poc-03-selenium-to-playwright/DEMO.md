---
file: DEMO.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# DEMO — PoC 03: Selenium → Playwright Converter

---

## 90-Second Demo Script

**Hook (0–10s):**
> "We have [TODO: X] Selenium tests that need migrating to Playwright. Manual migration is [TODO: Y hours/test]. Watch this."

**Problem (10–20s):**
> "Here's a Selenium Python test for a banking login flow. Old-style WebDriver, explicit waits, legacy locators. [Show code on screen.]"

**Demo Action (20–60s):**
> [Run converter — CLI or API] "Claude is analysing the structure, mapping every Selenium API call to its Playwright equivalent, converting the waits, modernising the locators."

**Result (60–75s):**
> [Open output `.spec.ts` file] "Output Playwright TypeScript. `page.locator()` instead of `find_element`. `await expect()` for assertions. Proper `async` structure. [TODO: run it] — passes."

**Impact (75–90s):**
> "[TODO: seconds] vs [TODO: hours]. Across [TODO: X] scripts — that's [TODO: weeks] of migration work removed. The team focuses on new coverage, not maintenance debt."

---

## Demo Setup Checklist

> Complete on Day 7 morning (2026-05-05) before recording.

- [ ] Converter backend / CLI running
- [ ] Synthetic Selenium Python input script ready in `input/`
- [ ] Conversion runs without error
- [ ] Output `.spec.ts` saved in `output/`
- [ ] Optional: `npx playwright test --dry-run` passes on the output script
- [ ] Screen recording software ready

---

## Demo Input

> **TODO (Gopi):** Describe the synthetic Selenium script. Store in `input/login_test.py`.

**Input:** [Reference: `input/login_test.py`]

---

## Expected Output

> **TODO (Gopi):** Describe the expected Playwright output. Store in `output/login_test.spec.ts`.

**Output:** [Reference: `output/login_test.spec.ts`]

---

## Fallback Plan

If converter fails during demo:
1. Open the side-by-side comparison slide (Selenium left, Playwright right)
2. Say: *"Let me show you the conversion I ran this morning. [Selenium code left, Playwright right.] Every `find_element` becomes `page.locator()`, every explicit wait becomes an `expect()` assertion."*
3. Walk through 3–4 key conversion patterns as a code walkthrough

---

## Demo Recording Instructions

> Record on Day 7 (2026-05-05).

1. Record 90-second script — consider showing both files side by side
2. Save as `poc-03-selenium-to-playwright-demo.mp4`
3. Add link to PITCH-DECK.md Slide 6
