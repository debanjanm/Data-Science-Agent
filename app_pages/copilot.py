import streamlit as st

from agentic_ds.agent_tools import run_agent
from agentic_ds.llm import get_chat_model, narrative_available

MEMORY_DB = "data/agentic_ds.db"

st.title("Copilot")
st.caption("Ask anything about the current dataset — hypothesis tests, GLM/Bayesian models, trends, survival, or a raw data question. It picks the right tool(s) for the question.")

df = st.session_state.df
if df is None:
    st.warning("Upload or pick a dataset first.")
    st.page_link("app_pages/upload.py", label="Go to Upload & target", icon=":material/arrow_back:")
    st.stop()

if not narrative_available():
    st.info("Set OPENROUTER_API_KEY to use the Copilot (see .env.example). Unlike the Data profile "
             "page's summary, there's no rule-based fallback for open-ended questions.")
    st.stop()

dataset_label = st.session_state.source_label or "dataset"
st.caption(f"Dataset: {dataset_label} · {len(df):,} rows × {len(df.columns)} columns")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("tool_calls"):
            st.caption("Used: " + ", ".join(c["tool"] for c in message["tool_calls"]))

question = st.chat_input("e.g. \"is petal length different across species?\" or \"what predicts survival?\"")
if question:
    st.session_state.chat_history.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = run_agent(df, dataset_label, get_chat_model(), question, memory_db=MEMORY_DB)
        st.markdown(result["answer"])
        if result["tool_calls"]:
            st.caption("Used: " + ", ".join(c["tool"] for c in result["tool_calls"]))
        st.session_state.chat_history.append({"role": "assistant", "content": result["answer"], "tool_calls": result["tool_calls"]})
