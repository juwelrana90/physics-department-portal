from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.student import Student
from app.models.user import User
from app.schemas.student import StudentProfileResponse


router = APIRouter()


@router.get(
    "/me",
    response_model=StudentProfileResponse,
)
def get_my_student_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Return the profile of the currently authenticated student.
    """

    student = db.execute(
        select(Student).where(
            Student.user_id == current_user.id
        )
    ).scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found.",
        )

    return student