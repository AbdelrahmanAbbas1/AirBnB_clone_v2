#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_page(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def index_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    mod_num = 'odd'
    if n % 2 == 0:
        mod_num = 'even'
    return render_template('6-number_odd_or_even.html', n=n, t_num=mod_num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
