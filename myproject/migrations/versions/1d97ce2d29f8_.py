"""empty message

Revision ID: 1d97ce2d29f8
Revises: db54b7c9e682
Create Date: 2022-08-25 03:21:44.241951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d97ce2d29f8'
down_revision = 'db54b7c9e682'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('roles_role_name_key', 'roles', type_='unique')
    op.alter_column('roles', 'role_name', nullable=False, new_column_name='name')
    op.create_unique_constraint(None, 'roles', ['name'])
    op.add_column('user_roles', sa.Column('id', sa.Integer(), nullable=False, autoincrement=True, unique=True, primary_key=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('roles_name_key', 'roles', type_='unique')
    op.drop_constraint(None, 'roles', type_='unique')
    op.drop_column('user_roles', 'id')
    op.alter_column('roles', 'name', nullable=False, new_column_name='role_name')
    op.create_unique_constraint('roles_role_name_key', 'roles', ['role_name'])
    # ### end Alembic commands ###
