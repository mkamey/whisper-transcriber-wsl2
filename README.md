<div align="center">
  <img src="assets/header.svg" alt="Whisper Transcriber" />
</div>

# 🎤 Whisper Transcriber

このリポジトリは、Whisperを使用して音声ファイルを文字起こしするアプリケーションです。フロントエンドはReact + TypeScript、バックエンドはFastAPIで構築されています。

## 🚀 使い方

1.  このリポジトリをクローンします。
2.  `whisper-transcriber`ディレクトリに移動します。
3.  Docker Composeを使用してアプリケーションを起動します。
    ```bash
    docker-compose up --build
    ```
4.  フロントエンドは `http://localhost:3000` で、バックエンドは `http://localhost:8000` でアクセスできます。
5.  フロントエンドのUIから音声ファイルをアップロードし、言語とモデルを選択して文字起こしを開始します。
6.  文字起こし結果が画面に表示されます。

## ⚙️ 設定

-   **言語**: デフォルトは日本語です。UIから変更できます。
-   **モデル**: デフォルトはmediumです。UIから変更できます。

## ⚠️ 注意事項

-   音声ファイルは、mp3, wav, m4a形式に対応しています。
-   Whisperのモデルは、初回実行時にダウンロードされます。
-   文字起こしには時間がかかる場合があります。

## 🛠️ 開発環境

-   Docker
-   React + TypeScript
-   FastAPI
-   Whisper
-   Python
