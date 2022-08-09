import pytest
from models import *
from werkzeug.security import generate_password_hash

#Fixtures-----
@pytest.fixture(scope='class')
def user_instance():
    user = User()
    user.email = "fuchs@example.at"
    user.password_hash =  generate_password_hash("password123")
    
    return user

@pytest.fixture(scope='class')
def user_instance2():
    user = User()
    user.email = "hase@example.at"
    user.password_hash =  generate_password_hash("password456")
    
    return user

@pytest.fixture(scope='class')
def source_of_data_instance():
    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")
    return source_of_data

@pytest.fixture(scope='class')
def source_of_data_instance2():
    source_of_data = Source_of_data("Oe24+", "2022-05-30 20:20:00")
    return source_of_data

@pytest.fixture(scope='class')
def address_instance(source_of_data_instance):
    address = Address(source_of_data_instance.id, "Seeweg", "4a", 1160, "Wien", "2022-05-30 20:20:00")
    return address

@pytest.fixture(scope='class')
def customer_instance(source_of_data_instance, address_instance):
    addresses = [address_instance]
    customer = Customer(source_of_data_instance.id, "Franz", "1970-05-03", "+123", "office@franz.at", "2022-05-30 20:20:00", addresses)
    return customer

@pytest.fixture(scope='class')
def invoice_instance1(source_of_data_instance, customer_instance):
    invoice = Invoice(source_of_data_instance.id, customer_instance.id, "2021-11-30", "1234564", "Anzeige", 1500.02,  "2022-05-30 20:20:00")
    return invoice