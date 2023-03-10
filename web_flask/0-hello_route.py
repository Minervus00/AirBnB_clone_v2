#!/usr/bin/python3
"""Sctript that starts a Flask Web apllication"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns the string to display on root"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
