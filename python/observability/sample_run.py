"""Sample run script showing a real LangSmith-style trace pipeline."""

from langsmith_trace_decorator import traced


@traced(name="sample_run")
def run_pipeline(question: str):
    return {
        "question": question,
        "retrieved": ["Temporal document chunk", "Agentic tool result"],
        "answer": "Use retrieval plus tool loops and cite evidence to stay grounded."
    }


if __name__ == "__main__":
    print(run_pipeline("How would you explain agentic RAG in 30 seconds?"))
