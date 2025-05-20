# utils/parse_date_columns.py 
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def parse_date_columns(df, date_columns, date_format='%d-%m-%Y'):
    """
    Convierte columnas de fecha de string a datetime.
    
    Verifica que:
    - No existan valores nulos (NaN)
    - Todos los valores sean convertibles al formato de fecha especificado
    - Creado para columnas de fechas

    Parámetros:
    - df: pandas.DataFrame
    - date_columns: lista de nombres de columnas a convertir
    - date_format: formato de entrada de la fecha (por defecto: '%d-%m-%Y')

    Retorna:
    - DataFrame con columnas convertidas a datetime
    """
    for col in date_columns:
        if col not in df.columns:
            logger.warning(f"⚠️ La columna '{col}' no existe en el DataFrame.")
            continue

        # Validación: valores nulos
        if df[col].isnull().any():
            null_count = df[col].isnull().sum()
            error_msg = f"❌ La columna '{col}' contiene {null_count} valores nulos. No se puede convertir a datetime."
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Validación: prueba de conversión antes de aplicar
        try:
            pd.to_datetime(df[col], format=date_format, errors='raise')
        except Exception as e:
            error_msg = f"❌ Error al convertir la columna '{col}' al formato '{date_format}': {e}"
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Conversión real
        df[col] = pd.to_datetime(df[col], format=date_format)
        logger.info(f"📅 Columna '{col}' convertida exitosamente a datetime.")

    return df

