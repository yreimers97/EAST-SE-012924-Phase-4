"""empty message

Revision ID: bdd6fd002de7
Revises: 965bf5b0fd58
Create Date: 2024-04-10 15:18:04.914380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdd6fd002de7'
down_revision = '965bf5b0fd58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hotel_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'hotels', ['hotel_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('hotel_id')

    # ### end Alembic commands ###
