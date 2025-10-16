import platform
import subprocess
import pyttsx3
import time
import traceback

def speak(text: str):
    text = (text or "").strip()
    print(f"[speaker] called with len={len(text)}; repr={repr(text)[:300]}")
    if not text:
        print("[speaker] empty text -> returning")
        return

    system = platform.system().lower()
    # Try macOS "say" first (most reliable)
    if 'darwin' in system:
        try:
            print("[speaker] using macOS 'say' ...")
            # use check=True so an exception shows if say fails
            subprocess.run(['say', text], check=True)
            print("[speaker] 'say' completed")
            return
        except Exception as e:
            print("[speaker] macOS 'say' failed:", repr(e))
            traceback.print_exc()

    # Fallback to pyttsx3
    try:
        print("[speaker] falling back to pyttsx3")
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
        print("[speaker] pyttsx3 completed")
    except Exception as e:
        print("[speaker] pyttsx3 failed:", repr(e))
        traceback.print_exc()
