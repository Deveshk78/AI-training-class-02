# Chapter 3 Cheat Sheet

## Core idea
The agent decides the next action instead of following a single fixed pipeline.

## Typical Java design
- `AgenticAiService` chooses a plan
- `RetrievalService` gathers context
- tool layer executes external actions
- response synthesizer returns the result

## Interview answer template
> “I designed the Java agent as a service with explicit planning and tool execution. The key win is that it can decide between search, tool use, and reasoning based on the query, rather than running a rigid one-size-fits-all flow.”
