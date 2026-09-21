import os
from typing import List
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env", override=False)


class Document:
    def __init__(self, text: str, metadata: dict | None = None):
        self.text = text
        self.metadata = metadata or {}


class SimpleVectorStore:
    def __init__(self):
        self.docs: List[Document] = []

    def add(self, doc: Document):
        self.docs.append(doc)

    def retrieve(self, query: str, top_k: int = 2):
        # This is a teaching placeholder for semantic retrieval.
        # Real systems usually use embeddings + a vector DB.
        query_lower = query.lower()
        scored = []
        for doc in self.docs:
            score = sum(1 for token in query_lower.split() if token in doc.text.lower())
            scored.append((score, doc))
        scored.sort(reverse=True)
        return [doc for _, doc in scored[:top_k]]


if __name__ == "__main__":
    store = SimpleVectorStore()
    docs = [
        Document("Temporal RAG retrieves results by both semantics and time metadata.", {"date": "2024-01-10"}),
        Document("Agentic RAG adds tools, planning, and iteration to retrieval loops.", {"date": "2024-02-15"}),
        Document("Multimodal systems can reason over image, audio, and video inputs.", {"date": "2024-03-05"}),
    ]
    for doc in docs:
        store.add(doc)

    query = "What is temporal RAG?"
    results = store.retrieve(query)
    print("Query:", query)
    for doc in results:
        print("-", doc.text, doc.metadata)
