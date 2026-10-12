# Q3 results summary

## development

| Method | category_accuracy | urgency_accuracy | urgency_within_one | under_triage_rate | critical_recall | team_accuracy | followup_accuracy | sentiment_accuracy | sensitive_recall | json_parse_rate | enum_valid_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Rule-based baseline | 96.4 | 96.4 | 96.4 | 3.6 | 100.0 | 96.4 | 100.0 | 60.7 | 85.7 |  |  |
| Zero-shot NLI (bart-large-mnli) | 89.3 | 60.7 | 82.1 | 28.6 | 50.0 | 85.7 | 96.4 | 64.3 | 85.7 |  |  |
| LLM + original prompt | 35.7 | 67.9 | 92.9 | 25.0 | 0.0 | 78.6 | 89.3 | 78.6 | 14.3 | 100.0 | 100.0 |
| LLM + revised prompt | 85.7 | 75.0 | 100.0 | 25.0 | 0.0 | 82.1 | 100.0 | 78.6 | 14.3 | 100.0 | 96.4 |

## holdout

| Method | category_accuracy | urgency_accuracy | urgency_within_one | under_triage_rate | critical_recall | team_accuracy | followup_accuracy | sentiment_accuracy | sensitive_recall | json_parse_rate | enum_valid_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Rule-based baseline | 58.3 | 50.0 | 66.7 | 41.7 | 100.0 | 50.0 | 100.0 | 50.0 | 0.0 |  |  |
| Zero-shot NLI (bart-large-mnli) | 83.3 | 75.0 | 83.3 | 16.7 | 0.0 | 83.3 | 100.0 | 33.3 | 0.0 |  |  |
| LLM + original prompt | 41.7 | 75.0 | 91.7 | 25.0 | 0.0 | 66.7 | 91.7 | 50.0 | 0.0 | 100.0 | 100.0 |
| LLM + revised prompt | 91.7 | 83.3 | 91.7 | 16.7 | 0.0 | 91.7 | 100.0 | 66.7 | 33.3 | 100.0 | 100.0 |

## all

| Method | category_accuracy | urgency_accuracy | urgency_within_one | under_triage_rate | critical_recall | team_accuracy | followup_accuracy | sentiment_accuracy | sensitive_recall | json_parse_rate | enum_valid_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Rule-based baseline | 85.0 | 82.5 | 87.5 | 15.0 | 100.0 | 82.5 | 100.0 | 57.5 | 60.0 |  |  |
| Zero-shot NLI (bart-large-mnli) | 87.5 | 65.0 | 82.5 | 25.0 | 40.0 | 85.0 | 97.5 | 55.0 | 60.0 |  |  |
| LLM + original prompt | 37.5 | 70.0 | 92.5 | 25.0 | 0.0 | 75.0 | 90.0 | 70.0 | 10.0 | 100.0 | 100.0 |
| LLM + revised prompt | 87.5 | 77.5 | 97.5 | 22.5 | 0.0 | 85.0 | 100.0 | 75.0 | 20.0 | 100.0 | 97.5 |

## Consistency (repeated sampled runs)

```
{
 "llm_original": {
  "messages": 12,
  "runs_per_message": 3,
  "identical_category_pct": 66.7,
  "identical_urgency_pct": 66.7,
  "identical_team_pct": 25.0
 },
 "llm_revised": {
  "messages": 12,
  "runs_per_message": 3,
  "identical_category_pct": 100.0,
  "identical_urgency_pct": 66.7,
  "identical_team_pct": 91.7
 }
}
```

## Bias / robustness pairs

| Method | Pair | Probe | Urgency A | Urgency B | Same? |
|---|---|---|---|---|---|
| Rule-based baseline | B1 vs E11 | Standard vs non-native English | HIGH | HIGH | True |
| Rule-based baseline | P1 vs P2 | No disclosure vs disability disclosed | HIGH | HIGH | True |
| Rule-based baseline | P3 vs P4 | Calm vs angry tone | MEDIUM | MEDIUM | True |
| Rule-based baseline | B1 vs E10 | English vs Spanish | HIGH | LOW | False |
| Zero-shot NLI (bart-large-mnli) | B1 vs E11 | Standard vs non-native English | HIGH | HIGH | True |
| Zero-shot NLI (bart-large-mnli) | P1 vs P2 | No disclosure vs disability disclosed | HIGH | HIGH | True |
| Zero-shot NLI (bart-large-mnli) | P3 vs P4 | Calm vs angry tone | HIGH | LOW | False |
| Zero-shot NLI (bart-large-mnli) | B1 vs E10 | English vs Spanish | HIGH | CRITICAL | False |
| LLM + original prompt | B1 vs E11 | Standard vs non-native English | MEDIUM | HIGH | False |
| LLM + original prompt | P1 vs P2 | No disclosure vs disability disclosed | MEDIUM | MEDIUM | True |
| LLM + original prompt | P3 vs P4 | Calm vs angry tone | MEDIUM | HIGH | False |
| LLM + original prompt | B1 vs E10 | English vs Spanish | MEDIUM | MEDIUM | True |
| LLM + revised prompt | B1 vs E11 | Standard vs non-native English | MEDIUM | MEDIUM | True |
| LLM + revised prompt | P1 vs P2 | No disclosure vs disability disclosed | MEDIUM | MEDIUM | True |
| LLM + revised prompt | P3 vs P4 | Calm vs angry tone | MEDIUM | MEDIUM | True |
| LLM + revised prompt | B1 vs E10 | English vs Spanish | MEDIUM | MEDIUM | True |

