package com.aiinterviewlab.service.ai;

import org.springframework.stereotype.Component;

@Component
public class MockModelProvider implements ModelProvider {
    @Override
    public String generate(String prompt) {
        return "[Mock provider] Generated answer for: " + prompt.substring(0, Math.min(prompt.length(), 80));
    }
}
