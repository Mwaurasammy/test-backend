from flask import jsonify, request, session, make_response
from models import db, User, Subscription
from flask_restful import Resource

class UserProfile(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        
        return user.to_dict(), 200
    
    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        
        data = request.get_json()

        # Update the name and email
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)

        # Update password only if provided and not empty
        password = data.get('password')
        if password:
            user.password = password  # This will trigger the password setter
            
        db.session.commit()
        return user.to_dict(), 200

    
class SubscriptionList(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        
        # Fetch the user's subscriptions
        subscriptions = Subscription.query.filter_by(user_id=user.id).all()
        return [sub.to_dict() for sub in subscriptions], 200

    def post(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        
        data = request.get_json()
        new_subscription = Subscription(
            name=data['name'],
            category=data['category'],
            cost=data['cost'],
            billing_cycle=data['billing_cycle'],
            date_of_payment=data['date_of_payment'],
            user_id=user.id
        )
        
        db.session.add(new_subscription)
        db.session.commit()
        
        return new_subscription.to_dict(), 201

class SubscriptionIndex(Resource):
    
    def delete(self, user_id, subscription_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        subscription = Subscription.query.filter_by(id=subscription_id, user_id=user_id).first()
        if not subscription:
            return {"error": "Subscription not found"}, 404
        db.session.delete(subscription)
        db.session.commit()

        return {"message": "Subscription deleted successfully"}, 200
