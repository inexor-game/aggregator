import json
from datetime import datetime

from flask import Flask, abort
from .Feeds import Source, Item
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict

def json_serial(obj):
    """
    JSON serializer for objects not serializable by default json code.
    """

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")

app = Flask(__name__)

@app.route('/feeds/')
def feeds():
    """
    Returns the list of sources.
    """
    sources = []
    for source in Source.select():
        sources.append(model_to_dict(source))

    print(sources)
    return json.dumps(sources)

@app.route('/feeds/latest/')
@app.route('/feeds/latest/<int:limit>/')
def latest_feeds(limit=10):
    """
    Returns the latest entries for all feeds by limit.
    """
    try:
        latest_feeds = []
        for entry in Item.select().limit(limit):
            latest_feeds.append(model_to_dict(entry))

        return json.dumps(latest_feeds, default=json_serial)
    except IntegrityError:
        abort(500)


@app.route('/feed/<int:id>/')
@app.route('/feed/<int:id>/<int:limit>/')
def feed_latest(id, limit=10):
    """
    Returns the latest entries for given feed
    """
    try:
        latest_feeds = []
        feed = Source.get(id=id)
        for entry in Item.select().filter(source=feed).limit(limit):
            latest_feeds.append(model_to_dict(entry))

        return json.dumps(latest_feeds, default=json_serial)
    except IntegrityError:
        abort(404) # No feed found


