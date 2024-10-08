#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config for Flask app  to determine the best match"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Returns best match of supported language"""

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def first_method():
    """To provide the correct display for each message"""

    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
