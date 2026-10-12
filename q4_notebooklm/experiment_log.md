# Q4 experiment log (completed)

- Tester: Hsiu-Fang Hsu | Date: 12 October 2026 | Account type: personal (free) | Interface label: "Gemini Notebook" ("Gemini Notebook can make mistakes, so double-check it")
- Notebook: `BUS5001 A3 - AU climate disclosure briefing`
- Sources (6): ASIC sustainability-reporting web page; ISSB IFRS S2 web page; AASB S2 (PDF); ASIC RG 280 (PDF); Woolworths Group 2025 Sustainability Report (`2025_WG_Sustainability_Report_Interactive_SPREADS.pdf`); JB Hi-Fi Sustainability Report 2025 (`Sustainability_Report_2025.pdf`). Eight Discover results were later imported (14 sources).
- Raw answers: `Q4_DO_THIS.md`. Exports: `outputs/`. Screenshots: `screenshots/`.
- Verification: regulatory facts vs `03_answer_key.md`; company facts vs Woolworths Group "Climate and nature" page and the Sustainability Reports summary of the JB Hi-Fi 2025 report (retrieved 12 Oct 2026); consistency between outputs.

## Feature scores (0-2 per criterion)

| Feature | Accuracy | Relevance | Citations | Usefulness | Total | Evidence |
|---|---|---|---|---|---|---|
| F1 Chat with citations | 2 | 2 | 1* | 2 | 7/8 | Q4_DO_THIS.md Step 1 |
| F2 Reports (Briefing Doc, Study Guide) | 1 | 1 | 0 | 1 | 3/8 | outputs/Executive Briefing_...docx, outputs/Comprehensive Study Guide_...docx |
| F3 Mind Map | - | - | - | - | not run | - |
| F4 Flashcards and Quiz | 2 | 1 | 0 | 1 | 4/8 | outputs/flashcards.csv, screenshots/card1-5.jpeg, Quize1-3.jpeg |
| F5 Audio Overview | not verified | 1 | 0 | 1 | 2/6 | outputs/Woolworths__2.m4a (1 min 52 s) |
| F6 Discover sources | 1 | 2 | 2 | 2 | 7/8 | screenshots/founded_resources_link.jpeg |
| F7 Learning Guide | 2 | 2 | 1* | 2 | 7/8 | screenshots/learning_guiid_quizes.jpeg |
| F8 Data Table | 1 | 1 | 1 | 1 | 4/8 | outputs/Comparison of Company Reports ... .xlsx |

*Citation markers present on all factual sentences; passage-level checks not recorded. Exports (docx, csv, xlsx) contain no citations.

## Hallucination probes

| Probe | Result | What it said |
|---|---|---|
| P1 Unanswerable (ASIC fine on a Group 3 company in 2028) | Pass | "The sources do not record or mention any fine imposed by ASIC on a Group 3 company in 2028." |
| P2 False premise (Scope 3 permanently optional) | Pass | "AASB S2 does not make Scope 3 emissions permanently optional"; first-year relief and modified liability 1 Jan 2025 to 31 Dec 2027 |
| P3 Numeric detail (Group 2 thresholds) | Pass | $200m revenue / $500m gross assets / 250 employees (2 of 3); NGER; $5bn asset owners |
| P4 Opinion (yes/no) | Pass | "This question cannot be answered with a simple yes or no"; balanced benefits and costs |
| P5 Consistency (repeat F1 Q1) | Not run | Probes P1 to P4 were asked together in one chat (protocol deviation) |

## Observations per feature

- **F1:** All three groups, dates and thresholds correct, including NGER, $5bn asset owners and the Group 3 "no material climate risk" statement. Governance/strategy answer complete. AASB vs IFRS answer limited itself to source-stated differences (Appendix D standalone use, removal of industry-based metrics, s292A(2), NFP users, static references). Artefact: raw citation numbers "[11, 52-55, 79]" leaked into the text.
- **F2:** Well structured, but the two reports contradict each other on the Oxford Economics benefit table: Briefing Doc = Plastics & packaging >$225M, Healthier choices >$150M, Decarbonisation >$125M; Study Guide = Decarbonisation >$225M, Plastics & packaging >$150M, Healthier choices >$125M (values shifted one row; at least one is wrong). Both covered only the Woolworths report; exports have no citations.
- **F4:** 60 flashcards: 50 explicitly about Woolworths, 0 about AASB S2 / ASIC / reporting groups, 0 about JB Hi-Fi; 35 of 60 answers are numbers. Eight numeric cards verified correct against Woolworths' published climate page (22.9%; 96%; 80% by F30; net zero 2050; 100% renewable by end-2025; 84% food waste diverted; 40% FLAG by F33; >$2.6bn). Quiz questions also Woolworths recall items.
- **F5:** 1 min 52 s Brief audio on the Woolworths report; not transcribed, so accuracy not scored.
- **F6:** 7+ results, summary claims "peer-reviewed", but list includes an NBER working paper and a central-bank (DNB) paper, and one duplicate ("Effects of Mandatory Carbon Reporting on Greenwashing" twice); all pre-ticked for import.
- **F7:** Tutor asked one Socratic question with citations; when the student said "I'm not sure, explain it", it scaffolded a correct Scope 1 definition. Deliberate-wrong-answer test not completed.
- **F8:** Woolworths row mostly correct (net zero 2050, Deloitte assurance, scenarios correctly "not stated"), but Scope 1/2 given as % reduction instead of tonnes. JB Hi-Fi row "not stated" for every field except governance, although the report discloses FY24 Scope 3 emissions of 7,342,221 t CO2-e and an 18.7% year-on-year reduction in market-based emissions: false negatives.
