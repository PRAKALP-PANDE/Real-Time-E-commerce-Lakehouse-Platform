Step 1

Start Kafka

docker compose up -d

--------------------------------

Step 2

Run Producer

python producer/generate_orders.py

--------------------------------

Step 3

Run Consumer

python consumer/consumer.py

--------------------------------

Step 4

Open Databricks

Run:

01_bronze_ingestion

--------------------------------

Step 5

Run:

02_silver_processing

--------------------------------

Step 6

Run:

03_merge

--------------------------------

Step 7

Run:

04_metrics

--------------------------------

Step 8

Run:

05_gold_summary