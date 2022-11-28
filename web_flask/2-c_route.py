#!/usr/bin/python3
"""Task2 Module"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """starts a Flask web application and display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """starts a Flask web application and display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_HBNB(text):
    """starts a Flask web application and display "C" + "<text>" """
    return f"C {text}".replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
