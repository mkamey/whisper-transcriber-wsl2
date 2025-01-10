# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリ設定
WORKDIR /app

# システム依存関係のインストール
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Python依存関係のインストール
COPY requirements.lock .
RUN pip install --no-cache-dir -r requirements.lock

# アプリケーションコードのコピー
COPY . .

# ポート公開
EXPOSE 8000

# 起動コマンド
CMD ["uvicorn", "src.whisper_transcriber.main:app", "--host", "0.0.0.0", "--reload"]