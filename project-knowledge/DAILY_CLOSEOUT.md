---
file: DAILY_CLOSEOUT.md
project: testpilot
owner: Gopi
created: 2026-04-30
purpose: End-of-day ritual — run this checklist before closing your laptop
---

# DAILY CLOSEOUT — TestPilot Sprint Ritual

> Run this in order every day before closing your laptop.
> Target: 10 minutes max. If any step takes longer, note it as a blocker.

---

## Step 1 — Git Commit + Push

```bash
# From repo root
git status                          # confirm what you built today
git add <specific files>            # never git add -A blindly
git status                          # verify staged files look right
git commit -m "Day N: <what you built>"
git push origin main
```

**Commit message format:** `Day N: <PoC name or area> — <1-line description>`
Examples:
- `Day 3: poc-01 — Confluence input adapter + PromptBuilder tests`
- `Day 5: poc-02 — JIRA REST client + defect ticket generation`
- `Day 9: pitch — deck slides 1–8 complete`

**Checklist before committing:**
- [ ] `git status` shows no `.env` file staged
- [ ] No hardcoded API keys in any file (`grep -r "sk-ant" .` to check)
- [ ] No files from `outputs/` staged (gitignored but verify)

---

## Step 2 — Update CLAUDE.md Sprint Status

Open `CLAUDE.md` and update the `## Current Sprint Status` section:

1. Change today's Day N row from "In Progress" to "Done ✅"
2. Update the "Day N+1 — Next" section with tomorrow's actual first task
3. Note any carry-overs from today

**Template update:**
```
### Day N — Done (YYYY-MM-DD)
- [x] Task 1 completed
- [x] Task 2 completed
- [ ] Task 3 — CARRY OVER to Day N+1 (reason: ...)

### Day N+1 — Next (YYYY-MM-DD)
- First task: [SPECIFIC, not vague — e.g. "Write Confluence input adapter in prompt_builder.py"]
```

---

## Step 3 — Pitch-Prep Micro-Task (5 min)

Pick one small pitch-prep task every day, even on PoC build days.
**Do not skip this** — pitch is Day 10 and it creeps up fast.

| Day | Suggested Micro-Task |
|-----|---------------------|
| D2 | Measure and record manual baseline times (stopwatch) |
| D3 | Draft 3 manager objections + your responses in PITCH_CONTEXT.md |
| D4 | Record 90-second testcase-gen demo video |
| D5 | Confirm pitch date/time with manager |
| D6 | Record 90-second defect creator demo video |
| D7 | Fill in ROI_SUMMARY.md actuals |
| D8 | Record 90-second UI Vision demo video |
| D9 | Full pitch deck complete + rehearse once |
| D10 | Final rehearsal — time it (target: under 15 min) |

**Today's logged pitch-prep task:**
> [FILL AT CLOSEOUT: what did you do for pitch prep today?]

---

## Step 4 — Tomorrow's First Task (Pre-Written)

Write the **exact first action** for tomorrow before closing tonight.
Vague = bad. Specific = good.

| Bad | Good |
|-----|------|
| "Continue poc-01" | "Open `services/claude_client.py`, wire up the async complete() method, run with test input" |
| "Work on pitch" | "Open `PITCH_CONTEXT.md`, fill in manager name + objection #3" |
| "Fix the bug" | "Debug the AADHAAR regex in `sanitizer.py` — false positive on account numbers" |

**Tomorrow's first task:**
> [FILL AT CLOSEOUT: write it now while context is fresh]

---

## Step 5 — Token Budget Check

Quick check to keep Claude API costs visible.

```
Anthropic dashboard → Usage → Today's usage
```

| Metric | Log it here |
|--------|------------|
| Date | |
| Approximate input tokens today | |
| Approximate output tokens today | |
| Running API cost this sprint (USD) | |
| Estimated sprint total at this rate | |

**Note:** Claude Sonnet 4.6 via Claude Pro is included in subscription.
API costs apply only if you move to direct API usage (`ANTHROPIC_API_KEY` calls).

---

## Done Checklist

- [ ] Git committed and pushed
- [ ] CLAUDE.md Day N status updated
- [ ] Pitch-prep micro-task logged
- [ ] Tomorrow's first task written (specific, not vague)
- [ ] Token budget noted (if using API directly)
- [ ] Laptop closed

**Sprint days remaining:** [UPDATE DAILY]
**Next milestone:** [UPDATE DAILY — e.g. "poc-01 demo video by Day 4"]
