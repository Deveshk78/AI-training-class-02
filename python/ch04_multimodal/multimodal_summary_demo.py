from pathlib import Path


class MultimodalTaskRouter:
    def __init__(self):
        self.task_map = {
            "image": "Use vision-model OCR and caption generation",
            "audio": "Use transcription and summarization pipeline",
            "video": "Extract frames, transcribe captions, and summarize scenes",
        }

    def recommend_pipeline(self, modality: str):
        if modality not in self.task_map:
            return "Unknown modality. Use image, audio, or video."
        return self.task_map[modality]


if __name__ == "__main__":
    router = MultimodalTaskRouter()
    for modality in ["image", "audio", "video"]:
        print(f"{modality}: {router.recommend_pipeline(modality)}")
