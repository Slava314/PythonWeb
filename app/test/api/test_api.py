import copy
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.db.db import db
from app.main import app
from app.models import model
from app.test.db.test_db import test_db


class IntegrationTests(unittest.TestCase):
    client = TestClient(app)
    test_user = model.User(login="Bob", password="pass1Word", user_id=2, courses=[1])

    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_get_all_courses(self):
        response = self.client.get("/courses/all")
        self.assertEqual(response.status_code, 200)
        actual = {"courses": db["courses"]}
        self.assertEqual(response.json(), actual)

    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_add_user(self):
        response = self.client.post(
            "/users/sign_up",
            json={
                "login": self.test_user.login,
                "password": self.test_user.password,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"login": self.test_user.login})

    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_add_course(self):
        self.client.post(
            "/users/sign_up",
            json={
                "login": self.test_user.login,
                "password": self.test_user.password,
            },
        )
        response = self.client.post(
            "/users/courses/add/1",
            json={
                "login": self.test_user.login,
                "password": self.test_user.password,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"course_name": "Python web"})
