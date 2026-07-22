from kafka import KafkaConsumer
import json
import os
from pathlib import Path

# Read Kafka bootstrap server from environment variable.
# Defaults to localhost for manual execution.
BOOTSTRAP_SERVER = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "localhost:9092"
)

# Landing directory can also be configured through an environment variable.
# This allows the same code to work both locally and inside Docker.
LANDING_PATH = os.getenv("LANDING_PATH", "landing")


def consume_orders(max_messages=10):

    consumer = KafkaConsumer(
        "orders",
        bootstrap_servers=BOOTSTRAP_SERVER,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )

    landing_dir = Path(LANDING_PATH)
    landing_dir.mkdir(parents=True, exist_ok=True)

    landing_file = landing_dir / "orders.jsonl"

    print("\nWaiting for messages...\n")

    count = 0

    try:
        with open(landing_file, "a", encoding="utf-8") as file:

            for message in consumer:

                order = message.value

                print("Received:", order)

                file.write(json.dumps(order) + "\n")
                file.flush()

                count += 1

                if count >= max_messages:
                    break

        print(f"\nSuccessfully consumed {count} messages.")
        print(f"Landing file: {landing_file}")

    except Exception as e:
        print(f"Error while consuming messages: {e}")
        raise

    finally:
        consumer.close()
        print("Kafka consumer closed.")


if __name__ == "__main__":
    consume_orders()