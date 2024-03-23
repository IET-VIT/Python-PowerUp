import pyttsx3
import requests

engine = pyttsx3.init()
engine.setProperty("rate", 180)
engine.setProperty("volume", 0.5)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

CITY_NAME = "Vellore"
API_KEY = "f8714125284321d19e2bc8973679a4d0"

def main():
    engine.say("Hello, How are you doing today? I am here to tell you the weather of your city. What is your city?")
    engine.runAndWait()
    
    CITY_NAME = input("Enter your city: ")
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={CITY_NAME}"
    
    engine.say("Please wait for a moment. I am fetching the data.")
    engine.runAndWait()
    
    response = requests.get(BASE_URL).json()
    
    temperature = response["main"]["temp"]
    temperature = temperature - 273.15
    description = response["weather"][0]["description"]
    main = response["weather"][0]["main"]
    humidity = response["main"]["humidity"]
    
    string = f"The temperature in {CITY_NAME} is {temperature:.2f} degree celsius and the weather is {main} with {description} and the humidity is {humidity} percent"
    
    engine.say(string)
    engine.runAndWait()
    
    
if __name__ == "__main__":
    main()