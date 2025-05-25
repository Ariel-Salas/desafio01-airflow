# utils/rating_parser.py
import pandas as pd
import re
import logging
from utils.parsers import parse_to_float

logger = logging.getLogger(__name__)

def clean_rating_column(df, column_name='Rating'):
    """
    Limpia y convierte la columna 'Rating' a float:
    - Elimina NaNs y valores con '|'
    - Elimina caracteres no numéricos
    - Convierte a float con parseo seguro
    - Elimina filas donde no se pudo convertir

    Retorna:
    - df limpio
    """
    if column_name not in df.columns:
        logger.warning(f"⚠️ La columna '{column_name}' no existe.")
        return df

    # Eliminar filas con NaN o símbolo |
    initial_count = df.shape[0]
    df = df[~df[column_name].isna()]
    df = df[~df[column_name].astype(str).str.contains(r'\|')]
    after_filter_count = df.shape[0]
    logger.info(f"🧽 Filas eliminadas por NaN o '|': {initial_count - after_filter_count}")

    # Eliminar caracteres no válidos para float (conservar dígitos, punto decimal y signo)
    def sanitize_value(val):
        val_str = str(val)
        val_cleaned = re.sub(r'[^\d\.\-]', '', val_str)
        return val_cleaned

    df[column_name] = df[column_name].apply(sanitize_value)

    # Intentar parsear a float
    def safe_parse(val):
        try:
            return parse_to_float(val)
        except Exception as e:
            logger.warning(f"⚠️ No se pudo convertir '{val}' a float: {e}")
            return None

    df[column_name] = df[column_name].apply(safe_parse)

    # Eliminar conversiones fallidas
    before_final = df.shape[0]
    df = df[~df[column_name].isna()]
    logger.info(f"✅ 'Rating' limpio. Filas eliminadas por conversion fallida: {before_final - df.shape[0]}")
    return df
