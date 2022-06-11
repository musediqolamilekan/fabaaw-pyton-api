"""add content  column to posts

Revision ID: e9a544bdcf5c
Revises: bb4a9eb6ede3
Create Date: 2022-06-11 16:30:26.498365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e9a544bdcf5c"
down_revision = "bb4a9eb6ede3"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
