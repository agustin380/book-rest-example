import random
import logging

from flask import Flask
from flask_restful import abort, Resource

from ..models import Book, Chapter
from ..utils import get_model_or_404

logger = logging.getLogger(__name__)

EXCEPTIONS = (IndexError, AttributeError, KeyError, TypeError, ValueError)


class ErrorResource(Resource):
    """Resource for generating random errors (for logging demostration purposes)"""

    def get(self):
        """Generate a random error.
        """

        Error = random.choice(EXCEPTIONS)
        raise Error('Some error message')
