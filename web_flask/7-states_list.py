#!/usr/bin/python3
"""A script that starts a Flask web application. """

from flask import Flask, request, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

# creates an instance of the Flask class and assigns it to the variable app
app = Flask(__name__)

# Teardown app context to remove the
# current SQLAlchemy session after each request
@app.teardown_appcontext
def teardown(exception):
   """Remove the current SQLAlchemy session."""
   storage.close()


# Define the route for '/states_list'
@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.

     States are sorted by name.
     """
     #Fetch all State objects from the DBStorage and sort them by name (A->Z)
     states = sorted(storage.all(State).values(), key=lambda s: s.name)

      # Render te template and pass the list of states to the template
      return render_template("7-states_list.html", states=states)

if __name__ == "__main__":
    # Start the Flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host="0.0.0.0", port=5000)



# Define the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


# Define the route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB'."""
    return "HBNB"


# Define the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Displays 'C' followed by the value of <text>.
    
    Replaces any underscores in <text> with slashes.
    """
    # Replaces any underscores with spaces in the text variable
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)

# Define the route for '/python/(<text>)'
@app.route('/python/', defaults={'text', 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Displays 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    # Replace underscores with spaces in the text variable
    formatted_text = text.replace('_', ' ')
    return "Python {}".format(formatted_text)


# Define the route for '/number_odd_or_even/<n>'
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
""" Displays an HTML page only if <n> is an integer
    States whether <n> is odd or even in the body.
    """
    # Check if n is an integer
    if isinstance(n, int):
        # Determine if n is even or odd
        even_or_odd = "even" if n % 2 == 0 else "odd"
        # Render the template and pass the
        #  value of n and even_or_odd to the template
        return render_template('6-number_odd_or_even.html',
                               n=n, even_or_odd=even_or_odd)
    else:
        # If n is not an integer, return an error message
        return "Invalid input. Please provide an integer."


# Define the route for '/number/<n>'
@app.route('/number/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays an HTML page only if <n> is an integer."""
    return "{} is a number".format(n)


# Define the route for '/number_template/<n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays an HTML page only if <n> is an integer."""
    # Then render the template and pass the value of n to the template
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    # Start the Flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
