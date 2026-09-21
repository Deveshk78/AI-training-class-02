# Chapter 2: Temporal RAG in Java

## Goal

Show how Java services can represent temporal context, versioning, and time-aware retrieval.

## Concepts

- metadata models
- valid-from / valid-to windows
- timestamp-aware filtering
- service-level retrieval APIs

## Example Domain Model

```java
record DocumentChunk(
    String content,
    String createdAt,
    String version,
    String source
) {}
```

## Interview Angle

> “In Java, I modeled time-aware retrieval as a domain service that filters by a valid time window and ranks by recency. This keeps the logic explicit and testable.”
