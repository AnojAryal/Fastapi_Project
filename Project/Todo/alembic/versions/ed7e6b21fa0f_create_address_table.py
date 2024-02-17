"""create address table

Revision ID: ed7e6b21fa0f
Revises: 0b9b192cee91
Create Date: 2024-02-17 20:56:50.215839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed7e6b21fa0f'
down_revision: Union[str, None] = '0b9b192cee91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
