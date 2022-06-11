"""create user table

Revision ID: 711787c72f4f
Revises: e9a544bdcf5c
Create Date: 2022-06-11 16:38:17.459880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "711787c72f4f"
down_revision = "e9a544bdcf5c"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
