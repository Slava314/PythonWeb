from fastapi import APIRouter

from app.models.course import course
from app.models.user import user

router = APIRouter()


@router.get("/")
def read_root():
    """Description."""
    return {"data": "education platform"}


@router.get("/users/courses/all")
async def get_all_user_courses(user_login: str, user_password: str):
    """Get all user courses."""
    if not user.check_login_password(user_login, user_password):
        return get_error("Incorrect login or password")
    return user.get_courses(user_login)


@router.get("/courses/all")
async def get_all_courses():
    """Get all courses."""
    return course.get_all_courses()


@router.get("/users/courses/{course_id}")
async def get_user_course(user_login: str, user_password: str, course_id: int):
    """Get course from user by id."""
    if not user.check_login_password(user_login, user_password):
        return get_error("Incorrect login or password")
    return user.get_course(user_login, course_id)


@router.post("/users/sign_up")
async def add_user(user_login: str, user_password: str):
    """Add user."""
    result = user.add_user(user_login, user_password)
    return result


@router.post("/users/courses/add")
async def add_user(user_login: str, user_password: str, course_id: int):
    """Add course to user."""
    if not user.check_login_password(user_login, user_password):
        return get_error("Incorrect login or password")
    return user.add_course(user_login, course_id)


def get_error(msg: str):
    return {"error": msg}
