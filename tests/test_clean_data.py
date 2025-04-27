import pandas as pd
from scripts.clean_data import clean_sales_to_float

def test_clean_sales_to_float_valid_string():
    assert clean_sales_to_float('$1,234.56') == 1234.56

def test_clean_sales_to_float_invalid_string():
    assert clean_sales_to_float('abc') == 0.0

def test_clean_sales_to_float_none():
    assert clean_sales_to_float(None) == 0.0

def test_clean_sales_to_float_float():
    assert clean_sales_to_float(123.45) == 123.45
