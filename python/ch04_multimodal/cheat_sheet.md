# Chapter 4 Cheat Sheet

## Core idea
Multimodal AI combines text, image, audio, and video understanding into one system.

## Common patterns
- Image: OCR, captioning, visual QA
- Audio: transcription, diarization, summarization
- Video: frame extraction, scene analysis, captioning

## Why it matters
Many real-world enterprise tasks involve screenshots, meetings, calls, user recordings, and documents.

## Interview answer template
> “I extended the AI pipeline beyond text by adding modalities like image, audio, and video. The main idea was to extract structured evidence from each source and then use that evidence in retrieval or reasoning workflows.”

## Design tips
- Use specialized models for each modality when possible
- Keep modality adapters modular
- Keep the orchestration layer common
- Use SLMs for pre-processing and LLMs for synthesis
