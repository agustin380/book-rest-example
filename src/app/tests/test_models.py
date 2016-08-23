import unittest

from ..models import Book, Chapter, db

class TestBookModel(unittest.TestCase):

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


class TestChapterModel(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_chapter_creation_and_deletion(self):
        """Test that a chapter can be created and deleted correctly."""
        title = 'Fahrenheit 451'
        author = 'Ray Bradbury'
        book = Book.create(title, author)

        name = 'Chapter 1'
        chapter = Chapter.create(book=book, name=name)

        chapter = Chapter.query.first()
        self.assertEqual(chapter.name, name)
        self.assertEqual(chapter.book, book)

        chapter.delete()
        self.assertEqual(len(book.chapters.all()), 0)

    def test_chapter_update(self):
        """Test that a chapter can be updated."""
        title = 'Fahrenheit 451'
        author = 'Ray Bradbury'
        book = Book.create(title, author)

        name = 'Chapter 1'
        chapter = Chapter.create(book=book, name=name)

        new_name = 'Chapter 2'
        chapter = chapter.update(name=new_name)

        self.assertEqual(chapter.name, new_name)

    def test_chapter_serialization(self):
        """Test that a chapter is serialized correctly."""
        title = 'Fahrenheit 451'
        author = 'Ray Bradbury'
        book = Book.create(title, author)

        name = 'Chapter 1'
        chapter = Chapter.create(book=book, name=name)

        data = {
            'id': 1,
            'name': name,
            'book': 1,
        }
        self.assertEqual(data, chapter.to_dict())
