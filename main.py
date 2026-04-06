import datetime
from brain import Brain
from perception import Perception
from tools.internet_ops import InternetOps
from tools.file_ops import FileOps  # Direct class import


def main():
    # 1. Initialize all systems
    sense = Perception()
    intellect = Brain()
    web_tools = InternetOps()
    file_tools = FileOps()  # Now it's clean and direct

    last_response = ""
    sense.speak("Systems integrated. All cores online ")

    while True:
        command = sense.listen()
        if not command:
            continue

        # --- 2. TOOL ROUTING (Instant Actions) ---
        if "weather" in command:
            report = web_tools.get_weather()
            sense.speak(report)
            continue

        if "search for" in command:
            search_query = command.replace("search for", "").strip()
            report = web_tools.web_search(search_query)
            sense.speak(report)
            continue

        if "save that code as" in command:
            # Logic to extract filename
            parts = command.split("as")
            filename = parts[-1].strip() if len(parts) > 1 else "script.cpp"

            if "." not in filename:
                filename += ".cpp"

            if last_response:
                # This calls the method inside tools/file_ops.py
                report = file_tools.save_code(last_response, filename)
                sense.speak(report)
            else:
                sense.speak("Sir, there is no code in my recent memory to save.")
            continue

        if "shutdown" in command or "go to sleep" in command:
            sense.speak("Powering down systems. Goodbye, sir.")
            break

        # --- 3. BRAIN ROUTING (Thinking/Coding) ---
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        full_prompt = f"Time: {current_time}. User: {command}"

        last_response = intellect.chat(full_prompt)
        sense.speak(last_response)


if __name__ == "__main__":
    main()