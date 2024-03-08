"""Initial migration.

Revision ID: b4094e8c79bb
Revises: ddc085fb0c53
Create Date: 2024-02-28 17:54:53.515039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4094e8c79bb'
down_revision = 'ddc085fb0c53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ckan_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('weather')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('datetime', sa.DATETIME(), nullable=True),
    sa.Column('temperature', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('ckan_data')
    # ### end Alembic commands ###