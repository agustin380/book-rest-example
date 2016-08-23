from flask_restful import Api

from .resources.books import BookListResource, BookResource
from .resources.chapters import ChapterListResource, ChapterResource

from .app import app

api = Api(app)

api.add_resource(ChapterResource, '/api/chapters/<chapter_id>/')
api.add_resource(ChapterListResource, '/api/books/<book_id>/chapters/')

api.add_resource(BookResource, '/api/books/<book_id>/')
api.add_resource(BookListResource, '/api/books/')
