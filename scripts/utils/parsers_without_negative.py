#utils/parsers_with_negative
import re
import logging

logger = logging.getLogger(__name__)

# Regex para eliminar todo lo que NO sea número, punto o coma decimal
_non_numeric_discount_re = re.compile(r'[^0-9.,]+')

# Contador global de negativos detectados
negative_count = 0

def parse_without_negative(value):
    """
    Convierte un valor a float para, por ejemplo, descuentos, asegurando:
    - Convierte negativos en positivos y los cuenta
    - Sólo valores entre 0.0 y 1.0 (inclusive)
    - Reemplaza coma decimal por punto (por ejemplo, 0,6 → 0.6)
    - Limpia caracteres no numéricos (excepto punto o coma)
    - Lanza error si el valor no cumple condiciones

    Parámetros:
    - value: valor a convertir (str, int, float)

    Retorna:
    - float entre 0.0 y 1.0

    Ejemplo de uso:
    parse_without_negative('0.2')     -> 0.2
    parse_without_negative('-0.3')    -> 0.3 (⚠️ negativo corregido)
    parse_without_negative('0,6%')    -> 0.6
    parse_without_negative('-0,8%')   -> 0.8 (⚠️ negativo corregido)
    parse_without_negative('abc')     -> ❌ error
    parse_without_negative('2.5')     -> ❌ error (fuera de rango)
    """
    global negative_count

    if value is None:
        raise ValueError("❌ Valor nulo encontrado")

    if isinstance(value, (int, float)):
        original = float(value)
        val_float = abs(original)  # Convertir a positivo
        if original < 0:
            negative_count += 1
            logger.warning(f"⚠️ Valor negativo detectado: {original} -> convertido a positivo")
    elif isinstance(value, str):
        if '-' in value:
            negative_count += 1
            logger.warning(f"⚠️ Valor negativo detectado: '{value}' -> convertido a positivo")

        # Eliminar todo excepto números, punto o coma
        cleaned = _non_numeric_discount_re.sub('', value)

        if cleaned == '':
            raise ValueError(f"❌ Valor vacío después de limpieza: '{value}'")

        # Reemplazar coma por punto
        cleaned = cleaned.replace(',', '.')

        try:
            val_float = abs(float(cleaned))
        except ValueError:
            logger.error(f"❌ No se pudo convertir '{value}' a float luego de limpieza. Resultado: '{cleaned}'")
            raise ValueError(f"No se pudo convertir a float: '{value}'")
    else:
        raise TypeError(f"❌ Tipo de dato no soportado: {type(value)}")

    # Validar rango
    if val_float > 1.0:
        raise ValueError(f"❌ Valor fuera del rango esperado [0.0, 1.0]: {val_float}")

    return val_float

