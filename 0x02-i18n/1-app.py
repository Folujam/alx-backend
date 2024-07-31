#!/usr/bin/env python3
"""a flask app Module"""
from flask import Flask, render_template
from flask_babel import Babel


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


# Define a route for the root URL ("/")
@app.route("/")
def index() -> str:
    """this renders templates/1-index.html"""
    return render_template("1-index.html")


if __name__ == "__main__":
    """main lane runner"""
    app.run(host="0.0.0.0", port=5000, debug=True)
