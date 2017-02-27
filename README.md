aggregator
====================
Aggregator is a RESTful web service that collects feeds, tweets, images and videos from various platforms.
It is configured using the `@inexor-game/blog-data` configuration files.

## How to set it up
Create a virtualenv and run `pip install -r requirements.txt` in the main directory, which will pull the necessary dependencies.
`Aggregator` has been written from scratch with `python3.5`, so it may or may not run on older versions (no promises made).
Since only a small footprint of data is produced we rely on `SQLite3` to store these informations.

## Embed into your webserver
You should embed this application into your webserver by proxying requests to the `Flask` webserver.
Instructions can be found on their [documentation](http://flask.pocoo.org/docs/0.12/deploying/).

## Add a cron job for the runner
The `runner` script does the collecting of all sources, running independently from the API. Therefore you should set up a cron job for it to be called
in an appropriate time span:

`* */15 * * /somewhere/to/your/virtualenv /where/the/script/is/aggregator/runner.py`

This anyhow shall be replaced with [uWSGI spool](https://uwsgi-docs.readthedocs.io/en/latest/Spooler.html).

### Notes on the future
In case the number of feeds, tweets and sources is growing to rapidly, and SQLite cannot handle everything, the best bet is to use PostgreSQL (peewee) and some worker, such as uWSGI spool.
