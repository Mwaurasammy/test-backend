from flask import Flask, Request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, User
from flask_cors import CORS
from auth import Signup, Login, Logout, Checksession
from user_profile import SubscriptionList, UserProfile, SubscriptionIndex
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)
migrate = Migrate(app, db)
CORS(app, supports_credentials=True)

api = Api(app)

api.add_resource(Signup, '/sign_up')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Checksession, '/check_session')
api.add_resource(UserProfile, '/user/<int:user_id>')
api.add_resource(SubscriptionList, '/user/<int:user_id>/subscriptions')
api.add_resource(SubscriptionIndex, '/user/<int:user_id>/subscriptions/<int:subscription_id>')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # enable this to test locally but disable when you push to avoid hosting issues
        # app.run(debug=True) 