"""auto

Revision ID: 30263c37ef55
Revises: 137585e6a46c
Create Date: 2023-06-12 08:31:15.210492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30263c37ef55'
down_revision = '137585e6a46c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('list', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'task', 'todolist', ['list'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'list')
    # ### end Alembic commands ###
