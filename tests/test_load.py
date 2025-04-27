import os
import shutil
import pytest
from scripts.load import load_data

@pytest.fixture
def setup_clean_file(tmp_path):
    # Crear CSV limpio falso
    clean_dir = tmp_path / "clean"
    clean_dir.mkdir()
    clean_file = clean_dir / "superstore_clean.csv"
    clean_file.write_text("Sales\n100\n200\n")
    return str(clean_file)

def test_load_data(monkeypatch, setup_clean_file, tmp_path):
    # Simular XCom pull
    monkeypatch.setitem(
        __import__('builtins').__dict__,
        'ti', type('obj', (object,), {'xcom_pull': lambda self, task_ids: setup_clean_file})()
    )

    # Crear kwargs que espera load_data
    kwargs = {'ti': ti}

    load_data(**kwargs)

    output_path = os.path.join('data', 'output', 'superstore_clean.csv')
    assert os.path.exists(output_path)

    # Limpiar después de prueba
    shutil.rmtree('data/output', ignore_errors=True)
