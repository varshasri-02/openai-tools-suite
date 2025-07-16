# 🧠 OpenAI Tools Suite

A collection of 3 practical AI-powered tools built using Python, OpenAI, LangChain, and Streamlit. Each project demonstrates how to apply generative AI in real-world use cases.

---

## 📁 Projects Included

### 1. 🎥 YouTube AI Summary

Summarizes YouTube videos using the transcript and OpenAI.

**Features:**
- Extracts transcript automatically using `youtube-transcript-api`
- Generates concise summaries using OpenAI's GPT models

**Tech Stack:** Python, OpenAI API, youtube-transcript-api

---

### 2. 🤖 AI ChatBot (Terminal Assistant)

A command-line chatbot that responds intelligently using GPT-3.5 and LangChain.

**Features:**
- Real-time interactive terminal assistant
- Uses LangChain + LangGraph with ReAct-style agent
- Supports streaming responses

**Tech Stack:** Python, LangChain, LangGraph, OpenAI

---

### 3. 📄 AI Resume Critiquer

Analyzes uploaded resumes and gives personalized feedback based on the target job role.

**Features:**
- Upload resume in `.pdf` or `.txt` format
- GPT-based analysis and suggestions
- Built with Streamlit for easy UI

**Tech Stack:** Python, Streamlit, OpenAI API, PyPDF2

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/varshasri-02/openai-tools-suite.git
cd openai-tools-suite
```

### 2. Create `.env` Files

Inside each project folder (that uses OpenAI), create a `.env` file:

```env
OPENAI_API_KEY=your-openai-api-key
```

### 3. Install Requirements

You can install requirements project-wise using each `requirements.txt`, or combine them all into one and run:

```bash
pip install -r requirements.txt
```

### 4. Run Projects

- `youtube-ai-summary`: Run the summary script using Python.
- `terminal-ai-assistant`: Run the CLI chatbot with:
  ```bash
  python main.py
  ```
- `ai-resume-critiquer`: Launch the web app:
  ```bash
  streamlit run app.py
  ```

---

## 🛑 Important

- Make sure your `.env` files are **not pushed to GitHub**.
- `.env`, `__pycache__/`, and `.vscode/` are already ignored in `.gitignore`.

---

## ⭐ If you like this project, feel free to star it!
