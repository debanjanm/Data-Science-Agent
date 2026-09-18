---
name: trend_check
description: Check whether a numeric column (treated as an ordered series) has a trend/seasonality, or fit a short-term forecast. Use when the user asks about trend, seasonality, stationarity, or forecast.
---

1. `check_series_stationarity(column)` — report the verdict (stationary/non-stationary/inconclusive) plainly.
2. Non-stationary and the user wants to model it (ARIMA) → `suggest_arima_differencing_order(column)` for `d`.
3. `compute_autocorrelation(column)` — a PACF cutoff at lag k suggests AR order p≈k, an ACF cutoff suggests MA order q≈k. Prefer small values (0-2) unless the data clearly needs more.
4. `fit_arima_model(column, p, d, q, forecast_steps)` — check `residual_whiteness` in the result; if not white noise, the order is probably wrong, try different p/q.
5. Report the forecast direction/magnitude in plain terms, plus AIC and whether residuals look clean.
