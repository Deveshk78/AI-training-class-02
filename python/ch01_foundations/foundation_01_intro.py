import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env", override=False)


def choose_model_for_task(task: str):
    """Simple decision helper for LLM vs SLM selection."""
    task_lower = task.lower()
    if any(word in task_lower for word in ["reasoning", "planning", "tool use", "synthesis", "complex qa"]):
        return os.getenv("MODEL_NAME", "gpt-4o-mini")
    return os.getenv("SMALL_MODEL", "phi-3-mini")


def mock_llm(prompt: str, model: str) -> str:
    """Mock response to let you learn the pattern without an external API."""
    return f"[Mock {model}] Response for: {prompt[:120]}"


if __name__ == "__main__":
    task = "Generate a brief answer grounded in retrieved context for a policy question."
    model = choose_model_for_task(task)
    answer = mock_llm(task, model)
    print(f"Selected model: {model}")
    print(answer)
