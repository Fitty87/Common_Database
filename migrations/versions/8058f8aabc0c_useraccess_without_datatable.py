"""UserAccess without Datatable

Revision ID: 8058f8aabc0c
Revises: f03a618f58b8
Create Date: 2022-08-10 13:39:55.249869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8058f8aabc0c'
down_revision = 'f03a618f58b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_useraccesses')
    op.drop_table('source_of_data_useraccesses')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('source_of_data_useraccesses',
    sa.Column('source_of_data_id', sa.INTEGER(), nullable=False),
    sa.Column('useraccess_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['source_of_data_id'], ['source_of_data.id'], ),
    sa.ForeignKeyConstraint(['useraccess_id'], ['user_access.id'], ),
    sa.PrimaryKeyConstraint('source_of_data_id', 'useraccess_id')
    )
    op.create_table('user_useraccesses',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('useraccess_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['useraccess_id'], ['user_access.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'useraccess_id')
    )
    # ### end Alembic commands ###
