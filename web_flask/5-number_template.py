#!/usr/bin/python3
"""Task4 module"""

from flask import Flask, render_template


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
    """starts a Flask web application and display 'C' + '<text>'"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_HBNB(text="is cool"):
    """starts a Flask web application and display 'python' + '<text>'"""
    return "python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number_HBNB(n):
    """starts a Flask web application and display 'n is a number'"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_HBNB(n):
    """starts a Flask web application and display a HTML page"""
    return render_template("5-number.html", name=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
