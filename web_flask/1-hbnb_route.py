#!/usr/bin/python3
"""A script that starts a Flask web application.
1-hbnb_route.py
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB!."""
    return "HBNB"


if __name__ == "__main__":
	# Start the Flask development server
	# Listen on all available network interfaces (0.0.0.0) and port 5000
	app.run(host='0.0.0.0', port=5000)

