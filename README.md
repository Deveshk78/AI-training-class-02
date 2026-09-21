# AI Interview Lab: Temporal RAG, Agentic RAG, and Multimodal AI

This workspace is designed as a hands-on, interview-ready learning path covering:

- Temporal RAG and time-aware retrieval
- Agentic RAG with tool use and reasoning loops
- Agentic AI patterns and orchestration
- MCP (Model Context Protocol) coding
- Multimodal AI: image, audio, and video understanding
- Observability with LangSmith
- Low-code/visual experimentation with LangFlow and LangServe
- Python and Java implementations in parallel

## Learning Flow

1. Foundations: embeddings, vector stores, prompt design, LLM/SLM selection
2. Temporal RAG: retrieval over time, versioning, event-aware memory
3. Agentic RAG: planner + retriever + tool executor + answer synthesizer
4. Multimodal AI: image, audio, and video processing workflows
5. MCP integration: tool invocation and protocol-based agents
6. Production patterns: tracing, guardrails, evaluation, and deployment

## Repository Structure

```text
ai-interview-lab/
├── README.md
├── architecture.md
├── requirements.md
├── .env.example
├── python/
│   ├── README.md
│   ├── requirements.txt
│   ├── .env.example
│   ├── ch01_foundations/
│   ├── ch02_temporal_rag/
│   ├── ch03_agentic_rag/
│   └── ch04_multimodal/
├── java/
│   ├── README.md
│   ├── pom.xml
│   ├── .env.example
│   ├── ch01_foundations/
│   ├── ch02_temporal_rag/
│   ├── ch03_agentic_rag/
│   └── ch04_multimodal/
└── assets/
    └── diagrams/
```

## Recommended Tools

- LLMs / SLMs: OpenAI GPT family, Azure OpenAI, Mistral, Llama, Phi, or a mocked fallback for demos
- Vector DB: Chroma, pgvector, FAISS, Weaviate
- Frameworks: LangChain, LangGraph, LangSmith, LangFlow, LangServe
- MCP: Python `mcp`, Java MCP SDK or minimal JSON-RPC tooling for learning
- Observability: LangSmith tracing and evaluation
- Deployment: FastAPI or Spring Boot for service exposure

## Quick Start

1. Copy environment variables:
   - `cp .env.example .env`
   - or use the language-specific `.env.example`
2. Install Python dependencies:
   - `python -m venv .venv`
   - `pip install -r python/requirements.txt`
3. Or install Java dependencies:
   - `cd java && mvn clean install`
4. Follow each chapter in order.
5. For interview prep, focus on explaining trade-offs, not only code syntax.

## Suggested Interview Story

> “I built a temporal RAG system that retrieved relevant knowledge across time windows, then layered an agentic planner that called external tools and synthesized answers with citations. I also extended it to multimodal inputs by understanding image, audio, and video content with a mix of LLMs and task-specific models.”

## Learning Principles

- Start with simple retrieval and move to orchestration.
- Use mock providers when the environment is not ready.
- Explain architecture before implementation.
- Treat observability and evaluation as first-class concerns.
- Build modular demos that can be discussed in interviews.

## Notes

This repository is intentionally designed to be a teaching scaffold. You can replace the mock providers with actual models and vector stores as your environment matures.
