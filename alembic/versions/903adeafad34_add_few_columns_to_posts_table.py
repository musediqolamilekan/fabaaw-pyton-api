"""add few columns to posts table

Revision ID: 903adeafad34
Revises: 6d0f90d1baeb
Create Date: 2022-06-11 17:04:47.096458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "903adeafad34"
down_revision = "6d0f90d1baeb"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
