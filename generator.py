import json
import random

cars = ["Toyota Camry", "Kia Rio", "Hyundai Solaris", "Skoda Octavia", "VW Polo"]
users = ["Ivanov Ivan", "Petrova Anna", "Sidorov Dmitry", "Kozlova Maria", "Novikov Petr"]
zones = ["Zone A", "Zone B", "Zone C", "Zone D"]
tariffs = ["per_minute", "per_km"]
conditions = ["excellent", "good", "fair"]

def generate_message():
    invalid = random.random() < 0.3  # 30% chance of invalid message

    tariff = random.choice(tariffs)
    duration_min = random.randint(5, 120)
    distance_km = round(random.uniform(1.0, 50.0), 1)

    message = {
        "car": random.choice(cars),
        "user": random.choice(users),
        "pickup_zone": random.choice(zones),
        "dropoff_zone": random.choice(zones),
        "tariff": tariff,
        "duration_min": duration_min,
        "distance_km": distance_km,
        "fare": round(random.uniform(-500, 0), 2) if invalid else round(
            duration_min * 4.5 if tariff == "per_minute" else distance_km * 25, 2
        ),
        "car_condition": random.choice(conditions)
    }

    return json.dumps(message)
