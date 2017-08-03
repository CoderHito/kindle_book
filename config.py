import os

from celery.schedules import crontab,timedelta


class Config(object):
    DEBUG = False
    TEST = False
    TRACER = os.getenv("TRACER", False)

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASS = os.getenv("DATABASE_PASS")
    DATABASE_URI = os.getenv("DATABASE_URI")
    DATABASE_PORT = 3306
    DATABASE_DB = os.getenv("DATABASE_DB", "kindle_book")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{USER}:{PASS}@{URI}:{PORT}/{DBNAME}?charset=utf8".format(
        USER=DATABASE_USER,
        PASS=DATABASE_PASS,
        URI=DATABASE_URI,
        PORT=DATABASE_PORT,
        DBNAME=DATABASE_DB,
    )
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    CELERY_TASK_SERIALIZER = "json"
    CELERY_TASK_RESULT_EXPIRES = 3600
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_RESULT_SERIALIZER = 'json'
    CELERYBEAT_SCHEDULE = {
        'get_info_every_hour': {
            'task': 'get_info_every_hour',
            # 'schedule': timedelta(seconds=3)
            'schedule': crontab(hour=1)
        },
    }
    CELERY_TIMEZONE = 'UTC'


# development
class DevelopmentConfig(Config):
    DEBUG = True
    TEST = True
    SECRET_KEY = "THIS_A_KEY"
    SQLALCHEMY_RECORD_QUERIES = True


# production
class ProductionConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY")
    TRACER = True


# testing
class TestingConfig(Config):
    TEST = True
    SECRET_KEY = "THIS_A_KEY"


app_config = {
    "DEVELOPMENT": DevelopmentConfig,
    "PRODUCTION": ProductionConfig,
    "TESTING": TestingConfig,
    "DEFAULT": TestingConfig,
}


def get_config_obj():
    return app_config[os.getenv("RUNTIME", "DEFAULT")]
