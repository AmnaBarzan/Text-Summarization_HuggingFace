---
title: Text Summarization
emoji: 📝
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.43.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# Text Summarization

A web application for summarizing long texts using the BART Large CNN model. Built with Hugging Face Transformers and Gradio, and deployed on Hugging Face Spaces.

## Live Demo

[Try it here](https://huggingface.co/spaces/amnabarzan/text_summarization)

## Architecture

```mermaid
flowchart TD
    A[Users] -->|Input Text| B[Frontend\nGradio Interface]
    B -->|Request| C[Backend\nHugging Face Transformers]
    C -->|Load Model| D[facebook/bart-large-cnn]
    D -->|Generate Summary| C
    C -->|Return Summary| B
    B -->|Display Result| A

    style A fill:#1565c0,color:#ffffff,stroke:#0d47a1
    style B fill:#6a1b9a,color:#ffffff,stroke:#4a148c
    style C fill:#2e7d32,color:#ffffff,stroke:#1b5e20
    style D fill:#e65100,color:#ffffff,stroke:#bf360c
```