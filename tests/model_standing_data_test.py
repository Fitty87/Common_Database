import os, sys
sys.path.insert(0,'tests')
from fixtures import *

class Test_Create_New_Records:
    
    def test_create_user_with_correct_content(self, user_instance):
        """
        GIVEN a User instance
        WHEN a new user instance was created
        THEN Check if the user has the right email-address and
                               the right password
        """
        user = user_instance

        assert user.email == "fuchs@example.at"
        assert check_password_hash(user.password_hash, "password123")


    def test_create_user_with_correct_datatypes(self, user_instance):
        """
        GIVEN a User instance
        WHEN a new user instance was created
        THEN Check if the users email-address is a String with less than 50 chars
                                which is not empty.
                   if the users hashed password is a String with less than 128 chars   
                                
        """
        user = user_instance

        assert type(user.email) == str #check automatic that email is not None
        assert len(user.email) <= 50
        assert user.email.count(" ") < len(user.email)
        assert type(user.password_hash) == str
        assert len(user.password_hash) <= 128


    def test_create_user_with_unique_email(self, user_instance, user_instance2):
        """
        GIVEN one existing user instance
        WHEN a second user instance was created
        THEN check that is not possible that both user have the same email address
        """
        user1 = user_instance
        user2 = user_instance2

        assert user1.email != user2.email
        

   