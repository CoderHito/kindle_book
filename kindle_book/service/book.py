from datetime import datetime

import requests
from bs4 import BeautifulSoup

from kindle_book.model.book import Book


def get_book():
    print "start"
    celerylog = open("celery_log.txt", "a")
    logdata = "start at ----" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    celerylog.write(logdata)
    celerylog.close()
    url = "http://t.bookdna.cn/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    result_set = soup.find_all('div', style="margin-bottom: 0.9em;")
    for tag in result_set:
        a = tag.a
        link = a["href"].encode("utf-8")
        title = a["title"].encode("utf-8")
        price_now = tag.find('span', style="color:#FF7237").text.encode("utf-8")
        div = tag.div
        author_info = div.text.encode("utf-8")
        book_to_db(link, title, price_now, author_info)
        # print (price_now)


def book_to_db(link, title, price_now, author_info):
    book = Book.query.filter_by(book_title=title).first()
    if not book:
        Book(title, author_info, link, price_now)


if __name__ == "__main__":
    from app_runner import app

    with app.app_context() as app:
        get_book()
