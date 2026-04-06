JARVIS Mark 1: Multi-Core AI Assistant
Overview
JARVIS Mark 1 is a localized AI assistant featuring a custom routing architecture that distributes tasks across specialized LLM cores (e.g., Llama 3.2 for general chat and Qwen 2.5 for coding).

Prerequisites
Ollama installed and running.

Python 3.10+

Git

Setup Instructions
Clone the Repository

Bash
git clone https://github.com/your-username/jarvis-mark1.git
cd jarvis-mark1
Pull Required Models

Bash
ollama pull llama3.2
ollama pull qwen2.5
Install Dependencies

Bash
pip install -r requirements.txt
Configuration
Update config.py (or your routing script) to ensure the API endpoints point to your local Ollama instance:

Chat Core: llama3.2

Coding Core: qwen2.5

Default Port: 11434

Execution

Bash
python main.py
Architecture
Router: Directs user queries based on intent.

Cores: Local LLMs served via Ollama.

Interface: Command-line execution on
