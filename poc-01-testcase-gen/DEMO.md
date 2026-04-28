---
file: DEMO.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# DEMO — PoC 01: Test Case Generator

---

## 90-Second Demo Script

**Hook (0–10s):**
> "I'm going to show you a user story from our backlog and what happens when I ask Claude to write the test cases."

**Problem (10–20s):**
> "Here's a synthetic KYC onboarding story. Normally, turning this into a proper test case Excel takes me around [TODO: X minutes]. Watch this."

**Demo Action (20–60s):**
> [Paste story into QA-Forge frontend → click Generate → watch streaming output]
> "Claude is reading the acceptance criteria, identifying positive and negative scenarios, structuring each case with preconditions and steps."

**Result (60–75s):**
> [Excel downloads automatically] "I now have [TODO: N] test cases — structured, traceable, ready for review. Test ID, scenario, steps, expected result, priority. All pre-formatted."

**Impact (75–90s):**
> "[TODO: X minutes] of work in [TODO: Y seconds]. Across [TODO: N] stories per sprint, that's [TODO: hours] back to the team."

---

## Demo Setup Checklist

> Complete this checklist on the morning of Day 4 (2026-05-02) before recording.

- [ ] Backend FastAPI server running locally (`uvicorn main:app --reload`)
- [ ] Frontend Next.js dev server running (`npm run dev`)
- [ ] `ANTHROPIC_API_KEY` set in `.env`
- [ ] Synthetic KYC user story input file ready in `samples/`
- [ ] `outputs/` directory is empty (clean demo run)
- [ ] Screen recording software ready (OBS / Windows screen record)
- [ ] Browser zoomed to 125% for visibility
- [ ] API connectivity tested within 30 minutes of demo

---

## Demo Input

> **TODO (Gopi):** Paste or reference the exact synthetic user story used for the demo. Store in `samples/kyc-onboarding-story.txt`.

**Story:** [Reference: `samples/kyc-onboarding-story.txt`]

---

## Expected Output

> **TODO (Gopi):** Document what the output should look like. How many test cases? What are the column values for the first 2 rows?

**Expected:** [Reference: `samples/expected-output-reference.xlsx` — create after first successful run]

---

## Fallback Plan

If the live API fails during the demo:

1. Open pre-generated Excel file from `samples/expected-output-reference.xlsx`
2. Say: *"The live connection isn't cooperating — let me show you the output I generated earlier this morning. This is exactly what the tool produces."*
3. Walk through the Excel columns and row content as planned
4. Do NOT apologise excessively — pre-recorded fallbacks are standard in live tech demos

---

## Demo Recording Instructions

> Record on Day 4 (2026-05-02).

1. Open OBS or Windows Game Bar (Win + G)
2. Set resolution to 1920×1080
3. Record the full 90-second script — no cuts, single take preferred
4. Save as `poc-01-testcase-gen-demo.mp4`
5. Store in `samples/` (excluded from git via `.gitignore` — add pattern if needed)
6. Upload to Google Drive / SharePoint and add link to PITCH-DECK.md Slide 4
