from aggregator.aggregator import app as application
from aggregator.Feeds import before_request_handler, after_request_handler

# Main entry point for uWSGI applications.
# Rate limiting should be done on the web server rather than by flask.
if __name__ == "__main__":
    application.before_request = before_request_handler
    application.after_request(after_request_handler)
    application.run() # Maybe add a port configuration here
