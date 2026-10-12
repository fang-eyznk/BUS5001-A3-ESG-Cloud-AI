# Q3: LLM-based ESG message triage

| Path | Content |
|---|---|
| `Q3_ESG_Triage_Colab.ipynb` | End-to-end experiment for Google Colab (T4 GPU) |
| `src/triage_lib.py` | Test set with gold labels, original and revised prompts, rule-based baseline, zero-shot adapter, JSON parsing, metrics, charts |
| `data/test_messages_with_gold_labels.csv` | 40 messages: 5 brief samples, 23 extensions (incl. adversarial, privacy and bias probes), 12 hold-out |
| `prompts/` | Original prompt, revised system prompt, few-shot examples |
| `results/rules_baseline_local/` | Rule-based baseline run locally (deterministic) |
| `results/` | Colab run of 11 Oct 2026 (Tesla T4, 13.2 min): raw JSONL outputs, `metrics_summary.csv`, `per_message_comparison.csv`, `robustness_checks.json`, `SUMMARY.md`, charts, `run_metadata.json` |
| `diagrams/q3_azure_architecture.png` | Proposed Azure architecture |

## Design notes
- **Models:** `Qwen/Qwen2.5-3B-Instruct` (open-source LLM, greedy decoding; consistency runs at temperature 0.7 with seeds 1 and 2) and `facebook/bart-large-mnli` (zero-shot NLI).
- **Hold-out set:** messages H1 to H12 were written after the rule lexicon and both prompts were frozen (`rules_frozen_sha256.txt` records the library hash before they were added), so they measure generalisation to unseen wording.
- **Lenient scoring of the original prompt:** its free-text categories and teams are mapped to the taxonomy with a keyword normaliser; the number of distinct free-text labels is reported separately.
- **Key metric:** under-triage rate (predicted urgency below every acceptable gold value), because missing a CRITICAL message is the most harmful error.

## Rule-based baseline (local run)

| Split | Category | Urgency | Team | Under-triage | Sentiment |
|---|---|---|---|---|---|
| Development (n=28) | 96.4% | 96.4% | 96.4% | 3.6% | 60.7% |
| Hold-out (n=12) | 58.3% | 50.0% | 50.0% | 41.7% | 50.0% |

## Results of the Colab run (all 40 messages)

| Method | Category | Urgency (incl. acceptable) | Under-triage | CRITICAL recall | Team | Sentiment |
|---|---|---|---|---|---|---|
| Rule-based baseline | 85.0% | 82.5% | 15.0% | 100% | 82.5% | 57.5% |
| Zero-shot NLI (bart-large-mnli) | 87.5% | 65.0% | 25.0% | 40% | 85.0% | 55.0% |
| LLM + original prompt | 37.5% | 70.0% | 25.0% | 0% | 75.0% | 70.0% |
| LLM + revised prompt | 87.5% | 77.5% | 22.5% | 0% | 85.0% | 75.0% |

Hold-out (n=12): revised LLM category 91.7%, urgency 83.3%, team 91.7%, under-triage 16.7%; rules 58.3%, 50.0%, 50.0%, 41.7%.

Key observations: strict JSON 20% (original) vs 100% (revised); original prompt obeyed the prompt injection in E13; revised prompt never used CRITICAL (but set `escalation_required` on all 5 CRITICAL messages); 19/40 evidence quotes were paraphrased; confidence always 0.9; bias pairs stable only with the revised prompt.
