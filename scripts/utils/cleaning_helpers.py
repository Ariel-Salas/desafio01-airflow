# utils/cleaning_helpers.py

import logging

logger = logging.getLogger(__name__)

def drop_duplicate_columns(df):
    """
    Elimina columnas duplicadas basadas en su contenido.
    """
    duplicated = df.T.duplicated()
    if duplicated.any():
        dup_cols = df.columns[duplicated].tolist()
        logger.info(f"🧹 Eliminando columnas duplicadas: {dup_cols}")
        df = df.loc[:, ~duplicated]
    else:
        logger.info("✅ No se encontraron columnas duplicadas.")
    return df
