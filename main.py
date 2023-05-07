import whisper
import gradio as gr


def AudioFileToText(input):
    """_summary_

    Args:
        input (array): アップロードされた音声ファイルのbinary配列

    Returns:
        string:音声から抽出したwhisperのテキストデータ
    """
    model = whisper.load_model("small")
    path = input
    result = model.transcribe(path, verbose=True, language="ja")
    text = result["text"]
    return text


with gr.Blocks() as Interface:
    with gr.Tab("音声からテキスト抽出"):
        AudioFileTo_input = gr.inputs.Audio(source="upload", type="filepath")
        AudioFileTo_output = gr.Textbox()
        AudioFileTo_button = gr.Button("音声からテキスト抽出")
    with gr.Tab("カモフラージュ"):
        sample_input = gr.inputs.Audio(source="upload", type="filepath")
    AudioFileTo_button.click(
        AudioFileToText, inputs=AudioFileTo_input, outputs=AudioFileTo_output
    )

Interface.launch()
