# Chapter 2: Temporal RAG

## Goal

Teach how to build retrieval pipelines that understand time.

## Why Temporal RAG Matters

The same concept can mean different things depending on when it is asked. Example:
- policy version before/after change
- latest maintenance note vs archived one
- product reference vs deprecated product policy

## Concepts

- time-aware metadata
- recency ranking
- date filters
- versioned context
- historical context retrieval

## Typical Workflow

1. Store documents with timestamps and versions
2. Retrieve documents using semantic search + metadata filters
3. Re-rank by recency or validity window
4. Generate answer with traceable references

## Interview Angle

> “I designed a time-aware retrieval layer where search included both semantic relevance and timestamp filters, so the system could prioritize current documents while still supporting historical comparisons.”

## Practice Idea

Build a denormalized retrieval index where each chunk has:
- `content`
- `created_at`
- `valid_from`
- `valid_to`
- `source`
- `version`
