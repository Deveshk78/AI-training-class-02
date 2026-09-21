# Chapter 2 Cheat Sheet

## Core idea
Temporal retrieval adds time-aware logic to the search layer.

## Core metadata
- createdAt
- validFrom
- validTo
- version
- source

## Typical strategy
1. Store documents with timestamps
2. Filter by validity window
3. Rank by semantic match and recency
4. Return the most relevant versioned evidence

## Interview answer template
> “In the Java service, I modeled time metadata explicitly so that retrieval could compare current versus historical versions and rank by both relevance and recency.”
