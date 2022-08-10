from datetime import datetime
import os, sys
sys.path.insert(0,'tests')
from fixtures import *


class Test_Create_New_User_Records:
    
    def test_correct_content(self, user_instance):
        """
        GIVEN a User instance
        WHEN this user instance was created
        THEN Check if the user has the right email-address and
                               the right password
        """
        user = user_instance

        assert user.email == "fuchs@example.at"
        assert check_password_hash(user.password_hash, "password123")


    def test_correct_datatypes(self, user_instance):
        """
        GIVEN a User instance
        WHEN this user instance was created
        THEN Check if the users email-address is a String with less than 50 chars
                                which is not empty.
                   if the users hashed password is a String with less than 128 chars   
                                
        """
        user = user_instance

        assert type(user.email) == str #check automatic that email is not 'None'
        assert len(user.email) <= 50
        assert user.email.count(" ") < len(user.email) #check that email is not an empty string

        assert type(user.password_hash) == str
        assert len(user.password_hash) <= 128


    def test_unique_email(self, user_instance, user_instance2):
        """
        GIVEN one existing user instance
        WHEN a second user instance was created
        THEN check that is not possible that both user have the same email address
        """
        user1 = user_instance
        user2 = user_instance2

        assert user1.email != user2.email
        
    
    def test_password_access(self, user_instance):
        """
        GIVEN a User instance
        WHEN this user instance was created
        THEN check that the password is not readable
        """

        with pytest.raises(Exception):
            pw = user_instance.password
   
class Test_Create_New_Source_Of_Data_Records:
    
    def test_correct_content(self, source_of_data_instance):
        """
        GIVEN a Source of data instance
        WHEN this Source of data instance was created
        THEN Check if the Source of data has the right name and
                               the right 'created_at' time
        """

        sod = source_of_data_instance

        assert sod.name == "Radio"
        assert sod.created_at == "2022-05-30 20:20:00"

    def test_correct_datatypes(self, source_of_data_instance):
        """
        GIVEN a Source of data instance
        WHEN this Source of data instance was created
        THEN Check if the Source of data name is a String with less than 50 chars
                                which is not empty.
                   if the Source of data 'created_at' is a String with the right format
                                
        """
        sod = source_of_data_instance

        assert type(sod.name) == str #check automatic that name is not 'None'
        assert len(sod.name) <= 50
        assert sod.name.count(" ") < len(sod.name) #check that name is not an empty string

        assert type(sod.created_at) == str
        assert datetime.strptime(sod.created_at, "%Y-%m-%d %H:%M:%S")
        
        
    def test_unique_name(self, source_of_data_instance, source_of_data_instance2):
        """
        GIVEN one existing Source of data instance
        WHEN a second Source of data instance was created
        THEN check that is not possible that both Source of data have the same name
        """
        sod1 = source_of_data_instance
        sod2 = source_of_data_instance2

        assert sod1.name != sod2.name

class Test_Create_New_Address_Records:
    
    def test_correct_content(self, address_instance):
        """
        GIVEN a Address instance
        WHEN this Address instance was created
        THEN Check if the Address has the right street and
                               the right street_number and
                               the right postcode and
                               the right location and
                               the right 'created_at' time
        """

        addr = address_instance

        assert addr.street == "Seeweg"
        assert addr.street_number == "4a"
        assert addr.postcode == 1160
        assert addr.location == "Wien"
        assert addr.created_at == "2022-05-30 20:20:00"

        
    def test_correct_datatypes(self, address_instance):
        """
        GIVEN a Address instance
        WHEN this Address instance was created
        THEN Check if the Address street is a String with less than 50 chars
                                which is not empty.
                   if the Address street_number is a String with less than 15 chars
                                which is not empty.
                   if the Address postcode is an integer.
                   if the Address location is a String with less than 30 chars
                                which is not empty.
                   if the Address 'created_at' is a String with the right format.
                                
        """
        addr = address_instance

        assert type(addr.street) == str #check automatic that street is not 'None'
        assert len(addr.street) <= 50
        assert addr.street.count(" ") < len(addr.street) #check that street is not an empty string

        assert type(addr.street_number) == str #check automatic that street_number is not 'None'
        assert len(addr.street_number) <= 15
        assert addr.street_number.count(" ") < len(addr.street_number) #check that street_number is not an empty string

        assert type(addr.postcode) == int

        assert type(addr.location) == str #check automatic that location is not 'None'
        assert len(addr.location) <= 30
        assert addr.location.count(" ") < len(addr.location) #check that location is not an empty string

        assert type(addr.created_at) == str
        assert datetime.strptime(addr.created_at, "%Y-%m-%d %H:%M:%S")

