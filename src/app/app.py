import logging

from flask import Flask, got_request_exception

from . import settings
from .utils import log_exception


app = Flask(__name__)

if not app.debug:
    file_handler = logging.FileHandler(settings.LOG_FILE_LOCATION)
    file_handler.setFormatter(logging.Formatter(settings.LOGGING_FORMAT))
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

    got_request_exception.connect(log_exception, app)
