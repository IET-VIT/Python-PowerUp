import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 280)
engine.setProperty("volume", 0.5)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def main():
    engine.say("Hello, What is your name?")
    engine.runAndWait()
    
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        string = f"Hello, {text}. How are you?"
        engine.say(string)
        engine.runAndWait()
        
        string = "Good to meet you. Bye!"
        engine.say(string)
        engine.runAndWait()
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the speech recognition service.")

if __name__ == "__main__":
    main()

