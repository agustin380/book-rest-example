import unittest
import json

import flaskr
from .. import settings
from ..models import db, Book, Chapter


class TestBookResources(unittest.TestCase):

    def setUp(self):
        settings.DATABASE_URI = 'sqlite:///:memory:'
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_get_ok(self):
        """Performing a GET request for an existing book returns a JSON
        representation of the book.
        """
        book = Book.create('title', 'author')
        r = self.app.get('/api/books/{}/'.format(book.id))
        data = json.loads(r.data)
        self.assertEqual(data, book.to_dict())
