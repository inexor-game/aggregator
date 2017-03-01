from .aggregator import app
from .Feeds import before_request_handler, after_request_handler

# Main entry point for uWSGI applications.
# Rate limiting should be done on the web server rather than by flask.
if __name__ == "__main__":
    app.before_request = before_request_handler
    app.after_request(after_request_handler)
    app.run() # Maybe add a port configuration here