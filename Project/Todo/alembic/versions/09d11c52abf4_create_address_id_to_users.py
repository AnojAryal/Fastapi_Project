"""create address_id to users

Revision ID: 09d11c52abf4
Revises: ed7e6b21fa0f
Create Date: 2024-02-17 21:11:17.738961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09d11c52abf4'
down_revision: Union[str, None] = 'ed7e6b21fa0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
