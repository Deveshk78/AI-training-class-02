# Chapter 3 Interview Q&A

## 1. What is an agent in Java enterprise terms?
An agent is an orchestrator that decides when to use retrieval, tools, and reasoning loops, often implemented as a service with explicit states or steps.

## 2. Why do we use tool execution?
To integrate outside systems like search, calendars, APIs, or database queries.

## 3. How is this different from a simple controller?
A controller responds to one request; an agent coordinates multiple reasoning and execution steps before returning a final answer.

## 4. What is the value of a state model?
It makes the agent predictable and easier to debug, trace, and test.

## 5. How do you describe MCP in Java terms?
It is a way to expose well-defined tools to an AI system in a reusable manner.
