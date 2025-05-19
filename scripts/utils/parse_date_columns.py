# utils/parsers.py o utils/date_utils.py
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def parse_date_columns(df, date_columns, date_format='%d-%m-%Y'):
    """
    Convierte columnas de fecha de string a datetime.
    Columnas debes estar libre de NaN
    Libre de caracteres no permitidos

    Parámetros:
    - df: pandas.DataFrame
    - date_columns: lista de nombres de columnas a convertir
    - date_format: formato de entrada de la fecha (por defecto: '%d-%m-%Y')

    Retorna:
    - DataFrame con las columnas de fecha convertidas a tipo datetime
    """
    for col in date_columns:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col], format=date_format)
                logger.info(f"📅 Columna '{col}' convertida exitosamente a datetime.")
            except Exception as e:
                logger.error(f"❌ Error al convertir la columna '{col}' a datetime: {e}")
                raise
        else:
            logger.warning(f"⚠️ La columna '{col}' no existe en el DataFrame.")
    return df
