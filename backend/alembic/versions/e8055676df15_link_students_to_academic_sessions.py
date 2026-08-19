"""Link students to academic sessions

Revision ID: e8055676df15
Revises: 9f343a1e3944
Create Date: 2026-08-18 12:50:37.632493

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e8055676df15"
down_revision: Union[str, Sequence[str], None] = "9f343a1e3944"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "students",
        sa.Column(
            "academic_session_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.create_index(
        op.f("ix_students_academic_session_id"),
        "students",
        ["academic_session_id"],
        unique=False,
    )

    op.create_foreign_key(
        "fk_students_academic_session_id",
        "students",
        "academic_sessions",
        ["academic_session_id"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_students_academic_session_id",
        "students",
        type_="foreignkey",
    )

    op.drop_index(
        op.f("ix_students_academic_session_id"),
        table_name="students",
    )

    op.drop_column(
        "students",
        "academic_session_id",
    )