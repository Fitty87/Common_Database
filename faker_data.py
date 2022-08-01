from config import db
from models import *
import random
import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask import flash

def Create_Random_Faker_data():
    fake = Faker("de_AT")
    fake_data_user = defaultdict(list)
    fake_data_source_of_data = defaultdict(list)
    fake_data_customer = defaultdict(list)
    fake_data_address = defaultdict(list)
    fake_data_invoice = defaultdict(list)


    #User---
    for _ in range(2):
        fake_data_user["email"].append(fake.email())
        fake_data_user["password_hash"].append(generate_password_hash("123"))

    dt_fake_data_user = pd.DataFrame(fake_data_user)

    dt_fake_data_user.to_sql('User', con='sqlite:///common_database.db', index=False, if_exists='append')

    #Source_of_data---
    for _ in range(4):
        fake_data_source_of_data["name"].append("sod_" + fake.color_name())
        fake_data_source_of_data["created_at"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    dt_fake_data_source_of_data = pd.DataFrame(fake_data_source_of_data)

    dt_fake_data_source_of_data.to_sql('Source_of_data', con='sqlite:///common_database.db', index=False, if_exists='append')

    count_source_of_data = db.session.query(Source_of_data).count()

    #Address---
    for _ in range(2):
        fake_data_address["source_of_data_id"].append(random.randint(1, count_source_of_data))
        fake_data_address["street"].append(fake.street_name())
        fake_data_address["street_number"].append(random.randint(1, 299))
        fake_data_address["postcode"].append(fake.postcode())
        fake_data_address["location"].append(fake.city())
        fake_data_address["created_at"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    df_fake_data_address = pd.DataFrame(fake_data_address)

    df_fake_data_address.to_sql('Address', con='sqlite:///common_database.db', index=False, if_exists='append')

    #Customer---
    for _ in range(2):
        fake_data_customer["source_of_data_id"].append(random.randint(1, count_source_of_data))
        fake_data_customer["name"].append(fake.first_name() + " " + fake.last_name())
        fake_data_customer["date_of_birth"].append(fake.date_of_birth())
        fake_data_customer["telephone_number"].append(fake.phone_number())
        fake_data_customer["email"].append(fake.email())
        fake_data_customer["created_at"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    df_fake_data_customer = pd.DataFrame(fake_data_customer)

    #Hier eig die env-Variable nutzen
    df_fake_data_customer.to_sql('Customer', con='sqlite:///common_database.db', index=False, if_exists='append')


    #Invoice---
    count_customer = db.session.query(Customer).count()

    for _ in range(2):
        fake_data_invoice["source_of_data_id"].append(random.randint(1, count_source_of_data))
        fake_data_invoice["customer_id"].append(random.randint(1, count_customer))
        fake_data_invoice["date"].append(fake.date_this_decade())
        fake_data_invoice["number"].append(random.randint(100, 999999999))
        fake_data_invoice["service"].append(fake.catch_phrase())
        fake_data_invoice["amount"].append(round(random.uniform(0.00, 10000.00), 2))
        fake_data_invoice["created_at"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    df_fake_data_invoice = pd.DataFrame(fake_data_invoice)

    df_fake_data_invoice.to_sql('Invoice', con='sqlite:///common_database.db', index=False, if_exists='append')

    #Customer_addresses (One Address for one customer)
    cust = Customer.query.all()
    addr = Address.query.all()

    for i in range(count_customer):
        cust[i].addresses.append(addr[i])
        

    #User Access
    count_user = db.session.query(User).count()
  
    user = User.query.all()
    sod = Source_of_data.query.all()

    for i in range(count_user +1):
        
        #not for admin
        if i <= 1:
            continue

        count_sods = random.randint(1, count_source_of_data)
        sods = []

        #random source of data
        for j in range(count_sods):
            randomSod = random.randint(0, count_source_of_data -1)

            if randomSod not in sods:
                sods.append(randomSod)

        #add UserAccess
        for x in range(len(sods)):
            user_access = UserAccess(user_id=i, source_of_data_id=sod[sods[x]].id)
            db.session.add(user_access)



    db.session.commit()#just one time at the end     
    
    flash("Faker Data were generated", "success")



       
