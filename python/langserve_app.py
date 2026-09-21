"""Simple LangServe-inspired API wrapper using FastAPI.

This is intentionally lightweight and uses a mock LLM response so you can learn the
service shape without needing a live provider.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Interview Lab LangServe API", version="1.0.0")


class ChatRequest(BaseModel):
    query: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    session_id: str | None = None


@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-interview-lab"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = (
        "Using temporal retrieval, agentic orchestration, and tool-aware reasoning, "
        f"the answer to '{request.query}' should emphasize grounded evidence, time awareness, "
        "and traceable tool calls."
    )
    return ChatResponse(answer=answer, session_id=request.session_id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
