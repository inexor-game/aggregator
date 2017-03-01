aggregator
====================
Aggregator is a RESTful web service that collects feeds, tweets, images and videos from various platforms.
It is configured using the `@inexor-game/blog-data` configuration files.

# Developing

## Install
Install the dependencies with `pip install -r requirements.txt`, best is a virtualenv.
We do use `python3.5` by default, no promises are made as for backward compatibility.
As well you must check out the `blog-data` submodule, which you can do with `git submodule update --init`

## Running the flask app
The flask app can be run with:
```
export FLASK_APP=aggregator/aggregator.py
export FLASK_DEBUG=1
flask run
```

## Fetching the contents
The `runner` is standalone and can called via `python aggregate/runner.py`

## Testing the uWSGI application
You can test the application like this:

```
uwsgi -ini aggregator.ini --socket=localhost:5000 --protocol=http
```
And whups, `aggregator` served by `uWSGI` at your place!

# Deploying

## Database choice
Currently SQlite3 is used, since the database footprint is small. In future, our [ORM](http://docs.peewee-orm.com/en/latest/) supports changing to PostgreSQL.

## Embed in your webserver
To embed it into your web server you can use `uwsgi` coming preconfigured with `uwsgi -ini aggregator.ini`
Other software, such as Gunicorn, may work as well, is not tested yet though.
For the respective web server configuration have a look [here](http://flask.pocoo.org/docs/0.12/deploying/uwsgi/).

## Adding a cron job for the runner
A simple cron job could look like this
```
* */15 * * sh -c 'cd /path/to/aggregator/ && /path/to/virtualenv/bin/python aggregator/runner.py
```

### A note on spoolers
In the future we may use [uWSGI spool](https://uwsgi-docs.readthedocs.io/en/latest/Spooler.html) to do the job the runner `__main__` does currently.
