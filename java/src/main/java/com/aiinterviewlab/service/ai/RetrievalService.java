package com.aiinterviewlab.service.ai;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RetrievalService {
    public List<String> retrieve(String query) {
        return List.of(
            "Temporal RAG uses semantic search and time-aware ranking.",
            "Agentic RAG adds tools and iterative decision making.",
            "Multimodal systems process more than text alone."
        );
    }
}
