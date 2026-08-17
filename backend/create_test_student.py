from sqlalchemy import select

from app.core.database import Base, engine, SessionLocal
from app.core.security import hash_password
from app.models.user import User, UserRole
from app.models.student import Student


# Make sure the database tables exist.
Base.metadata.create_all(bind=engine)


USERNAME = "101"
PASSWORD = "Student@2026"

NU_REGISTRATION = "TEST-2026-001"


def create_test_student():
    db = SessionLocal()

    try:
        existing_user = db.execute(
            select(User).where(User.username == USERNAME)
        ).scalar_one_or_none()

        if existing_user:
            print("Test student already exists.")
            print(f"Username: {USERNAME}")
            return

        user = User(
            username=USERNAME,
            password_hash=hash_password(PASSWORD),
            role=UserRole.student,
            is_active=True,
        )

        db.add(user)
        db.flush()

        student = Student(
            user_id=user.id,
            nu_registration_number=NU_REGISTRATION,
            class_roll=USERNAME,
            name="Test Student",
            batch="2025-26",
            year_level=1,
            section="A",
        )

        db.add(student)
        db.commit()

        print("====================================")
        print("Test student created successfully!")
        print("====================================")
        print(f"Username / Roll: {USERNAME}")
        print(f"Password:        {PASSWORD}")
        print("Role:            student")
        print("====================================")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    create_test_student()