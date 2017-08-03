from flask import Flask

from config import app_config,get_config_obj
from kindle_book.ext import db


def create_app(config_name):
    print config_name
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    from kindle_book.view.view_blueprint import view_blueprint
    app.register_blueprint(view_blueprint)

    return app
