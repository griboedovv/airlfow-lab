from kafka import KafkaProducer
import time
from generator import generate_message

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: v.encode("utf-8")
)

topic = "carsharing"

while True:
    message = generate_message()

    print("SEND:", message)

    producer.send(topic, message)

    time.sleep(2)
