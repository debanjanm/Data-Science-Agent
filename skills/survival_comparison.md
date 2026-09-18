---
name: survival_comparison
description: Compare time-to-event between two groups (e.g. does a treatment affect time until churn, failure, or recurrence), or model what affects that risk. Use when the data has a duration column plus an event/censoring indicator.
---

1. Confirm which columns are duration (time until event or censoring) and event (1 = event happened, 0 = censored/still ongoing).
2. Two groups to compare → `compare_survival_groups(duration_column, event_column, group_column)` — report the log-rank p-value and which group's curve stays higher (lower hazard).
3. One overall curve → `compute_kaplan_meier(duration_column, event_column)` — report median survival time, or note it wasn't reached (more than half never had the event).
4. Multiple covariates and the question is "what affects risk" rather than "do these two groups differ" → `fit_cox_model(duration_column, event_column, covariate_columns)` — report hazard ratios (>1 raises risk, <1 protective) for significant covariates (p<0.05) and the concordance index as discrimination quality.
