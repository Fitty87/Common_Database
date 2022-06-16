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

#Fixtures-----
@pytest.fixture(scope='module')
def source_of_data_instance():
    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")
    return source_of_data

@pytest.fixture(scope='module')
def address_instance(source_of_data_instance):
    address = Address(source_of_data_instance.id, "Seeweg", 4, 1160, "Wien", "2022-05-30 20:20:00")
    return address

@pytest.fixture(scope='module')
def customer_instance(source_of_data_instance):
    customer = Customer(source_of_data_instance.id, "Franz", "1970-05-03", "+4369911314976", "office@franz.at", "2022-05-30 20:20:00")
    return customer

@pytest.fixture(scope='module')
def invoice_instance1(source_of_data_instance, customer_instance):
    invoice = Invoice(source_of_data_instance.id, customer_instance.id, "2021-11-30", 123456, "Anzeige", 1500,  "2022-05-30 20:20:00")
    return invoice

@pytest.fixture(scope='module')
def invoice_instance2(source_of_data_instance, customer_instance):
    invoice = Invoice(source_of_data_instance.id, customer_instance.id, "2021-11-30", 7891, "Abo", 500,  "2022-05-30 20:20:00")
    return invoice


#Create_new_record-----
@pytest.mark.create_new_record
def test_new_Source_of_Data(source_of_data_instance):
    """
    GIVEN a Source of Data Model
    WHEN a new Source of Data is created
    THEN Check if name is correct,
                if a name of at least 3 characters is entered,
                if the date_added is correct
    """
    count_chars_name = len(source_of_data_instance.name)

    assert source_of_data_instance.name == "Radio"
    assert count_chars_name >= 3
    assert source_of_data_instance.date_added == "2022-05-30 20:20:00"


@pytest.mark.create_new_record
def test_new_address(source_of_data_instance, address_instance):
    """
    GIVEN a Address Model and a datasource record
    WHEN a new Address is created
    THEN Check if the id of the datasource is save correctly,
               if a street of at least 3 characters is entered
               if a street don't contain any numbers
               if a street number starts with a number (for example 24a is a correct street number)
               if a postcode is > 0
               if a location of at least 3 characters is entered
               if a location don't contain any numbers
    """

    count_chars_street = len(address_instance.street)
    count_numbers_street = len(re.sub("[^0-9]", "", address_instance.street))
    first_char_street_number = str(address_instance.street_number)[0].isnumeric()
    count_chars_location = len(address_instance.location)
    count_numbers_location = len(re.sub("[^0-9]", "", address_instance.location))

    assert address_instance.source_of_data_id == source_of_data_instance.id
    assert address_instance.street == "Seeweg"
    assert count_chars_street >= 3
    assert count_numbers_street == 0
    assert address_instance.street_number == 4
    assert first_char_street_number == 1
    assert address_instance.postcode > 0 
    assert address_instance.postcode == 1160
    assert address_instance.location == "Wien"
    assert count_chars_location >= 3
    assert count_numbers_location == 0
    assert address_instance.date_added == "2022-05-30 20:20:00"


#email valid verbessern
@pytest.mark.create_new_record
def test_new_customer(source_of_data_instance, customer_instance):
    """
    GIVEN a Customer Model and a datasource record
    WHEN a new Customer is created
    THEN Check if the id of the datasource is save correctly,
            if a name of at least 3 characters is entered
            if a name don't contain any numbers
            if the format for the date_of_birth is correct
            if the telephone number do not exceed the maximum of 15 numbers (incl. Countrycode) and has a valid format
    """
   
    count_chars_name = len(customer_instance.name)
    count_numbers_name = len(re.sub("[^0-9]", "", customer_instance.name))    
    #Mit welchem Datumsformat wollen wir arbeiten???
    valid_date = bool(re.findall(r'\d{4}-\d{2}-\d{2}', customer_instance.date_of_birth))
    #Feld Telefon zu Handy ändern?
    #Hier noch anpassen 1 Stele weniger wenn +!
    valid_telephone_number = bool(re.match("^\\+|[0]{2}[1-9][0-9]{7,14}$", customer_instance.telephone_number))

    valid_email = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", customer_instance.email))

    assert customer_instance.source_of_data_id == source_of_data_instance.id
    assert customer_instance.name == "Franz"
    assert count_chars_name >= 3
    assert count_numbers_name == 0
    assert customer_instance.date_of_birth == "1970-05-03"
    assert valid_date == True
    assert customer_instance.telephone_number == "+4369911314976"
    assert valid_telephone_number == True
    assert customer_instance.email == "office@franz.at"
    assert valid_email == True
    assert customer_instance.date_added == "2022-05-30 20:20:00"

@pytest.mark.create_new_record
def test_new_invoice(source_of_data_instance, customer_instance, invoice_instance1):
    """
    GIVEN a Invoice Model, a datasource record and a customer record
    WHEN a new Invoice is created
    THEN Check if the id of the datasource, id of customer, date, number, service, amount and created_at is correct 
    """
    assert invoice_instance1.source_of_data_id == source_of_data_instance.id
    assert invoice_instance1.customer_id == customer_instance.id
    assert invoice_instance1.date == "2021-11-30"
    assert invoice_instance1.number == 123456
    assert invoice_instance1.service == "Anzeige"
    assert invoice_instance1.amount == 1500
    assert invoice_instance1.created_at == "2022-05-30 20:20:00"

#Relationship-----
@pytest.mark.relationship
def test_relationship_customer_and_invoice(customer_instance, invoice_instance1, invoice_instance2):
    """
    GIVEN one address and two source_of_data
    WHEN a address gets two source_of_data
    THEN Check if the adress returns these two source_of_data  
    """
    customer_instance.invoices.append(invoice_instance1)
    customer_instance.invoices.append(invoice_instance2)

    assert customer_instance.invoices[0].number == 123456
    assert customer_instance.invoices[1].number == 7891