#!/usr/bin/python3
<<<<<<< HEAD
""" Starts a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
=======
"""Starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> d577dd864bf9e4e11ea89e2298dde622ae347831
