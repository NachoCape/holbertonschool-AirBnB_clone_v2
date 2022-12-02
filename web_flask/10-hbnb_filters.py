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


@app.route("/hbnb_filters", strict_slashes=False)
def states_HBNB():
    """"""
    return render_template("10-hbnb_filters.html",
                           state=storage.all("State").values(),
                           city=storage.all("City").values(),
                           amenity=storage.all("Amenity").values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
