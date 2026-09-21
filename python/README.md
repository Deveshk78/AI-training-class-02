# Python Learning Track

This track walks from beginner to advanced topics using Python, LangChain, LangGraph, LangSmith, LLMs/SLMs, and vector stores.

## Chapters

1. Ch01: Foundations
   - Prompting basics
   - Embeddings and vector stores
   - Simple RAG patterns
2. Ch02: Temporal RAG
   - Time-aware retrieval
   - Metadata filters
   - Historical context and recency scoring
3. Ch03: Agentic RAG
   - Planner + retriever + tool loop
   - LangGraph workflows
   - MCP and tool integration
4. Ch04: Multimodal AI
   - Image, audio, and video processing with LLMs
   - Use of SLMs for focused tasks
   - Local or mock pipelines for learning

## Python Stack

- LangChain
- LangGraph
- LangSmith
- Python dotenv
- Chroma
- OpenAI / Azure / local fallback

## Commands

```bash
cd python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python ch01_foundations/foundation_01_intro.py
```

## Interview Focus

Practice explaining:
- retrieval strategy
- metadata design
- time-aware ranking
- why the agent needs tools
- how observability changes debugging
- how multimodal models fit into RAG
