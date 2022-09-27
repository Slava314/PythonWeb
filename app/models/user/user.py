import re

from app.db import db


def get_user(user_id: int):
    return {"user_id": user_id, "login": "login_{0}".format(user_id)}


def add_user(login: str, password: str):
    if db.user_with_login_exists(login):
        return {"error": "such login exists"}
    if not password_is_strong(password):
        return {"error": "password must contain mixed case letters and numbers"}
    new_user = db.add_user(login, password)
    return {"login": new_user.login}


def password_is_strong(password: str):
    number_pattern = re.compile(r"\d")
    if not number_pattern.search(password):
        return False
    letter_pattern = re.compile(r"[a-z]")
    if not letter_pattern.search(password):
        return False
    capital_letter_pattern = re.compile(r"[A-Z]")
    if not capital_letter_pattern.search(password):
        return False
    return True


def check_login_password(login: str, password: str) -> bool:
    return db.user_exists(login, password)


def get_courses(login: str):
    user = db.get_user(login)
    return db.get_courses(user.courses)


def get_course(login: str, course_id: int):
    return db.get_courses([course_id])[0]


def add_course(login: str, course_id: int):
    user = db.get_user(login)
    course = db.get_courses([course_id])[0]
    user.courses.append(course.course_id)
    return {"course_name": course.name}
