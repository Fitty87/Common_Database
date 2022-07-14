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
fake = Faker()
fake_data = defaultdict(list)

count_source_of_data = db.session.query(Source_of_data).count()

for _ in range(10):
    fake_data["source_of_data_id"].append(random.randint(1, count_source_of_data))
    fake_data["name"].append(fake.first_name() + " " + fake.last_name())
    fake_data["date_of_birth"].append(fake.date_of_birth())
    fake_data["telephone_number"].append(fake.phone_number())
    fake_data["email"].append(fake.email())
    fake_data["created_at"].append(datetime.now())

df_fake_data = pd.DataFrame(fake_data)

#Hier eig die env-Variable nutzen
df_fake_data.to_sql('Customer', con='sqlite:///common_database.db', index=False, if_exists='append')




# Run App
if __name__ == '__main__':
    app.run()

