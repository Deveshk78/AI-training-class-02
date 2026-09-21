# Installation and Setup Requirements

## Core Prerequisites

- Python 3.11+
- Java 27
- Maven 3.9+
- Git
- Virtual environment support
- Access to model provider or mock mode

## Python Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
pip install -r python/requirements.txt
cp python/.env.example python/.env
```

## Java Setup

```bash
cd java
cp .env.example .env
mvn clean install
```

## Environment Variables

Set the values according to your environment:

```env
LLM_PROVIDER=mock
OPENAI_API_KEY=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
MODEL_NAME=gpt-4o-mini
SMALL_MODEL=phi-3-mini
VECTOR_DB=chroma
CHROMA_PERSIST_DIR=./data/chroma
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT=ai-interview-lab
LANGSMITH_TRACING=true
LANGFLOW_HOST=http://localhost:7860
LANGSERVE_HOST=http://localhost:8000
```

## Optional Services

- Chroma server or local persistence
- LangSmith project configured for tracing
- LangFlow local environment for UI workflows
- LangServe deployment for API hosting

## Recommended Operating Notes

- Start with mock mode to avoid provider lock-in.
- Use a local vector store for workshops and demos.
- Prefer SLMs for lightweight tasks and LLMs for synthesis and planning.
- Turn on tracing early so you can explain tool behavior during interviews.

## Troubleshooting

- If dependencies fail, upgrade pip and setuptools.
- If Java build fails, confirm Java 27 is active: `java -version`
- If model calls fail, switch `LLM_PROVIDER=mock` for offline demo work.

## Security

- Never commit real API keys to the repository.
- Store secrets in local `.env` files only.
- Use environment-scoped credentials for production practice.
