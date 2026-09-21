# Chapter 1 Cheat Sheet

## Core idea
RAG stacks retrieval and generation to ground responses in evidence.

## Key terms
- LLM: large language model for reasoning and generation
- SLM: smaller language model for fast, local, or cheaper tasks
- Embedding: vector representation of text
- Vector store: stores embeddings and supports nearest-neighbor search
- Chunking: splitting large documents into smaller pieces

## Simple flow
1. Split documents into chunks
2. Convert chunks into embeddings
3. Store in vector DB
4. Retrieve relevant chunks for each query
5. Pass retrieved content + query to the model
6. Generate grounded answer

## Interview answer template
> “I started with a simple retrieval pipeline where documents were chunked, embedded, and stored in a vector database. The model then answered using the retrieved evidence rather than hallucinating from memory.”

## Common pitfalls
- poor chunking
- no metadata filtering
- too much irrelevant context
- no evaluation of retrieval quality
