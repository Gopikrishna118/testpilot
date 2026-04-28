---
file: DEMO-SCRIPT.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# DEMO-SCRIPT — QA-Forge Live Demo Narration

> Each section is a 90-second script: Hook → Problem → Demo Action → Result → Impact.
> Practise until you can deliver each without reading. Record screen + voice on the designated day.

---

## PoC 01 — Test Case Generator

### 90-Second Narration Script

**Hook (0–10s):**
> "Every sprint, I spend [TODO: X hours] manually writing test cases for user stories. I want to show you what happens when I let Claude do the first draft."

**Problem (10–20s):**
> "Here's a typical KYC onboarding user story from our backlog. [Show input on screen.] Right now, turning this into a structured test case Excel takes me about [TODO: Y minutes]. Let's see what Claude does with it."

**Demo Action (20–60s):**
> "I paste the story into QA-Forge. Hit Generate. [Pause — watch output stream.] It's identifying the acceptance criteria, deriving positive and negative scenarios, formatting each as a test case with ID, steps, and expected results."

**Result (60–75s):**
> "In [TODO: Z seconds], I have [TODO: N] test cases — all structured, all traceable to the story. I download the Excel. [Open Excel.] Look at the columns: Test ID, Scenario, Preconditions, Steps, Expected Result, Priority. Human review still required — but the heavy lifting is done."

**Impact (75–90s):**
> "That's [TODO: manual time − AI time] saved on a single story. Across [TODO: stories per sprint] stories per sprint and [TODO: QA count] engineers — the numbers add up fast. Let me show you the next one."

---

### Demo Input Description

> **TODO (Gopi):** Describe the synthetic user story used for the demo. Format: Epic, Story title, Acceptance criteria (3–5 points). Store the actual input in `poc-01-testcase-gen/samples/`.

---

### Expected Output

> **TODO (Gopi):** Describe the expected Excel output. How many test cases? What columns? What does a "good" row look like? Paste a sample row here for rehearsal reference.

---

### Recovery Script (If Demo Fails)

> **TODO (Gopi):** Prepare a static fallback. Suggested: pre-run the demo, save the Excel output, have it open in a tab. Script:
> "The live connection isn't cooperating — let me show you the output I prepared earlier. [Switch to pre-saved Excel.] This is exactly what the tool generated from the same input. The live version would produce this in real time."

---
---

## PoC 02 — JIRA Defect Creator

### 90-Second Narration Script

**Hook (0–10s):**
> "Raising a good JIRA defect takes [TODO: X minutes] when done properly — environment, steps to reproduce, severity, expected vs. actual. Most engineers shortcut it. QA-Forge doesn't."

**Problem (10–20s):**
> "Here's a defect I found in the payment flow. [Show freetext description on screen.] In 2 sentences, I've described what went wrong. Watch what happens."

**Demo Action (20–60s):**
> "I paste my description into QA-Forge Defect Creator. Hit Create. [Pause.] Claude is structuring the summary, writing reproducible steps, inferring severity, adding environment metadata. It's calling the JIRA API now."

**Result (60–75s):**
> "[Open JIRA in browser.] The ticket is live. [Scroll through ticket.] Complete summary, clear steps to reproduce, severity set to [TODO], labels applied, component assigned. Ready for triage."

**Impact (75–90s):**
> "From freetext to complete JIRA ticket in [TODO: seconds]. No back-and-forth from developers asking 'how do I reproduce this?' That's [TODO: time] saved per defect, [TODO: defects/sprint] defects a sprint."

---

### Demo Input Description

> **TODO (Gopi):** Describe the synthetic payment failure defect description used for demo. Include environment, actual behaviour, expected behaviour (all synthetic). Store in `poc-02-defect-creator/samples/`.

---

### Expected Output

> **TODO (Gopi):** Describe the expected JIRA ticket fields: Summary, Description, Steps to Reproduce, Severity, Priority, Labels, Component. Paste the expected ticket content here.

---

### Recovery Script (If Demo Fails)

