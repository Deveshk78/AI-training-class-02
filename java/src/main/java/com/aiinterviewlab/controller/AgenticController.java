package com.aiinterviewlab.controller;

import com.aiinterviewlab.service.AgenticAiService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class AgenticController {
    private final AgenticAiService agenticAiService;

    public AgenticController(AgenticAiService agenticAiService) {
        this.agenticAiService = agenticAiService;
    }

    @PostMapping("/agentic")
    public ResponseEntity<Map<String, Object>> agentic(@RequestBody Map<String, String> payload) {
        String query = payload.getOrDefault("query", "Explain agentic RAG");
        return ResponseEntity.ok(Map.of(
            "query", query,
            "plan", agenticAiService.plan(query),
            "tools", agenticAiService.executeTools(query),
            "answer", agenticAiService.answer(query)
        ));
    }
}
