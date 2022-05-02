from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

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

    #Create A String
    def __repr__(self):
        return '<Name %r>' % self.name

class Kunde(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    geburtsdatum = db.Column(db.DateTime, nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)


#Create InsertForms-----
class FormDatenquelle(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

class FormDatenquelle(FlaskForm):
name = StringField("Name", validators=[DataRequired()])
submit = SubmitField("Submit")

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Add administrative views here
admin = Admin(app, name='microblog', template_mode='bootstrap3')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Database')
def database():
    allDatenquelle = Datenquelle.query.order_by(Datenquelle.date_added)
    return render_template('database.html', allDatenquelle=allDatenquelle)

@app.route('/Add_Datenquelle', methods=['GET', 'POST'])
def add_Datenquelle():
    name = None
    form = FormDatenquelle()

    if form.validate_on_submit():
        datenquelle = Datenquelle.query.filter_by(name=form.name.data).first()
        if datenquelle is None:
            datenquelle = Datenquelle(name=form.name.data)
            db.session.add(datenquelle)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
         
    allDatenquelle = Datenquelle.query.order_by(Datenquelle.date_added)

    return render_template('add_datenquelle.html', form=form, name=name, allDatenquelle=allDatenquelle)

@app.route('/Add_Kunde', methods=['GET', 'POST'])
def add_Kunde():
    allDatenquelle = Datenquelle.query.order_by(Datenquelle.date_added)
    name = None
    form = FormDatenquelle()
    return render_template('add_kunde.html', form=form, name=name, allDatenquelle=allDatenquelle)

@app.route('/Add_Rechnung')
def add_Rechnung():
    return render_template('add_rechnung.html')

#Run App
if __name__ == '__main__':
    app.run()


