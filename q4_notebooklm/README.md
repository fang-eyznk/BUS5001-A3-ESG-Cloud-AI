# Q4: Evaluating Gemini Notebook (formerly NotebookLM) for university use

Google renamed NotebookLM to **Gemini Notebook** on 16 July 2026; existing notebooks carried over. The report uses "NotebookLM (now Gemini Notebook)".

This folder is the **experiment protocol and evidence log** for Q4. Everything was run with the free personal tier.

| File | Purpose |
|---|---|
| `01_scenario_and_sources.md` | The academic scenario and the exact sources uploaded |
| `02_test_script.md` | Step-by-step test script: one block per feature, with exact prompts and what to capture |
| `03_answer_key.md` | Ground truth used to score accuracy and to detect hallucinations |
| `04_scoring_rubric.md` | 0-2 scoring scale for accuracy, relevance, citation faithfulness and usefulness |
| `experiment_log.md` | **Filled in during testing**: outputs, scores, observations, screenshot names |
| `screenshots/` | Screenshot evidence, named `F1_chat_answer.png`, `F2_briefing_doc.png`, and so on |
| `outputs/` | Copied text of generated outputs (briefing doc, study guide, quiz, flashcards, data table, audio transcript notes) |

## Method in one paragraph

One notebook, one realistic ESG academic scenario, eight features. Each feature is used the way a student, researcher or lecturer would actually use it, with fixed prompts so the test is repeatable. Every factual claim in the outputs is checked against `03_answer_key.md` and against the cited passage (citation faithfulness). Five deliberate **hallucination probes** (unanswerable question, false premise, numeric detail, out-of-scope opinion and repeat-question consistency) test failure modes. Scores use the 0-2 rubric so features can be compared.
