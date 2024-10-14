from flask import request, make_response, jsonify, session
from flask_restful import Resource
from models import db, User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Signup(Resource):
    def post(self):
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return make_response(jsonify({"message": "All fields are required"}), 400)

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return make_response(jsonify({"message": "User already exists"}), 409)

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create new user with hashed password
        new_user = User(name=name, email=email, _password_hash=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()

            # Return the newly created user details in the response
            return make_response(jsonify({"user": {"name": new_user.name, "email": new_user.email}}), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"message": "Failed to register user"}), 500)

class Checksession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return user.to_dict(), 200
        return make_response({"error": "no active session"}, 401)
        
class Login(Resource):
    def post(self):
        name = request.get_json().get('name')
        password = request.get_json().get('password')
        
        user = User.query.filter(User.name == name).first()
        if user and user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200
        else:
            return make_response({"error": "401 unauthorized"}, 401)
        
class Logout(Resource):
    def post(self):
        session.pop('user_id', None)
        return make_response({"message": "Successfully logged out."}, 200)
