from flask import render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_admin.contrib.sqla import ModelView
import flask_admin as admin
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_admin import AdminIndexView
from sqlalchemy.sql import not_
from flask_admin.menu import MenuLink


from config import app
from models import *
from forms import *

@app.route('/')
def index():
    return '<a href="/login">Please Login</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                print("Login was successful")

                admin.name = "User: " +  str(current_user.email)
     
                if(user.id == 1): #Der erste User ist Admin
                    return redirect(url_for('admin.index'))
                else:
                    return redirect('admin/customer')
            else: 
                print("Login failed")
        else:
            print("User doesn't exist!")  

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    print("Logout")
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.password_hash = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        print("successful registration")

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

#Create_Custom_View
class UserView(ModelView):
    page_size = 10

    def on_model_change(self, form, instance):
        if instance:
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def get_query(self):
        if current_user.is_authenticated: 
            if current_user.id != 1:
                self.can_create = False
                self.can_delete = False
                self.can_edit = False

                ids_not_accessable = []

                all_ids = Source_of_data.query.all()
                user_accessable_ids = self.session.query(UserAccess.source_of_data_id).filter(UserAccess.user_id == current_user.id)

                filtered_model = self.session.query(self.model).filter((self.model.source_of_data_id.in_(user_accessable_ids)))
               
                return filtered_model        
                
            else:
                self.can_create = True
                self.can_delete = True
                self.can_edit = True

                return self.session.query(self.model)
        else:
            return None


    def is_accessible(self):
        if current_user.is_authenticated: 
            if current_user.id != 1:
                if self.model == User or self.model == Source_of_data or self.model == UserAccess:
                    return False
                else:
                    return True
            else:
                return True
        return False
            

#Admin_Index_View
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated: #Ist User eingeloggt!
            if current_user.id == 1: #Admin hat id=1
                return True
        else:
            return False
  

#Create_Admin_Interface
admin = admin.Admin(name="Common Database", template_mode='bootstrap4', index_view=MyAdminIndexView())

admin.add_view(UserView(User, db.session))
admin.add_view(UserView(UserAccess, db.session))
admin.add_view(UserView(Source_of_data, db.session))
admin.add_view(UserView(Customer, db.session))
admin.add_view(UserView(Address, db.session))
admin.add_view(UserView(Invoice, db.session))
admin.init_app(app)

admin.add_link(MenuLink(name='Logout', category='', url="/logout"))

#Login_Manager
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)