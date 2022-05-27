from flask_admin.contrib.sqla import ModelView
import flask_admin as admin

from config import app
from models import *



# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

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