"""rename address

Revision ID: c17426be0346
Revises: d3461125da04
Create Date: 2025-01-14 13:47:33.008261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c17426be0346'
down_revision = 'd3461125da04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
