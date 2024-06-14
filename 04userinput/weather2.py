import json
import os
import urllib
import urllib.parse
from urllib.request import urlopen

# import requests
from dotenv import load_dotenv

# Load config from .env file
load_dotenv()
API_KEY = os.environ["API_KEY"]


def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={API_KEY}"
    query = urllib.parse.quote(query)
    url = api_url.format(query)
    data = urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {
            "description": parsed["weather"][0]["description"],
            "temperature": parsed["main"]["temp"],
            "city": parsed["name"],
        }
    return weather
