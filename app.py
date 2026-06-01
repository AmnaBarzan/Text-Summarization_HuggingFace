import os
os.environ["USE_TF"] = "0"
os.environ["USE_TORCH"] = "1"

from transformers import pipeline
import gradio as gr

model = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def predict(text):
    return model(text, max_length=120, min_length=30, do_sample=False)[0]["summary_text"]

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=6, placeholder="Enter text to summarize"),
    outputs="text"
)

demo.launch()