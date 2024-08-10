#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def page(text):
    mod_text = text.replace("_", " ")
    return f'C {mod_text}'


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def page_py(text):
    mod_text = text.replace("_", " ")
    return f'Python {mod_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
