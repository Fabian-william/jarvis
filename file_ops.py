import os

class FileOps:
    def __init__(self):
        # Create a dedicated folder on your Desktop
        self.export_path = os.path.join(os.path.expanduser("~"), "Desktop", "Jarvis_Exports")
        if not os.path.exists(self.export_path):
            os.makedirs(self.export_path)

    def save_code(self, code_content, file_name="script.cpp"):
        try:
            full_path = os.path.join(self.export_path, file_name)
            with open(full_path, "w") as f:
                f.write(code_content)
            return f"Sir, I've saved the code to your desktop in the Jarvis_Exports folder as {file_name}."
        except Exception as e:
            return f"I failed to write the file: {e}"