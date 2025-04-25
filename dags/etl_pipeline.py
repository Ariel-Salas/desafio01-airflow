# dags/etl_pipeline.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

# ✅ Ruta absoluta en el contenedor
sys.path.append('/opt/airflow/scripts')

from extract import extract_csv

with DAG(
    dag_id='etl_csv_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['etl', 'csv'],
) as dag:

    extract_task = PythonOperator(
        task_id='extract_csv',
        python_callable=extract_csv,
    )

