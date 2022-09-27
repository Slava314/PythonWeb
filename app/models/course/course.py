from app.db import db


def get_all_courses():
    return db.get_all_courses()
