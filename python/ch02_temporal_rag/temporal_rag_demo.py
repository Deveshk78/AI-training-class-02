from datetime import datetime
from typing import List, Dict, Any


class TemporalDocument:
    def __init__(self, text: str, created_at: str, version: str, tags: List[str] | None = None):
        self.text = text
        self.created_at = created_at
        self.version = version
        self.tags = tags or []


class TemporalRAG:
    def __init__(self):
        self.docs: List[TemporalDocument] = []

    def add_document(self, doc: TemporalDocument):
        self.docs.append(doc)

    def retrieve(self, query: str, as_of: str | None = None, top_k: int = 3):
        as_of_dt = datetime.fromisoformat(as_of) if as_of else datetime.now()
        results = []
        for doc in self.docs:
            doc_dt = datetime.fromisoformat(doc.created_at)
            recency_score = max(0, 1 - (as_of_dt - doc_dt).days / 365)
            semantic_match = 1 if any(term in doc.text.lower() for term in query.lower().split()) else 0
            total_score = semantic_match + recency_score
            results.append((total_score, doc))
        results.sort(reverse=True)
        return [doc for _, doc in results[:top_k]]


if __name__ == "__main__":
    rag = TemporalRAG()
    rag.add_document(TemporalDocument("Version 1 of the policy allowed local experiments.", "2023-01-01", "v1", ["policy", "ops"]))
    rag.add_document(TemporalDocument("Version 2 updated the policy to require approval gates.", "2024-06-15", "v2", ["policy", "ops", "approval"]))
    rag.add_document(TemporalDocument("Version 3 moved policy enforcement to automated monitoring.", "2025-08-01", "v3", ["policy", "monitoring"]))

    query = "What is the current policy for approval gates?"
    results = rag.retrieve(query, as_of="2025-09-01", top_k=2)
    print("Query:", query)
    for doc in results:
        print(f"{doc.version} | {doc.created_at} | {doc.text}")
