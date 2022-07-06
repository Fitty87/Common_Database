import pytest
from config import app
from models import Source_of_data
from models import Address
from models import Customer
from models import Invoice
from models import User
from routes import UserView
from flask import request
import re
from config import db

#Fixtures-----
"""
@pytest.fixture(scope='class')
def user_instance():
    #user = User("s.wolf@oe24.at", "password123")
    user = User()
    user.email = "s.wolf@oe24.at"
    user.password = "password123"
    
    return user
"""

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
    address = Address(source_of_data_instance.id, "Seeweg", 4, 1160, "Wien", "2022-05-30 20:20:00")
    return address

@pytest.fixture(scope='class')
def address_instance2(source_of_data_instance):
    address = Address(source_of_data_instance.id, "Friedrichstraße", 10, 1010, "Wien", "2022-05-30 20:20:00")
    return address

@pytest.fixture(scope='class')
def customer_instance(source_of_data_instance):
    customer = Customer(source_of_data_instance.id, "Franz", "1970-05-03", "+123", "office@franz.at", "2022-05-30 20:20:00")
    return customer

@pytest.fixture(scope='class')
def invoice_instance1(source_of_data_instance, customer_instance):
    invoice = Invoice(source_of_data_instance.id, customer_instance.id, "2021-11-30", "1234564", "Anzeige", 1500,  "2022-05-30 20:20:00")
    return invoice

@pytest.fixture(scope='class')
def invoice_instance2(source_of_data_instance, customer_instance):
    invoice = Invoice(source_of_data_instance.id, customer_instance.id, "2021-11-30", "7891", "Abo", 500,  "2022-05-30 20:20:00")
    return invoice

#Fixtures Wrong Instances-----
@pytest.fixture(scope='class')
def wrong_source_of_data_instance_too_short():
    source_of_data = Source_of_data("Ra", "30.05.2022")
    return source_of_data

