## "RESTful Book" Web Service

A RESTful server example for a book database. Supports books and chapters data.

Requires Python 3.4 or greater.

### Endpoints
All endpoints are documented alongside their implementation. For more information, check the `src/app/resources` directory.

### Running

`pip install -r requirements.txt`

`python src/manage.py syncdb` will create the necessary database tables to run the app.
`python src/manage.py runserver --host 0.0.0.0 --port 8080` will run a development server.

### Settings
Settings can be found in the `src/app/settings.py` file.

`DATABASE_URI`: The location where the database will be stored. Defaults to the project root.

### Testing

`python src/manage.py test` will run the whole test suite. Tests are located in the `src/app/tests` directory.
