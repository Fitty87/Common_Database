from models import *
from routes import *
from config import app
from config import db
from werkzeug.security import generate_password_hash
from datetime import datetime
import random

import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine

import os
import os.path as op

# Setup
app_dir = op.realpath(os.path.dirname(__file__))
database_path = op.join(app_dir, app.config['SQLALCHEMY_DATABASE_URI'])
migration_path = op.join(app_dir, 'migrations')

#db.drop_all()
#db.create_all()
#db.session.commit()

#Create first User as Admin if countUser == 0
countUser = User.query.count()
if countUser == 0:
    user = User()
    user.email = "admin@oe24.at"
    user.password_hash = generate_password_hash("admin")
    user.is_authenticated = True
    db.session.add(user)
    db.session.commit()

#Random Data with Faker
fake = Faker("de_AT")
fake_data_customer = defaultdict(list)
fake_data_address = defaultdict(list)
fake_data_invoice = defaultdict(list)

count_source_of_data = db.session.query(Source_of_data).count()

#Customer---
for _ in range(10):
    fake_data_customer["source_of_data_id"].append(random.randint(1, count_source_of_data))
    fake_data_customer["name"].append(fake.first_name() + " " + fake.last_name())
    fake_data_customer["date_of_birth"].append(fake.date_of_birth())
    fake_data_customer["telephone_number"].append(fake.phone_number())
    fake_data_customer["email"].append(fake.email())
    fake_data_customer["created_at"].append(datetime.now())

df_fake_data_customer = pd.DataFrame(fake_data_customer)

#Hier eig die env-Variable nutzen
#df_fake_data_customer.to_sql('Customer', con='sqlite:///common_database.db', index=False, if_exists='append')


#Address---
for _ in range(10):
    fake_data_address["source_of_data_id"].append(random.randint(1, count_source_of_data))
    fake_data_address["street"].append(fake.street_name())
    fake_data_address["street_number"].append(random.randint(1, 299))
    fake_data_address["postcode"].append(fake.postcode())
    fake_data_address["location"].append(fake.city())
    fake_data_address["date_added"].append(datetime.now())

df_fake_data_address = pd.DataFrame(fake_data_address)

#df_fake_data_address.to_sql('Address', con='sqlite:///common_database.db', index=False, if_exists='append')

#Invoice---
count_customer = db.session.query(Customer).count()

for _ in range(10):
    fake_data_invoice["source_of_data_id"].append(random.randint(1, count_source_of_data))
    fake_data_invoice["customer_id"].append(random.randint(1, count_customer))
    fake_data_invoice["date"].append(fake.date_this_decade())
    fake_data_invoice["number"].append(random.randint(100, 999999999))
    fake_data_invoice["service"].append(fake.catch_phrase())
    fake_data_invoice["amount"].append(round(random.uniform(0.00, 10000.00), 2))
    fake_data_invoice["created_at"].append(datetime.now())

df_fake_data_invoice = pd.DataFrame(fake_data_invoice)

df_fake_data_invoice.to_sql('Invoice', con='sqlite:///common_database.db', index=False, if_exists='append')


# Run App
if __name__ == '__main__':
    app.run()

