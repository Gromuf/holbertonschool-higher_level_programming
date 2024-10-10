#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "password": generate_password_hash("password1"),
        "role": "user"
        },
    "admin": {
        "password": generate_password_hash("adminpass"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
        users[username]['password'], password
    ):
        return username
    return None


@app.route('/')
def home():
    return jsonify({"message": "Hello, this is an open endpoint!"})


@app.route('/login', methods=['POST'])
@auth.login_required
def login():
    current_user = auth.current_user()

    access_token = create_access_token(identity={
        "username": current_user,
        "role": users[current_user]['role']
    })

    return jsonify(access_token=access_token), 200


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({
        "message": "Hello, {}!, you have access to this protected endpoint!"
        .format(current_user['username']),
        "role": current_user['role']
    })


@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_user = get_jwt_identity()

    if current_user['role'] != 'admin':
        return jsonify({
            "error": "Unauthorized access, admin privileges required"
            }), 403
    return jsonify({"message": "Hello Admin {}, welcome to the admin area!"
                    .format(current_user['username'])
                    })


if __name__ == '__main__':
    app.run(debug=True, port=5002)
