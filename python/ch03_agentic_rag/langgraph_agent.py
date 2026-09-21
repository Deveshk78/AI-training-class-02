"""LangGraph-based agent orchestration demo.

This example is intentionally framework-first and interview-friendly. It shows:
- state management
- planning/tool selection
- retrieval and answer synthesis
- a mock LLM fallback for local learning
"""

from __future__ import annotations

from typing import TypedDict, List, Annotated

try:
    from langgraph.graph import StateGraph, END
except Exception:  # pragma: no cover - for environments without LangGraph installed
    StateGraph = None
    END = "__end__"


class AgentState(TypedDict):
    query: str
    retrieved: List[str]
    tool_outputs: List[str]
    answer: str


def mock_retriever(query: str) -> List[str]:
    docs = {
        "policy": [
            "The policy requires a review before a production deployment.",
            "The latest process enforces a documented approval gate.",
        ],
        "calendar": [
            "The team meeting is scheduled on Tuesday at 4 PM.",
            "The engineering review happens after the architecture sync.",
        ],
    }
    lowered = query.lower()
    for key, items in docs.items():
        if key in lowered:
            return items
    return ["No matching local memory. Use the fallback reasoning path."]


def choose_tools(query: str) -> List[str]:
    lowered = query.lower()
    tools = []
    if "policy" in lowered or "document" in lowered:
        tools.append("search_policy")
    if "calendar" in lowered or "meeting" in lowered:
        tools.append("check_calendar")
    if not tools:
        tools.append("search_policy")
    return tools


def run_tool(tool_name: str, query: str) -> str:
    if tool_name == "search_policy":
        return f"Policy tool result for '{query}': the process includes approval before release."
    if tool_name == "check_calendar":
        return f"Calendar tool result for '{query}': Tuesday 4:00 PM is open."
    return f"Fallback tool result for '{query}'"


def planner_node(state: AgentState) -> AgentState:
    state["retrieved"] = mock_retriever(state["query"])
    state["tool_outputs"] = [run_tool(tool, state["query"]) for tool in choose_tools(state["query"])]
    return state


def answer_node(state: AgentState) -> AgentState:
    evidence = "\n".join(state["retrieved"] + state["tool_outputs"])
    state["answer"] = (
        f"Answer to: {state['query']}\n"
        f"Evidence:\n{evidence}\n"
        "Final synthesis: Use the retrieved context and the tool outputs to answer grounded questions."
    )
    return state


def build_graph():
    if StateGraph is None:
        return None

    workflow = StateGraph(AgentState)
    workflow.add_node("planner", planner_node)
    workflow.add_node("answer", answer_node)
    workflow.add_edge("planner", "answer")
    workflow.add_edge("answer", END)
    return workflow.compile()


if __name__ == "__main__":
    sample_query = "Check the policy and the meeting schedule before the release."
    if StateGraph is None:
        initial_state = {"query": sample_query, "retrieved": [], "tool_outputs": [], "answer": ""}
        planner_node(initial_state)
        answer_node(initial_state)
        print(initial_state["answer"])
    else:
        graph = build_graph()
        result = graph.invoke({"query": sample_query, "retrieved": [], "tool_outputs": [], "answer": ""})
        print(result["answer"])
