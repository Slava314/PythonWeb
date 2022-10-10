from typing import List, Optional

import model

db = {
    "tasks": [],
    "ids": {"tasks": 0},
}


def get_all_tasks() -> List[model.Task]:
    """Get all tasks from db"""
    return db["tasks"]


def get_filtered_tasks(course_id: int, login: str) -> List[model.Task]:
    """Get all tasks for user with 'login' and for course with 'course_id' from db"""
    return list(filter(lambda task: task.course_id == course_id and
                                    task.login == login,
                       db["tasks"]))


def add_task(description: str, course_id: int, login: str, score: int) -> model.Task:
    """Add new task to db"""
    task_id = db["ids"]["tasks"]
    task_id += 1
    db["ids"]["tasks"] = task_id
    new_task = model.Task(id=task_id,
                          description=description,
                          course_id=course_id,
                          login=login,
                          score=score)
    get_all_tasks().append(new_task)
    return new_task


def get_task(id: int, course_id: int, login: str) -> Optional[model.Task]:
    """Get task by id from db"""
    all_tasks = get_filtered_tasks(course_id, login)
    for t in all_tasks:
        if t.id == id:
            return t
    return None
