---
file: PITCH_CONTEXT.md
project: testpilot
owner: Gopi
created: 2026-04-30
status: FILL BEFORE PITCH — items marked [GOPI-FILL] require your input
---

# PITCH CONTEXT — TestPilot Manager Presentation

> This file is loaded into Claude Project so Claude can tailor all pitch-prep assistance
> to your specific audience, date, and success criteria.
> Fill every [GOPI-FILL] before Day 9 (2026-05-07).

---

## 1. Audience

| Field | Value |
|-------|-------|
| Manager name | Rajesh Kumar |
| Manager role / title | QA Manager |
| Direct team size | 12 engineers |
| Domain / product line | Finastra banking products — [GOPI-FILL: specific product e.g. Fusion Essence, Lending] |
| Manager's AI familiarity | [GOPI-FILL: Skeptic / Curious / Enthusiastic] |
| Manager's primary concern | [GOPI-FILL: e.g. data security, cost, adoption, compliance, speed] |

---

## 2. Pitch Format

| Field | Value |
|-------|-------|
| Target pitch date | Day 10 — 2026-05-08 (or earlier if manager available) |
| Confirmed date | [GOPI-FILL: confirm with manager by Day 7] |
| Format | [GOPI-FILL: Deck only / Live demo / Deck + demo / Informal walkthrough] |
| Setting | [GOPI-FILL: 1:1 meeting / Team meeting / Formal review] |
| Time available | [GOPI-FILL: 15 min / 30 min / 60 min] |
| Slides tool | [GOPI-FILL: PowerPoint / Google Slides / see docs/pitch/] |

---

## 3. Success Criteria — What "Yes" Looks Like

Rank these outcomes. Pitch to the Target; celebrate the Minimum; stretch for the Stretch.

| Tier | What it means | Your version |
|------|--------------|-------------|
| **Minimum** | "Keep exploring" — verbal encouragement, no budget | [GOPI-FILL: acceptable?] |
| **Target** | Pilot budget approved; 2–4 week pilot with 1–2 QA team members | [GOPI-FILL: realistic?] |
| **Stretch** | Escalation to QA lead / Director; cross-team roadmap | [GOPI-FILL: plausible given manager's level?] |

**What specific ask will you make at the end of the pitch?**
[GOPI-FILL: e.g. "I'd like 2 weeks and 1 more QA colleague to run a formal pilot on the next sprint."]

---

## 4. Known Objections — Top 3

Prepare a 30-second response to each before Day 9.

| # | Likely Objection | Prepared Response |
|---|-----------------|------------------|
| 1 | "Is this compliant? Can we send data to an external AI?" | Data is synthetic-only for PoC; production routes via InfoSec-approved gateway (Bedrock). Sanitizer layer rejects PII before any API call. See SECURITY.md. |
| 2 | "The output needs human review anyway — where's the time saving?" | The save is in the first-draft generation (80% of the effort). Human review of a draft takes 10 min vs writing from scratch takes [X] hrs. |
| 3 | "What if it generates incorrect test cases? We can't ship faulty tests in a banking product." | Every output is labelled "AI-GENERATED — requires human review." The tool accelerates first-draft creation; a QA engineer still owns sign-off. Hallucinations show up as obviously vague steps — easier to catch in review than a missed test case that was never written at all. |

**Additional objections your manager might raise:**
- "Who maintains this when you're busy?" — It's a thin FastAPI wrapper around a prompt file. Any QA engineer can update the prompt in `docs/prompts/testcase-gen-master.md`; no ML knowledge needed.
- "What's the ongoing cost?" — Claude Sonnet 4.6 via API: ~$3 per 1 M input tokens. A full test case generation run is ~2 K tokens → less than $0.01 per run. 12 engineers × 5 runs/day = under $1/day.
- "What about model updates breaking the output?" — The prompt pins the JSON schema. Output format is validated by the parser before anything reaches Excel; schema violations surface immediately as errors, not silently wrong test cases.

---

## 5. Demo Flow

Recommended order — lead with the highest-impact, lowest-risk PoC.

| Order | PoC | Why this order | Status |
|-------|-----|---------------|--------|
| 1st | **poc-01: Test Case Generator** | Highest daily-use impact; universal QA pain point; safest live demo | Build by Day 4 |
| 2nd | **poc-02: JIRA Defect Creator** | Tangible output (real JIRA ticket); manager can verify live | Build by Day 6 |
| 3rd | **poc-04: UI Vision** | Visual = memorable; shows AI vision capability; screenshot is safe demo content | Build by Day 8 |
| Skip live | **poc-03: Selenium → Playwright** | Code-heavy; less relatable to non-technical manager; show video instead | Build by Day 7 |

**Demo script location:** `poc-XX/DEMO.md` for each PoC
**Fallback plan:** [GOPI-FILL: if live demo fails mid-pitch, have recorded video ready]

---

## 6. Post-Pitch Ask — The Specific Next Step

The pitch ends with one concrete ask. Write it here and rehearse it verbatim.

**Your ask:** [GOPI-FILL — example: "Can we schedule a 30-minute follow-up next week to define the pilot scope — which team, which sprint, and what success looks like?"]

**If the answer is "maybe later":** Ask for one of these instead:
- "Can I send you a 1-page summary to share with the team?"
- "Can I demo this to one more person on the team for feedback?"
- "What would need to be true for you to say yes to a pilot?"

---

## 7. Competitive Context

> Fill if your manager will ask "why not use [other tool]?"

| Alternative | Why TestPilot is better for your context |
|-------------|------------------------------------------|
| GitHub Copilot | Copilot is code-completion; TestPilot generates QA artifacts (test cases, defect tickets) tailored to banking domain |
| ChatGPT / raw Claude | No structured output, no sanitization layer, no banking domain prompt engineering, no Excel output |
| Existing ALM tools (Micro Focus ALM, Zephyr) | These manage test cases; TestPilot generates them — complementary, not competing |
| [GOPI-FILL: other tool your team uses] | [GOPI-FILL: your differentiation] |
