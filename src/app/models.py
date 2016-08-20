import os

from flask_sqlalchemy import SQLAlchemy

from ..main import app
from .. import settings

app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80), unique=True)

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return '<Book title:{} author:{}>'.format(self.title, self.author)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship(
        'Book', backref=db.backref('chapters', lazy='dynamic')
    )

    def __init__(self, name, book):
        self.name = name
        self.book = book

    def __repr__(self):
        return '<Chapter {}>'.format(self.name)
