from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

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

    validate_environment = EmptyOperator(
        task_id="validate_environment"
    )

    finish = EmptyOperator(
        task_id="finish"
    )

    start >> validate_environment >> finish