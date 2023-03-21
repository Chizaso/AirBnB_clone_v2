#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
=======
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
>>>>>>> 8af10d6c5863092a75db2c1d90d6b6ba0501a1a5
"""
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/", strict_slashes=False)
def hello_hbnb():
=======
@app.route('/', strict_slashes=False)
def hello_route():
>>>>>>> 8af10d6c5863092a75db2c1d90d6b6ba0501a1a5
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
