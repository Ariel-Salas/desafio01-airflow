# dags/etl_pipeline.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append('/opt/airflow/scripts')

from extract import extract_csv
from clean_data import clean_data
from load import load_data

with DAG(
    dag_id='etl_csv_pipeline_v2',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['etl', 'csv'],
    description="ETL para limpiar y guardar datos de ventas desde CSV."
) as dag:

    extract_task = PythonOperator(
        task_id='extract_csv',
        python_callable=extract_csv,
    )

    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    extract_task >> clean_task >> load_task
