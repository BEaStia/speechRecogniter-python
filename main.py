# -*- coding: utf-8 -*-
__author__ = 'igorp'
import speech_recognition as sr
from gtts import gTTS
import subprocess
from subprocess import Popen, PIPE
import amplify

tts = gTTS(text=u"Открыть окно?", lang="ru")
filename = "hello.mp3"
tts.save(filename)
subprocess.call("rm -rf hello.wav", shell=True)

proc = Popen("ffmpeg -i hello.mp3 -acodec pcm_u8 -ar 22050 hello.wav", shell=True, stdout=PIPE, stderr=PIPE)
proc.wait()    # дождаться выполнения
amplify.normalize("hello.wav","hello1.wav")

r = sr.Recognizer()
r.language = "ru-RU"
with sr.WavFile("hello1.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)
# with sr.Microphone() as source:                # use the default microphone as the audio source
#     audio = r.listen(source)                   # listen for the first phrase and extract it into audio data


try:
    list = r.recognize(audio)
    print("Probably you said:"+list)

        #print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")