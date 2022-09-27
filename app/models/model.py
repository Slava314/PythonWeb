from typing import List

from pydantic import BaseModel


class User(BaseModel):
    """User class."""

    login: str
    password: str
    user_id: int
    courses: List[int]


class Course(BaseModel):
    """Course class."""

    name: str
    course_id: int
    description: str
