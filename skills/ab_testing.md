---
name: ab_testing
description: Compare a metric (conversion rate or continuous) between a control and treatment group — the standard A/B test. Use when the user asks to compare two groups/variants, check if an experiment "worked", or compute lift/significance between two conditions.
---

1. Decide if the metric is a proportion (conversion rate, click-through) or continuous (revenue, time-on-page).
2. Raw counts given directly (not columns) → `two_sample_proportion_test(count_a, nobs_a, count_b, nobs_b)`.
3. Metric lives in a column → `compare_two_groups(numeric_column, group_column)` (auto-picks Welch's t-test or Mann-Whitney).
4. Compute relative lift yourself from the result's group means/proportions: (treatment - control) / control, as a percentage — no tool returns lift directly.
5. State plainly: significant or not at α=0.05, and what that means for the decision (ship treatment / keep control / inconclusive, need more data).

Known gap: no sample-size/power-calculator tool exists yet (tracked in PLAN.md Non-goals). If asked "how many samples do I need", say so honestly instead of guessing.
