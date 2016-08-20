import unittest

from ..models import Book, Chapter, db

class TestModels(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        Book.query.delete()
        Chapter.query.delete()

    def test_book_creation(self):
        """Test that a book can be created correctly."""
        title = 'Fahrenheit 451'
        author = 'Ray Bradbury'
        book = Book(title=title, author=author)
        db.session.add(book)
        db.session.commit()

        book = Book.query.first()
        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)

    def test_chapter_creation(self):
        """Test that a chapter can be created correctly."""
        title = 'Fahrenheit 451'
        author = 'Ray Bradbury'
        book = Book(title=title, author=author)
        db.session.add(book)
        db.session.commit()

        name = 'Chapter 1'
        chapter = Chapter(name=name, book=book)
        db.session.add(chapter)
        db.session.commit()
        self.assertEqual(chapter.name, name)
        self.assertIn(chapter, book.chapters.all())
