"""LangSmith setup and tracing demo.

This script demonstrates how to wire tracing into a local learning environment.
It is intentionally safe and uses a mock response when the API key is absent.
"""

import os
from typing import Dict, Any

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env", override=False)


def configure_langsmith() -> Dict[str, Any]:
    configuration = {
        "api_key": os.getenv("LANGCHAIN_API_KEY", ""),
        "project": os.getenv("LANGCHAIN_PROJECT", "ai-interview-lab"),
        "tracking": os.getenv("LANGSMITH_TRACING", "true").lower() == "true",
    }
    if not configuration["api_key"]:
        configuration["status"] = "mocked - no LangSmith API key configured"
    else:
        configuration["status"] = "ready"
    return configuration


def run_traced_mock_step(prompt: str):
    cfg = configure_langsmith()
    if cfg["tracking"]:
        return {
            "trace": "langsmith_mock_trace",
            "project": cfg["project"],
            "result": f"Mock traced output for: {prompt[:80]}",
            "status": cfg["status"],
        }
    return {
        "trace": "disabled",
        "project": cfg["project"],
        "result": f"Mock output for: {prompt[:80]}",
        "status": "tracing disabled",
    }


if __name__ == "__main__":
    result = run_traced_mock_step("Summarize the temporal RAG design and explain the tool loop.")
    print(result)
