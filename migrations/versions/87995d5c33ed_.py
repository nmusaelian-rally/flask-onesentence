"""empty message

Revision ID: 87995d5c33ed
Revises: 
Create Date: 2019-04-23 08:25:34.185161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87995d5c33ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('onesentence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('story', sa.Text(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('onesentence')
    # ### end Alembic commands ###