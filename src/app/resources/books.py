from flask import Flask
from flask_restful import reqparse, abort, Resource

from ..models import Book, Chapter
from ..utils import get_model_or_404

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, location='json')
parser.add_argument('author', type=str, location='json')


class BookResource(Resource):

    def get(self, book_id):
        """Get data of a single book, including its chapters ids.

        :param book_id: the id of a book.
        :type book_id: int
        :return: book data in JSON format.
        :rtype: JSON

        :Example:

        GET /api/books/5/
        >>> {"id": 5, "title": "Stardust", "author": "Neil Gaiman", "chapters": [4, 6, 9]}
        """

        book = get_model_or_404(Book, book_id)
        return book.to_dict(), 200

    def delete(self, book_id):
        """Delete a book and its chapters.

        :param book_id: the id of a book.
        :type book_id: int
        :return: empty string.
        :rtype: str

        :Example:

        DELETE /api/books/1/
        """

        book = get_model_or_404(Book, book_id)
        book.delete()
        return '', 204

    def put(self, book_id):
        """Modify an existing book.

        :param book_id: the id of a book.
        :type book_id: int
        :param title: the title of a book (in the JSON body).
        :type title: str
        :param author: the author of a book (in the JSON body).
        :type author: str
        :return: book data in JSON format.
        :rtype: JSON

        :Example:

        PUT /api/books/14/ {"title": "Martian Chronicles", "author": "Ray Bradbury"}
        >>> {"id": 14, "title": "Martian Chronicles", "author": "Ray Bradbury", "chapters": [5, 7, 33, 42]}
        """

        book = get_model_or_404(Book, book_id)
        args = parser.parse_args()
        title = args['title']
        author = args['author']
        book.update(title, author)
        return book.to_dict(), 201


class BookListResource(Resource):

    def get(self):
        """Get a list of all the books.

        :return: list of book data in JSON format.
        :rtype: JSON

        :Example:

        GET /api/books/
        >>> [{"id": 1, ...}, {"id": 2, ...}, {"id": 3, ...}]
        """

        return [book.to_dict() for book in Book.query.all()]

    def post(self):
        """Create a new book.

        :param title: the title of a book (in the JSON body).
        :type title: str
        :param author: the author of a book (in the JSON body).
        :type author: str
        :return: book data in JSON format.
        :rtype: JSON

        :Example:

        POST /api/books/ {"title": "The Hobbit", "author": "J. R. R. Tolkien"}
        >>> {"id": 56, "title": "The Hobbit", "author": "J. R. R. Tolkien", "chapters": []}
        """

        args = parser.parse_args()
        title = args['title']
        author = args['author']
        if not title or not author:
            abort(400, message='Missing parameters')
        book = Book.create(title=args['title'], author=args['author'])
        return book.to_dict(), 201
