from models import *
from routes import *
from config import app
from config import db
from werkzeug.security import generate_password_hash
from datetime import datetime
from faker_data import *


import os
import os.path as op

# Setup
app_dir = op.realpath(os.path.dirname(__file__))
database_path = op.join(app_dir, app.config['SQLALCHEMY_DATABASE_URI'])
migration_path = op.join(app_dir, 'migrations')



#Create first User as Admin if countUser == 0
countUser = 0
try:
    countUser = User.query.count()
except:#when database not exists
    db.create_all()
    db.session.commit()

if countUser == 0:
    user = User()
    user.email = "admin@oe24.at"
    user.password_hash = generate_password_hash("admin")
    user.created_at = datetime.now()
    db.session.add(user)
    db.session.commit()

# Run App
if __name__ == '__main__':
    app.run()

