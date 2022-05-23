from models import *
from routes import *
from config import app
from config import db

import os
import os.path as op
import subprocess

# Setup
app_dir = op.realpath(os.path.dirname(__file__))
database_path = op.join(app_dir, app.config['SQLALCHEMY_DATABASE_URI'])
migration_path = op.join(app_dir, 'migrations')

#if not os.path.isfile(database_path):
    #print("DBbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

#if not os.path.exists(database_path):
    #db.drop_all()
    #db.create_all()
    #db.session.commit()
    #print("DBbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

#if not os.path.exists(migration_path):
    #subprocess.run("flask db init", shell=True, check=True)
    #subprocess.run("flask db migrate -m 'Init Migration'", shell=True, check=True)
    #subprocess.run("flask db upgrade", shell=True, check=True)
    #print("HIIIIIIIIIIIIIIIER")
    #os.system("flask db init")

# Run App
if __name__ == '__main__':
    app.run()

