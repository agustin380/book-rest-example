import os

from flask_sqlalchemy import SQLAlchemy

from .app import app
from . import settings

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

    @classmethod
    def create(cls, title, author):
        book = cls(title, author)
        db.session.add(book)
        db.session.commit()
        return book

    def update(self, title=None, author=None):
        if title:
            self.title = title
        if author:
            self.author = author
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """Special method for serialization."""
        chapters = [chapter.id for chapter in self.chapters.all()]
        data = {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'chapters': chapters,
        }
        return data

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship(
        'Book', foreign_keys=book_id, backref=db.backref(
            'chapters', cascade="all, delete-orphan", lazy='dynamic'
        )
    )

    def __init__(self, name, book):
        self.name = name
        self.book = book

    def __repr__(self):
        return '<Chapter {}>'.format(self.name)

    @classmethod
    def create(cls, name, book):
        chapter = cls(name, book)
        db.session.add(chapter)
        db.session.commit()
        return chapter

    def update(self, name=None):
        if name:
            self.name = name
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """Special method for serialization."""
        data = {
            'id': self.id,
            'name': self.name,
            'book': self.book.id,
        }
        return data
