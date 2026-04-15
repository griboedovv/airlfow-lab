import json
import random

tutors = ["Ivan", "Anna", "Dmitry"]
students = ["Olga", "Petr", "Maria"]
subjects = ["Math", "Physics", "English", "Programming"]

def generate_message():
    invalid = random.random() < 0.3  # 30% chance of invalid message

    message = {
        "tutor": random.choice(tutors),
        "student": random.choice(students),
        "subject": random.choice(subjects),
        "price": random.choice([-500, 0]) if invalid else random.randint(10, 50),
        "rating": round(random.uniform(5.5, 7.0), 1) if invalid else round(random.uniform(3, 5), 1)
    }

    return json.dumps(message)