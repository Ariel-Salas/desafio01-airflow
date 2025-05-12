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

def drop_columns(df, columns):
    """
    Elimina columnas específicas si existen en el DataFrame.
    """
    existing = [col for col in columns if col in df.columns]
    if existing:
        logger.info(f"🗑️ Eliminando columnas: {existing}")
        df = df.drop(columns=existing)
    else:
        logger.info("✅ Ninguna de las columnas a eliminar estaba presente.")
    return df
