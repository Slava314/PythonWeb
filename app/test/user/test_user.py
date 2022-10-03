import copy
import unittest
from unittest.mock import patch

from app.db.db import db
from app.models import model
from app.models.user import user
from app.test.db.test_db import test_db


class TestUser(unittest.TestCase):
    dev_user = model.User(
        login="dev", password="adminPassword1", user_id=1, courses=[1]
    )
    test_user = model.User(login="Bob", password="pass1Word", user_id=2, courses=[2])

    def test_good_password(self):
        self.assertTrue(user.password_is_strong("pass1Word"))

    def test_bad_password(self):
        self.assertFalse(user.password_is_strong("pass1W"))
        self.assertFalse(user.password_is_strong("password"))
        self.assertFalse(user.password_is_strong("password1"))

    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_check_login_password(self):
        self.assertTrue(
            user.check_login_password(self.dev_user.login, self.dev_user.password)
        )

        self.assertFalse(
            user.check_login_password(self.test_user.login, self.test_user.password)
        )

    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_get_courses(self):
        courses = user.get_courses(self.dev_user.login)
        self.assertListEqual([1], [x.course_id for x in courses])

    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_add_course(self):
        course_name = user.add_course(self.dev_user.login, 2)["course_name"]
        self.assertEqual(course_name, "Haskell")
        self.assertListEqual(
            [1, 2], [x.course_id for x in user.get_courses(self.dev_user.login)]
        )

    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_add_user(self):
        self.assertIn(
            "error", user.add_user(self.dev_user.login, self.dev_user.password)
        )
        self.assertEqual(
            self.test_user.login,
            user.add_user(self.test_user.login, self.test_user.password)["login"],
        )
