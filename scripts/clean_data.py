
# scripts/clean_data.py
import pandas as pd
import re
import logging
from typing import Union, Dict, Any
from pandas import DataFrame

logger = logging.getLogger(__name__)
_non_numeric_re = re.compile(r'[^\d.,-]+')

def clean_sales_to_float(value: Union[str, int, float, None]) -> float:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return 0.0  # Si quieres que sea cero en lugar de vacío

    if isinstance(value, (int, float)):
        return float(value)
    
    if isinstance(value, str):
        value_cleaned = re.sub(r'[^\d.,-]', '', value)
        value_cleaned = value_cleaned.replace(',', '')  # eliminar comas de miles
        try:
            return float(value_cleaned)
        except ValueError:
            return 0.0  # si no se puede convertir, lo ponemos en 0

    return 0.0  # en cualquier otro caso, valor por defecto

def clean_data(**kwargs) -> DataFrame:
    """
    Función principal para limpiar los datos.
    Recibe el contexto de Airflow para manejar XComs.
    """
    try:
        # Obtener el DataFrame del XCom del task anterior
        ti = kwargs['ti']
        df = ti.xcom_pull(task_ids='extract_csv')
        
        # Verificar que sea un DataFrame
        if not isinstance(df, pd.DataFrame):
            raise ValueError("El dato recibido no es un DataFrame de Pandas")
            
        # Limpieza de la columna Sales
        df['Sales'] = df['Sales'].apply(clean_sales_to_float)
        
        # Verificación y logging
        logger.info(f"✅ Datos limpios. Tipo de Sales: {df['Sales'].dtype}")
        logger.info(f"Valores nulos en Sales: {df['Sales'].isna().sum()}")
        
        negativos = df[df['Sales'] < 0]
        if not negativos.empty:
            logger.warning(f"⚠️ Valores negativos detectados en 'Sales': {len(negativos)}")
        else:
            logger.info("✅ No se encontraron valores negativos en 'Sales'")
            
        return df
        
    except Exception as e:
        logger.error(f"❌ Error al limpiar los datos: {e}")
        raise 