import pyttsx3 as tts


class SoniaSpeak:
    def __init__(self):
        # setup sonias voice
        self.speaker = tts.init()
        self.speaker.setProperty('rate', 160)

        self.voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('voice', self.voices[1].id)

        for voice in self.voices:
            print(voice.languages)


    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()


sonia = SoniaSpeak()
sonia.speak('this is')

