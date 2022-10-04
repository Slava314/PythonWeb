import model

test_db = {
    "tasks": [
        model.Task(id=1, description="grpc", course_id=1, login="dev", score=10)
    ],
    "ids": {"tasks": 1},
}