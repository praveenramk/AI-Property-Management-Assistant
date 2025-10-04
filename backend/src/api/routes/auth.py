from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.user import User
from ..repositories.user_repository import UserRepository

auth_bp = Blueprint('auth', __name__)
user_repository = UserRepository()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    hashed_password = generate_password_hash(password)
    user = User(username=username, password=hashed_password)

    user_repository.add_user(user)
    return jsonify({'message': 'User registered successfully.'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = user_repository.get_user_by_username(username)
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful.'}), 200

    return jsonify({'message': 'Invalid username or password.'}), 401