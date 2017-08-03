from flask import Blueprint

view_blueprint = Blueprint("/", __name__, template_folder="templates", url_prefix='/')


@view_blueprint.route("/")
def index():
    return "index"