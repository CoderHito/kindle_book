import uuid
from datetime import datetime

from app_runner import db


class Book(db.Model):
    book_id = db.Column(db.String(64), primary_key=True)
    book_title = db.Column(db.String(128))
    book_author_info = db.Column(db.String(256))
    book_price_now = db.Column(db.String(64))
    book_link = db.Column(db.String(512))
    create_time = db.Column(db.DateTime)

    def __init__(self, book_title, book_author, book_link, book_price_now):
        self.book_id = str(uuid.uuid4())
        self.book_author_info = book_author
        self.book_title = book_title
        self.book_price_now = book_price_now
        self.book_link = book_link
        self.create_time = datetime.now()
        db.session.add(self)
        db.session.commit()
