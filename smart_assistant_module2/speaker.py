import platform, subprocess, pyttsx3

def speak(text):
    text = text.strip()
    if not text:
        return
    system = platform.system().lower()
    if 'darwin' in system:
        subprocess.run(['say', text])
    else:
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.say(text)
        engine.runAndWait()
