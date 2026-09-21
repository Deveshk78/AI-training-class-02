package com.aiinterviewlab.service.ai;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class InterviewAiService {
    private final RetrievalService retrievalService;
    private final ModelProvider modelProvider;

    public InterviewAiService(RetrievalService retrievalService, ModelProvider modelProvider) {
        this.retrievalService = retrievalService;
        this.modelProvider = modelProvider;
    }

    public String answer(String query) {
        List<String> context = retrievalService.retrieve(query);
        String prompt = "Use the following context to answer the question: " + String.join(" ; ", context) + " Question: " + query;
        return modelProvider.generate(prompt);
    }
}
