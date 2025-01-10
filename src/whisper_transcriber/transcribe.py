import whisper
import os

def transcribe_audio(audio_path, output_path):
    model = whisper.load_model("medium")
    result = model.transcribe(audio_path, language="ja")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

if __name__ == "__main__":
    audio_file = os.path.join(os.path.dirname(__file__), "..", "..", "..", "test", "20250110.mp3")
    output_file = os.path.join(os.path.dirname(__file__), "..", "..", "..", "test", "20250110.txt")
    transcribe_audio(audio_file, output_file)