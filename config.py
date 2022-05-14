from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create flask app
app = Flask(__name__, template_folder='templates')

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oe24Example.db'

#Secret Key
app.config['SECRET_KEY'] = "my secret key" 

#Initialize the database
db = SQLAlchemy(app)