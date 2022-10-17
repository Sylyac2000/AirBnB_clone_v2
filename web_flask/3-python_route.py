#!/usr/bin/python3
""" Starts Flask application """

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
