# src/app/app.py

import os


class Config:
    """
    Configuration class for the application.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_super_secret_key'


def create_app():
    """
    Creates and configures the Flask application instance.
    """
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def hello_world():
        """
        Root endpoint that returns a greeting.
        """
        return 'Hello, World!'

    return app
