#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """Config for Flask app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns best match of supported language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def first_method():
    """html template"""

    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
