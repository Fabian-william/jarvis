# 🤖 JARVIS Mark 1 — Multi-Core AI Assistant

> *"Just A Rather Very Intelligent System"*
> Inspired by Tony Stark's legendary AI from Iron Man — built by AR Fabian William.

---

## 💡 Why JARVIS?

I'm a huge Iron Man fan. Tony Stark's JARVIS has always been my vision of what an ideal AI assistant looks like — intelligent, context-aware, voice-driven, and always one step ahead. This project is my own take on building that from the ground up, using local LLMs so it runs entirely on your own machine.

> ⚠️ **Note:** JARVIS is currently in active development. Some features may be limited or experimental. This is just Mark 1 — more capabilities are being added continuously.

---

## 🧠 What Is JARVIS Mark 1?

JARVIS Mark 1 is a **locally-running, voice-powered AI assistant** with a custom multi-core routing architecture. Instead of sending every query to a single model, JARVIS intelligently routes tasks to the best specialist model based on the type of request — just like different departments in a real organisation.

It runs entirely on your machine using **Ollama**, with no cloud subscription required.

---

## ⚡ Features

| Feature | Description |
|---|---|
| 🗣️ Voice Input | Speaks to JARVIS using your microphone |
| 🔊 Voice Output | JARVIS responds using Windows SAPI TTS |
| 🧠 Multi-Core Routing | Routes queries to the right LLM automatically |
| 💻 Code Generation | Dedicated coding core (Qwen 2.5) |
| 🌐 Web Search | Opens browser searches on command |
| 🌤️ Weather Reports | Real-time weather based on your IP location |
| 💾 File Save | Saves generated code to your Desktop |
| 🔌 Fully Offline | Runs on local hardware via Ollama |

---

## 🏗️ Architecture

```
User Voice Input
       │
       ▼
  ┌─────────────┐
  │   Perception │  ← speech_recognition + SAPI TTS
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │    Router    │  ← Keyword-based intent detection
  └──────┬──────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌─────────┐  ┌──────────────┐
│ Chat  │ │  Coder  │  │  Tool Layer  │
│ Core  │ │  Core   │  │  (Weather /  │
│Llama  │ │  Qwen   │  │   Search /   │
│ 3.2   │ │  2.5    │  │   File Ops)  │
└───────┘ └─────────┘  └──────────────┘
```

### Core Routing Logic

| Query Type | Model Used | Why |
|---|---|---|
| General chat / casual | `llama3.2:1b` | Fast, conversational |
| Code / algorithms / C++ / Python | `qwen2.5:3b` | Optimised for coding tasks |
| Research / complex analysis | `gpt-oss:120b-cloud` | High-reasoning cloud core |
| Weather / search / file ops | Tool layer | Instant, no LLM needed |

---

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- **[Ollama](https://ollama.ai)** — local LLM runner
- **Python 3.10+**
- **Windows OS** (required for SAPI voice output via `win32com`)
- **Git**
- A working **microphone**

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Fabian-william/jarvis-mark1.git
cd jarvis-mark1
```

### 2. Pull Required Models via Ollama

```bash
ollama pull llama3.2
ollama pull qwen2.5
```

> Make sure Ollama is running before this step (`ollama serve` in a separate terminal).

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Configuration

Open `brain.py` and confirm the model names and Ollama port match your setup:

```python
self.chat_model  = "llama3.2:1b"      # General chat
self.coder_model = "qwen2.5:3b"       # Code generation
# Default Ollama port: 11434
```

### 5. Run JARVIS

```bash
python main.py
```

JARVIS will greet you and begin listening for voice commands.

---

## 🎙️ Voice Commands Reference

| Command | What JARVIS Does |
|---|---|
| `"What's the weather?"` | Reports current weather for your city |
| `"Search for [topic]"` | Opens Google search in your browser |
| `"Write a Python function to..."` | Generates code using Qwen 2.5 |
| `"Explain [concept]"` | Routes to cloud core for deep analysis |
| `"Save that code as script.py"` | Saves last generated code to Desktop |
| `"Shutdown"` / `"Go to sleep"` | Powers down JARVIS gracefully |

---

## 📁 Project Structure

```
jarvis-mark1/
│
├── main.py              # Entry point — orchestrates all systems
├── brain.py             # Multi-core routing + LLM communication
├── perception.py        # Voice input (STT) + voice output (TTS)
├── __init__.py          # Package initialiser
│
└── tools/
    ├── internet_ops.py  # Weather API + web search
    └── file_ops.py      # Code export to Desktop
```

---

## 🔧 Dependencies

```
ollama
speechrecognition
pyaudio
requests
beautifulsoup4
pywin32
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🗺️ Roadmap — What's Coming in Future Marks

> JARVIS Mark 1 is just the beginning. Here's what's planned:

- [ ] 🖥️ GUI Interface — web-based or desktop dashboard
- [ ] 📂 File Reading — summarise documents and PDFs
- [ ] 📧 Email Integration — read and draft emails
- [ ] 🗓️ Calendar & Reminders — schedule management
- [ ] 🎵 Media Control — play/pause/skip music
- [ ] 🧠 Long-term Memory — persistent conversation context
- [ ] 🔌 Plugin System — easily add new tool modules
- [ ] 🌐 Cross-platform Support — Linux and macOS compatibility

---

## ⚠️ Known Limitations (Mark 1)

- Windows only (SAPI TTS uses `win32com`)
- Internet required for weather and web search features
- Cloud core (`gpt-oss:120b`) requires Ollama cloud access
- Speech recognition depends on Google's API (internet required)

---

## 👨‍💻 About the Developer

**AR Fabian William** — Software Developer, Chennai, India

A passionate developer who has been a huge Iron Man fan since childhood. Building JARVIS is not just a project — it's a tribute to one of the greatest fictional AIs ever imagined, and a personal challenge to see how close we can get to it with today's real technology.

> *"The best way to predict the future is to invent it."*

- 🌐 Portfolio: [ar-fabian-william.github.io](https://fabian-william.github.io)
- 💼 LinkedIn: [linkedin.com/in/ar-fabian-william](https://www.linkedin.com/in/ar-fabian-william/)
- 💻 GitHub: [github.com/Fabian-william](https://github.com/Fabian-william)
- 📧 arfabianwilliam@gmail.com

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">
  <strong>JARVIS Mark 1</strong> — Built with 🔥 by AR Fabian William<br/>
  <em>"I have successfully privatised world peace." — Tony Stark</em>
</p>
