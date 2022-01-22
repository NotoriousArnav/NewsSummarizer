from local.feed_processing import *
from flask import Blueprint, jsonify

app = Blueprint("api", "api", url_prefix="/api/v1")

with open('rss_list.json', 'r') as _: rss_channels = json.loads(_.read())

@app.route("/")
def index_():
    data = {
                'available_channels':[list(x) for x in enumerate(rss_channels)],
                'instructions': {
                1:"""
                Do a GET at /api/v1/{channel_id}
                to get all the headlines, their articles, and summary of the article
                """,
                2:"""
                Do GET /api/v1/all to get data from articles from all channels
                """,
                3:"""
                Do /api/v1/{channel_id} or
                Do /api/v1/all
                to get all data.
                By putting summary equals True or False, you can turn on summary, same goes with 'article' keyword.
                'title' or the headline cant be turned off
                """
                }
            }
    return jsonify(
                {
                    'status': [200, 'Working'],
                    'data':data
                    }
            )
