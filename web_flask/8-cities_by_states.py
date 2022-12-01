#!/usr/bin/python3
"""Task4 module"""

from flask import Flask, render_template
from models import storage
from os import getenv


app = Flask(__name__)


@app.teardown_appcontext
def teardown(q):
    """"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def Hello_HBNB():
    """"""
    return render_template("8-cities_by_states.html",
                           stt=storage.all("State").values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
