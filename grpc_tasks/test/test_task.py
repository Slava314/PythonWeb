import copy
import unittest
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch

import grpc
import model
import task_client
import task_server
from builds.service_pb2_grpc import (
    add_TaskServiceServicer_to_server as add_to_server,
)
from db import db
from parameterized import parameterized

from test_db import test_db


class TestServer(unittest.TestCase):
    test_task = model.Task(id=1, description="grpc", course_id=1, login="dev", score=10)
    new_task = model.Task(id=2, description="db", course_id=1, login="dev", score=0)

    def setUp(self):
        super().setUp()
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        add_to_server(task_server.Service(), self.server)
        self.server.add_insecure_port('[::]:4044')
        self.server.start()

    def tearDown(self):
        super().tearDown()
        self.server.stop(None)

    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_get_task(self):
        task = task_client.get_task(self.test_task.id,
                                    self.test_task.course_id,
                                    self.test_task.login)
        self.assertEqual(task, self.test_task)

    @parameterized.expand(
        [[model.Task(id=2, description="db", course_id=1, login="dev", score=0)],
         [model.Task(id=3, description="", course_id=2, login="Bob", score=5)]]
    )
    @patch.dict(db, copy.deepcopy(test_db), clear=True)
    def test_add_task(self, task: model.Task):
        task_client.add_task(task)
        task = task_client.get_task(task.id,
                                    task.course_id,
                                    task.login)
        self.assertEqual(task, task)
