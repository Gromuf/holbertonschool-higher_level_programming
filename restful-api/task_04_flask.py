#!/usr/bin/python3
"""
A simple Flask API that manages user data.

This API allows you to:
- View a list of users
- Check the API status
- Retrieve details of a specific user
- Add new users via POST requests
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {

        "jane": {
            "username": "jane",
            "name": "Jane",
            "age": 28,
            "city": "Los Angeles"
        },
        "john": {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
    }


@app.route("/")
def home():
    """Returns a welcome message for the root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def username():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the status of the API."""
    return ("OK")


@app.route("/users/<username>")
def get_user(username):
    """Returns details of a specific user if they exist."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    """Handles adding a new user via POST request."""
    new_user = request.get_json()
    if (
        not new_user or 'username' not in new_user
        or 'name' not in new_user or 'age' not in new_user
        or 'city' not in new_user
    ):
        return jsonify({"error": "Invalid input"}), 400
    username = new_user['username']

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": new_user['name'],
        "age": new_user['age'],
        "city": new_user['city']
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
