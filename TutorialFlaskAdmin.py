from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin.contrib.sqla import ModelView

import flask_admin as admin

# Create flask app
app = Flask(__name__, template_folder='templates')

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oe24Example.db'

#Secret Key
app.config['SECRET_KEY'] = "my secret key" 

#Initialize the database
db = SQLAlchemy(app)

#Create Model
class Datenquelle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __unicode__(self):
        return self.name


class Adresse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    straße = db.Column(db.String(50))
    hausnummer = db.Column(db.String(15))
    plz = db.Column(db.Integer)
    ort = db.Column(db.String(30))

    def __unicode__(self):
        return self.name

class Kunde(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    geburtsdatum = db.Column(db.Date)
    telefonnummer = db.Column(db.Integer)
    email = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now)
    #datenquellen = db.relationship(Datenquelle, backref='Datenquelle.id')

    def __unicode__(self):
        return self.name


class Rechnung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.Date)
    nummer = db.Column(db.Integer)
    leistung = db.Column(db.String(50))
    betrag = db.Numeric(10,2)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __unicode__(self):
        return self.name


# Flask views
@app.route('/')
def index():
    #db.create_all()
    #db.session.commit()
    return '<a href="/admin/">Click me to get to Admin!</a>'

# Create admin interface
admin = admin.Admin(name="Flask Admin Example", template_mode='bootstrap4')
admin.add_view(ModelView(Datenquelle, db.session))
admin.add_view(ModelView(Adresse, db.session))
admin.add_view(ModelView(Kunde, db.session))
admin.add_view(ModelView(Rechnung, db.session))
admin.init_app(app)

# Run App
if __name__ == '__main__':
    app.run()