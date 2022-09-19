from typing import List

from pydantic import BaseModel


class User(BaseModel):
    """User class."""

    login: str
    user_id: int
    courses: List[int]


def get_user(user_id: int):
    return {"user_id": user_id, "login": "login_{0}".format(user_id)}
