from flask import Flask
from Feed import Source, Item
import json

app = Flask(__name__)
@app.route('/feeds')
def feeds():
    """
    Returns the list of sources.
    """
    sources = []
    for source in Source.select():
        sources.append(source)

    return json.dumps(sources)

@app.route('/feed/:url/')
def feed_latest():
    """
    Returns the latest entries for given feed
    """
    pass

@app.route('/feeds/search/:query')
def search_feeds():
    """
    Returns feeds by query.
    You can query by date currently
    """
    pass