class Test_Create_New_Customer_Records:
    
    def test_correct_content(self, customer_instance):
        """
        GIVEN a Customer instance
        WHEN this Customer instance was created
        THEN Check if the Customer has the right name and
                               the right date_of_birth and
                               the right telephone_number and
                               the right email and
                               the right 'created_at' time
        """

        cust = customer_instance

        assert cust.name == "Franz"
        assert cust.date_of_birth == "1970-05-03"
        assert cust.telephone_number == "+123"
        assert cust.email == "office@franz.at"
        assert cust.created_at == "2022-05-30 20:20:00"

    
    def test_correct_datatypes(self, customer_instance):
        """
        GIVEN a Customer instance
        WHEN this Customer instance was created
        THEN Check if the Customer name is a String with less than 50 chars
                                which is not empty.
                   if the Customer date_of_birth is from type String.
                   if the Customer telephone_number is a String with less than 50 chars
                                which is not empty.
                   if the Customer email is a String with less than 50 chars
                                which is not empty.
                   if the Customer 'created_at' is a String with the right format.
                                
        """
        cust = customer_instance

        assert type(cust.name) == str #check automatic that name is not 'None'
        assert len(cust.name) <= 50
        assert cust.name.count(" ") < len(cust.name) #check that name is not an empty string

        assert type(cust.date_of_birth) == str

        assert type(cust.telephone_number) == str #check automatic that telephone_number is not 'None'
        assert len(cust.telephone_number) <= 50
        assert cust.telephone_number.count(" ") < len(cust.telephone_number) #check that telephone_number is not an empty string
        
        assert type(cust.email) == str #check automatic that email is not 'None'
        assert len(cust.email) <= 50
        assert cust.email.count(" ") < len(cust.email) #check that email is not an empty string
       
        assert type(cust.created_at) == str
        assert datetime.strptime(cust.created_at, "%Y-%m-%d %H:%M:%S")

class Test_Create_New_Invoice_Records:
    
    def test_correct_content(self, invoice_instance1):
        """
        GIVEN a Invoice instance
        WHEN this Invoice instance was created
        THEN Check if the Invoice has the right date and
                               the right number and
                               the right service and
                               the right amount and
                               the right 'created_at' time
        """

        inv = invoice_instance1

        assert inv.date == "2021-11-30"
        assert inv.number == "1234564"
        assert inv.service == "Anzeige"
        assert inv.amount == 1500.02
        assert inv.created_at == "2022-05-30 20:20:00"


    def test_correct_datatypes(self, invoice_instance1):
        """
        GIVEN a Invoice instance
        WHEN this Invoice instance was created
        THEN Check if the Invoice date is a String and 
                   if the Invoice number is a String with less than 30 chars
                                which is not empty.
                   if the Invoice Service is a String with less than 50 chars
                                which is not empty.
                   if the Invoice Amount is a Numeric Type with max 10 digits left and 2 digits right from the decimal-point
                   if the Invoice 'created_at' is a String with the right format.
                                
        """
        inv = invoice_instance1

        assert type(inv.date) == str

        assert type(inv.number) == str #check automatic that number is not 'None'
        assert len(inv.number) <= 30
        assert inv.number.count(" ") < len(inv.number) #check that number is not an empty string

        assert type(inv.service) == str #check automatic that service is not 'None'
        assert len(inv.service) <= 50
        assert inv.service.count(" ") < len(inv.service) #check that service is not an empty string
    
        assert type(inv.amount) == float
        assert str(inv.amount)[::-1].find(".") == 2 #count positions after decimal-point
        assert str(inv.amount)[::].find(".") <= 10

        assert type(inv.created_at) == str
        assert datetime.strptime(inv.created_at, "%Y-%m-%d %H:%M:%S")

class Test_Create_New_UserAccess_Records:
    
    def test_correct_content(self, useraccess_instance):
        """
        GIVEN a UserAccess instance
        WHEN this UserAccess instance was created
        THEN Check if the UserAccess has the right User_id and
                               the right Source_of_Data_id
        """

        ua = useraccess_instance

        assert ua.user_id == 1
        assert ua.source_of_data_id == 1

    
    def test_correct_datatypes(self, useraccess_instance):
        """
        GIVEN a UserAccess
        WHEN this UserAccess instance was created
        THEN Check if the UserAccess User_id is a Integer and 
                   if the UserAccess Source_of_Data_id is a Integer                         
        """

        ua = useraccess_instance

        assert type(ua.user_id) == int
        assert type(ua.source_of_data_id) == int



