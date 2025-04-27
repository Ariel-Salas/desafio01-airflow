# scripts/clean_data.py
import pandas as pd
import re
import os
import logging

logger = logging.getLogger(__name__)
_non_numeric_re = re.compile(r'[^\d.,-]+')

def clean_sales_to_float(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        value_cleaned = re.sub(r'[^\d.,-]', '', value).replace(',', '')
        try:
            return float(value_cleaned)
        except ValueError:
            return 0.0
    return 0.0

def clean_data(**kwargs):
    """
    Limpia los datos de ventas en el CSV extraído.
    """
    ti = kwargs['ti']
    extracted_file_path = ti.xcom_pull(task_ids='extract_csv')

    if not os.path.exists(extracted_file_path):
        raise FileNotFoundError(f"No se encontró el archivo extraído en {extracted_file_path}")

    df = pd.read_csv(extracted_file_path)

    df['Sales'] = df['Sales'].apply(clean_sales_to_float)

    output_clean_path = '/tmp/superstore_clean.csv'
    df.to_csv(output_clean_path, index=False)
    logger.info(f"✅ Datos limpios guardados en {output_clean_path}")

    return output_clean_path
