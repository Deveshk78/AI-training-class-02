package com.aiinterviewlab.service;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AgenticAiService {
    public String plan(String query) {
        String lower = query.toLowerCase();
        if (lower.contains("calendar") || lower.contains("schedule")) {
            return "Plan: 1) check schedule 2) fetch relevant docs 3) answer";
        }
        if (lower.contains("policy") || lower.contains("document")) {
            return "Plan: 1) retrieve docs 2) evaluate policy 3) summarize";
        }
        return "Plan: 1) search memory 2) gather evidence 3) synthesize response";
    }

    public List<String> executeTools(String query) {
        return List.of(
            "retrieval_tool",
            "calendar_tool",
            "memory_tool"
        );
    }

    public String answer(String query) {
        return "Planned workflow: " + plan(query) + ". Tools executed: " + executeTools(query);
    }
}
