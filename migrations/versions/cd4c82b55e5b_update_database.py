"""update database

Revision ID: cd4c82b55e5b
Revises: 290ba631d1a3
Create Date: 2018-05-30 19:58:54.519720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd4c82b55e5b'
down_revision = '290ba631d1a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=11), nullable=True))
    op.add_column('user', sa.Column('realname', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('work_years', sa.SmallInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'work_years')
    op.drop_column('user', 'realname')
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###