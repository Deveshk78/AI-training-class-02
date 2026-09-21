# Chapter 1 Interview Q&A

## 1. What is the difference between an LLM and an SLM?
An LLM is larger and usually better for complex reasoning and generation. An SLM is smaller, cheaper, and faster, making it suitable for summarization, routing, and edge deployment.

## 2. Why do we need retrieval before generation?
Retrieval grounds the answer in relevant evidence and reduces hallucinations. It makes the system more explainable and allows the model to answer against a known knowledge base.

## 3. What is a vector database used for?
A vector database stores embeddings so similarity search can find relevant documents quickly.

## 4. What is chunking and why does it matter?
Chunking splits long documents into smaller sections so retrieval is more precise and context stays relevant.

## 5. What is the simplest valid RAG workflow?
Embed documents, store them, retrieve relevant chunks, then pass them with the user query to the model for grounded synthesis.
