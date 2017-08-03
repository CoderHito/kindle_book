FROM python:2.7

RUN mkdir /kindle_book
COPY . /kindle_book
WORKDIR /kindle_book

RUN pip install -r requests.txt
CMD python app_runner.py

EXPOSE 5000