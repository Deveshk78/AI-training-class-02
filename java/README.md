# Java Learning Track

This track mirrors the Python curriculum using Java 27 and enterprise-friendly frameworks and APIs.

## Chapters

1. Ch01: Foundations
   - Java and AI basics
   - LLM abstraction patterns
   - Embeddings and retrieval concepts
2. Ch02: Temporal RAG
   - Time-indexed retrieval and metadata filters
   - Historical memory loops
3. Ch03: Agentic RAG
   - Agent orchestration patterns in Java
   - Tool calls and reasoning loops
4. Ch04: Multimodal AI
   - Vision, audio, and video processing orchestrations
   - Model integration patterns

## Java Stack

- Java 27
- Maven
- Spring Boot
- LangChain4j (or equivalent) when available
- Vector DB abstraction with pgvector or in-memory fallback
- Mock provider strategy for learning

## Commands

```bash
cd java
mvn clean install
mvn test
```

## Interview Focus

Explain:
- Java architecture for AI services
- structured domain modeling
- asynchronous tool execution
- API design for agentic flows
- integration concerns across retrieval and tools
