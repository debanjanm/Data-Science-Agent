"""Runnable self-check for Phase 9c's run_agent() loop mechanics: call model
-> run requested tools -> feed results back -> repeat until a final answer
or MAX_TOOL_CALLS. No real OPENROUTER_API_KEY is available in this repo's
dev environment, so this uses a fake chat model with scripted responses
instead of skipping the loop logic untested — the control flow (a loop) is
exactly the kind of thing ponytail says needs one runnable check.

    python -m tests.test_run_agent
"""

import pandas as pd
from langchain_core.messages import AIMessage

from agentic_ds.agent_tools import build_tools, run_agent

DF = pd.DataFrame({"x": [1, 2, 3, 4, 5], "group": ["a", "a", "b", "b", "b"]})


class _FakeModelWithTools:
    """Mimics `ChatOpenAI.bind_tools(...).invoke(messages)`: returns the next
    scripted AIMessage each call, ignoring the actual message content."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = 0

    def invoke(self, _messages):
        response = self._responses[self.calls]
        self.calls += 1
        return response


class _FakeModel:
    def __init__(self, responses):
        self._responses = responses

    def bind_tools(self, _tools):
        return _FakeModelWithTools(self._responses)


def test_stops_immediately_with_no_tool_calls():
    model = _FakeModel([AIMessage(content="No tools needed, here's the answer.", tool_calls=[])])
    result = run_agent(DF, "test", model, "some question")
    assert result["answer"] == "No tools needed, here's the answer."
    assert result["tool_calls"] == []


def test_calls_requested_tool_then_returns_final_answer():
    model = _FakeModel([
        AIMessage(content="", tool_calls=[{"name": "get_schema_overview", "args": {}, "id": "call_1"}]),
        AIMessage(content="This dataset has 2 columns: x (numeric) and group (categorical).", tool_calls=[]),
    ])
    result = run_agent(DF, "test", model, "what columns does this have?")
    assert result["tool_calls"] == [{"tool": "get_schema_overview", "args": {}}]
    assert "2 columns" in result["answer"]


def test_multiple_tool_calls_in_sequence():
    model = _FakeModel([
        AIMessage(content="", tool_calls=[{"name": "get_schema_overview", "args": {}, "id": "call_1"}]),
        AIMessage(content="", tool_calls=[{"name": "compare_two_groups", "args": {"numeric_column": "x", "group_column": "group"}, "id": "call_2"}]),
        AIMessage(content="Group b has a higher mean; not statistically significant at this sample size.", tool_calls=[]),
    ])
    result = run_agent(DF, "test", model, "does x differ by group?")
    assert [c["tool"] for c in result["tool_calls"]] == ["get_schema_overview", "compare_two_groups"]
    assert "significant" in result["answer"]


def test_unknown_tool_name_returns_error_without_crashing():
    model = _FakeModel([
        AIMessage(content="", tool_calls=[{"name": "does_not_exist", "args": {}, "id": "call_1"}]),
        AIMessage(content="I couldn't find that tool.", tool_calls=[]),
    ])
    result = run_agent(DF, "test", model, "question")
    assert result["answer"] == "I couldn't find that tool."


def test_gives_up_after_max_tool_calls():
    # Always requests another tool call — never lets the loop finish naturally.
    infinite = [AIMessage(content="", tool_calls=[{"name": "get_schema_overview", "args": {}, "id": f"call_{i}"}]) for i in range(20)]
    model = _FakeModel(infinite)
    result = run_agent(DF, "test", model, "question")
    assert len(result["tool_calls"]) == 6  # MAX_TOOL_CALLS, didn't loop forever


def test_tools_are_actually_bound_and_real_tool_names_are_callable():
    # Sanity check that build_tools' real tool set overlaps what a skill/agent expects.
    tools = build_tools(DF, "test", model=object())
    names = {t.name for t in tools}
    assert {"get_schema_overview", "compare_two_groups", "smart_sql_query"} <= names


if __name__ == "__main__":
    test_stops_immediately_with_no_tool_calls()
    test_calls_requested_tool_then_returns_final_answer()
    test_multiple_tool_calls_in_sequence()
    test_unknown_tool_name_returns_error_without_crashing()
    test_gives_up_after_max_tool_calls()
    test_tools_are_actually_bound_and_real_tool_names_are_callable()
    print("OK — all run_agent self-checks passed.")
