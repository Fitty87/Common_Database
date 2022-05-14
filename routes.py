from flask_admin.contrib.sqla import ModelView
import flask_admin as admin

from config import app
from models import *

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
admin.init_app(app)