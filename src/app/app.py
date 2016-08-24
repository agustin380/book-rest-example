import logging

from flask import Flask, got_request_exception

from .utils import log_exception


app = Flask(__name__)

if not app.debug:
    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
    ))
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

    got_request_exception.connect(log_exception, app)
