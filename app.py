import requests
import json 
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request 

load_dotenv() # This line loads the variables from .env
app = Flask(__name__) # Initialize the Flask app

# Now get the API key using os.getenv()
api_key = os.getenv("API_KEY")

# Get weather function
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

# The main page route
@app.route('/')
def index():
    return render_template('index.html')

# The route to handle the form submission and display weather
@app.route('/weather')
def get_weather_route():
    city = request.args.get('city') # Get city from form
    weather_data = None
    if city:
        api_key = os.getenv("API_KEY")
        weather_data = get_weather(api_key, city)
    return render_template('weather.html', weather=weather_data)

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