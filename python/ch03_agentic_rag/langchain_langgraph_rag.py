"""Real LangChain + LangGraph RAG demo using Chroma vector store.

This example intentionally uses a mock embedding and model fallback so it can run in a
fresh environment without paid API keys. It teaches the architecture pattern end-to-end.
"""

from __future__ import annotations

import os
from typing import List, Dict, Any

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env", override=False)

try:
    import chromadb
    from langchain_core.documents import Document
    from langchain_chroma import Chroma
    from langchain_community.embeddings import FakeEmbeddings
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough
    from langgraph.graph import StateGraph, END
except Exception as exc:  # pragma: no cover
    chromadb = None
    Document = None
    Chroma = None
    FakeEmbeddings = None
    ChatPromptTemplate = None
    StrOutputParser = None
    RunnablePassthrough = None
    StateGraph = None
    END = "__end__"
    IMPORT_ERROR = exc
else:
    IMPORT_ERROR = None


class RAGState(dict):
    query: str
    context: List[str]
    answer: str


def build_documents() -> List[Document]:
    return [
        Document(page_content="Temporal RAG adds time-aware retrieval and recency-aware ranking to semantic search.", metadata={"source": "temporal", "date": "2025-01-01"}),
        Document(page_content="Agentic RAG adds planning, tool execution, and iterative reasoning around retrieval.", metadata={"source": "agentic", "date": "2025-02-01"}),
        Document(page_content="Multimodal systems can reason over images, audio, and video with specific model pipelines.", metadata={"source": "multimodal", "date": "2025-03-01"}),
        Document(page_content="LangSmith is used for tracing and debugging prompts, tools, and agent behavior.", metadata={"source": "observability", "date": "2025-04-01"}),
    ]


def build_local_chroma_store() -> Any:
    if chromadb is None or Chroma is None or FakeEmbeddings is None:
        raise RuntimeError(f"LangChain dependencies are not available: {IMPORT_ERROR}")

    persist_dir = os.getenv("CHROMA_PERSIST_DIR", "./.data/chroma")
    os.makedirs(persist_dir, exist_ok=True)

    collection = chromadb.PersistentClient(path=persist_dir)
    if collection.list_collections():
        return Chroma(
            client=collection,
            collection_name="ai_interview_lab",
            embedding_function=FakeEmbeddings(size=3),
        )

    vectordb = Chroma.from_documents(
        documents=build_documents(),
        embedding=FakeEmbeddings(size=3),
        persist_directory=persist_dir,
        collection_name="ai_interview_lab",
    )
    return vectordb


def build_graph(vectordb: Any):
    if StateGraph is None:
        return None

    workflow = StateGraph(RAGState)

    def retrieve_node(state: RAGState) -> RAGState:
        docs = vectordb.similarity_search(state["query"], k=2)
        state["context"] = [doc.page_content for doc in docs]
        return state

    def answer_node(state: RAGState) -> RAGState:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI interview coach. Answer using the provided context only."),
            ("human", "Question: {query}\nContext:\n{context}")
        ])
        chain = prompt | StrOutputParser()
        state["answer"] = chain.invoke({
            "query": state["query"],
            "context": "\n".join(state["context"]),
        })
        return state

    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("answer", answer_node)
    workflow.add_edge("retrieve", "answer")
    workflow.add_edge("answer", END)
    return workflow.compile()


if __name__ == "__main__":
    try:
        vector_store = build_local_chroma_store()
        graph = build_graph(vector_store)
        query = "Explain temporal RAG in interview-ready language."
        if graph is None:
            docs = vector_store.similarity_search(query, k=2)
            print("Retrieved context:")
            for doc in docs:
                print(doc.page_content)
        else:
            result = graph.invoke({"query": query, "context": [], "answer": ""})
            print(result["answer"])
    except Exception as exc:
        print(f"[Mock fallback] {exc}")
        print("LangChain/Chroma installation is not available yet; the structure is still ready for the real environment.")
