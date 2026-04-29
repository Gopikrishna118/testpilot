---
file: GLOSSARY.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# GLOSSARY — TestPilot Terms of Reference

> **TODO (Gopi):** Expand definitions with Finastra-specific context where relevant before the pitch. Definitions marked with * are especially important for non-QA stakeholders in the pitch audience.

---

## Section 1: Banking Terms

| Term | Definition |
|------|-----------|
| **KYC** (Know Your Customer) | Regulatory process banks use to verify the identity of customers before and during service delivery; a key compliance workflow QA teams must test thoroughly. |
| **AML** (Anti-Money Laundering) | Set of laws, regulations, and procedures to prevent financial crimes; AML transaction monitoring is a high-coverage QA area in banking systems. |
| **PII** * (Personally Identifiable Information) | Any data that can identify an individual — name, account number, PAN, Aadhaar, phone, email. **Never** used in TestPilot inputs; replaced with synthetic equivalents. |
| **PAN** (Permanent Account Number) | 10-character alphanumeric Indian tax identifier (`ABCDE1234F` format). Classified as Restricted data. Never to be included in prompts. |
| **Aadhaar** | 12-digit unique identification number issued by UIDAI to Indian residents. Classified as Restricted data. Never to be included in prompts. |
| **IFSC** (Indian Financial System Code) | 11-character alphanumeric code identifying bank branches for NEFT/RTGS/IMPS transactions. Example: `HDFC0001234`. |
| **ISO 20022** | International standard for electronic data interchange between financial institutions; increasingly used for payment messaging (replaces SWIFT MT formats). Relevant for payment module test cases. |
| **Core Banking** | Centralized back-end system performing fundamental banking operations (accounts, loans, deposits); all channels (mobile, branch, ATM) connect to it. Usually the highest-criticality test domain. |

---

## Section 2: QA Terms

| Term | Definition |
|------|-----------|
| **Test Case** * | A documented set of inputs, execution preconditions, steps, and expected results designed to validate a specific software behaviour. The primary deliverable of poc-01. |
| **Defect** * (Bug) | A deviation between actual and expected software behaviour discovered during testing. The primary input to poc-02. |
| **Severity** | Classification of how badly a defect impacts the system (Critical / High / Medium / Low). Determined by the QA engineer; used in JIRA ticket creation. |
| **Priority** | Classification of how urgently a defect must be fixed (P1–P4). Determined by the product owner in consultation with QA. |
| **Regression** | Re-testing previously passing test cases after a code change to ensure nothing is broken. High-volume, high-cost — a key automation target. |
| **Smoke Test** | A shallow, fast test run covering the most critical paths to confirm a build is stable enough for full testing. Usually the first gate after a deployment. |
| **Acceptance Criteria** | Conditions defined in a user story that must be satisfied for the story to be considered "done"; the primary source of test case content for poc-01. |
| **RTM** (Requirements Traceability Matrix) | A document mapping each requirement to its corresponding test cases, ensuring full coverage and enabling impact analysis for change requests. |

---

## Section 3: AI / Claude Terms

| Term | Definition |
|------|-----------|
| **LLM** * (Large Language Model) | A deep learning model trained on vast text data capable of generating, summarising, and transforming natural language. Claude is an LLM built by Anthropic. |
| **Prompt** | The instruction text sent to an LLM to guide its output. Quality of the prompt directly determines quality of the output; see `docs/prompts/` for TestPilot master prompts. |
| **Hallucination** * | When an LLM generates plausible-sounding but factually incorrect or fabricated content. A key risk (R-01) in TestPilot; mitigated by human review and anti-hallucination prompt guards. |
| **Context Window** | The maximum amount of text (measured in tokens) an LLM can process in a single interaction. Claude Sonnet 4.6 has a 200K token context window. |
| **Token** | The basic unit of text processed by an LLM — roughly 0.75 words on average. API pricing is per token (input + output). Relevant to cost estimation in METRICS.md. |
| **Sonnet 4.6** | Claude Sonnet 4.6 — the AI model used across all TestPilot PoCs. Balance of capability, speed, and cost. Model ID: `claude-sonnet-4-6`. |
| **MCP** (Model Context Protocol) | Anthropic's open protocol allowing Claude to connect to external tools and data sources (e.g., JIRA, Confluence) in a standardised way. Relevant for production architecture. |
| **Agent** | An AI system that can autonomously take multi-step actions, use tools, and make decisions to complete a goal. Claude Code (used to build TestPilot) is an agent. Production TestPilot could be agentic. |
