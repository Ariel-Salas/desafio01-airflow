# scripts/extract.py
import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

def extract_csv(file_name: str = 'Superstore01.csv', data_dir: str = 'data', tmp_dir: str = '/tmp') -> str:
    """
    Extrae datos de un CSV y guarda una copia en /tmp para procesamiento posterior.
    Retorna la ruta del archivo extraído.
    """
    file_path = os.path.join(data_dir, file_name)
    tmp_path = os.path.join(tmp_dir, 'superstore_raw.csv')

    # Validar si el archivo de entrada existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ El archivo de entrada no existe en: {file_path}")

    try:
        df = pd.read_csv(file_path)
        os.makedirs(tmp_dir, exist_ok=True)
        df.to_csv(tmp_path, index=False)
        logger.info(f"✅ Datos extraídos y guardados temporalmentes en {tmp_path}.")
        return tmp_path

    except Exception as e:
        logger.error(f"❌ Error extrayendo CSV: {e}")
        raise
