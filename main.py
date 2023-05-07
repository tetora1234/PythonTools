import whisper
import gradio as gr
import openai

openai.api_key = "sk-123"


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


with gr.Blocks() as Interface:
    with gr.Tab("Whisper"):
        AudioFileTo_input = gr.inputs.Audio(source="upload", type="filepath")
        AudioFileTo_output = gr.Textbox(lines=4, placeholder="抽出テキスト")
        AudioFileTo_button = gr.Button("Whisper実行")
    with gr.Tab("ChatGpt"):
        ChatGPT_input = gr.Textbox(lines=4, placeholder="送信テキスト")
        ChatGPT_output = gr.Textbox(lines=4, placeholder="返答テキスト")
        ChatGPT_button = gr.Button("ChatGpt実行")
    AudioFileTo_button.click(
        AudioFileToText, inputs=AudioFileTo_input, outputs=AudioFileTo_output
    )
    ChatGPT_button.click(ChatGptAsk, inputs=ChatGPT_input, outputs=ChatGPT_output)

Interface.launch()
