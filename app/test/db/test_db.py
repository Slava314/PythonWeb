from app.models import model

test_db = {
    "users": [
        model.User(login="dev", password="adminPassword1", user_id=1, courses=[1])
    ],
    "courses": [
        model.Course(name="Python web", course_id=1, description="good"),
        model.Course(name="Haskell", course_id=2, description="\\x -> x * x"),
    ],
    "ids": {"users": 1, "courses": 2},
}
