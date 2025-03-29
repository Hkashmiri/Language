import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print(f"Google Speech Recognition thinks you said: {text}")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service")




