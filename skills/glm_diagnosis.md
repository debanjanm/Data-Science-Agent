---
name: glm_diagnosis
description: Fit a statistical model to explain or predict a target from other columns, with real coefficients/p-values, not just a black-box prediction. Use when the user asks "what predicts X" or "build a model for X" and wants to know why, not just get a prediction.
---

1. `suggest_glm_family(target_column)` — don't guess the family yourself, the tool already encodes the shape-detection logic.
2. `fit_glm_model(target_column, predictor_columns, family)` with the suggested family.
3. If family was "poisson" and the result's `overdispersion.overdispersed` is true, refit with `family="negative_binomial"` — mention why (Poisson's equal mean-variance assumption failed).
4. Report: significant predictors (p < 0.05) and their direction, model fit quality (AIC, pseudo-R² if present), and any overdispersion caveat.
5. If the user specifically wants a full posterior/credible intervals instead of a point estimate + p-value, use `suggest_bayesian_family`/`fit_bayesian_model` instead — mention it's slower (MCMC, several seconds).
