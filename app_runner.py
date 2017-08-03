import os

from kindle_book import create_app, db

RUNTIME = os.getenv("RUNTIME", "DEFAULT")
app = create_app(RUNTIME)


def make_celery(app):
    from kindle_book.ext import celery
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


def init_db():
    print ("____initdatabase____")
    try:
        with app.app_context(), app.test_request_context():
            from kindle_book.model.user import User
            from kindle_book.model.book import Book

            db.create_all()
        print ("____initdatabase finish____")
    except Exception as e:
        print e


init_db()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000')
