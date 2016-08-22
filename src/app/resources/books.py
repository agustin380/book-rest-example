from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from ..models import Book, Chapter
from ..utils import get_model_or_404

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, location='json')
parser.add_argument('author', type=str, location='json')


class BookResource(Resource):

    def get(self, book_id):
        book = get_model_or_404(Book, book_id)
        return book.to_dict()

    def delete(self, book_id):
        book = get_model_or_404(Book, book_id)
        book.delete()
        return '', 204

    def put(self, book_id):
        book = get_model_or_404(Book, book_id)
        args = parser.parse_args()
        title = args['title']
        author = args['author']
        book.update(title, author)
        return book.to_dict(), 201


class BookListResource(Resource):
    def get(self):
        return [book.to_dict() for book in Book.query.all()]

    def post(self):
        args = parser.parse_args()
        book = Book.create(title=args['title'], author=args['author'])
        return book.to_dict(), 201
