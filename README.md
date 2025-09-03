# 🧑‍💻 Voice-Powered AI Coding Assistant

This project is an AI coding assistant that listens to your voice, transcribes it into text, and processes your query using a LangGraph-powered agent with access to tools like terminal command execution.
It maintains conversation state using MongoDB checkpointing.

## 🚀 Features

- 🎤 Voice input using speech_recognition

- 🤖 AI Assistant powered by langgraph + langchain

- 🛠️ Tool integration (e.g., run terminal commands)

- 💾 Checkpointing with MongoDB for persistent state

- 📂 Works inside a ./cursor directory for file operations

## 📦 Installation

### Clone the repository:
```bash
git clone https://github.com/yourusername/voice-ai-coding-assistant.git
cd voice-ai-coding-assistant
```


### Create a virtual environment & install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```
```bash
pip install -r requirements.txt
```


### Set up environment variables in a .env file:

```bash
OPENAI_API_KEY=your_openai_api_key
```

### Make sure MongoDB is running locally:

```bash
docker run -d -p 27017:27017 --name mongodb \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=admin \
  mongo
```

## ▶️ Usage

### Run the assistant:

```bash
python main.py
```

## 🛠️ Tech Stack

- LangGraph

- LangChain

- OpenAI GPT-4.1

- SpeechRecognition

- MongoDB

## 📌 Notes

The assistant mainly works inside the ./cursor directory for file operations.

Ensure your microphone is working properly.

You can adjust thread_id in the config for multiple conversation threads.
