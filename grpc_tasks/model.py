from pydantic import BaseModel


class Task(BaseModel):
    """Task Class"""

    id: int
    description: str
    course_id: int
    login: str
    score: int
