# scripts/clean_data.py
# scripts/clean_data.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))  # Asegura acceso a utils

from utils.parsers import parse_to_float

import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_column(df, column_name):
    if column_name not in df.columns:
        raise ValueError(f"❌ La columna '{column_name}' no existe en el DataFrame")

    def safe_parse(value):
        try:
            return parse_to_float(value)
        except Exception as e:
            logger.error(f"❌ Error en valor '{value}' de columna '{column_name}': {e}")
            raise

    try:
        df[column_name] = df[column_name].apply(safe_parse)
    except Exception as e:
        logger.error(f"❌ Error al limpiar columna '{column_name}': {e}")
        raise
    return df

def clean_data(column_name='Sales', output_path='/tmp/cleaned.csv', **kwargs):
    ti = kwargs['ti']
    extracted_file_path = ti.xcom_pull(task_ids='extract_csv')

    if not os.path.exists(extracted_file_path):
        raise FileNotFoundError(f"❌ No se encontró el archivo extraído en {extracted_file_path}")

    logger.info(f"📥 Leyendo archivo CSV: {extracted_file_path}")
    df = pd.read_csv(extracted_file_path)

    logger.info(f"🧼 Limpiando columna: {column_name}")
    df = clean_column(df, column_name)

    logger.info(f"📊 {len(df)} filas procesadas en la limpieza")
    df.to_csv(output_path, index=False)
    logger.info(f"✅ Datos limpios guardados en {output_path}")

    return output_path
