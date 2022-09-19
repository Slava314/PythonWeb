from pydantic import BaseModel


class Course(BaseModel):
    """Course class."""

    name: str
    course_id: int
    decription: str
