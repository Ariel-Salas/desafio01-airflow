# scripts/load.py
import pandas as pd
import os
import logging
from typing import Union, Dict, Any

logger = logging.getLogger(__name__)

def load_data(**kwargs) -> None:
    """
    Guarda el DataFrame limpio como nuevo CSV.
    Recibe el contexto de Airflow para manejar XComs.
    """
    try:
        # Obtener el DataFrame del task anterior
        ti = kwargs['ti']
        df = ti.xcom_pull(task_ids='clean_data')
        
        # Verificar que sea un DataFrame
        if not isinstance(df, pd.DataFrame):
            raise ValueError(f"Se esperaba DataFrame, se recibió: {type(df)}")
        
        # Configuración de salida
        output_dir = kwargs.get('output_dir', 'data/output')
        output_file = kwargs.get('output_file', 'superstore_clean.csv')
        output_path = os.path.join(output_dir, output_file)
        
        # Crear directorio si no existe
        os.makedirs(output_dir, exist_ok=True)
        
        # Guardar el CSV
        df.to_csv(output_path, index=False)
        
        logger.info(f"✅ Datos guardados en: {output_path}")
        logger.info(f"📊 Resumen: {df.shape[0]} filas y {df.shape[1]} columnas")
        
    except Exception as e:
        logger.error(f"❌ Error al guardar el archivo: {e}")
        raise