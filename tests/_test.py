import pytest
from config import app
from models import Source_of_data
from models import Address
from models import Customer
from models import Invoice
from routes import UserView
from flask import request
import re

from config import db

def test_new_Source_of_Data():
    """
    GIVEN a Source of Data Model
    WHEN a new Source of Data is created
    THEN Check if the name and date_added is correct
    """
    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")
    
    assert source_of_data.name == "Radio"
    assert source_of_data.date_added == "2022-05-30 20:20:00"
    return source_of_data


def test_new_address():
    """
    GIVEN a Address Model and a datasource record
    WHEN a new Address is created
    THEN Check if the id of the datasource, street, street_number, postcode,  location, date_added is correct
    """
    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")

    address = Address(source_of_data.id, "Seeweg", 4, 1160, "Wien", "2022-05-30 20:20:00")

    assert address.source_of_data_id == source_of_data.id
    assert address.street == "Seeweg"
    assert address.street_number == 4
    assert address.postcode == 1160
    assert address.location == "Wien"
    assert address.date_added == "2022-05-30 20:20:00"
    return address

#Wie teste ich n:m??
def test_new_customer():
    """
    GIVEN a Customer Model and a datasource record
    WHEN a new Customer is created
    THEN Check if the id of the datasource, name, date_of_birth, telephone_number, email, date_added is correct and if the email format is valid
    """

    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")

    customer = Customer(source_of_data.id, "Franz", "1970-05-03", "0699123456789", "office@franz.at", "2022-05-30 20:20:00")

    valid_email = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", customer.email))

    assert customer.source_of_data_id == source_of_data.id
    assert customer.name == "Franz"
    assert customer.date_of_birth == "1970-05-03"
    assert customer.telephone_number == "0699123456789"
    assert customer.email == "office@franz.at"
    assert valid_email == True
    assert customer.date_added == "2022-05-30 20:20:00"
    return customer

def test_new_invoice():
    """
    GIVEN a Invoice Model, a datasource record and a customer record
    WHEN a new Invoice is created
    THEN Check if the id of the datasource, id of customer, date, number, service, amount and created_at is correct 
    """

    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")
    customer = Customer(source_of_data.id, "Franz", "1970-05-03", "0699123456789", "office@franz.at", "2022-05-30 20:20:00")
     
    invoice = Invoice(source_of_data.id, customer.id, "2021-11-30", 123456, "Anzeige", 1500,  "2022-05-30 20:20:00")

    assert invoice.source_of_data_id == source_of_data.id
    assert invoice.customer_id == customer.id
    assert invoice.date == "2021-11-30"
    assert invoice.number == 123456
    assert invoice.service == "Anzeige"
    assert invoice.amount == 1500
    assert invoice.created_at == "2022-05-30 20:20:00"
    return invoice


def test_admin_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/')

        assert response.status_code == 200


def test_source_of_data_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/source_of_data/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/source_of_data/')

        assert response.status_code == 200


def test_address_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/address/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/address/')

        assert response.status_code == 200


def test_customer_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/customer/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/customer/')

        assert response.status_code == 200


def test_invoice_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/invoice/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/invoice/')

        assert response.status_code == 200