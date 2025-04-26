# dags/etl_pipeline.py

# dags/etl_pipeline.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/scripts')

from extract import extract_csv
from clean_data import clean_data
from load import load_data  # Asumo que tendrás un load.py





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

    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
        provide_context=True,  # ← Permite pasar el contexto (kwargs)
    )

    load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    provide_context=True,  # Habilita el paso del contexto (kwargs)
    op_kwargs={
        'output_dir': 'data/output',
        'output_file': 'superstore_clean.csv'
    }
)
    extract_task >> clean_task >> load_task
