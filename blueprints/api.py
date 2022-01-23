from local.feed_processing import *
from flask import Blueprint, jsonify, request
import threading
import base64
import time

app = Blueprint("api", "api", url_prefix="/api/v1")

with open('rss_list.json', 'r') as _: rss_channels = json.loads(_.read())

links = []

def bg_thread():
    global links
    while True:
        for x in rss_channels:
            print('Downloading ',x)
            links.append([(y[0], y[1], base64.b64encode(y[1].encode()).decode()) for y in get_feed(x)])
        print(len(links),'\n', ''.join([str(len(x)) for x in links]))
        time.sleep(1*60)
        links.clear()

feed_thread = threading.Thread(target=bg_thread)
feed_thread.start()

@app.route("/")
def index_():
    data = {
                'available_channels':[list(x) for x in enumerate(rss_channels)],
            }
    return jsonify(
                {
                    'status': [200, 'Working'],
                    'data':data
                    }
            )

@app.route('/available_articles')
def return_articles():
    return jsonify(
            {
                'articles':links
            }
            )

@app.route('/get_article/<b64encodedString>')
def return_link(b64encodedString):
    link = base64.b64decode(b64encodedString).decode().replace('\n', '')
    print(link)
    title, article = article_extracter(link)
    return jsonify(
            {
                "title":title,
                "url":link,
                "summary":summarize(article),
                "article":article,
                }
            )
