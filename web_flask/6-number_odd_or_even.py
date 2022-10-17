#!/usr/bin/python3
""" Starts Flask application """

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def func_c(text):
    """ a script that starts a Flask web application"""
    text = text.replace('_', ' ')
    return 'C {0}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def func_python(text="is cool"):
    """ Returns Python followed by the value of the text """
    text = text.replace('_', ' ')
    return 'Python {0}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Returns n is a number only if n is an integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """ Returns an HTML page only if n is an integer """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """ Returns an HTML page only if n is an integer """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
