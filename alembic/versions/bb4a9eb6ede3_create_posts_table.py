"""create posts table

Revision ID: bb4a9eb6ede3
Revises: 
Create Date: 2022-06-11 15:10:12.121330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bb4a9eb6ede3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )

    pass


def downgrade():
    op.drop_table("posts")
    pass
