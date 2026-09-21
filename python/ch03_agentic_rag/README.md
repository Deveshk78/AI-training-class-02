# Chapter 3: Agentic RAG

## Goal

Build systems where the model can reason, route, plan, retrieve, call tools, and iterate.

## Core Pattern

- Planner decides next step
- Retriever fetches context
- Tool executor uses APIs or functions
- Synthesis layer generates final response
- Feedback loop continues until stop condition

## Why It Matters

Static retrieval alone is not enough when the answer requires:
- external lookup
- multiple tools
- multi-hop reasoning
- action-taking or structured output

## LangGraph Example Pattern

```python
from langgraph.graph import StateGraph, END

# Graph states: query -> retrieve -> decide -> tool_use -> answer
```

## Interview Angle

> “I moved from retrieval-only systems to agentic RAG by adding a planner that could decide when to search, when to call a tool, and when to stop. This made the system far more robust for dynamic and multi-step questions.”

## Tools to Discuss

- search
- database query
- file system access
- external APIs
- MCP tools
- browser-like actions