@pytest.fixture(scope='class')
def wrong_source_of_data_instance_too_long():
    source_of_data = Source_of_data("Raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "30.05.2022")
    return source_of_data

#Test_Classes-----
class Test_Create_New_Records:
    
    #Hier noch Test unterteilen in Stammdaten testen / Funktional Tests
    def test_new_user(self, user_instance):
        """
        GIVEN a User Model
        WHEN a new User is created
        THEN Check if email is valid,
                   if password do not exceed the max of chars
                   if password is not an empty String
        """
        
        valid_email = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", user_instance.email))
        count_passwordchars = len(user_instance.password)
        count_passwordchars_empties = user_instance.password.count(' ')

        assert valid_email == True
        assert count_passwordchars <= 20
        assert count_passwordchars_empties != len(user_instance.password)


    def test_new_Source_of_Data(self, source_of_data_instance, wrong_source_of_data_instance_too_short, wrong_source_of_data_instance_too_long):
        """
        GIVEN a Source of Data Model
        WHEN a new Source of Data is created
        THEN Check if name is correct,
                    if a name of at least 3 characters is entered,
                    if a name do not exceed the max lenght
                    if the date_added is correct
        """
        count_chars_name = len(source_of_data_instance.name)

        assert source_of_data_instance.name == "Radio"
        assert count_chars_name >= 3
        assert count_chars_name <= 50
        assert source_of_data_instance.date_added == "2022-05-30 20:20:00"

        count_chars_name_wrong_too_short = len(wrong_source_of_data_instance_too_short.name)
        count_chars_name_wrong_too_long = len(wrong_source_of_data_instance_too_long.name)

        assert not count_chars_name_wrong_too_short >= 3
        assert count_chars_name_wrong_too_short <= 50
        assert count_chars_name_wrong_too_long >= 3
        assert not count_chars_name_wrong_too_long <= 50



    def test_new_address(self, source_of_data_instance, address_instance):
        """
        GIVEN a Address Model and a datasource record
        WHEN a new Address is created
        THEN Check if the id of the datasource is save correctly,
                if a street of at least 3 characters is entered
                if a street do not exceed the max lenght
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
        assert count_chars_street <= 50
        assert count_numbers_street == 0
        assert address_instance.street_number == 4
        assert first_char_street_number == 1
        assert address_instance.postcode > 0 
        assert address_instance.postcode == 1160
        assert address_instance.location == "Wien"
        assert count_chars_location >= 3
        assert count_numbers_location == 0
        assert address_instance.date_added == "2022-05-30 20:20:00"


    def test_new_customer(self, source_of_data_instance, customer_instance):
        """
        GIVEN a Customer Model and a datasource record
        WHEN a new Customer is created
        THEN Check if the id of the datasource is save correctly,
                if a name of at least 3 characters is entered
                if a name do not exceed the max lenght
                if a name don't contain any numbers
                if the format for the date_of_birth is correct
                if the telephone number starts optional with a + and continue with numbers
        """
    
        count_chars_name = len(customer_instance.name)
        count_numbers_name = len(re.sub("[^0-9]", "", customer_instance.name))    
        valid_date = bool(re.findall(r'\d{4}-\d{2}-\d{2}', customer_instance.date_of_birth))
        valid_telephone_number = bool(re.match("^[+]?[0-9]*$", customer_instance.telephone_number))
        #Bessere Validation finden
        valid_email = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", customer_instance.email))

        assert customer_instance.source_of_data_id == source_of_data_instance.id
        assert customer_instance.name == "Franz"
        assert count_chars_name >= 3
        assert count_chars_name <= 50
        assert count_numbers_name == 0
        assert customer_instance.date_of_birth == "1970-05-03"
        assert valid_date == True
        assert customer_instance.telephone_number == "+123"
        assert valid_telephone_number == True
        assert customer_instance.email == "office@franz.at"
        assert valid_email == True
        assert customer_instance.date_added == "2022-05-30 20:20:00"


    def test_new_invoice(self, source_of_data_instance, customer_instance, invoice_instance1):
        """
        GIVEN a Invoice Model, a datasource record and a customer record
        WHEN a new Invoice is created
        THEN Check if the id of the datasource is save correctly, 
                   if the id of the customer is save correctly,
                   if the format for the invoice_date is correct,
                   if a number of at least 3 characters is entered
                   if a number do not exceed the max lenght
                   if a service of at least 3 characters is entered
                   if a service do not exceed the max lenght
                   if a amount not equal 0 is entered                           
        """
        #Dont repeat yourself --> extra Class for dateCheck...string check..?
        valid_date = bool(re.findall(r'\d{4}-\d{2}-\d{2}', invoice_instance1.date))
        count_chars_number = len(invoice_instance1.number)
        count_chars_service = len(invoice_instance1.service)
        
        assert invoice_instance1.source_of_data_id == source_of_data_instance.id
        assert invoice_instance1.customer_id == customer_instance.id
        assert invoice_instance1.date == "2021-11-30"
        assert valid_date == True
        assert invoice_instance1.number == "1234564"
        assert count_chars_number >= 3
        assert count_chars_number <= 30
        assert count_chars_service >= 3
        assert count_chars_service <= 50
        assert invoice_instance1.service == "Anzeige"
        assert invoice_instance1.amount == 1500
        assert not invoice_instance1.amount == 0
        assert invoice_instance1.created_at == "2022-05-30 20:20:00"
  

class Test_Update_Records:
    
    def test_update_Source_of_Data(self, source_of_data_instance):
        """
        GIVEN a Source of Data Record
        WHEN a Source of Data is updated
        THEN Check if the changes will be correct
        """

        source_of_data_instance.name = "Other_Name"

        assert source_of_data_instance.name == "Other_Name"


    def test_update_Address(self, address_instance):
        """
        GIVEN a Address Record
        WHEN a Address is updated
        THEN Check if the changes will be correct
        """

        address_instance.street = "Other_Street"
        address_instance.street_number = "Other_Street_Number"
        address_instance.postcode = 1110
        address_instance.location = "Linz"

        assert address_instance.street == "Other_Street"
        assert address_instance.street_number == "Other_Street_Number"
        assert address_instance.postcode == 1110
        assert address_instance.location == "Linz"


    def test_update_customer(self, customer_instance, invoice_instance1, address_instance2):
        """
        GIVEN a Customer Record, a new invoice and another address
        WHEN a Customer is updated
        THEN Check if the changes will be correct
        """

        customer_instance.name = "Other_Name"
        customer_instance.telephone_number = 147258369
        customer_instance.email = "Other_email@gmx.net"
        customer_instance.invoices.append(invoice_instance1)

        customer_instance.addresses.append(address_instance2)

        customer_instance.addresses[0].street = "Other_Street"
        customer_instance.addresses[0].street_number = "Other_Street_Number"
        customer_instance.addresses[0].postcode = 1111
        customer_instance.addresses[0].location = "Belgrad"

        assert customer_instance.name == "Other_Name"
        assert customer_instance.telephone_number == 147258369
        assert customer_instance.email == "Other_email@gmx.net"
        assert customer_instance.invoices[0].number == invoice_instance1.number
        assert customer_instance.addresses[0].street == "Other_Street"
        assert customer_instance.addresses[0].street_number == "Other_Street_Number"
        assert customer_instance.addresses[0].postcode == 1111
        assert customer_instance.addresses[0].location == "Belgrad"


    def test_update_invoice(self, invoice_instance1):
        """
        GIVEN a invoice Record
        WHEN a invoice is updated
        THEN Check if the changes will be correct
        """

        invoice_instance1.date = "2021-11-30"
        invoice_instance1.number = 159487263
        invoice_instance1.service = "Other_Service"
        invoice_instance1.amount = 200

        assert invoice_instance1.date == "2021-11-30"
        assert invoice_instance1.number == 159487263
        assert invoice_instance1.service == "Other_Service"
        assert invoice_instance1.amount == 200


#Andere Beziehungen noch testen
class Test_Relationsships:
    
    def test_relationship_customer_and_invoice(self, customer_instance, invoice_instance1, invoice_instance2):
        """
        GIVEN one address and two source_of_data
        WHEN a address gets two source_of_data
        THEN Check if the adress returns these two source_of_data  
        """
        customer_instance.invoices.append(invoice_instance1)
        customer_instance.invoices.append(invoice_instance2)

        assert customer_instance.invoices[0].number == "1234564"
        assert customer_instance.invoices[1].number == "7891"


class Test_Unique_Records:
    
    def test_unique_source_of_data(self, source_of_data_instance, source_of_data_instance2):
        """
        GIVEN one source_of_data instance
        WHEN a second source_of_data will be created
        THEN Check if the second source_of_data is not equal the first source_of_data (depending on the name)
        """

        assert not source_of_data_instance.name == source_of_data_instance2.name
      

    def test_unique_invoice_number(self, invoice_instance1, invoice_instance2):
        """
        GIVEN one invoice instance
        WHEN a second invoice will be created
        THEN Check if the second invoice has not the same invoice_number
        """
        
        assert not invoice_instance1.number == invoice_instance2.number