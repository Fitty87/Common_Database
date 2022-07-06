from flask import render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_admin.contrib.sqla import ModelView
import flask_admin as admin
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

from config import app
from models import *
from forms import *



# Flask views
@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(123)

    return render_template('login.html', form=form)




@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

# Create custom view
class UserView(ModelView):
    page_size = 5


# Create admin interface
admin = admin.Admin(name="Flask Admin Example", template_mode='bootstrap4')
admin.add_view(UserView(Source_of_data, db.session))
admin.add_view(UserView(Address, db.session))
admin.add_view(UserView(Customer, db.session))
admin.add_view(UserView(Invoice, db.session))
admin.init_app(app)