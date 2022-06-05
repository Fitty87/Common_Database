import pytest
from config import app
from models import Source_of_data
from models import Address
from routes import UserView
from flask import request

from config import db

def test_new_Source_of_Data():
    """
    GIVEN a Source of Data Model
    WHEN a new Source of Data is created
    THEN Check if the name and date_added is correct
    """
    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")
    
    assert(source_of_data.name == "Radio")
    assert(source_of_data.date_added == "2022-05-30 20:20:00")
    return source_of_data

def test_new_address():
    """
    GIVEN a Address Model and a datasource record
    WHEN a new Address is created
    THEN Check if the id of the datasource, 
    """
    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")

    address = Address(source_of_data.id, "Seeweg", 4, 1160, "Wien", "2022-05-30 20:20:00")

    assert(address.source_of_data_id == source_of_data.id)
    assert(address.street == "Seeweg")
    assert(address.street_number == 4)
    assert(address.postcode == 1160)
    assert(address.location == "Wien")
    assert(address.date_added == "2022-05-30 20:20:00")
    return address







     


