from flask import Flask, make_response, jsonify, render_template
from instance.config import app_config
from db.createdb import init_db

from flask import current_app


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.app_context().push()
    init_db(app.config['DATABASE_URI'])

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
