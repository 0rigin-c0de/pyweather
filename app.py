import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(api_key, city, units):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': units
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    else:
        return None

def display_weather(weather, units):
    if weather:
        unit_symbol = "°C" if units == "metric" else "°F" if units == "imperial" else "K"
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}{unit_symbol}")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Error: Could not fetch weather data")

def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")  
    if not api_key:
        print("Error: No API key found. Please set the OPENWEATHER_API_KEY environment variable.")
        return

    city = input("Enter city name: ")
    units = input("Enter units (metric, imperial, standard): ").strip().lower()
    if units not in ["metric", "imperial", "standard"]:
        print("Invalid units. Using 'metric' by default.")
        units = "metric"
    weather = get_weather(api_key, city, units)
    display_weather(weather, units)

if __name__ == "__main__":
    main()
