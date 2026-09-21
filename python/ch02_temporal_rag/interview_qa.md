# Chapter 2 Interview Q&A

## 1. What is temporal RAG?
Temporal RAG adds time awareness to retrieval, so the system can reason with recency, version history, and validity windows.

## 2. Why is timestamp metadata important?
Without timestamps, the system may retrieve outdated or irrelevant policies. Timestamp metadata supports historical comparison and recency-based ranking.

## 3. How do you choose between current-context and historical-context retrieval?
Use current documents for most user questions, and historical or versioned documents when the question asks about prior states, changes, or comparisons.

## 4. What is a valid-time filter?
A valid-time filter restricts retrieval to documents that were active during the selected period.

## 5. How would you explain temporal RAG in one sentence?
It is retrieval augmented with both semantic relevance and time-aware knowledge ranking.
