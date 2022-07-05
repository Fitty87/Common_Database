from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    #@Tom: Hier auf Lenght auch prüfen gut?
    email = StringField('email', validators=[InputRequired(), Length(min=10, max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=3, max=20)])

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='invalid email'), Length(min=10, max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=3, max=20)])
