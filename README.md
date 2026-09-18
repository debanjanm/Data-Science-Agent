# Agentic Data Science

An agentic data science workbench for tabular data, through a Streamlit
UI: upload a CSV (or pick a built-in dataset), then either run AutoML
(profiling, a trained-model leaderboard, predictions) or classical
statistics (hypothesis testing, GLM, Bayesian modeling, time series,
survival analysis) on it, with a chat copilot throughout. See
[PLAN.md](PLAN.md) for the full product design and roadmap — all 8
planned phases are done.

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Sectioned nav: **Data** (Upload & target, Data profile, Data prep) →
**AutoML** (Train, Leaderboard, Predict) → **Statistics** (Hypothesis
testing, Statistical modeling, Bayesian modeling, Time series, Survival
analysis) → **Copilot**. AutoML and Statistics are independent problem
types sharing only the Data pages — each Statistics page has its own
example questions and column pickers, not tied to the AutoML target.
Optional AI features (Data profile's summary, Leaderboard's executive
summary, every Statistics page's plain-English explanation, Copilot)
activate if `OPENROUTER_API_KEY` is set (see `.env.example`) — everything
else works without it. Copilot is a real tool-calling agent (26 tools —
every hypothesis test, GLM, Bayesian, ARIMA, Cox, plus NL-to-SQL — guided
by 5 `skills/*.md` playbooks), not just a SQL box.

## Self-check

```bash
python3 -m tests.test_modeling
python3 -m tests.test_data_prep
python3 -m tests.test_sql_safety
python3 -m tests.test_stats_tests
python3 -m tests.test_glm
python3 -m tests.test_bayesian
python3 -m tests.test_timeseries
python3 -m tests.test_survival
python3 -m tests.test_agent_tools
python3 -m tests.test_skills
python3 -m tests.test_run_agent
```
