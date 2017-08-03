import uuid
from datetime import datetime

from kindle_book.ext import db


class User(db.Model):
    user_id = db.Column(db.String(64), primary_key=True)
    user_name = db.Column(db.String(64), unique=True)
    user_email = db.Column(db.String(128))
    user_pass = db.Column(db.String(64))
    create_time = db.Column(db.DateTime)

    def __init__(self, user_name, user_pass, user_email=''):
        self.user_id = str(uuid.uuid4())
        self.user_name = user_name
        self.user_pass = user_pass
        self.user_email = user_email
        self.create_time = datetime.now()
        db.session.add(self)
        db.session.commit()
