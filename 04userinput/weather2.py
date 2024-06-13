import json
import urllib
import urllib.parse
from urllib.request import urlopen


def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0189b36c2f484e0d281f6adf002feed4"
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
