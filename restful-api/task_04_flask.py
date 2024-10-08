#!/usr/bin/python3

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
    return "Welcome to the Flask API!"


@app.route("/data")
def username():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return ("OK")


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
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
