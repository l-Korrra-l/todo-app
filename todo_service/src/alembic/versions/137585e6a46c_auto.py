"""auto

Revision ID: 137585e6a46c
Revises: 712d57431129
Create Date: 2023-06-12 08:28:15.799203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137585e6a46c'
down_revision = '712d57431129'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('owner', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todolist')
    # ### end Alembic commands ###