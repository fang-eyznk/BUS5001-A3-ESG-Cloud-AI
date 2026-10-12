# Conversation design (generated from the agent JSON)

## Intents

| Intent | Parameters | # phrases | Example training phrases |
|---|---|---|---|
| Default Negative Intent | - | 0 | fallback (no-match) |
| Default Welcome Intent | - | 12 | "hello GreenDesk"; "start"; "what can you do" |
| agent.human | - | 14 | "operator"; "I need a staff member"; "get me a person" |
| confirmation.no | - | 17 | "that's not right"; "change it"; "start again" |
| confirmation.yes | - | 18 | "that's correct"; "sure"; "go ahead" |
| conversation.end | - | 11 | "close the chat"; "thank you bye"; "all good thanks" |
| incident.report | incident_type (@incident_type), building (@building), urgency (@urgency_level) | 29 | "log a facilities issue"; "I want to report a water leak"; "There is a water leak in Building C that has been running all morning" |
| waste.guidance | waste_item (@waste_item) | 22 | "Which bin does a coffee cup go in?"; "can coffee cups be recycled"; "How do I recycle batteries?" |

## Entity types (map entities, fuzzy matching on)

| Entity | Reference values | Example synonyms |
|---|---|---|
| @building | Building A, Building B, Building C, Building D, Main Building, Warehouse, Car Park | Block A, A Block; Block B, B Block; Block C, C Block ... |
| @incident_type | water leak, energy waste, waste contamination, hazardous spill, accessibility barrier | leak, leaking; wasting energy, lights left on; recycling contamination, contaminated recycling ... |
| @urgency_level | urgent, ongoing, minor | emergency, dangerous; still happening, still running; small, not urgent ... |
| @waste_item | coffee cup, soft plastics, batteries, e-waste, food scraps, paper and cardboard, glass, printer cartridges, plastic bottles and containers | coffee cups, takeaway cup; soft plastic, plastic bag; battery, AA batteries ... |

## Flows, pages and routes

### Flow: Default Start Flow

_Entry point: welcome, AI disclosure and routing to the Incident Reporting, Waste Guidance or Human Handoff flows._

Start-page routes (in scope on every page of this flow):

| Trigger | Sets | Target |
|---|---|---|
| intent `Default Welcome Intent` | - | (stay) |
| intent `incident.report` | - | flow: Incident Reporting |
| intent `waste.guidance` | - | flow: Waste Guidance |
| intent `agent.human` | - | flow: Human Handoff |
| intent `conversation.end` | - | End Session |

Flow event handlers: sys.no-match-default, sys.no-input-default

### Flow: Incident Reporting

_Structured sustainability incident capture: form filling, urgency-based escalation, team assignment, confirmation, optional follow-up consent._

Start-page routes (in scope on every page of this flow):

| Trigger | Sets | Target |
|---|---|---|
| condition `true` | - | Collect Incident Details |
| intent `agent.human` | - | flow: Human Handoff |

Flow event handlers: sys.no-match-default, sys.no-input-default

#### Page: Assign Team

| Trigger | Sets | Target |
|---|---|---|
| condition `$session.params.incident_type = "water leak" OR $session.params.incident_type = "energy waste"` | assigned_team=Facilities & Energy Management | Confirm Report |
| condition `$session.params.incident_type = "waste contamination"` | assigned_team=Waste & Recycling Services | Confirm Report |
| condition `$session.params.incident_type = "hazardous spill"` | assigned_team=Environment, Health & Safety (EHS) | Confirm Report |
| condition `$session.params.incident_type = "accessibility barrier"` | assigned_team=Accessibility & Inclusion team with Facilities | Confirm Report |
| condition `true` | assigned_team=ESG Operations Desk | Confirm Report |

#### Page: Collect Email

| Form parameter | Entity | Required | Redacted | Reprompt handlers |
|---|---|---|---|---|
| followup_email | @sys.email | True | True | sys.no-match-1, sys.no-match-2, sys.no-input-default |

| Trigger | Sets | Target |
|---|---|---|
| condition `$page.params.status = "FINAL"` | contact_preference=email updates | Report Submitted |
| intent `confirmation.no` | contact_preference=anonymous (no follow-up), followup_email=None | Report Submitted |

#### Page: Collect Incident Details

| Form parameter | Entity | Required | Redacted | Reprompt handlers |
|---|---|---|---|---|
| incident_type | @incident_type | True | False | sys.no-match-1, sys.no-match-2, sys.no-match-3 -> Human Handoff, sys.no-input-default |
| building | @building | True | False | sys.no-match-1, sys.no-match-2, sys.no-match-3 -> Human Handoff, sys.no-input-default |
| location_detail | @sys.any | True | True | sys.no-match-1, sys.no-match-2, sys.no-input-default |
| urgency | @urgency_level | True | False | sys.no-match-1, sys.no-match-2, sys.no-match-3 -> Human Handoff, sys.no-input-default |

