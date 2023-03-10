"""empty message

Revision ID: 776844323bbd
Revises: 1c9e27f29143
Create Date: 2023-02-09 15:32:29.738211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '776844323bbd'
down_revision = '1c9e27f29143'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.alter_column('isbn',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.alter_column('isbn',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
