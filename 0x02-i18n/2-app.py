#!/usr/bin/env python3
"""
Basic Flask app with Babel setup and locale selector
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """
    Configuration class for Flask-Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Select the best match language for the user
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Route for the index page
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
