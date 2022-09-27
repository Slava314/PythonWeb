from typing import List

from app.models import model

db = {
    "users": [model.User(login="dev", password="admin", user_id=1, courses=[1])],
    "courses": [
        model.Course(name="Python web", course_id=1, description="good"),
        model.Course(name="Haskell", course_id=2, description="\\x -> x * x"),
    ],
}
db_ids = {"users": 1, "courses": 0}


def get_all_users() -> List[model.User]:
    return db["users"]


def get_all_courses() -> List[model.Course]:
    return db["courses"]


def user_with_login_exists(login: str) -> bool:
    users = get_all_users()
    for u in users:
        if u.login == login:
            return True
    return False


def add_user(login: str, password: str) -> model.User:
    user_id = db_ids["users"]
    user_id += 1
    db_ids["users"] = user_id
    new_user = model.User(login=login, password=password, user_id=user_id, courses=[])
    get_all_users().append(new_user)
    return new_user


def user_exists(login: str, password: str) -> bool:
    users = get_all_users()
    for u in users:
        if u.login == login and u.password == password:
            return True
    return False


def add_course(name: str, description: str) -> model.Course:
    course_id = db_ids["courses"]
    course_id += 1
    db_ids["course"] = course_id
    new_course = model.Course(name=name, course_id=course_id, description=description)
    get_all_courses().append(new_course)
    return new_course


def get_courses(ids: List[int]) -> List[model.Course]:
    all_courses = get_all_courses()
    ans = []
    for c in all_courses:
        if c.course_id in ids:
            ans.append(c)
    return ans


def get_user(login: str) -> model.User:
    users = get_all_users()
    for u in users:
        if u.login == login:
            return u
    return None
