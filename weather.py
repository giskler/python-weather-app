import requests
import json 
import os
from dotenv import load_dotenv 

load_dotenv() # This line loads the variables from .env

# Now get the API key using os.getenv()
api_key = os.getenv("API_KEY")

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' # Can be changed to 'imperial' for Fahrenheit
     }
    response = requests.get(base_url, params=params)  

    if response.status_code == 200: 
        weather_data = response.json() 
        return weather_data
    else:
        print(f"Error from API: Status Code {response.status_code}")
        print(response.json())
    return None 

def display_weather(weather_data):
    if weather_data:
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed'] 

        print(f"Weather: {main_weather} ({description})")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Could not retrieve weather data.") 

if __name__ == "__main__":
    if not api_key:
        print("Error: API_KEY not found. Please set it in your .env file.")
    else:
        city = input("Enter a city name: ")
        weather_info = get_weather(api_key, city)
        display_weather(weather_info)