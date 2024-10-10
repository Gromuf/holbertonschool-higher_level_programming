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
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth : Access Granted"})


@app.route('/login', methods=['POST'])
@auth.login_required
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity={'username': username, "role": user['role']}
            )
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify({
        "message": "JWT Auth: Access Granted", "user": current_user
    }), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()

    if current_user['role'] != 'admin':
        return jsonify({
            "error": "Admin Access Required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5002)
