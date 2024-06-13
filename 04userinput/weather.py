import os

import requests
from dotenv import load_dotenv

# Load config from .env file
load_dotenv()
API_KEY = os.environ["API_KEY"]

city = input("Enter City name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    tempinc = temp - 273.15
    desc = data["weather"][0]["description"]
    print(f"Temperature: {temp} C")
    print(f"Description: {desc}")
else:
    print("Error fetching weather data")
