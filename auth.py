from flask import request, make_response, jsonify, session
from flask_restful import Resource
from flasgger import swag_from
from models import db, User
from flask_bcrypt import Bcrypt
from swagger_spec import sign_up_spec, login_spec, logout_spec, checksession_spec

bcrypt = Bcrypt()

class Signup(Resource):
    @swag_from(sign_up_spec)
    def post(self):
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return {"message": "All fields are required"}, 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"message": "User already exists"}, 409

        new_user = User(name=name, email=email)
        new_user.password = password
        db.session.add(new_user)
        db.session.commit()

        return {"user": {"name": new_user.name, "email": new_user.email}}, 201

class Login(Resource):
    @swag_from(login_spec)
    def post(self):
        data = request.get_json()
        name = data.get('name')
        password = data.get('password')

        if not name or not password:
            return {"error": "Missing name or password"}, 400

        user = User.query.filter(User.name == name).first()
        if user and user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200
        else:
            return {"error": "Unauthorized"}, 401

class Logout(Resource):
    @swag_from(logout_spec)
    def post(self):
        session.pop('user_id', None)
        return {"message": "Logged out successfully"}, 200

class Checksession(Resource):
    @swag_from(checksession_spec)
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.filter_by(id=user_id).first()
            if user:
                return jsonify(user.to_dict()), 200
        return {"error": "No active session"}, 401
