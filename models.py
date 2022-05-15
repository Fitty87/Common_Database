from config import db
from datetime import datetime

#Create Model
customer_addresses = db.Table('customer_addresses', 
                db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
                db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True))

datasource_addresses = db.Table('datasource_addresses', 
db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
db.Column('datasource_id', db.Integer, db.ForeignKey('datasource.id'), primary_key=True))


class Datasource(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique=True)
    customer = db.relationship('Customer', backref='datasource')
    invoices = db.relationship('Invoice', backref='datasource')
    addresses = db.relationship('Address', backref='datasource')
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.name


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datasource_id = db.Column(db.Integer, db.ForeignKey('datasource.id'))
    street = db.Column(db.String(50), nullable = False)
    street_number = db.Column(db.String(15), nullable = False)
    postcode = db.Column(db.Integer, nullable = False)
    location = db.Column(db.String(30), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.street+' '+str(self.street_number)+', '+str(self.postcode)+' '+self.location


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datasource_id = db.Column(db.Integer, db.ForeignKey('datasource.id'))
    name = db.Column(db.String(50), nullable = False)
    date_of_birth = db.Column(db.Date, nullable = False)
    telephone_number = db.Column(db.Integer, nullable = False, unique=True)
    email = db.Column(db.String(50), nullable = False, unique=True)  
    invoices = db.relationship('Invoice', backref='customer')
    addresses = db.relationship('Address', secondary="customer_addresses", lazy='subquery', backref=db.backref('customer', lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.name


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datasource_id = db.Column(db.Integer, db.ForeignKey('datasource.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    date = db.Column(db.Date, nullable = False)
    number = db.Column(db.Integer, nullable = False, unique=True)
    service = db.Column(db.String(50), nullable = False)
    amount = db.Numeric(10,2)
    created_at = db.Column(db.DateTime, default=datetime.now)
   
    def __str__(self):
        return str(self.number)
