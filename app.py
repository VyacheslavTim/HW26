from flask import Flask
from flask_migrate import Migrate

from config import Config
from db import db
from views import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(main_bp)
    return app
