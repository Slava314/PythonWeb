from random import randint

from fastapi import APIRouter

from app.models import course, user

router = APIRouter()


@router.get("/")
def read_root():
    """Description."""
    return {"data": "education platform"}


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    """Get user."""
    return user.get_user(user_id)


@router.get("/courses/{course_id}")
async def get_course(course_id: int, name: str, description: str | None = None):
    """Get course."""
    course = {"course_id": course_id, "name": name}
    if description:
        course.update({"description": description})
    return course


@router.get("/users/{user_id}/cources/{course_id}")
async def read_user_course(
    user_id: int, course_id: int, description: str | None = None
):
    """Get course from user by id."""
    item = {
        "course_id": course_id,
        "owner_id": user_id,
        "name": "course {0}".format(randint(0, course_id)),
    }
    if description:
        item.update({"description": description})
    return item


@router.post("/users/{user_id}")
async def add_course(user_id: int, course: course.Course):
    """Add course to user."""
    user = {"user_id": user_id}
    user.update({"courses": [course.course_id]})
    return user
