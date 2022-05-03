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
    name = db.Column(db.String(50), nullable = False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    kunde_id = db.Column(db.Integer, db.ForeignKey('kunde.id'))
    adresse_id = db.Column(db.Integer, db.ForeignKey('adresse.id'))
    rechnung_id = db.Column(db.Integer, db.ForeignKey('rechnung.id'))

    def __str__(self):
        return self.name


class Adresse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    straße = db.Column(db.String(50), nullable = False)
    hausnummer = db.Column(db.String(15), nullable = False)
    plz = db.Column(db.Integer, nullable = False)
    ort = db.Column(db.String(30), nullable = False)
    datenquellen = db.relationship('Datenquelle', backref='adresse')
    kunde_id = db.Column(db.Integer, db.ForeignKey('kunde.id'))
    #kunden = db.relationship("Kunden_Adressen", back_populates="adresse")

    def __str__(self):
        return self.straße+' '+str(self.hausnummer)+', '+str(self.plz)+' '+self.ort


class Kunde(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    geburtsdatum = db.Column(db.Date, nullable = False)
    telefonnummer = db.Column(db.Integer, nullable = False, unique=True)
    email = db.Column(db.String(50), nullable = False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    datenquellen = db.relationship('Datenquelle', backref='kunde')
    rechnungen = db.relationship('Rechnung', backref='kunde')
    adressen = db.relationship('Adresse', backref='kunde')
    #adressen = db.relationship("Kunden_Adressen", back_populates="kunde")

    def __str__(self):
        return self.name


class Rechnung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.Date, nullable = False)
    nummer = db.Column(db.Integer, nullable = False, unique=True)
    leistung = db.Column(db.String(50), nullable = False)
    betrag = db.Numeric(10,2)
    created_at = db.Column(db.DateTime, default=datetime.now)
    datenquellen = db.relationship('Datenquelle', backref='rechnung')
    kunde_id = db.Column(db.Integer, db.ForeignKey('kunde.id'))

    def __str__(self):
        return str(self.nummer)

#class Kunden_Adressen(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #kunde_id = db.Column(db.Integer, db.ForeignKey('kunde.id'))
    #adresse_id = db.Column(db.Integer, db.ForeignKey('adresse.id'))
    #kunde = db.relationship('Kunde', back_populates='adressen')
    #adresse = db.relationship('Adresse', back_populates='kunden')

# Flask views
@app.route('/')
def index():
    #db.drop_all()
    #db.create_all()
    #db.session.commit()
    return '<a href="/admin/">Click me to get to Admin!</a>'

# Create custom view
class UserView(ModelView):
    column_hide_backrefs = False
    page_size = 5


# Create admin interface
admin = admin.Admin(name="Flask Admin Example", template_mode='bootstrap4')
admin.add_view(UserView(Datenquelle, db.session))
admin.add_view(UserView(Adresse, db.session))
admin.add_view(UserView(Kunde, db.session))
admin.add_view(UserView(Rechnung, db.session))
#admin.add_view(UserView(Kunden_Adressen, db.session))
admin.init_app(app)

# Run App
if __name__ == '__main__':
    app.run()