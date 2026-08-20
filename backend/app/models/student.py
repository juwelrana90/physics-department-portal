from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        index=True,
    )

    academic_session_id: Mapped[int] = mapped_column(
        ForeignKey("academic_sessions.id"),
        nullable=False,
        index=True,
    )

    academic_session: Mapped["AcademicSession"] = relationship(
        "AcademicSession",
        back_populates="students",
    )

    nu_registration_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
    )

    class_roll: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(150))

    batch: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    year_level: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    section: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    profile_photo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )