import json
import os
import urllib
import urllib.parse
from urllib.request import urlopen

import feedparser
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load config from .env file
load_dotenv()
API_KEY = os.environ["API_KEY"]

app = Flask(__name__)

RSS_FEEDS = {
    "omgubuntu": "https://omgubuntu.co.uk/feed",
    "sysdig": "https://sysdig.com/feed/",
    "dice": "https://www.dicebreaker.com/feed",
    "python": "https://realpython.com/atom.xml",
}

DEFAULTS = {"publication": "omgubuntu", "city": "London,UK"}


@app.route("/")
def home():
    # get customized headlines, based on user input or default
    publication = request.args.get("publication")
    if not publication:
        publication = DEFAULTS["publication"]
    articles = get_news(publication)
    # get customized weather based on user input or default
    city = request.args.get("city")
    if not city:
        city = DEFAULTS["city"]
    weather = get_weather(city)


return render_template("home.html", articles=articles, weather=weather)


def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS["publication"]
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed["entries"]


def get_weather(query):
    api_url = (
        "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="
        + API_KEY
    )
    query = urllib.parse.quote(query)
    url = api_url.format(query)
    # data = urlopen(url).read()
    with urlopen(url) as response:
        data = response.read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {
            "description": parsed["weather"][0]["description"],
            "temperature": parsed["main"]["temp"],
            "city": parsed["name"],
        }
    return weather


if __name__ == "__main__":
    app.run(port=5000, debug=True)
