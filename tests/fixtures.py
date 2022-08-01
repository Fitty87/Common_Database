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