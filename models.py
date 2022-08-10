from config import *
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin.contrib.sqla import ModelView
from flask_admin import expose

#Data-Tables
customer_addresses = db.Table('customer_addresses', 
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True))


#Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.now())

    @property
    def password(self):
        raise AttributeError('Password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __str__(self):
        return str(self.email)

#Prüfen Kombi aus beiden darf nur einmal vorkommen!
class UserAccess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    source_of_data_id = db.Column(db.Integer, db.ForeignKey('source_of_data.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())

    users = db.relationship('User', backref='useraccess', lazy=True, primaryjoin="User.id == UserAccess.user_id")
    source_of_datas = db.relationship('Source_of_data', backref='useraccess', lazy=True, primaryjoin="Source_of_data.id == UserAccess.source_of_data_id")
    

class Source_of_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    customers = db.relationship('Customer', backref='Source_of_data')
    invoices = db.relationship('Invoice', backref='Source_of_data')
    addresses = db.relationship('Address', backref='Source_of_data')


    def __str__(self):
        return str(self.name)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_of_data_id = db.Column(db.Integer, db.ForeignKey('source_of_data.id'))
    street = db.Column(db.String(50), nullable = False)
    street_number = db.Column(db.String(15), nullable = False)
    postcode = db.Column(db.Integer, nullable = False)
    location = db.Column(db.String(30), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return str(self.street + ' ' + str(self.street_number) + ', ' + str(self.postcode) + ' ' + self.location)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_of_data_id = db.Column(db.Integer, db.ForeignKey('source_of_data.id'))
    name = db.Column(db.String(50), nullable = False)
    date_of_birth = db.Column(db.Date, nullable = False)
    telephone_number = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)  
    created_at = db.Column(db.DateTime, default=datetime.now())

    invoices = db.relationship('Invoice', backref='customer')
    addresses = db.relationship('Address', secondary="customer_addresses", lazy='subquery', backref=db.backref('customer', lazy=True))


    def __str__(self):
        return str(self.name)


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_of_data_id = db.Column(db.Integer, db.ForeignKey('source_of_data.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    date = db.Column(db.Date, nullable = False)
    number = db.Column(db.String(30), nullable = False, unique=True)
    service = db.Column(db.String(50), nullable = False)
    amount = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return str(self.number)
