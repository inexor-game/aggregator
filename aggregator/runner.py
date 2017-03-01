import json
import os.path
from datetime import datetime
from html import escape
import feedparser
from peewee import IntegrityError
from Feeds import DATABASE_FILE, Source, Item, db

_PARDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
FEEDS_FILE = os.path.join(_PARDIR + '/blog-data/config/feeds.json')

def update_feed_sources():
    """
    Loads the list of feeds from the configuration file and writes / updates the database.
    """
    feeds_file = open(FEEDS_FILE)
    feeds = json.load(feeds_file)
    feeds_file.close()

    for feed in feeds:
        try:
            Source.create_or_get(name=feed, url=feeds[feed])
        except IntegrityError:
            pass

    for source in Source.select().where(Source.url.not_in([feeds.values()])):
        source.delete() # Delete old sources

# Step by step
# - create a database if it doesn't exist
# - update the feed sources from the JSON files
# - for every feed find the latest entries, and add new entries if available

def fetch_entries():
    if not os.path.isfile(DATABASE_FILE):
        db.create_tables([Source, Item])
    else:
        db.connect()

    update_feed_sources()
    for source in Source.select():
        feed = feedparser.parse(source.url)
        for entry in feed.entries:
            try:
                Item.create(source=source, url=entry.link, created=entry.published, last_updated=datetime.now(), content=escape(entry.summary_detail.value))
            except IntegrityError:
                # This is beeing thrown due the unique constraint
                item = Item.get(url=entry.link)
                item.content = escape(entry.summary_detail.value)
                item.last_updated = datetime.now()

    db.close()

# This is for development usage only and should not be used otherwise
if __name__ == "__main__":
    fetch_entries()