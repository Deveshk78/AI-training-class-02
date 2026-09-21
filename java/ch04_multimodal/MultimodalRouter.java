public class MultimodalRouter {
    public String recommendPipeline(String modality) {
        switch (modality.toLowerCase()) {
            case "image":
                return "Use vision-model OCR, captioning, and visual Q&A";
            case "audio":
                return "Use transcription, diarization, and summarization";
            case "video":
                return "Extract frames, transcribe scenes, and summarize footage";
            default:
                return "Unknown modality. Use image, audio, or video.";
        }
    }
}
