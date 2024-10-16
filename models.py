from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    subscriptions = db.relationship('Subscription', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")
    
    @password.setter
    def password(self, password):
        self._password_hash = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "subscriptions": [subscription.to_dict() for subscription in self.subscriptions]
        }

class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    billing_cycle = db.Column(db.String(20), nullable=False)
    date_of_payment = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        category_list=["streaming","music","software","shopping","gaming","education","cloud storage"]

        if value not in category_list:
            raise ValueError(f"Category must be one of {category_list}")
        self._category=value



    @property
    def billing_cycle(self):
        return self._billing_cycle
    
    @billing_cycle.setter
    def billing_cycle(self,value):
        billing_cycle_list=["Weekly","Monthly","Yearly"]

        if value not in billing_cycle_list:
            raise ValueError(f"Category must be one of {billing_cycle_list}")
        self._billing_cycle=value

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'cost': self.cost,
            'billing_cycle': self.billing_cycle,
            'date_of_payment': self.date_of_payment.isoformat(),
        }

# Helper function for email validation
import re

def is_valid_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)
