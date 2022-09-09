"""empty message

Revision ID: d4ee2308fb7d
Revises: 1d97ce2d29f8
Create Date: 2022-09-03 21:41:46.984002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4ee2308fb7d'
down_revision = '1d97ce2d29f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('roles', 'name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_constraint('user_roles_id_key', 'user_roles', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_roles_id_key', 'user_roles', ['id'])
    op.alter_column('roles', 'name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###
