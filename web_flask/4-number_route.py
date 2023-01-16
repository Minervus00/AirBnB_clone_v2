#!/usr/bin/python3
"""Sctript that starts a Flask Web apllication"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns the string to display on root"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Returns the string to display on that root"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_smthg(text):
    """Returns the string to display /c subpaths"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is_fun"):
    """Returns the string to display /python subpaths"""
    return 'python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """Returns the string to display /number subpaths"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
