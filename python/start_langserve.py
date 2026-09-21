"""Startup script for the FastAPI + LangServe learning server.

This is a small working app used for local demos and interview practice.
It exposes a simple /health endpoint and a /chat endpoint with a mock response,
while also showing how a LangServe-style API is wrapped around a model workflow.
"""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Interview Lab - LangServe Demo", version="1.0.0")


class ChatRequest(BaseModel):
    query: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    session_id: str | None = None


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "ai-interview-lab-langserve"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    answer = (
        "This is a LangServe-style answer. "
        "In a production setup, the agent would retrieve relevant context, use tools or MCP, "
        "and ground the response with evidence before answering. "
        f"Question: {request.query}"
    )
    return ChatResponse(answer=answer, session_id=request.session_id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("start_langserve:app", host="0.0.0.0", port=8000, reload=False)
