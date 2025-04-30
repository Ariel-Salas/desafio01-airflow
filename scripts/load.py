# scripts/load.py
import os
import shutil
import logging

logger = logging.getLogger(__name__)

def load_data(**kwargs):
    """
    Mueve el CSV limpio al directorio final de salida.
    """
    ti = kwargs['ti']
    clean_file_path = ti.xcom_pull(task_ids='clean_data')

    if not os.path.exists(clean_file_path):
        raise FileNotFoundError(f"No se encontró el archivo limpio en {clean_file_path}")

    output_dir = 'data/output'
    output_file = 'superstore_clean.csv'
    os.makedirs(output_dir, exist_ok=True)

    final_output_path = os.path.join(output_dir, output_file)

    # 👉 Advertir si se sobrescribe archivo
    if os.path.exists(final_output_path):
        logger.warning(f"⚠️ El archivo de salida ya existía y fue sobrescrito: {final_output_path}")

    shutil.copy(clean_file_path, final_output_path)

    logger.info(f"✅ Archivo final guardado en {final_output_path}")


