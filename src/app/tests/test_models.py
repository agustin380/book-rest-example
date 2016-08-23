import unittest

from ..models import Book, Chapter, db

class TestModels(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_book_creation_and_deletion(self):
        """Test that a book can be created and deleted correctly."""
        title = 'Fahrenheit 451'
        author = 'Ray Bradbury'
        book = Book.create(title, author)

        book = Book.query.first()
        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)

        book.delete()
        book = Book.query.first()
        self.assertIsNone(book)

    def test_book_update(self):
        """Test that a book can be updated."""
        book = Book.create('title', 'author')
        title = 'Fahrenheit 451'
        author = 'Ray Bradbury'
        book.update(title, author)

        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)

    def test_book_serialization(self):
        """Test that a book is serialized correctly."""
        title = 'Fahrenheit 451'
        author = 'Ray Bradbury'
        book = Book.create(title, author)

        data = {
            'id': 1,
            'title': title,
            'author': author,
            'chapters': [],
        }
        self.assertEqual(data, book.to_dict())
