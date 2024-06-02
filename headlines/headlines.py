import feedparser

from flask import Flask

app = Flask (__name__)

RSS_FEEDS = {'OMG Ubuntu': 'https://omgubuntu.co.uk/feed',
            'Sysdig': 'https://sysdig.com/feed/',
            'Dicebreaker': 'https://www.dicebreaker.com/feed',
            'Real Python': 'https://realpython.com/atom.xml'}

@app.route("/")
@app.route("/omg")
def omgubuntu():
  return get_news('OMG Ubuntu')

@app.route("/sysdig")
def sysdig():
  return get_news('Sysdig')

@app.route("/dice")
def dice():
  return get_news('Dicebreaker')

@app.route("/python")
def python():
  return get_news('Real Python')

def get_news(publication):
  feed = feedparser.parse(RSS_FEEDS[publication])
  first_article = feed['entries'][0]
  return """<html>
    <body>
      <h1>Headlines</h1>
      <b>{0}</b> <br />
      <i>{1}</i> <br />
      <p>{2}</p> <br />
    </body>
  </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == '__main__':
  app.run(port=5000, debug=True)
