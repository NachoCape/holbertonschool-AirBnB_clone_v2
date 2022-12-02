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


@app.route("/states", strict_slashes=False)
def states_HBNB():
    """"""
    return render_template("7-states_list.html",
                           stt=storage.all("State").values())


@app.route("/states/<id>", strict_slashes=False)
def states_id_HBNB(id):
    """"""
    return render_template("9-states.html", id=id, flag=0,
                           stt=storage.all("State").values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