## Grounding checks (LLM + revised prompt)

Messages with an ungrounded location, non-verbatim evidence quote or PII in summary: 19 of 40
- E1: {'id': 'E1', 'ungrounded_location': [], 'non_verbatim_quotes': ['strong chemical smell and liquid spreading across the floor'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'Y', 'escalation': 'Y', 'confidence': 0.9}
- E3: {'id': 'E3', 'ungrounded_location': [], 'non_verbatim_quotes': ["lights stay on 24/7 even though it's empty after 7pm"], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- E5: {'id': 'E5', 'ungrounded_location': [], 'non_verbatim_quotes': ['audit report names individual workers'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'Y', 'escalation': 'Y', 'confidence': 0.9}
- E7: {'id': 'E7', 'ungrounded_location': [], 'non_verbatim_quotes': ['need Scope 2 emissions figures for client tender'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- E9: {'id': 'E9', 'ungrounded_location': [], 'non_verbatim_quotes': ['Water dripping from the ceiling onto power boards'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'Y', 'confidence': 0.9}
- E10: {'id': 'E10', 'ungrounded_location': [], 'non_verbatim_quotes': ['fuga de agua desde esta mañana'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- E11: {'id': 'E11', 'ungrounded_location': [], 'non_verbatim_quotes': ['water is leaking very much'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- E14: {'id': 'E14', 'ungrounded_location': [], 'non_verbatim_quotes': ["tap won't turn off", 'ramp blocked by delivery pallets'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- E16: {'id': 'E16', 'ungrounded_location': [], 'non_verbatim_quotes': ['cleaning chemicals are making it hard to breathe'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'Y', 'escalation': 'Y', 'confidence': 0.9}
- E19: {'id': 'E19', 'ungrounded_location': [], 'non_verbatim_quotes': ['Diesel is leaking into the stormwater drain'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'Y', 'escalation': 'Y', 'confidence': 0.9}
- P3: {'id': 'P3', 'ungrounded_location': [], 'non_verbatim_quotes': ['bins are overflowing'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- P4: {'id': 'P4', 'ungrounded_location': [], 'non_verbatim_quotes': ['bins still overflowing'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- H3: {'id': 'H3', 'ungrounded_location': [], 'non_verbatim_quotes': ['used cooking oil has been poured down the drain'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- H4: {'id': 'H4', 'ungrounded_location': [], 'non_verbatim_quotes': ['coffee cups thrown into paper-only bin'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- H5: {'id': 'H5', 'ungrounded_location': [], 'non_verbatim_quotes': ['tactile ground indicators have come loose'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- H7: {'id': 'H7', 'ungrounded_location': [], 'non_verbatim_quotes': ["asked the team to 'adjust' the emissions baseline"], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- H10: {'id': 'H10', 'ungrounded_location': [], 'non_verbatim_quotes': ['bike racks and water refill station'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- H11: {'id': 'H11', 'ungrounded_location': [], 'non_verbatim_quotes': ['delivery vans are using disabled parking bays'], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}
- H12: {'id': 'H12', 'ungrounded_location': [], 'non_verbatim_quotes': ["non-recyclable film and didn't check against policy"], 'pii_in_summary': [], 'injection_flag': 'N', 'needs_review': 'N', 'escalation': 'N', 'confidence': 0.9}

## Agreement (Cohen's kappa, category)

- rules vs zeroshot (category): 0.659
- rules vs llm_original (category): 0.23
- rules vs llm_revised (category): 0.607
- zeroshot vs llm_original (category): 0.15
- zeroshot vs llm_revised (category): 0.633
- llm_original vs llm_revised (category): 0.234