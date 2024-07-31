#!/usr/bin/env python3
"""a flask app Module"""
from flask import Flask, render_template, request
from flask_babel import Babel, localeselector, get_local


# Create a Flask app instance
app = Flask(__name__)


# Create config class definition with attributes
class Config:
    """config class that inits ffg attribs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
# set the config class as the app's configuration


app.config.from_object(Config)
# Instantiate babel obj
babel = Babel(app)


# create get_locale with @babel.localeselector
@app.localeselector
def get_locale() -> str:
    """gets the accepted language"""
    accepted_locale_language = request.accept_languages.values()

    # Find best match lang
    best_match = None
    for lang in accepted_locale_language:
        if lang[:2] in Config.LANGUAGES:
            best_match = lang[:2]
            break
    return best_match if not None else "en"


# Define a route for the root URL ("/")
@app.route("/")
def index() -> str:
    """this renders templates/2-index.html"""
    return render_template("2-index.html")


if __name__ == "__main__":
    """main lane runner"""
    app.run(host="0.0.0.0", port=5000, debug=True)
