from models import *
from routes import *
from config import app
from config import db
from werkzeug.security import generate_password_hash


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
    print(user.password_hash)
    user.is_authenticated = True
    db.session.add(user)
    db.session.commit()

# Run App
if __name__ == '__main__':
    app.run()

