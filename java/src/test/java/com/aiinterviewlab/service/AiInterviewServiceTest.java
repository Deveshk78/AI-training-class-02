package com.aiinterviewlab.service;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

class AiInterviewServiceTest {
    @Test
    void shouldAnswerTemporalRagQuery() {
        AiInterviewService service = new AiInterviewService();
        String answer = service.answer("Explain temporal rag");
        assertTrue(answer.toLowerCase().contains("time-aware") || answer.toLowerCase().contains("temporal"));
    }
}
