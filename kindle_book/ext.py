from celery import Celery
from flask_sqlalchemy import SQLAlchemy

from config import get_config_obj

db = SQLAlchemy()
celery = Celery(
    __name__,
    include=[
        "kindle_book.spider"
    ],
    broker=get_config_obj().CELERY_BROKER_URL
)
celery.config_from_object(get_config_obj(), force=True)
