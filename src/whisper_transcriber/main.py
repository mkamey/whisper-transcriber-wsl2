from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import whisper
import os
import uuid

app = FastAPI()

# CORS設定
origins = [
    "http://localhost:3000",  # フロントエンドのオリジン
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Whisperモデルのロード
model_name = os.environ.get("WHISPER_MODEL", "medium")
model = whisper.load_model(model_name)

@app.post("/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...),
    language: str = "ja",
    model: str = "medium"
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="ファイル名がありません")

    file_extension = os.path.splitext(file.filename)[1]
    if file_extension not in [".mp3", ".wav", ".m4a"]:
        raise HTTPException(status_code=400, detail="サポートされていないファイル形式です")

    try:
        temp_file_path = f"/tmp/{uuid.uuid4()}{file_extension}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(await file.read())

        result = model.transcribe(temp_file_path, language=language)
        os.remove(temp_file_path)
        return {
            "text": result["text"],
            "language": result["language"],
            "duration": result["segments"][-1]["end"] if result["segments"] else 0,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))