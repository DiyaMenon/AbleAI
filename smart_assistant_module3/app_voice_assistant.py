import subprocess, os
from speech_to_text import listen_command
from speaker import speak

# base AbleAI folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def run_module1():
    path = os.path.join(PROJECT_ROOT, "smart_assistant_module1", "app.py")
    print("🗂️ Module 1 path:", path)
    if not os.path.exists(path):
        speak("Module 1 not found.")
        print("❌ File missing:", path)
        return
    speak("Opening text reader.")
    subprocess.run(["python", path, "--mode", "camera"])

def run_module2():
    path = os.path.join(PROJECT_ROOT, "smart_assistant_module2", "app_object_detect.py")
    print("🗂️ Module 2 path:", path)
    if not os.path.exists(path):
        speak("Module 2 not found.")
        print("❌ File missing:", path)
        return
    speak("Starting object detection.")
    subprocess.run(["python", path])

def main():
    speak("Voice Assistant ready. Say 'read text', 'detect objects', or 'exit'.")
    while True:
        cmd = listen_command()
        if not cmd:
            continue
        if "read" in cmd or "text" in cmd:
            run_module1()
        elif "detect" in cmd or "object" in cmd:
            run_module2()
        elif "exit" in cmd or "quit" in cmd:
            speak("Goodbye.")
            break
        else:
            speak("I didn't understand. Say read, detect, or exit.")

if __name__ == "__main__":
    main()
