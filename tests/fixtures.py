import pytest
from models import *
from werkzeug.security import generate_password_hash

#Fixtures-----
@pytest.fixture(scope='class')
def user_instance():
    user = User()
    user.id = 1
    user.email = "fuchs@example.at"
    user.password_hash =  generate_password_hash("password123")
    user.created_at = "2022-05-30 20:20:00"
    
    return user

@pytest.fixture(scope='class')
def user_instance2():
    user = User()
    user.id = 2
    user.email = "hase@example.at"
    user.password_hash =  generate_password_hash("password456")
    user.created_at = "2022-05-30 20:20:00"
    
    return user

@pytest.fixture(scope='class')
def source_of_data_instance():
    source_of_data = Source_of_data()
    source_of_data.id = 1
    source_of_data.name = "Radio"
    source_of_data.created_at = "2022-05-30 20:20:00"

    return source_of_data

@pytest.fixture(scope='class')
def source_of_data_instance2():
    source_of_data = Source_of_data()
    source_of_data.id = 2
    source_of_data.name = "Oe24+"
    source_of_data.created_at = "2022-05-30 20:20:00"

    return source_of_data

@pytest.fixture(scope='class')
def address_instance(source_of_data_instance):
    address = Address()
    address.id = 1
    address.source_of_data_id = source_of_data_instance.id
    address.street = "Seeweg"
    address.street_number = "4a"
    address.postcode = 1160
    address.location = "Wien"
    address.created_at = "2022-05-30 20:20:00"

    return address

@pytest.fixture(scope='class')
def customer_instance(source_of_data_instance, address_instance):
    addresses = [address_instance]
    customer = Customer()
    
    customer.id = 1
    customer.source_of_data_id = source_of_data_instance.id
    customer.name = "Franz"
    customer.date_of_birth = "1970-05-03"
    customer.telephone_number = "+123"
    customer.email = "office@franz.at"
    customer.created_at = "2022-05-30 20:20:00"
    customer.addresses = addresses

    return customer

@pytest.fixture(scope='class')
def invoice_instance1(source_of_data_instance, customer_instance):
    invoice = Invoice()
    
    invoice.id = 1
    invoice.source_of_data_id = source_of_data_instance.id
    invoice.customer_id = source_of_data_instance.id
    invoice.date = "2021-11-30"
    invoice.number = "1234564"
    invoice.service = "Anzeige"
    invoice.amount = 1500.02
    invoice.created_at = "2022-05-30 20:20:00"

    return invoice

@pytest.fixture(scope='class')
def useraccess_instance(user_instance, source_of_data_instance):
    useraccess = UserAccess
    useraccess.user_id = user_instance.id
    useraccess.source_of_data_id = source_of_data_instance.id
    useraccess.created_at = "2022-05-30 20:20:00"

    return useraccess