# Chapter 4: Multimodal AI

## Goal

Understand how LLMs and SLMs can work with text plus other modalities:
- images
- audio
- video

## Brief Breakdown

### Images
- OCR
- object detection
- image captioning
- visual question answering

### Audio
- transcription
- diarization
- summarization
- speech-to-text and text-to-speech evaluation

### Video
- frame extraction
- caption generation
- scene detection
- summarization of long meetings or demos

## Model Selection

- Use a large multimodal model when deep reasoning is needed.
- Use lightweight or specialized models for transcription, OCR, and subsequent summarization.
- Use SLMs for fast local pre-processing.

## Interview Angle

> “I extended RAG beyond text by integrating image, audio, and video understanding. The key idea was not just multimodal inference, but combining those embeddings and extracted signals into a retrieval or reasoning pipeline.”

## Example Workflows

1. Image: generate captions from photos and index them
2. Audio: transcribe minutes and summarize insights
3. Video: extract frames and generate meeting notes
