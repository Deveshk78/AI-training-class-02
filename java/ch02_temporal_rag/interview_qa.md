# Chapter 2 Interview Q&A

## 1. How do you model temporal retrieval in Java?
Use a domain model that includes content, timestamps, version, and validity metadata, then apply filters and recency ranking.

## 2. Why is recency important?
It helps prioritize not just semantic relevance but also policy freshness and current operating conditions.

## 3. What is version-aware retrieval?
It means the system can compare or select older vs newer document versions depending on the question.

## 4. What is a time-window filter?
It restricts retrieval to only documents valid during a selected interval.

## 5. How do you explain temporal RAG in a Java service?
As a retrieval service with explicit metadata and ranking rules, not just a simple string search.
