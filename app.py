import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    print(f"\nWeather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Description: {data['weather'][0]['description'].title()}")
else:
    print("\nCity not found. Please try again.")