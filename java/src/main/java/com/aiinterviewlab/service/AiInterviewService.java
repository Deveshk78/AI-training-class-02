package com.aiinterviewlab.service;

import org.springframework.stereotype.Service;

@Service
public class AiInterviewService {
    public String answer(String query) {
        String lower = query.toLowerCase();

        if (lower.contains("temporal")) {
            return "Temporal RAG adds time-aware retrieval and recency-aware ranking to standard semantic search.";
        }
        if (lower.contains("agentic")) {
            return "Agentic RAG adds a planner, tool execution, and iterative reasoning loop around retrieval.";
        }
        if (lower.contains("mcp")) {
            return "MCP standardizes tool exposure so agents can call reusable capabilities consistently.";
        }
        if (lower.contains("multimodal") || lower.contains("image") || lower.contains("audio") || lower.contains("video")) {
            return "Multimodal AI combines text, image, audio, and video understanding into one reasoning pipeline.";
        }
        return "This interview-ready AI service explains retrieval, tool orchestration, time-aware context, and multimodal reasoning.";
    }
}
