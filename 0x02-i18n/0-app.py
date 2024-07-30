#!/usr/bin/env python3
"""a flask app Module"""
from flask import Flask, render_template


# Create a Flask app instance
app = Flask(__name__)
# Define a route for the root URL ("/")
@app.route("/")
def index():
    """this renders templates/0-index.html"""
    return render_template("templates/0-index.html")

if __name__ == "__main__":
    """main lane runner"""
    app.run(debug=True)
