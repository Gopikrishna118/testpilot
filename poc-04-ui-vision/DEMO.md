---
file: DEMO.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# DEMO — PoC 04: UI Vision

---

## 90-Second Demo Script

**Hook (0–10s):**
> "When a new screen lands in QA with no test cases, we rely on visual inspection. What if Claude could do that first pass for us?"

**Problem (10–20s):**
> "Here's a synthetic loan application form mockup. No requirements, no test plan. Just the screen. [Display screenshot.]"

**Demo Action (20–60s):**
> [Upload screenshot to TestPilot UI Vision → click Analyse]
> "Claude is identifying the form fields, buttons, validation zones, compliance-sensitive inputs. It's generating scenarios for each."

**Result (60–75s):**
> [Results render on screen] "[TODO: N] test scenarios. Look at scenario [TODO: highlight best one] — [TODO: quote a scenario that would surprise the audience, e.g., a compliance check or boundary value]. That's something I'd likely have missed."

**Impact (75–90s):**
> "First-pass test scenario coverage from a screenshot in [TODO: seconds]. Especially valuable on Day 1 of a new feature in QA — before the developer even writes the tests."

---

## Demo Setup Checklist

> Complete on Day 8 morning (2026-05-06) before recording.

- [ ] Backend vision endpoint running
- [ ] Synthetic banking UI screenshot ready in `screenshots/`
- [ ] Screenshot is a clean, high-contrast mockup (not a real screen — see R-07 in RISK.md)
- [ ] Analysis runs without error and produces ≥ 5 scenarios
- [ ] Frontend renders scenario cards cleanly
- [ ] Screen recording software ready

---

## Demo Input

> **TODO (Gopi):** Create or source the synthetic banking UI screenshot. Options:
> - Design in Figma (free tier) — export as PNG
> - Use a Canva banking UI template
> - Build a simple HTML form and screenshot it
>
> Store in `screenshots/loan-application-form.png`.

**Input:** [Reference: `screenshots/loan-application-form.png`]

---

## Expected Output

> **TODO (Gopi):** After first successful run, document expected output. How many scenarios? What does the best/most impressive scenario look like?

**Output:** [Reference: `outputs/scenarios_loan_application_<ts>.json`]

---

## Best Scenario to Highlight

> **TODO (Gopi):** After first successful run, identify the 1 scenario that would most impress a non-technical manager — typically a compliance check or unexpected edge case. Write it here to quote during the pitch.

---

## Fallback Plan

If vision analysis fails:
1. Show the pre-generated JSON output (`outputs/` pre-run file)
2. Display screenshot and JSON side by side on screen
3. Say: *"Here's the analysis TestPilot produced when I ran this earlier. [Point to best scenario.] This level of coverage from a screenshot in under 10 seconds."*

---

## Demo Recording Instructions

> Record on Day 8 (2026-05-06).

1. Show screenshot upload, processing, rendered scenario cards
2. Zoom in on the most impressive scenario for 10 seconds
3. Save as `poc-04-ui-vision-demo.mp4`
4. Add link to PITCH-DECK.md Slide 6
