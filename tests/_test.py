import pytest
from config import app
from models import Source_of_data
from routes import UserView
from flask import request

from config import db

def test_new_Source_of_Data():
    """
    GIVEN a Source of Data Model
    WHEN a new Source of Data is created
    THEN Check if the name is correct
    """
    source_of_data = Source_of_data("Radio", "2022-05-30 20:20:00")
    
    assert(source_of_data.name == "Radio")
    assert(source_of_data.date_added == "2022-05-30 20:20:00")
    return source_of_data







     


