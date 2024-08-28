#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, g, request
import logging
from flask_babel import Babel
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config for Flask app  to determine the best match"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Returns best match of supported language"""

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Setting user and default time zone"""

    timezone = request.args.get('timezone')
    if timezone in app.config['LANGUAGES']:
        return timezone

    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """Find the user"""

    user_id = request.args.get("login_as")

    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """Get user before any request is made"""

    g.user = get_user()


@app.route("/")
def first_method():
    """To provide the correct the display for each message"""

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
