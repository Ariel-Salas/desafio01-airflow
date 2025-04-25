# scripts/extract.py

import pandas as pd
import os
import logging

# Configura el logger de Airflow
logger = logging.getLogger(__name__)

def extract_csv(file_name: str = 'Superstore014.csv', data_dir: str = 'data') -> pd.DataFrame:
    file_path = os.path.join(data_dir, file_name)

    try:
        df = pd.read_csv(file_path)
        logger.info(f"✅ Archivo cargado desde {file_path}, contiene {df.shape[0]} filas y {df.shape[1]} columnas.")
        return df

    except FileNotFoundError:
        logger.error(f"❌ Error: El archivo '{file_path}' no existe. Verifica el nombre o la ruta.")
        raise

    except pd.errors.ParserError:
        logger.error(f"❌ Error al parsear el archivo '{file_path}'. Verifica el formato del CSV.")
        raise

    except Exception as e:
        logger.error(f"❌ Error inesperado al cargar el archivo '{file_path}': {e}")
        raise
