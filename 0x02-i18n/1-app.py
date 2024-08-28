#!/usr/bin/env python
"""Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """Config for Flask app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)


@app.route("/")
def first_method():
    """html template"""

    render.template('1-index.html')


if __name__ == '__main__':
    app.run()
