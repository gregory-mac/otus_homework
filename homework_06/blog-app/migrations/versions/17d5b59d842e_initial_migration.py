"""Initial migration

Revision ID: 17d5b59d842e
Revises: 
Create Date: 2022-07-02 13:21:03.719833

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String, Integer, ForeignKey


# revision identifiers, used by Alembic.
revision = '17d5b59d842e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column("id", Integer, primary_key=True),
        sa.Column("name", String(50), nullable=False, unique=False),
        sa.Column("username", String(20), nullable=False, unique=True),
        sa.Column("email", String(30), nullable=False, unique=True),
    )
    op.create_table(
        'posts',
        sa.Column("id", Integer, primary_key=True),
        sa.Column("user_id", Integer, ForeignKey("users.id"), nullable=False, unique=False),
        sa.Column("title", String(100), nullable=False, unique=True),
        sa.Column("body", String(500), nullable=False, unique=False),
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('posts')
