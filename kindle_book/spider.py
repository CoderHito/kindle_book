from app_runner import celery
from kindle_book.service.book import get_book


@celery.task(name='get_book_info')
def get_book_info():
    get_book()
