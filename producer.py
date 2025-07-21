
from kafka import KafkaProducer
from datetime import datetime
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

users = ['John', 'Dude', 'Pyh', 'Vara']

while True:
    event = {
        "user": random.choice(users),
        "amount": random.randint(10, 500),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    producer.send('purchases', value=event)
    print("Produced:", event)
    time.sleep(5)
