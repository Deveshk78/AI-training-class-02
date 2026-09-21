# Chapter 1: Foundations for RAG and Agentic AI

## Goal

Learn the basics of:
- prompt engineering
- embeddings and vector search
- simple retrieval-augmented generation
- LLM vs SLM selection
- environment setup with mock and real providers

## Topics

1. What is an LLM / SLM?
2. Prompting basics
3. Embeddings and semantic search
4. Vector DB basics with Chroma
5. Simple RAG workflow
6. When to use mock mode for learning

## Interview Story

> “I began by building a small retrieval workflow that turned text into embeddings, stored chunks in a vector store, and used a model to answer grounded questions. This exposed the core design pattern behind RAG and later agentic systems.”

## Key Concepts

- Model selection: use a larger LLM for reasoning; use an SLM for lightweight classification, summarization, or local inference.
- Retrieval: find semantically similar context before generating a response.
- Grounding: answer from retrieved evidence rather than ungrounded guesswork.

## Practical Example

The included script creates a tiny mock document set and uses a simple in-memory embedding approach. This teaches the pattern without requiring a paid API immediately.

## Suggested Questions to Practice

- When is a small model enough?
- Why not answer directly without retrieval?
- How do chunk size and overlap affect quality?
- How do you choose a vector database?
