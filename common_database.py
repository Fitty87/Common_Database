from models import *
from routes import *
from config import app
from config import db

import os
import os.path as op


# Setup
app_dir = op.realpath(os.path.dirname(__file__))
database_path = op.join(app_dir, app.config['SQLALCHEMY_DATABASE_URI'])
migration_path = op.join(app_dir, 'migrations')

# Run App
if __name__ == '__main__':
    app.run()

