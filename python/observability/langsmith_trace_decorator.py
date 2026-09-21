"""LangSmith trace decorator example.

This uses a decorator-style pattern so you can wrap functions and then trace
their execution metadata in a LangSmith-compatible setup. When no API key is
configured, it falls back to a local mock trace log.
"""

from __future__ import annotations

import os
from functools import wraps
from typing import Any, Callable, Dict

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env", override=False)


def traced(name: str = "ai_interview_step"):
    def decorator(fn: Callable[..., Any]):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            api_key = os.getenv("LANGCHAIN_API_KEY", "")
            project = os.getenv("LANGCHAIN_PROJECT", "ai-interview-lab")
            traced_enabled = os.getenv("LANGSMITH_TRACING", "true").lower() == "true"

            if not traced_enabled:
                return fn(*args, **kwargs)

            if not api_key:
                print(f"[LangSmith mock trace] {name}: local mock trace created for project={project}")
                return fn(*args, **kwargs)

            print(f"[LangSmith trace] {name}: tracking enabled for project={project}")
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@traced(name="temporal_rag_step")
def temporal_rag_step(query: str):
    return f"Temporal RAG answer for: {query}"


@traced(name="agentic_rag_step")
def agentic_rag_step(query: str):
    return f"Agentic RAG answer for: {query}"


if __name__ == "__main__":
    print(temporal_rag_step("Explain temporal context in an interview"))
    print(agentic_rag_step("When should I use a planner and tool call?"))
