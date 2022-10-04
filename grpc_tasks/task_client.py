import typing

import grpc

from builds.service_pb2 import GetTaskArg, Task, GetAllTasksArg
from builds.service_pb2_grpc import TaskServiceStub
import model


def get_task_from_proto(task) -> model.Task:
    """Make `model.Task` from proto.Task"""
    return model.Task(
        id=task.id,
        description=task.description,
        course_id=task.course_id,
        login=task.login,
        score=task.score
    )


def add_task(task: model.Task):
    """Add new task"""
    with grpc.insecure_channel('localhost:4044') as channel:
        client = TaskServiceStub(channel)
        client.AddTask(Task(
            id=task.id,
            description=task.description,
            course_id=task.course_id,
            login=task.login,
            score=task.score)
        )


def get_task(id: int, course_id: int, login: str) -> model.Task:
    """Get task by id"""
    with grpc.insecure_channel('localhost:4044') as channel:
        client = TaskServiceStub(channel)
        task = client.GetTask(GetTaskArg(id=id, course_id=course_id, login=login))
        return get_task_from_proto(task)


def get_all_tasks(course_id: int, login: str) -> typing.List[model.Task]:
    """Get all tasks for user and course"""
    with grpc.insecure_channel('localhost:4044') as channel:
        client = TaskServiceStub(channel)
        tasks = client.GetAllTasks(GetAllTasksArg(course_id=course_id, login=login))
        return [get_task_from_proto(task) for task in tasks.items]
