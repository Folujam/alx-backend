#!/usr/bin/env python3
"""a flask app Module"""
from flask import Flask, render_template


# Create a Flask app instance
app = Flask(__name__)
# Define a route for the root URL ("/")


@app.route("/")
def index() -> str:
    """this renders templates/0-index.html"""
    return render_template("0-index.html")


if __name__ == "__main__":
    """main lane runner"""
    app.run(host="0.0.0.0", port=5000, debug=True)
