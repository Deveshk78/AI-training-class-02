# Chapter 3 Cheat Sheet

## Core idea
Agentic RAG adds planning, tool calls, and iterative reasoning around retrieval.

## Main components
- planner
- retriever
- tool executor
- answer synthesizer
- memory/state

## Typical flow
1. Receive user query
2. Decide whether to retrieve, call tools, or ask a clarifying question
3. Read the relevant context
4. Execute tool(s) when needed
5. Synthesize final answer
6. Stop or continue until a criterion is met

## Interview answer template
> “I moved from static retrieval to agentic RAG by introducing a planner that could decide when to search, when to use tools, and when to stop. This made the system more robust for real-world tasks that require multi-step reasoning.”

## Common tool examples
- search
- calendar
- database query
- file retrieval
- external API calls

## MCP concept
MCP gives a common interface so tools can be exposed and reused consistently across agents.
