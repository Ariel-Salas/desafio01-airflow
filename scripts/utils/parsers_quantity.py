import re
import logging

logger = logging.getLogger(__name__)

# Regex para eliminar todo lo que NO sea número, punto o coma decimal
_non_numeric_quantity_re = re.compile(r'[^0-9.,-]+')

# Contador global para rastrear valores corregidos
quantity_negative_count = 0
quantity_decimal_count = 0

def parse_quantity(value):
    """
    Limpia y convierte valores de la columna Quantity:
    - Convierte a entero (truncando decimales)
    - Elimina caracteres no numéricos
    - Convierte negativos en positivos y los cuenta
    - Convierte strings con coma decimal
    - Lanza error si no puede interpretarse como número

    Retorna:
    - int (positivo)

    Ejemplos:
    parse_quantity('3.5')    -> 3  (⚠️ decimal truncado)
    parse_quantity('-2,5')   -> 2  (⚠️ negativo y decimal corregido)
    parse_quantity('abc')    -> ❌ error
    parse_quantity(4.0)      -> 4
    """
    global quantity_negative_count, quantity_decimal_count

    if value is None:
        raise ValueError("❌ Valor nulo encontrado")

    if isinstance(value, (int, float)):
        original = value
        if original < 0:
            quantity_negative_count += 1
            logger.warning(f"⚠️ Valor negativo detectado: {original} -> convertido a positivo")
        if isinstance(original, float) and not original.is_integer():
            quantity_decimal_count += 1
            logger.warning(f"⚠️ Valor decimal detectado: {original} -> truncado a entero")
        return abs(int(original))  # Truncar decimales y convertir a positivo

    elif isinstance(value, str):
        if '-' in value:
            quantity_negative_count += 1
            logger.warning(f"⚠️ Valor negativo detectado: '{value}' -> convertido a positivo")

        cleaned = _non_numeric_quantity_re.sub('', value)
        if cleaned == '':
            raise ValueError(f"❌ Valor vacío después de limpieza: '{value}'")

        cleaned = cleaned.replace(',', '.')

        try:
            float_val = abs(float(cleaned))
            if not float_val.is_integer():
                quantity_decimal_count += 1
                logger.warning(f"⚠️ Valor decimal detectado: '{value}' -> truncado a entero")
            return int(float_val)  # Truncar el decimal
        except ValueError:
            logger.error(f"❌ No se pudo convertir '{value}' a número. Resultado: '{cleaned}'")
            raise ValueError(f"No se pudo convertir a número: '{value}'")
    else:
        raise TypeError(f"❌ Tipo de dato no soportado: {type(value)}")
