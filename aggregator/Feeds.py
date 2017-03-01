import os.path
from peewee import *

DATABASE_FILE = os.path.abspath(os.path.join(os.getcwd(), 'aggregator.db'))

db = SqliteDatabase(DATABASE_FILE)

class Source(Model):
    name = CharField(max_length=120)
    url = TextField(unique=True)

    class Meta:
        database = db

class Item(Model):
    source = ForeignKeyField(Source)
    url = TextField(unique=True)
    created = DateTimeField()
    last_updated = DateTimeField()
    content = TextField()

    class Meta:
        database = db

# Important for requests
def before_request_handler():
    db.connect()

def after_request_handler():
    db.close()
