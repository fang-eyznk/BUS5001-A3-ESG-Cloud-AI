# BUS5001 Assessment 3: RPA, AI and Cloud-Enabled ESG Analytics

Evidence repository for the Assessment 3 report (La Trobe University, BUS5001 Cloud Platforms and Analytics, 2026 Semester 2).
Author: Hsiu-Fang Hsu. The organisation in the scenario, *Corvale Group*, is fictional.

| Folder | Question | What is inside |
|---|---|---|
| [`q1_dialogflow_cx/`](q1_dialogflow_cx/) | Q1 ESG chatbot | Importable Dialogflow CX agent (`corvale_greendesk_agent.zip`), the agent as readable JSON, design tables, simulator test scripts, video script, diagrams, conceptual webhook |
| [`q2_cloud_security/`](q2_cloud_security/) | Q2 cloud security | Snowflake 2024 incident timeline, sources, attack-chain and shared-responsibility diagrams |
| [`q3_llm_triage/`](q3_llm_triage/) | Q3 LLM triage | Colab notebook, experiment library, 40 labelled test messages, prompts, raw model outputs (JSONL), metrics, charts, robustness checks |
| [`q4_notebooklm/`](q4_notebooklm/) | Q4 NotebookLM / Gemini Notebook | Test protocol, source pack, prompts, answer key, scoring rubric, experiment log, screenshots, generated outputs |
| [`docs/`](docs/) | All | Generative AI use statement |

## Reproduce the Q3 experiment

1. Open `q3_llm_triage/Q3_ESG_Triage_Colab.ipynb` in Google Colab (File > Upload notebook).
2. `Runtime > Change runtime type > T4 GPU`, then `Runtime > Run all` (about 10 to 20 minutes).
3. The notebook downloads `q3_results.zip`; its contents are committed in `q3_llm_triage/results/`.

The rule-based baseline is deterministic and can also be run locally:

```bash
cd q3_llm_triage/src
python -c "import triage_lib as L; print(L.summarise([(g, L.rules_classify(g['message'])) for g in L.TEST_SET]))"
```

## Evidence index

| Report item | Evidence in this repository |
|---|---|
| Q1(c) Dialogflow implementation | `q1_dialogflow_cx/agent_export/`, `conversation_design.md`, screenshots in the report |
| Q1(c) Console and simulator evidence | `q1_dialogflow_cx/*.jpeg`, test results in `q1_dialogflow_cx/README.md` |
| Q1(e) Demo video | Microsoft Stream link in the report; copy in `q1_dialogflow_cx/GreenDesk_demo_executive_1m53s.mp4` |
| Q3(a) Prompt outputs | `q3_llm_triage/results/llm_original_raw_outputs.jsonl`, `llm_revised_raw_outputs.jsonl` |
| Q3(b) Baseline comparison | `q3_llm_triage/results/metrics_summary.csv`, `per_message_comparison.csv`, `robustness_checks.json`, `SUMMARY.md` |
| Q4 Experiment log | `q4_notebooklm/experiment_log.md` (scored), `Q4_DO_THIS.md` (raw answers), `screenshots/`, `outputs/` (exported briefing, study guide, flashcards, data table, audio) |
