from flask import Flask
from .routes import register_routes
from .error_handlers import register_error_handlers


def create_app():
    app = Flask(__name__)

    register_routes(app)
    register_error_handlers(app)

    return app
