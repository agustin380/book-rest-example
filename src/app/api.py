from .resources.books import BookListResource, BookResource, Api

from .app import app
api = Api(app)

api.add_resource(BookListResource, '/api/books/')
api.add_resource(BookResource, '/api/books/<book_id>/')
