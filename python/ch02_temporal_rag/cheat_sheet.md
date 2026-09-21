# Chapter 2 Cheat Sheet

## Core idea
Temporal RAG adds time-awareness to retrieval.

## Important signals
- created_at
- valid_from / valid_to
- version
- source
- recency

## Typical pattern
1. Store time metadata with each chunk
2. Filter by date or validity window
3. Retrieve semantically similar results
4. Re-rank by recency or version relevance
5. Answer with the most current and relevant evidence

## Interview answer template
> “Temporal RAG is essential when the same concept changes over time. I added timestamp metadata and recency-based ranking so the system could distinguish current policy from historical context.”

## Common questions
- Should I return the latest state or the historical state?
- How do I handle versioned or deprecated documents?
- How do I avoid stale answers when the question is time-sensitive?
