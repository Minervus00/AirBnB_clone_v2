#!/usr/bin/python3
"""Sctript that starts a Flask Web apllication"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Returns a html page with all states objects"""
    return render_template(
        "7-states_list.html", states=storage.all("State").values())


@app.teardown_appcontext
def teardown(exc):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
