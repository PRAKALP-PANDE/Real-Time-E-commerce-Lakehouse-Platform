from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import sys

sys.path.append("/opt/airflow/project")

from producer.generate_orders import generate_orders
from consumer.order_consumer import consume_orders


with DAG(
    dag_id="first_pipeline",
    start_date=datetime(2026, 7, 1),
    schedule=None,
    catchup=False,
    tags=["learning", "project2"],
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    generate_orders_task = BashOperator(
        task_id="generate_orders",
        bash_command="cd /opt/airflow/project && python producer/generate_orders.py"
    )

    consume_orders_task = BashOperator(
        task_id="consume_orders",
        bash_command="python /opt/airflow/project/consumer/order_consumer.py"
    )

    finish = EmptyOperator(
        task_id="finish"
    )

    start >> generate_orders_task >> consume_orders_task >> finish