aggregator
====================
Aggregator is a RESTful web service that collects feeds, tweets, images and videos from various platforms.
It is configured using the `@inexor-game/blog-data` configuration files.

# Developing

## Install
Install the dependencies with `pip install -r requirements.txt`, best is a virtualenv.
We do use `python3.5` by default, no promises are made as for backward compatibility.

## Running the flask app
The flask app can be run with:
```
export FLASK_APP=aggregator/aggregator.py
export FLASK_DEBUG=1
flask run
```

## Fetching the contents
The `runner` is standalone and can called via `python aggregate/runner.py`

# Deploying

## Database choice
Currently SQlite3 is used, since the database footprint is small. In future, our [ORM](http://docs.peewee-orm.com/en/latest/) supports changing to PostgreSQL.

## Embed in your webserver
For deployment we will use [uWSGI spool](https://uwsgi-docs.readthedocs.io/en/latest/Spooler.html), since that also offers `spool` for polling the information.
See [documentation](http://flask.pocoo.org/docs/0.12/deploying/).


