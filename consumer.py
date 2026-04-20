from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "carsharing",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: x.decode("utf-8")
)

def validate(message):
    data = json.loads(message)

    if data["fare"] <= 0:
        return False

    if data["distance_km"] < 0:
        return False

    if data["duration_min"] <= 0:
        return False

    return True


for msg in consumer:
    message = msg.value

    if validate(message):
        print("RECEIVED:", message)
    else:
        print("NOT VALID:", message)
