package com.aiinterviewlab.controller;

import com.aiinterviewlab.service.AiInterviewService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class ChatController {
    private final AiInterviewService aiInterviewService;

    public ChatController(AiInterviewService aiInterviewService) {
        this.aiInterviewService = aiInterviewService;
    }

    @GetMapping("/chat")
    public ResponseEntity<Map<String, Object>> chatGet(@RequestParam(value = "query", defaultValue = "Explain temporal RAG") String query) {
        String answer = aiInterviewService.answer(query);
        return ResponseEntity.ok(Map.of("query", query, "answer", answer, "method", "GET"));
    }

    @PostMapping("/chat")
    public ResponseEntity<Map<String, Object>> chat(@RequestBody Map<String, String> payload) {
        String query = payload.getOrDefault("query", "Explain temporal RAG");
        String answer = aiInterviewService.answer(query);
        return ResponseEntity.ok(Map.of("query", query, "answer", answer, "method", "POST"));
    }
}
