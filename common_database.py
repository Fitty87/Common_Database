from models import *
from routes import *
from config import app
from config import db
from werkzeug.security import generate_password_hash


import os
import os.path as op

# Setup
app_dir = op.realpath(os.path.dirname(__file__))
database_path = op.join(app_dir, app.config['SQLALCHEMY_DATABASE_URI'])
migration_path = op.join(app_dir, 'migrations')

#db.drop_all()
#db.create_all()
#db.session.commit()

#Create first User as Admin if countUser == 0
countUser = User.query.count()
if countUser == 0:
    user = User()
    user.email = "admin@oe24.at"
    user.password_hash = generate_password_hash("admin")
    print(user.password_hash)
    user.is_authenticated = True
    db.session.add(user)
    db.session.commit()

#So kann man Nur Datatables Queries machen
#test = db.session.query(customer_addresses).all()

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

def upgrade():
    with op.batch_alter_table('test', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.drop_constraint('fk_test_user_id_user', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_test_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')


# Run App
if __name__ == '__main__':
    app.run()

