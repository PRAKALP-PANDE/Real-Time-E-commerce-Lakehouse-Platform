from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

'''Kafka cannot directly send a Python dictionary. It must first be converted into bytes.

That's what value_serializer does.'''

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:

    order = {
        "order_id": random.randint(1000, 9999),
        "customer_id": random.randint(1, 100),
        "product_id": random.randint(1, 50),
        "quantity": random.randint(1, 5),
        "amount": round(random.uniform(100, 5000), 2),
        "timestamp": datetime.now().isoformat()
    }

    producer.send("orders", order)

    print("Sent:", order)

    time.sleep(2)