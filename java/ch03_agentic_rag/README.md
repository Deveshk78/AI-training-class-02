# Chapter 3: Agentic RAG in Java

## Goal

Teach how Java applications can orchestrate multi-step agent logic with retrieval and tool use.

## Pattern

- Input arrives at controller
- Agent decides if retrieval is needed
- Tool execution is invoked via service layer
- Final response is constructed and returned

## Common Components

- `AgentRouter`
- `RetrievalService`
- `ToolExecutor`
- `AnswerSynthesizer`
- `TraceLogger`

## Interview Angle

> “I designed the Java agent as a set of clear services and explicit state transitions. That makes the system easier to reason about, test, and explain under interview pressure.”
