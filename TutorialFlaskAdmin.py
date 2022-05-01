from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oe24Example.db'
#Initialize the database
db = SQLAlchemy(app)

#Create Model
class Datenquelle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #Create A String
    def __repr__(self):
        return '<Name %r>' % self.name


# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Add administrative views here
admin = Admin(app, name='microblog', template_mode='bootstrap3')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Add_Datenquelle')
def add_Datenquelle():
    return render_template('add_datenquelle.html')

@app.route('/Add_Kunde')
def add_Kunde():
    return render_template('add_kunde.html')

@app.route('/Add_Rechnung')
def add_Rechnung():
    return render_template('add_rechnung.html')

#Run App
if __name__ == '__main__':
    app.run()


