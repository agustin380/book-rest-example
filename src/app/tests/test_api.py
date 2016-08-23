import unittest
import json

from ..app import app
from .. import settings
from ..models import db, Book, Chapter


class ApiTestCase(unittest.TestCase):
    """Base API test case."""
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()


class TestBookApi(ApiTestCase):

    def test_get_ok(self):
        """Performing a GET request for an existing book returns a JSON
        representation of the book.
        """
        book = Book.create('title', 'author')
        r = self.app.get('/api/books/{}/'.format(book.id))
        self.assertEqual(r.status_code, 200)
        response = json.loads(r.data.decode('utf-8'))
        self.assertEqual(response, book.to_dict())

    def test_get_not_found(self):
        """Performing a GET request for a non-existing book returns a 404
        status code.
        """
        r = self.app.get('/api/books/{}/'.format(1))
        self.assertEqual(r.status_code, 404)

    def test_put_ok(self):
        """Performing a PUT request for an existing book updates said book.
        """
        book = Book.create('title', 'author')
        book_data = book.to_dict()
        data = {
            'title': 'title_2',
            'author': 'author_2',
        }
        r = self.app.put(
            '/api/books/{}/'.format(1),
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(r.status_code, 201)
        book_data.update(data)
        response = json.loads(r.data.decode('utf-8'))
        self.assertEqual(response, book_data)

    def test_put_not_found(self):
        """Performing a PUT request for a non-existing book returns a 404
        status code.
        """
        r = self.app.put('/api/books/{}/'.format(1))
        self.assertEqual(r.status_code, 404)

    def test_delete_ok(self):
        """Performing a DELETE request for an existing book deletes it.
        """
        book = Book.create('title', 'author')
        r = self.app.delete('/api/books/{}/'.format(1))
        self.assertEqual(r.status_code, 204)
        self.assertIsNone(Book.query.first())

    def test_delete_not_found(self):
        """Performing a DELETE request for a non-existing book returns a 404
        status code.
        """
        r = self.app.delete('/api/books/{}/'.format(1))
        self.assertEqual(r.status_code, 404)


class TestBookListApi(ApiTestCase):

    def test_get_ok(self):
        """Performing a GET request returns a list of the existing books.
        """
        book = Book.create('title', 'author')
        book_2 = Book.create('title_2', 'author_2')

        r = self.app.get('/api/books/')
        self.assertEqual(r.status_code, 200)

        response = json.loads(r.data.decode('utf-8'))
        expected = [
            {'id': 1, 'title': 'title', 'author': 'author', 'chapters': []},
            {'id': 2, 'title': 'title_2', 'author': 'author_2', 'chapters': []},
        ]
        self.assertEqual(response, expected)

    def test_post_ok(self):
        """Performing a POST request creates a new book."""
        data = {
            'title': 'title',
            'author': 'author',
        }
        r = self.app.post(
            '/api/books/',
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(r.status_code, 201)
        book = Book.query.get(1)
        response = json.loads(r.data.decode('utf-8'))
        self.assertEqual(response, book.to_dict())

    def test_post_error(self):
        """Performing a POST request with missing parameters returns a
        400 status code.
        """
        data = {
            'title': 'title',
        }
        r = self.app.post(
            '/api/books/',
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(r.status_code, 400)
        response = json.loads(r.data.decode('utf-8'))
        self.assertEqual(response, {'message': 'Missing parameters'})


class TestChapterListApi(ApiTestCase):

    def test_get_ok(self):
        """Performing a GET request returns a list of a book's chapters.
        """
        book = Book.create('title', 'author')
        chapter_1 = Chapter.create(name='chapter_1', book=book)
        chapter_2 = Chapter.create(name='chapter_2', book=book)

        r = self.app.get('/api/books/1/chapters/')
        self.assertEqual(r.status_code, 200)

        response = json.loads(r.data.decode('utf-8'))
        expected = [
            {'id': 1, 'name': 'chapter_1', 'book': 1},
            {'id': 2, 'name': 'chapter_2', 'book': 1},
        ]
        self.assertEqual(response, expected)

    def test_post_ok(self):
        """Performing a POST request creates a new chapter."""
        book = Book.create('title', 'author')
        data = {
            'name': 'chapter_1',
        }
        r = self.app.post(
            '/api/books/1/chapters/',
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(r.status_code, 201)
        chapter = Chapter.query.get(1)
        response = json.loads(r.data.decode('utf-8'))
        self.assertEqual(response, chapter.to_dict())

    def test_post_error(self):
        """Performing a POST request with missing parameters returns a
        400 status code.
        """
        book = Book.create('title', 'author')
        data = {}
        r = self.app.post(
            '/api/books/1/chapters/',
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(r.status_code, 400)
        response = json.loads(r.data.decode('utf-8'))
        self.assertEqual(response, {'message': 'Missing parameters'})


class TestChapterApi(ApiTestCase):

    def test_get_ok(self):
        """Performing a GET request for an existing chapter returns a JSON
        representation of the chapter.
        """
        book = Book.create('title', 'author')
        chapter = Chapter.create(name='chapter', book=book)

        r = self.app.get('/api/chapters/{}/'.format(book.id))
        self.assertEqual(r.status_code, 200)

        response = json.loads(r.data.decode('utf-8'))
        self.assertEqual(response, chapter.to_dict())

    def test_get_not_found(self):
        """Performing a GET request for a non-existing chapter returns a 404
        status code.
        """
        r = self.app.get('/api/chapters/{}/'.format(1))
        self.assertEqual(r.status_code, 404)

    def test_put_ok(self):
        """Performing a PUT request for an existing chapter updates said chapter.
        """
        book = Book.create('title', 'author')
        chapter = Chapter.create(name='chapter', book=book)
        chapter_data = chapter.to_dict()
        data = {
            'name': 'chapter_2',
        }
        r = self.app.put(
            '/api/chapters/{}/'.format(1),
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(r.status_code, 201)
        chapter_data.update(data)
        response = json.loads(r.data.decode('utf-8'))
        self.assertEqual(response, chapter_data)

    def test_put_not_found(self):
        """Performing a PUT request for a non-existing chapter returns a 404
        status code.
        """
        r = self.app.put('/api/chapters/{}/'.format(1))
        self.assertEqual(r.status_code, 404)

    def test_delete_ok(self):
        """Performing a DELETE request for an existing chapter deletes it.
        """
        book = Book.create('title', 'author')
        chapter = Chapter.create(name='chapter', book=book)
        r = self.app.delete('/api/chapters/{}/'.format(1))
        self.assertEqual(r.status_code, 204)
        self.assertEqual(len(Chapter.query.all()), 0)

    def test_delete_not_found(self):
        """Performing a DELETE request for a non-existing chapter returns a 404
        status code.
        """
        r = self.app.delete('/api/chapters/{}/'.format(1))
        self.assertEqual(r.status_code, 404)
