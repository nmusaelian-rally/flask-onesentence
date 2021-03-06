"""empty message

Revision ID: bc5becc9e91c
Revises: 
Create Date: 2019-04-21 22:37:09.241041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc5becc9e91c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('onesentence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('story', sa.Text(), nullable=True),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('onesentence')
    # ### end Alembic commands ###
