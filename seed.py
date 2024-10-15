from faker import Faker
from models import db, Subscription,User
import random
from sqlalchemy.exc import SQLAlchemyError
from app import app
from werkzeug.security import generate_password_hash

fake = Faker()
if __name__ == '__main__':
    with app.app_context():

     Subscription.query.delete()
     User.query.delete()
     
     db.session.commit()
     

     users=[]
     for _ in range(5):
       user = User (
        name=fake.name(), 
        email=fake.email(),
        _password_hash=generate_password_hash(fake.password())

       )
       users.append(user)
       db.session.add_all(users)
       db.session.commit()

     subscriptions=[]

     for _ in range(5):
      subscription = Subscription( 
        name=fake.name(), 
        category=random.choice(["streaming","music","software","shopping","gaming","education","cloud storage"]),  
        cost=random.randint(1, 1000),       
        billing_cycle=random.choice(["Weekly","Monthly","Yearly"]),
        date_of_payment=fake.date_time_this_decade(),
        user_id=random.choice(User.query.all()).id

                                  )
      subscriptions.append(subscription)
      
      
      db.session.add_all(subscriptions)
      db.session.commit()

      