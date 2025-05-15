FROM apache/airflow:2.10.5

# Copia el archivo de requerimientos a la imagen
COPY requirements.txt /requirements.txt

# Instala los paquetes y primero actualiza pip
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt

# Nombre de kernel personalizado para Jupyter
# RUN python -m ipykernel install --user --name eda-kernel --display-name "EDA Kernel"    