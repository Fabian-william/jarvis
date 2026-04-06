import win32com.client
import time
import speech_recognition as sr


class Perception:
    def __init__(self):
        # SAPI.SpVoice is the most stable direct-to-Windows driver
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")

    def speak(self, text):
        print(f"Assistant: {text}")
        # '1' starts the speech without stopping the code
        self.speaker.Speak(text, 1)

        # This loop waits until the assistant IS FINISHED talking
        # before letting the code move to the 'listen' step.
        while self.speaker.Status.RunningState != 1:
            time.sleep(0.1)

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # High sensitivity for FAB-PC2 laptop mic
            r.dynamic_energy_threshold = True
            r.pause_threshold = 0.8

            print("Listening... (Speak now)")
            try:
                # We use a short timeout to keep the loop fresh
                audio = r.listen(source, timeout=None, phrase_time_limit=10)
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User: {query}")
                return query.lower()
            except Exception:
                return ""