from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pendulum

from src.main import main

default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="opensky_pipeline",
    start_date=pendulum.datetime(2026, 1, 17, tz="UTC"),
    schedule_interval="@hourly",
    catchup=False,
    default_args=default_args,
    tags=["opensky", "api", "etl"],
) as dag:

    run_pipeline = PythonOperator(
        task_id="run_opensky_pipeline",
        python_callable=main,
    )

    run_pipeline
