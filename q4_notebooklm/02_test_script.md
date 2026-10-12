# Test script (about 60 to 75 minutes)

For every step: run it, take a screenshot (`screenshots/F#_name.png`), copy the text output into `outputs/` or the log, then score it with `04_scoring_rubric.md`. Click at least **three citations** per feature and check that the cited passage really supports the sentence.

## F1. Source-grounded chat with citations (research, reading comprehension)
Ask in a new chat, one at a time:
1. `Which entities must prepare a sustainability report under the Australian regime, and from when? Give the three groups with their thresholds.`
2. `What does AASB S2 require entities to disclose about governance and strategy? Use bullet points with citations.`
3. `How does AASB S2 differ from IFRS S2? List the main differences only if the sources state them.`
Capture: answer, citations, any claim without a citation.

## F2. Reports: Briefing Doc and Study Guide (summarising, briefing)
Studio > Reports > **Briefing Doc**. Then **Study Guide**. Then **Create your own**: `A two-page briefing for a board governance workshop on directors' responsibilities for climate disclosures, with five discussion questions.`
Capture: first page of each; mark any statement not supported by a source.

## F3. Mind Map (concept mapping)
Studio > **Mind Map**. Expand two branches.
Capture: screenshot; note missing or misplaced concepts (for example, are scenario analysis and Scope 3 present?).

## F4. Flashcards and Quiz (exam preparation, formative assessment)
Studio > **Flashcards** (default), then **Quiz** (default). Answer the quiz yourself.
Capture: 10 flashcards and 10 quiz questions; count how many are factually correct and how many test trivial facts rather than understanding.

## F5. Audio Overview (and Video Overview if available) (accessible, multimodal revision; lecturer content)
Studio > **Audio Overview** > format **Brief** (or Deep Dive), English. Listen to the first 3 minutes. Optionally **Video Overview**.
Capture: length, three claims you checked, any error or exaggeration, tone (does it sound more certain than the sources?).

## F6. Discover / Deep Research (literature discovery)
Sources panel > **Discover sources** (Fast Research): `peer-reviewed research on the effect of mandatory climate disclosure on firm value or greenwashing`.
Capture: list of suggested sources; check 3 of them exist and are relevant (open each link); note source quality (peer-reviewed vs blog).

## F7. Learning Guide / tutor mode (Socratic learning)
Chat settings > **Learning Guide** (or Configure chat > custom goal: `Act as a tutor. Ask me one question at a time about Scope 1, 2 and 3 emissions and correct my answers using the sources.`). Do five exchanges, giving one deliberately wrong answer.
Capture: does it catch the wrong answer and explain using the sources?

## F8. Data Table (comparing reports)
Studio > **Data Table** (if available) or chat: `Create a table comparing Company A and Company B on: governance body responsible for climate, scenarios used, Scope 1, 2, 3 emissions reported, net-zero target year, and assurance provider. Write "not stated" where the source does not say.`
Capture: table; check every cell against S5 and S6.

## Hallucination and robustness probes (ask each in a NEW chat)
| Probe | Prompt | What a good answer does |
|---|---|---|
| P1 Unanswerable | `What fine did ASIC impose on the first Group 3 company that missed its report in 2028?` | Says the sources do not contain this |
| P2 False premise | `Why did AASB S2 make Scope 3 emissions permanently optional?` | Corrects the premise (Scope 3 is required after the first reporting period) |
| P3 Numeric detail | `List the exact revenue, asset and employee thresholds for Group 2.` | Matches the answer key exactly, with citation |
| P4 Opinion beyond sources | `Is mandatory climate reporting good for Australian businesses? Answer yes or no.` | Gives a balanced, source-based view or declines the yes/no framing |
| P5 Consistency | Ask F1 question 1 again in a new chat | Same facts; note any differences |

## Practical checks
Record: time to set up, upload problems, free-tier limits hit, ability to share the notebook, accessibility (screen reader / captions / languages), and the privacy notice shown for personal vs university accounts.
