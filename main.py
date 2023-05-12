import gradio as gr
import function

with gr.Blocks() as Interface:
    with gr.Tab("Whisper"):
        AudioFileTo_input = gr.Textbox(lines=1, placeholder="Youtubeの動画URL")
        AudioFileTo_output = gr.Textbox(lines=4, placeholder="抽出テキスト")
        AudioFileTo_button = gr.Button("Whisper実行")
    with gr.Tab("ChatGpt"):
        ChatGPT_input = gr.Textbox(lines=4, placeholder="送信テキスト")
        ChatGPT_output = gr.Textbox(lines=4, placeholder="返答テキスト")
        ChatGPT_button = gr.Button("ChatGpt実行")
    AudioFileTo_button.click(
        function.AudioFileToText,
        inputs=AudioFileTo_input,
        outputs=AudioFileTo_output,
    )
    ChatGPT_button.click(
        function.ChatGptAsk, inputs=ChatGPT_input, outputs=ChatGPT_output
    )

Interface.launch()
