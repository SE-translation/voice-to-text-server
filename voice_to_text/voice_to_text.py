import speech_recognition as sr

r = sr.Recognizer()


def transcribe_audio(file, audio_engine="sphinx") -> str:
    """Turn audio into text, audio_engine can be sphinx or google"""
    audio_file = sr.AudioFile(file)
    with audio_file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    if audio_engine == "sphinx":
        text = r.recognize_sphinx(audio)
    elif audio_engine == "google":
        text = r.recognize_google(audio)
    else:
        text = r.recognize_sphinx(audio)
    return text

