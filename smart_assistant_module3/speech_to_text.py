import speech_recognition as sr

def listen_command(timeout=None, phrase_time_limit=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("🎤 Listening...")
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except Exception as e:
            print("⏱️ Error:", e)
            return ""
    try:
        text = r.recognize_google(audio).lower()
        print("🗣️ Heard:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand.")
        return ""
