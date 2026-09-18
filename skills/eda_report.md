---
name: eda_report
description: Produce a written profile of the dataset (or a subset of columns) — schema, stats, correlations, outliers. Use when the user asks to explore/profile/summarize the data, or "what stands out".
---

1. `get_schema_overview()` — dtypes, missing %, cardinality.
2. `get_numeric_summary()` — descriptive stats on numeric columns.
3. `get_correlation_matrix()` — call out the strongest pair(s).
4. Any column with high missing % or an extreme range → `detect_column_outliers(column)`.
5. Categorical columns of interest → `get_top_value_counts(column)`.
6. Synthesize: 4-6 bullets on data quality issues, interesting distributions, and anything worth investigating before modeling. Don't just restate the raw numbers back.
