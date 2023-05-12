from yt_dlp import YoutubeDL
import openai
import whisper
import glob
import os

openai.api_key = "sk-123"


def AudioFileToText(url):
    """_summary_

    Args:
        input (array): アップロードされた音声ファイルのbinary配列

    Returns:
        string:音声から抽出したwhisperのテキストデータ
    """
    option = {
        "outtmpl": "/temp/%(title)s.%(ext)s",
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",  # 変換したい形式を指定
                "preferredquality": "192",  # ビットレートを指定
            }
        ],
    }
    ydl = YoutubeDL(option)
    result = ydl.download([url])

    files = glob.glob("./temp/*")
    for file in files:
        oldFileName = os.path.splitext(os.path.basename(file))[0]
        newFilePathName = "./temp/" + "temp" + ".mp3"
        os.rename("./temp/" + oldFileName + ".mp3", newFilePathName)

    model = whisper.load_model("large-v2")
    result = model.transcribe(newFilePathName, verbose=True, language="ja")
    text = result["text"]
    os.remove(newFilePathName)
    return text


def ChatGptAsk(text):
    """_summary_

    Args:
        text (sring): gptに送信するテキスト

    Returns:
        string: gptの結果テキスト
    """
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text},
        ],
    )
    return res["choices"][0]["message"]["content"]
