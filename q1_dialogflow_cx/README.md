# Q1: Corvale GreenDesk, an ESG Sustainability Support Assistant (Dialogflow CX)

**Use case:** sustainability incident reporting (water leaks, energy waste, recycling contamination, hazardous spills, accessibility barriers), plus recycling guidance and escalation to a person.
**Organisation:** Corvale Group, a fictional ASX-listed property and facilities company (about 6,500 staff, 40 sites).

## Contents

| Path | What it is |
|---|---|
| `corvale_greendesk_agent.zip` | **Importable agent** (Dialogflow CX JSON package). Restore it into an empty agent (steps below) |
| `agent_export/` | The same agent unzipped, so the design can be read on GitHub (flows, pages, intents, entities as JSON) |
| `conversation_design.md` | Intents, entities, pages, routes, fallback and escalation logic in tables |
| `test_scripts.md` | Four simulator test conversations (happy path, urgent escalation, correction + fallback, recycling side journey) |
| `video_script.md` | Script and shot list for the demonstration video (under 2 minutes) |
| `diagrams/` | Conversation map and conceptual cloud workflow |
| `webhook_concept/main.py` | Conceptual Cloud Run webhook showing how a submitted report would become a ticket and an analytics event (not deployed) |

## Free ways to use Dialogflow CX (no cost to you)

Dialogflow CX (Conversational Agents, flows) charges about US$0.007 per text request. Building and testing this agent takes roughly 100 to 300 requests (under US$3), and you can cover that with free credit:

1. **Best: the subject's Google Cloud education credits (no credit card).** LMS > Module 10 > *Google Cloud Education Credits for Students*. Request the coupon with your La Trobe email, redeem it, and it creates a billing account funded by the credit. Create a new project, choose that billing account, enable the **Dialogflow API**, then create the agent. When credits run out, nothing is charged; access simply stops.
2. **Conversational Agents no-charge trial credit.** Google gives new Conversational Agents users US$600 of flow credit (valid 12 months), applied automatically on first use. The project still needs a billing account; if you don't have education credits, the standard Google Cloud free trial (US$300 for 90 days) provides one. It asks for a card to verify identity but does not charge unless you manually upgrade to a paid account.
3. **Protect yourself:** Billing > Budgets & alerts > create a US$5 budget with email alerts. Delete the project after the marks are released.

Do not switch to Dialogflow ES (which has a free edition): the rubric assesses a *Dialogflow CX* implementation.

## Restore the agent (about 5 minutes)

1. Open the Dialogflow CX / Conversational Agents console (`https://dialogflow.cloud.google.com/cx/` or `https://conversational-agents.cloud.google.com/`) and select your Google Cloud project.
2. **Create agent** > *Build your own* (flow-based) > name `Corvale GreenDesk`, location `global` (or `australia-southeast1`), time zone `Australia/Melbourne`, language English.
3. In the agent list, open the three-dot menu of the new agent > **Restore** > upload `corvale_greendesk_agent.zip` > Restore. (In the new console: *Agent settings > General > Export and import > Restore*.)
4. Wait for training to finish, then open **Test agent** (simulator) and type `hi`.

The zip follows Google's documented JSON-package format (display-name references, `agent.json` at the zip root). If the restore reports an error, build the agent manually using `conversation_design.md` (about 60 to 90 minutes); every value you need is in those tables.


## Evidence captured (12 October 2026)

| File | Shows |
|---|---|
| `diagram.jpeg` | Agent-level map of the four flows |
| `Incident_Reporting.jpeg` | Incident Reporting flow: pages and routes |
| `collect_Incident_Details.jpeg` | Collect Incident Details page: entry fulfillment, form parameters, FINAL routes |
| `incident_type.jpeg` | incident_type parameter prompt with chips payload |
| `training_process.jpeg` | NLU settings (Advanced NLU, threshold 0.3) and training completed for all flows |
| `GreenDesk_demo_executive_1m53s.mp4` | Demonstration video (1:53) submitted via Microsoft Stream |

| Test | Result | Note |
|---|---|---|
| T1 Happy path | Pass | issue, building and urgency filled from one sentence; P2 to Facilities & Energy |
| T2 Urgent escalation | Pass | safety message, P1, EHS |
| T3 Fallback + handoff | Partial | reprompts and handoff worked; synonym 'lights left on' not accepted at the form prompt (fix: answer intent with annotated phrases + CX test cases) |
| T4 Recycling + handoff | Pass | coffee cup and battery guidance; Speak Up signpost |

## Screenshots to capture for the report

1. Flow graph of **Incident Reporting** (Build tab).
2. The **Collect Incident Details** page showing the four form parameters and the route list.
3. The **incident.report** intent with annotated training phrases.
4. The **@incident_type** entity type.
5. Route conditions on **Collect Incident Details** and **Assign Team**.
6. Simulator: test script T1 (happy path), T2 (urgent escalation), T3 (correction + fallback) and T4 (recycling).
7. A parameter panel in the simulator showing `incident_type`, `building`, `urgency`, `priority` and `assigned_team` being filled.
8. Agent settings showing logging, and the `followup_email` / `location_detail` parameters marked **Redact in log**.