Entry message: "Thanks for reporting this. I'll ask a few quick questions; it takes about a minute. If this is about a person's conduct or wellbeing, say 'talk to a person' instead."

| Trigger | Sets | Target |
|---|---|---|
| condition `$page.params.status = "FINAL" AND $session.params.urgency = "urgent"` | priority=P1 - respond within 1 hour | Urgent Safety Check |
| condition `$page.params.status = "FINAL" AND $session.params.incident_type = "hazardous spill"` | priority=P1 - respond within 1 hour | Urgent Safety Check |
| condition `$page.params.status = "FINAL" AND $session.params.urgency = "ongoing"` | priority=P2 - same business day | Assign Team |
| condition `$page.params.status = "FINAL"` | priority=P3 - within 3 business days | Assign Team |

#### Page: Confirm Report

Entry message: "Here's your report:
- Issue: $session.params.incident_type
- Location: $session.params.building, $session.params.location_detail
- Urgency: $session.params.urgency ($session.params.priority)
- Will be sent to: $session.p..."

| Trigger | Sets | Target |
|---|---|---|
| intent `confirmation.yes` | - | Follow-up Preference |
| intent `confirmation.no` | incident_type=None, building=None, location_detail=None, urgency=None, priority=None, assigned_team=None, followup_email=None, contact_preference=None | Collect Incident Details |

Page event handlers: sys.no-match-default, sys.no-input-default

#### Page: Follow-up Preference

Entry message: "Would you like updates on this report by email? Your email is used only to update you about this report. Say 'no' to submit it anonymously."

| Trigger | Sets | Target |
|---|---|---|
| intent `confirmation.yes` | - | Collect Email |
| intent `confirmation.no` | contact_preference=anonymous (no follow-up) | Report Submitted |

Page event handlers: sys.no-match-default

#### Page: Report Submitted

Entry message: "Thank you. Your report has been logged and sent to $session.params.assigned_team with priority $session.params.priority. Contact preference: $session.params.contact_preference. Reports like yours feed our monthly ESG das..."

| Trigger | Sets | Target |
|---|---|---|
| condition `true` | incident_type=None, building=None, location_detail=None, urgency=None, priority=None, assigned_team=None, followup_email=None, contact_preference=None | End Flow |

#### Page: Urgent Safety Check

Entry message: "This sounds urgent. If anyone is injured or in immediate danger, call 000 now, then Site Security on extension 5555. Please keep a safe distance and don't try to clean up chemicals yourself. I'm flagging this as Priority..."

| Trigger | Sets | Target |
|---|---|---|
| condition `true` | - | Assign Team |

### Flow: Waste Guidance

_Side journey: disposal guidance for common workplace items (reduces recycling contamination)._

Start-page routes (in scope on every page of this flow):

| Trigger | Sets | Target |
|---|---|---|
| condition `true` | - | Identify Item |
| intent `agent.human` | - | flow: Human Handoff |
| intent `incident.report` | - | flow: Incident Reporting |

Flow event handlers: sys.no-match-default, sys.no-input-default

#### Page: Identify Item

| Form parameter | Entity | Required | Redacted | Reprompt handlers |
|---|---|---|---|---|
| waste_item | @waste_item | True | False | sys.no-match-1, sys.no-match-2, sys.no-match-3 -> Human Handoff, sys.no-input-default |

| Trigger | Sets | Target |
|---|---|---|
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "coffee cup"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "soft plastics"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "batteries"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "e-waste"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "food scraps"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "paper and cardboard"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "glass"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "printer cartridges"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL" AND $session.params.waste_item = "plastic bottles and containers"` | waste_item=None | End Flow |
| condition `$page.params.status = "FINAL"` | waste_item=None | End Flow |

### Flow: Human Handoff

_Escalation endpoint: live-agent handoff to the ESG Operations Desk and signposting of confidential channels._

Start-page routes (in scope on every page of this flow):

| Trigger | Sets | Target |
|---|---|---|
| condition `true` | - | Connect to Person |

Flow event handlers: sys.no-match-default, sys.no-input-default

#### Page: Connect to Person

Entry message: "I'll connect you with the ESG Operations Desk (staffed Monday to Friday, 8am to 6pm). What you've told me so far will be passed on, so you won't need to repeat yourself."

| Trigger | Sets | Target |
|---|---|---|
| condition `true` | - | End Session |
