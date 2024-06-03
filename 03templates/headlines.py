import feedparser
from flask import Flask, render_template

app = Flask(__name__)

RSS_FEEDS = {
    "omgubuntu": "https://omgubuntu.co.uk/feed",
    "sysdig": "https://sysdig.com/feed/",
    "dice": "https://www.dicebreaker.com/feed",
    "python": "https://realpython.com/atom.xml",
}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="omgubuntu"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed["entries"][0]
    return render_template(
        "home.html",
        title=first_article.get("title"),
        published=first_article.get("published"),
        summary=first_article.get("summary"),
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
