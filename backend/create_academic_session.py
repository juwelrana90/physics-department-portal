from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.academic_session import AcademicSession


def main():
    db = SessionLocal()

    try:
        existing = db.scalar(
            select(AcademicSession).where(
                AcademicSession.name == "2025-26"
            )
        )

        if existing:
            print(f"Academic session already exists: {existing.name}")
            print(f"ID: {existing.id}")
            print(f"Active: {existing.is_active}")
            return

        session = AcademicSession(
            name="2025-26",
            start_year=2025,
            end_year=2026,
            is_active=True,
        )

        db.add(session)
        db.commit()
        db.refresh(session)

        print("Academic session created successfully.")
        print(f"ID: {session.id}")
        print(f"Name: {session.name}")
        print(f"Active: {session.is_active}")

    finally:
        db.close()


if __name__ == "__main__":
    main()