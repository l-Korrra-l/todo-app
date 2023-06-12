"""auto

Revision ID: 5433257d8e55
Revises: 500d09828595
Create Date: 2023-06-12 08:01:45.890309

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision = '5433257d8e55'
down_revision = '500d09828595'
branch_labels = None
depends_on = None


def upgrade() -> None:
    taskstatusenum = postgresql.ENUM('IN_PROGRESS', 'DONE', name='taskstatusenum')
    taskstatusenum.create(op.get_bind())
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('status', sa.Enum('IN_PROGRESS', 'DONE', name='taskstatusenum'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'status')
    # ### end Alembic commands ###