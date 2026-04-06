# JARVIS Mark 1: Multi-Core AI Assistant

## Overview
JARVIS Mark 1 is a localized AI assistant featuring a custom routing architecture that distributes tasks across specialized LLM cores.

## Prerequisites
* **Ollama** (Llama 3.2 & Qwen 2.5)
* **Python 3.10+**

## Setup & Installation

1. **Clone/Download Files**
   Download all project files into a single root directory. 

2. **Note on Flat Directory Structure**
   Currently, all core logic and utility files are located in the **root directory** rather than a `tools/` folder. Ensure your imports are configured as follows:
   * Use `import core_router` instead of `from tools import core_router`.
   * Ensure `requirements.txt` is in the same folder as `main.py`.

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
