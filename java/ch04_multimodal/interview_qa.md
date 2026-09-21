# Chapter 4 Interview Q&A

## 1. Why is multimodal design important in Java services?
It lets enterprise services support more realistic AI workloads such as document understanding, meeting summaries, and media analysis.

## 2. How do you structure the Java services?
Use separate adapters and processors per modality with a common orchestration layer.

## 3. What is the difference between image, audio, and video pipelines?
Image is usually OCR or vision QA; audio is transcription and summarization; video adds temporal analysis across frames and scenes.

## 4. Why do you recommend decoupled adapters?
They simplify testing, replacement, and integration with different provider models.

## 5. How would you present this in an interview?
As a modular architecture where each modality is handled by a task-specific pipeline, all coordinated by a common AI orchestration service.
