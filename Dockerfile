FROM python:2.7

RUN mkdir /kindle_book
COPY . /kindle_book
WORKDIR /kindle_book

RUN pip install -r requests.txt
CMD python app_runner.py
CMD celery -A kindle_book.spider beat -s celerybeat-schedule
CMD celery -A kindle_book.spider worker --loglevel=info

EXPOSE 5000
