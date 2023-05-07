import whisper
import gradio as gr

model = whisper.load_model("base")


def speechRecognitionModel(input):
    ## モデル（データセット）読み込み
    model = whisper.load_model("small")

    ## 音声へのパス
    path = input

    ## 結果を出力と同時に取得
    result = model.transcribe(path, verbose=True, language="ja")
    text = result["text"]
    return text


gr.Interface(
    title="Whisper Speech Recognition Model",
    fn=speechRecognitionModel,
    inputs=[gr.inputs.Audio(source="upload", type="filepath")],
    outputs=["textbox"],
    live=True,
).launch()
