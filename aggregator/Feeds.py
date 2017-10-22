import os.path
import configparser
from peewee import *

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'aggregator.ini'))

db = MySQLDatabase(host=config['database']['host'], user=config['database']['user'], passwd=config['database']['password'], db=config['database']['db'])

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
