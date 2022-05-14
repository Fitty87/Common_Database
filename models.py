from config import db
from datetime import datetime

#Create Model
kundenadressen = db.Table('kundenadressen', 
                db.Column('adresse_id', db.Integer, db.ForeignKey('adresse.id'), primary_key=True),
                db.Column('kunde_id', db.Integer, db.ForeignKey('kunde.id'), primary_key=True))

datenquellenadressen = db.Table('datenquellenadressen', 
db.Column('adresse_id', db.Integer, db.ForeignKey('adresse.id'), primary_key=True),
db.Column('datenquelle_id', db.Integer, db.ForeignKey('datenquelle.id'), primary_key=True))


class Datenquelle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique=True)
    kunden = db.relationship('Kunde', backref='datenquelle')
    rechnungen = db.relationship('Rechnung', backref='datenquelle')
    adressen = db.relationship('Adresse', backref='datenquelle')
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.name


class Adresse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datenquelle_id = db.Column(db.Integer, db.ForeignKey('datenquelle.id'))
    straße = db.Column(db.String(50), nullable = False)
    hausnummer = db.Column(db.String(15), nullable = False)
    plz = db.Column(db.Integer, nullable = False)
    ort = db.Column(db.String(30), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.straße+' '+str(self.hausnummer)+', '+str(self.plz)+' '+self.ort


class Kunde(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datenquelle_id = db.Column(db.Integer, db.ForeignKey('datenquelle.id'))
    name = db.Column(db.String(50), nullable = False)
    geburtsdatum = db.Column(db.Date, nullable = False)
    telefonnummer = db.Column(db.Integer, nullable = False, unique=True)
    email = db.Column(db.String(50), nullable = False, unique=True)  
    rechnungen = db.relationship('Rechnung', backref='kunde')
    adressen = db.relationship('Adresse', secondary="kundenadressen", lazy='subquery', backref=db.backref('kunden', lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.name


class Rechnung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datenquelle_id = db.Column(db.Integer, db.ForeignKey('datenquelle.id'))
    kunde_id = db.Column(db.Integer, db.ForeignKey('kunde.id'))
    datum = db.Column(db.Date, nullable = False)
    nummer = db.Column(db.Integer, nullable = False, unique=True)
    leistung = db.Column(db.String(50), nullable = False)
    betrag = db.Numeric(10,2)
    created_at = db.Column(db.DateTime, default=datetime.now)
   
    def __str__(self):
        return str(self.nummer)