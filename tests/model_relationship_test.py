import os, sys
sys.path.insert(0,'tests')
from fixtures import *

#class Test_Relationship_UserAccess_Records:
   
   #Das geht iwie nicht ... später machen
   #def test_relationship_user(self, useraccess_instance, user_instance):
      #"""
      #GIVEN one UserAccess instance and one User instance
      #WHEN a new UserAccess was created
      #THEN Check if the UserAccess returns these User
      #"""
     # ua = useraccess_instance

      #print(str((ua.users[0].email)))

      #u = user_instance
      #users.append(u)

      #assert ua.users[0].email == "fuchs@example.at"

      #print(str(useraccess_instance.users[0]))

class Test_Relationship_Source_of_data_Records:
   
   def test_relationship_customer(self, source_of_data_instance, customer_instance):
      """
      GIVEN one Source of Data instance and one Customer instance
      WHEN a new Customer was created
      THEN Check if the Source of Data returns that Customer
      """

      sod = source_of_data_instance
      sod.customers.append(customer_instance)

      assert sod.customers[0].name == "Franz"
      assert sod.customers[0].date_of_birth == "1970-05-03"
      assert sod.customers[0].telephone_number == "+123"
      assert sod.customers[0].email == "office@franz.at"

   def test_relationship_invoice(self, source_of_data_instance, invoice_instance1):
      """
      GIVEN one Source of Data instance and one Invoice instance
      WHEN a new Invoice was created
      THEN Check if the Source of Data returns that Invoice
      """

      sod = source_of_data_instance
      sod.invoices.append(invoice_instance1)

      assert sod.invoices[0].date == "2021-11-30"
      assert sod.invoices[0].number == "1234564"
      assert sod.invoices[0].service == "Anzeige"
      assert sod.invoices[0].amount == 1500.02

   def test_relationship_address(self, source_of_data_instance, address_instance):
      """
      GIVEN one Source of Data instance and one Address instance
      WHEN a new Address was created
      THEN Check if the Source of Data returns that Address
      """

      sod = source_of_data_instance
      sod.addresses.append(address_instance)

      assert sod.addresses[0].street == "Seeweg"
      assert sod.addresses[0].street_number == "4a"
      assert sod.addresses[0].postcode == 1160
      assert sod.addresses[0].location == "Wien"
  
class Test_Relationship_Customer_Records:
   
   def test_relationship_invoice(self, customer_instance, invoice_instance1):
      """
      GIVEN one Customer instance and one Invoice instance
      WHEN a new Invoice was created
      THEN Check if the Customer returns that Invoice
      """

      cust = customer_instance
      cust.invoices.append(invoice_instance1)

      assert cust.invoices[0].date == "2021-11-30"
      assert cust.invoices[0].number == "1234564"
      assert cust.invoices[0].service == "Anzeige"
      assert cust.invoices[0].amount == 1500.02


   def test_relationship_address(self, customer_instance, address_instance):
      """
      GIVEN one Customer instance and one Address instance
      WHEN a new Address was created
      THEN Check if the Customer returns that Address
      """

      cust = customer_instance
      cust.addresses.append(address_instance)

      assert cust.addresses[0].street == "Seeweg"
      assert cust.addresses[0].street_number == "4a"
      assert cust.addresses[0].postcode == 1160
      assert cust.addresses[0].location == "Wien"