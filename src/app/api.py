from .resources.books import BookListResource, BookResource, Api

from .app import app
api = Api(app)

api.add_resource(BookListResource, '/books/')
api.add_resource(BookResource, '/books/<book_id>/')
