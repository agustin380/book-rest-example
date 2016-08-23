from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from ..models import Book, Chapter
from ..utils import get_model_or_404

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location='json')


class ChapterResource(Resource):

    def get(self, chapter_id):
        """Get data of a single chapter.

        :param chapter_id: the id of a chapter.
        :type chapter_id: int
        :return: book data in JSON format.
        :rtype: JSON

        :Example:

        GET /api/chapters/42/
        >>> {"id": 42, "name": "There Will Come Soft Rains", "book_id": 14}
        """
        chapter = get_model_or_404(Chapter, chapter_id)
        return chapter.to_dict()

    def delete(self, chapter_id):
        """Delete a chapter.

        :param chapter_id: the id of a chapter.
        :type chapter_id: int
        :return: empty string.
        :rtype: str

        :Example:

        DELETE /api/chapters/15/
        """

        chapter = get_model_or_404(Chapter, chapter_id)
        chapter.delete()
        return '', 204

    def put(self, chapter_id):
        """Modify an existing chapter.

        :param chapter_id: the id of a chapter.
        :type chapter_id: int
        :param name: the name of a chapter (in the JSON body).
        :type name: str
        :return: chapter data in JSON format.
        :rtype: JSON

        :Example:

        PUT /api/chapters/33/ {"name": "The Long Years"}
        >>> {"id": 33, "name": "The Long Years", "book_id": 14}
        """
        chapter = get_model_or_404(Chapter, chapter_id)
        args = parser.parse_args()
        name = args['name']
        chapter.update(name)
        return chapter.to_dict(), 201


class ChapterListResource(Resource):

    def get(self, book_id):
        """Get a list of all the chapters of a book.

        :param book_id: the id of a book.
        :type book_id: int
        :return: list of chapters data in JSON format.
        :rtype: JSON

        :Example:

        GET /api/books/23/chapters/
        >>> [{"id": 4, ...}, {"id": 6, ...}, {"id": 16, ...}]
        """
        book = get_model_or_404(Book, book_id)
        return [chapter.to_dict() for chapter in book.chapters.all()]

    def post(self, book_id):
        """Create a new chapter for a book.

        :param book_id: the id of a book.
        :type book_id: int
        :param name: the name of a chapter (in the JSON body).
        :type name: str
        :return: book data in JSON format.
        :rtype: JSON

        :Example:

        POST /api/books/33/chapters/ {"name": "The Silent Towns"}
        >>> {"id": 42, "name": "The Silent Towns", "book_id": 33
        """

        book = get_model_or_404(Book, book_id)
        args = parser.parse_args()
        name = args['name']
        if not name:
            abort(400, message='Missing parameters')
        chapter = Chapter.create(name=args['name'], book=book)
        return chapter.to_dict(), 201
