import pyttsx3


def text_to_speach(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()