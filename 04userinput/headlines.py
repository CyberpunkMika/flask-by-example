import json
import urllib
import urllib.parse

import feedparser
import urllib3
from flask import Flask, render_template, request

app = Flask(__name__)

RSS_FEEDS = {
    "omgubuntu": "https://omgubuntu.co.uk/feed",
    "sysdig": "https://sysdig.com/feed/",
    "dice": "https://www.dicebreaker.com/feed",
    "python": "https://realpython.com/atom.xml",
}

def get_weather(query):
    api_url = https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0189b36c2f484e0d281f6adf002feed4
    query = urllib.parse.quote(query)
    url = api_url.format(query)
    data = urllib3.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":
            parsed["weather"][0]["description"],
            "temperature":parsed["main"]["temp"],
            "city":parsed["name"]
            }
    return weather

@app.route("/", methods=["GET", "POST"])
def get_news():
    query = request.form.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "omgubuntu"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed["entries"])


if __name__ == "__main__":
    app.run(port=5000, debug=True)
