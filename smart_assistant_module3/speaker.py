import platform, subprocess, pyttsx3

def speak(text):
    text = (text or "").strip()
    if not text:
        return
    if 'darwin' in platform.system().lower():
        try:
            subprocess.run(['say', text], check=True)
            return
        except Exception:
            pass
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()
