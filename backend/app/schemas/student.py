from pydantic import BaseModel


class AcademicSessionResponse(BaseModel):
    id: int
    name: str
    start_year: int
    end_year: int
    is_active: bool


class StudentProfileResponse(BaseModel):
    id: int
    name: str
    nu_registration_number: str
    class_roll: str
    batch: str | None
    year_level: int | None
    section: str | None
    email: str | None
    phone: str | None
    profile_photo_url: str | None
    academic_session: AcademicSessionResponse