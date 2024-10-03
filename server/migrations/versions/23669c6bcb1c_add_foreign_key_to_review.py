"""add foreign key to Review

Revision ID: 23669c6bcb1c
Revises: b48dc052e2b7
Create Date: 2024-10-03 19:47:55.131116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23669c6bcb1c'
down_revision = 'b48dc052e2b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
