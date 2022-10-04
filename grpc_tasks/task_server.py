from concurrent.futures import ThreadPoolExecutor

import grpc

import db as db
from builds.service_pb2 import Null, Task, TaskList
from builds.service_pb2_grpc import (
    TaskServiceServicer as ServiceServicer,
    add_TaskServiceServicer_to_server as add_to_server)
import model as model


def get_proto_task(task: model.Task) -> Task:
    """Make proto.Task from model.Task"""
    return Task(id=task.id,
                description=task.description,
                course_id=task.course_id,
                login=task.login,
                score=task.score)


class Service(ServiceServicer):

    def AddTask(self, request, context):
        db.add_task(request.description,
                    request.course_id,
                    request.login,
                    request.score)
        return Null()

    def GetTask(self, request, context):
        task = db.get_task(request.id, request.course_id, request.login)
        if task:
            task_proto = get_proto_task(task)
            return task_proto
        else:
            return Null()

    def GetAllTasks(self, request, context):
        tasks = db.get_filtered_tasks(request.course_id, request.login)
        task_list = TaskList()
        for task in tasks:
            task_proto = task_list.items.add()
            task_proto.id = task.id
            task_proto.description = task.description,
            task_proto.course_id = task.course_id,
            task_proto.login = task.login,
            task_proto.score = task.score
        return task_list


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_to_server(Service(), server)
    server.add_insecure_port("[::]:4044")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