> **TODO (Gopi):** If JIRA API fails — show pre-created ticket screenshot. If Claude API fails — show pre-generated JSON output. Script:
> "The JIRA connection dropped — let me show you the structured output that would have been created. [Show JSON or screenshot.] This is the exact payload QA-Forge generated; in a live session it would be in JIRA right now."

---
---

## PoC 03 — Selenium → Playwright Converter

### 90-Second Narration Script

**Hook (0–10s):**
> "We have [TODO: X] Selenium tests. Playwright is the standard. Migration by hand is [TODO: time estimate] of work. Watch this."

**Problem (10–20s):**
> "Here's a Selenium test for our login flow. [Show Selenium code.] Python, WebDriver, old-style locators. Migrating this manually means rewriting every selector, every wait, every assertion."

**Demo Action (20–60s):**
> "I drop this file into QA-Forge Converter. Hit Convert. [Pause — watch output.] Claude is analysing the structure, mapping Selenium APIs to Playwright equivalents, modernising the locators, converting waits to async/await."

**Result (60–75s):**
> "Output Playwright script. [Open file.] Notice: `page.locator()` instead of `find_element`, `await expect()` for assertions, proper `async` structure. I run it — [TODO: confirm it executes] — green."

**Impact (75–90s):**
> "One script migrated in [TODO: seconds] vs [TODO: manual hours]. Scale that to [TODO: script count] scripts — that's [TODO: weeks] of migration work compressed. The QA team stays focused on new coverage, not maintenance."

---

### Demo Input Description

> **TODO (Gopi):** Describe the synthetic Selenium script used. Language (Python/Java), what it tests (login? payment form?), complexity level. Store in `poc-03-selenium-to-playwright/input/`.

---

### Expected Output

> **TODO (Gopi):** Describe the expected Playwright TypeScript output. Does it run? What framework (Playwright test)? Store in `poc-03-selenium-to-playwright/output/`.

---

### Recovery Script (If Demo Fails)

> **TODO (Gopi):** Pre-run conversion and save the `.ts` output. Show side-by-side comparison (Selenium input left, Playwright output right) as a static slide. Script:
> "Let me show you the conversion I ran earlier. [Open side-by-side.] On the left, the Selenium original. On the right, the Playwright output QA-Forge produced."

---
---

## PoC 04 — UI Vision (Screenshot → Test Scenarios)

### 90-Second Narration Script

**Hook (0–10s):**
> "Exploratory testing from a UI is pure human skill — or is it? I want to show you Claude reading a banking screen and suggesting test cases I hadn't thought of."

**Problem (10–20s):**
> "Here's a mockup of our loan application form. [Show screenshot.] A new QA engineer sitting down with this screen might miss edge cases in [TODO: field name], validation on [TODO: field], or the flow when [TODO: scenario]. Let's see what Claude sees."

**Demo Action (20–60s):**
> "I upload the screenshot to QA-Forge UI Vision. Hit Analyse. [Pause.] Claude is identifying UI components: form fields, dropdowns, buttons, validation zones. It's generating test scenarios for each."

**Result (60–75s):**
> "Output: [TODO: N] test scenarios. [Scroll through JSON output or rendered list.] Look at scenario 4 — [TODO: quote a good unexpected scenario]. That's an edge case I'd likely have missed in manual exploratory testing."

**Impact (75–90s):**
> "First-pass test scenario coverage from a screenshot in [TODO: seconds]. Especially valuable for new features where there are no existing test cases yet."

---

### Demo Input Description

> **TODO (Gopi):** Describe the synthetic banking UI screenshot used. What screen (loan form, KYC upload, payment confirmation)? Where is it stored (`poc-04-ui-vision/screenshots/`)?

---

### Expected Output

> **TODO (Gopi):** Describe the expected JSON output format. How many scenarios? What fields per scenario (Scenario ID, Description, Test Steps, Expected Result)?

---

### Recovery Script (If Demo Fails)

> **TODO (Gopi):** Pre-run analysis and save JSON output. Show screenshot + JSON side-by-side as static slide. Script:
> "Let me show you what QA-Forge produced when I ran this earlier. [Show screenshot + JSON.] [TODO: highlight best scenario]. This is the output that would have appeared live."
