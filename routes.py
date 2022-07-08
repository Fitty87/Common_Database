from flask import render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_admin.contrib.sqla import ModelView
import flask_admin as admin
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

from config import app
from models import *
from forms import *

#Flask_Routes
@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                print("Login was successful")
            else: 
                print("Login failed")
        else:
            print("User doesn't exist!")  

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.password_hash = generate_password_hash(form.password.data)
        #user.authenticated = True
        db.session.add(user)
        db.session.commit()
        print("successful registration")

    return render_template('register.html', form=form)

#Create_Custom_View
class UserView(ModelView):
    page_size = 5


#Create_Admin_Interface
admin = admin.Admin(name="Flask Admin Example", template_mode='bootstrap4')
admin.add_view(UserView(Source_of_data, db.session))
admin.add_view(UserView(Address, db.session))
admin.add_view(UserView(Customer, db.session))
admin.add_view(UserView(Invoice, db.session))
admin.init_app(app)

#Login_Manager
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)