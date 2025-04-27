import os
import pytest
import pandas as pd
from scripts.extract import extract_csv

@pytest.fixture
def setup_data(tmp_path):
    # Crear un CSV ficticio para prueba
    data = {'Sales': [100, 200, 300]}
    df = pd.DataFrame(data)
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    file_path = data_dir / "Superstore01.csv"
    df.to_csv(file_path, index=False)
    return str(file_path.parent)

def test_extract_csv(setup_data, tmp_path):
    tmp_dir = tmp_path
    output_file = extract_csv(file_name='Superstore01.csv', data_dir=setup_data, tmp_dir=str(tmp_dir))

    assert os.path.exists(output_file)
    df = pd.read_csv(output_file)
    assert 'Sales' in df.columns
