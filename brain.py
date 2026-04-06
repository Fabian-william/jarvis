import ollama


class Brain:
    def __init__(self):
        # Local Specialists (Stay on your RTX 3050)
        self.chat_model = "llama3.2:1b"
        self.coder_model = "qwen2.5:3b"

        # Cloud Specialist (Runs on Ollama's Servers)
        self.cloud_model = "gpt-oss:120b-cloud"

        self.messages = [{"role": "system", "content": "You are JARVIS. Be concise and professional."}]

    def chat(self, user_input):
        user_input_lower = user_input.lower()

        # 1. THE ROUTING ENGINE
        coding_keywords = ["code", "python", "c++", "plus plus", "program", "function", "array", "queue", "algorithm"]

        if any(word in user_input_lower for word in ["analyze", "research", "complex", "explain"]):
            target = self.cloud_model
            print(f"DEBUG: Using 120B Cloud Core")
        elif any(word in user_input_lower for word in coding_keywords):
            target = self.coder_model
            print(f"DEBUG: Using Coder Core (Qwen)")
        else:
            target = self.chat_model
            print(f"DEBUG: Using Chat Core (Llama 1b)")

        # 2. THE EXECUTION
        try:
            self.messages.append({"role": "user", "content": user_input})

            response = ollama.chat(model=target, messages=self.messages)

            # Ensure we are extracting the content correctly from the Ollama response object
            if 'message' in response and 'content' in response['message']:
                reply = response['message']['content']
                self.messages.append({"role": "assistant", "content": reply})
                return reply
            else:
                return "Sir, the core responded but the message was empty."

        except Exception as e:
            print(f"CRITICAL ERROR: {str(e)}")
            return f"I'm having trouble thinking, sir. Error: {str(e)}"