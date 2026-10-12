# Simulator test scripts (expected behaviour)

Run each in a fresh simulator session (reset the conversation between tests). Screenshot each one. Bot replies below are the designed responses; wording appears exactly as written in the agent.

## T1: Happy path with slot-filling and anonymous reporting
| Turn | User | Expected bot behaviour |
|---|---|---|
| 1 | hi | Welcome, AI disclosure, privacy reminder, menu chips (Report an issue / Recycling help / Talk to a person) |
| 2 | There is a water leak in Building C that has been running all morning | `incident.report` matched. Session params: incident_type = water leak, building = Building C, urgency = ongoing. Enters Incident Reporting flow and asks only for **location_detail** |
| 3 | Level 2 kitchen near the dishwasher | Route `FINAL AND urgency = ongoing` sets priority = P2; Assign Team sets assigned_team = Facilities & Energy Management; summary shown with "Is this correct?" |
| 4 | yes | Follow-up Preference: email updates or stay anonymous |
| 5 | no, stay anonymous | contact_preference = anonymous; Report Submitted with team + priority; flow ends and returns to the main menu |
| 6 | bye | `conversation.end`, goodbye, session ends |

## T2: Urgent escalation (hazardous spill)
| Turn | User | Expected |
|---|---|---|
| 1 | there's a chemical spill in the warehouse and it's spreading | type = hazardous spill, building = Warehouse, urgency = urgent; asks for location |
| 2 | next to loading bay 3 | Route 1 (urgent) sets P1; **Urgent Safety Check** message (000, Security ext 5555, keep clear); Assign Team sets EHS; confirmation summary |
| 3 | yes > yes > name@corvale.com.au | Email collected (redacted in logs); Report Submitted |

## T3: Correction, reprompt and fallback escalation
| Turn | User | Expected |
|---|---|---|
| 1 | I want to report an issue | Asks for incident type (with chips) |
| 2 | the thing is broken | no-match-1 reprompt listing the five types |
| 3 | lights left on | type = energy waste; asks building |
| 4 | Building A | asks location, then urgency |
| 5 | meeting room 4 > minor | P3; summary |
| 6 | no | "No problem, let's fix it": parameters cleared, questions asked again |
| 7 | (type three unrecognised answers to the first question, for example "asdf") | no-match-1, no-match-2, then no-match-3 hands over to the **Human Handoff** flow (live-agent handoff message) |

## T4: Recycling side journey, then switch to reporting
| Turn | User | Expected |
|---|---|---|
| 1 | which bin does a coffee cup go in? | Waste Guidance flow: coffee cup guidance; returns to menu |
| 2 | how do I recycle batteries | Battery guidance (fire risk, B-cycle drop-off) |
| 3 | talk to a person | Human Handoff: ESG Operations Desk and confidential Speak Up line |
