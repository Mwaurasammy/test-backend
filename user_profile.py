from flask import jsonify, request, session,abort, make_response
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

        # Get optional filters from query parameters
        name_filter = request.args.get('name')  # Filter by subscription name
        category_filter = request.args.get('category')  # Filter by subscription category
        start_date = request.args.get('start_date')  # Filter by start date
        end_date = request.args.get('end_date')  # Filter by end date

        # Base query to get subscriptions for the user
        query = Subscription.query.filter_by(user_id=user_id)

        # Apply filters if the parameters are provided
        if name_filter:
            query = query.filter(Subscription.name.ilike(f"%{name_filter}%"))  # Case-insensitive match
        if category_filter:
            query = query.filter_by(category=category_filter)  # Exact match on category
        if start_date and end_date:
            query = query.filter(Subscription.date_of_payment.between(start_date, end_date))  # Date range

        # Execute the query and return the results
        subscriptions = query.all()
        return [sub.to_dict() for sub in subscriptions], 200

    def post(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        
        # # def post(self):
        # if not session.get('user_id'):
        #     response_body={
        #         "error":"unauthorized"
        #     }
        #     return make_response(jsonify(response_body),401)
        data = request.get_json()
        name = data.get("name")
        category = data.get('category')
        cost = data.get('cost')
        billing_cycle = data.get('billing_cycle')
        date_of_payment = data.get('date_of_payment')
        

        # user_id=session.get("user_id")
        # if not user_id:
        #     return make_response(jsonify({"errors":"unauthorized"}),401)
        # # Validate input data
        if name is None or category is None or cost is None or billing_cycle is None or date_of_payment is None:
            return make_response({"errors": ["Validation errors: 'name', 'category','billing_cycle','date_of_payment' and 'cost' are required."]}, 400)

          
        try:

            new_subscription=Subscription(
                name=name,
                category=category,
                cost=cost,
                billing_cycle=billing_cycle,
                date_of_payment=date_of_payment,
                user_id=user_id

            )
            db.session.add(new_subscription)
            db.session.commit()

            new_subscription_data={
                "id":new_subscription.id,
                "name":new_subscription.name,
                "category":new_subscription.category,
                "cost":new_subscription.cost,
                "billing_cycle":new_subscription.billing_cycle,
                "date_of_payment":new_subscription.date_of_payment
            }

            response = make_response(new_subscription_data, 201)
            return response
        
        except Exception as e:
           
            db.session.rollback()
            return make_response({"errors": [str(e)]}, 500)
class DeleteSubscription(Resource):        
    def delete(self, user_id, subscription_id):
        # Retrieve the subscription by its ID
        subscription = Subscription.query.filter_by(id=subscription_id, user_id=user_id).first()

        if subscription is None:
            abort(404, description="Subscription not found.")

        # If the subscription is found, delete it
        db.session.delete(subscription)
        db.session.commit()

        return jsonify({"message": "Subscription deleted successfully."})
    
class Subscriptions(Resource):
    def get(self):
        # if not session.get('user_id'):
        #     response_body={
        #         "error":"unauthorized"
        #     }
        #     return make_response(jsonify(response_body),401)
        response_to_dict = [n.to_dict() for n in Subscription.query.all()]
        print(response_to_dict)
        return jsonify(response_to_dict)    