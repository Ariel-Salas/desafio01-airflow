#script/clean_data.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))  # Asegura acceso a utils

from utils.parsers import parse_to_float
from utils.cleaning_helpers import drop_columns
from utils.parse_date_columns import parse_date_columns
from utils.parsers_without_negative import parse_without_negative
from utils.parsers_quantity import parse_quantity
from utils.raiting_parser import clean_rating_column


import pandas as pd
import logging

logger = logging.getLogger(__name__)

# Limpia una columna específica convirtiendo sus valores a float
def clean_column(df, column_name):
    if column_name not in df.columns:
        raise ValueError(f"❌ La columna '{column_name}' no existe en el DataFrame")

    def safe_parse(value):
        try:
            return parse_to_float(value)
        except Exception as e:
            logger.error(f"❌ Error en valor '{value}' de columna '{column_name}': {e}")
            raise

    df[column_name] = df[column_name].apply(safe_parse)
    return df


def clean_data(output_path='/tmp/cleaned.csv', **kwargs):
    ti = kwargs['ti']
    extracted_file_path = ti.xcom_pull(task_ids='extract_csv')

    if not os.path.exists(extracted_file_path):
        raise FileNotFoundError(f"❌ No se encontró el archivo extraído en {extracted_file_path}")

    logger.info(f"📥 Leyendo archivo CSV: {extracted_file_path}")
    df = pd.read_csv(extracted_file_path)

    # ✅ Limpiar columna 'Discount' si existe
    if 'Discount' in df.columns:
        logger.info("🧼 Limpiando columna: Discount")
        try:
            df['Discount'] = df['Discount'].apply(parse_without_negative)
        except Exception as e:
            logger.error(f"❌ Error al limpiar columna 'Discount': {e}")
            raise
    else:
        logger.warning("⚠️ La columna 'Discount' no se encontró en los datos originales")



    # ✅ Limpiar columna 'Quantity' si existe
    if 'Quantity' in df.columns:
        logger.info("🧼 Limpiando columna: Quantity")
        try:
            df['Quantity'] = df['Quantity'].apply(parse_quantity)
        except Exception as e:
            logger.error(f"❌ Error al limpiar columna 'Quantity': {e}")
            raise
    else:
        logger.warning("⚠️ La columna 'Quantity' no se encontró en los datos originales")




    # ✅ Limpiar columna 'Rating' si existe
    if 'Rating' in df.columns:
        logger.info("🧼 Limpiando columna: Rating")
        try:
            df = clean_rating_column(df, column_name='Rating')
        except Exception as e:
            logger.error(f"❌ Error al limpiar columna 'Rating': {e}")
            raise
    else:
        logger.warning("⚠️ La columna 'Rating' no se encontró en los datos originales")


    # ✅ Limpiar las columnas 'Sales' y 'Profit' si existen
    for col in ['Sales', 'Profit']:
        if col in df.columns:
            logger.info(f"🧼 Limpiando columna: {col}")
            df = clean_column(df, col)
        else:
            logger.warning(f"⚠️ La columna '{col}' no se encontró en los datos originales")


    # ✅ Limpiar columnas de fechas
    date_columns = ['Order Date', 'Ship Date']
    date_columns_present = [col for col in date_columns if col in df.columns]
    if date_columns_present:
        logger.info(f"📅 Convirtiendo columnas de fecha: {date_columns_present}")
        df = parse_date_columns(df, date_columns_present, date_format='%d-%m-%Y')


    # ✅ Eliminamos columnas innecesarias
    df = drop_columns(df, ['Transaction'])

    logger.info(f"📊 {len(df)} filas procesadas en la limpieza")
    df.to_csv(output_path, index=False)
    logger.info(f"✅ Datos limpios guardados en {output_path}")

    return output_path

