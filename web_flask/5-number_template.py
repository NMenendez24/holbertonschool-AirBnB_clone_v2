#!/usr/bin/python3
"""Runs a simple flask app"""
from flask import Flask, Markup, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays a statement"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display a statement"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_print(text):
    """Display a statement"""
    return "C {}".format(Markup.escape(text.replace('_', ' ')))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_print(text='is cool'):
    """Returns a statement"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_print(n):
    """Returns a statement only if n is a integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
