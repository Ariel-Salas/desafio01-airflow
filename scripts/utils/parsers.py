# utils/parsers.py
import re

_non_numeric_re = re.compile(r'[^\d.,-]+')

def parse_to_float(value):
    """
    Convierte un valor numérico representado como string a float.
    La columna debe estar limpia de nulos, si no: 
    Lanza excepciones si el valor es nulo o de tipo no esperado.
    """
    if value is None:
        raise ValueError("❌ Valor nulo encontrado")

    if isinstance(value, (int, float)):
        return float(value)

    if isinstance(value, str):
        value_cleaned = _non_numeric_re.sub('', value).replace(',', '')
        try:
            return float(value_cleaned)
        except ValueError:
            # 👉 Agregado para mayor trazabilidad del valor fallido
            print(f"❌ Error al convertir '{value}' a float.")
            raise ValueError(f"❌ No se pudo convertir a float: '{value}'")

    raise TypeError(f"❌ Tipo de dato no soportado: {type(value)}")


