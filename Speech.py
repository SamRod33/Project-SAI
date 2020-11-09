import speech_recognition as sr

r = sr.Recognizer()
import speech_recognition as sr
with sr.Microphone(device_index=2) as source:
    #r.adjust_for_ambient_noise(source)
    print("S P E A K")
    audio = r.listen(source, timeout = 10)

print("Using Google recognize: " + r.recognize_google(audio))
