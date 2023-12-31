"""Create dog model

Revision ID: d5eec431d315
Revises: 
Create Date: 2023-11-26 18:12:27.877215

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5eec431d315'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), server_default='Sparkey', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dogs')
    # ### end Alembic commands ###
