from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from ..models import Book, Chapter
from ..utils import get_model_or_404

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location='json')


class ChapterResource(Resource):

    def get(self, chapter_id):
        chapter = get_model_or_404(Chapter, chapter_id)
        return chapter.to_dict()

    def delete(self, chapter_id):
        chapter = get_model_or_404(Chapter, chapter_id)
        chapter.delete()
        return '', 204

    def put(self, chapter_id):
        chapter = get_model_or_404(Chapter, chapter_id)
        args = parser.parse_args()
        name = args['name']
        chapter.update(name)
        return chapter.to_dict(), 201


class ChapterListResource(Resource):

    def get(self, book_id):
        book = get_model_or_404(Book, book_id)
        return [chapter.to_dict() for chapter in book.chapters.all()]

    def post(self, book_id):
        book = get_model_or_404(Book, book_id)
        args = parser.parse_args()
        name = args['name']
        if not name:
            abort(400, message='Missing parameters')
        chapter = Chapter.create(name=args['name'], book=book)
        return chapter.to_dict(), 201
