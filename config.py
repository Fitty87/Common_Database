from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create flask app
app = Flask(__name__, template_folder='templates')

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oe24Example.db'

#Secret Key
app.config['SECRET_KEY'] = "my secret key" 

#Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)