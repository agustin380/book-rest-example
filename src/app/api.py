from flask_restful import Api

from .resources.books import BookListResource, BookResource
from .resources.chapters import ChapterListResource, ChapterResource
from .resources.errors import ErrorResource

from .app import app

api = Api(app, catch_all_404s=True)

api.add_resource(ChapterResource, '/api/chapters/<chapter_id>/')
api.add_resource(ChapterListResource, '/api/books/<book_id>/chapters/')

api.add_resource(BookResource, '/api/books/<book_id>/')
api.add_resource(BookListResource, '/api/books/')

api.add_resource(ErrorResource, '/api/errors/')
