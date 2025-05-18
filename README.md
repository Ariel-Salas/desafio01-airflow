

Proyecto creado con docker











Para correr los test se deben ejecutar en bash el sgte comando: 

docker-compose exec airflow-scheduler bash
pytest tests/


Para cambair el motor de kernel para el EDA.ipynb:
1) Tener la extensión instalada de Dev Containers
1) Presionar f1 en VSC
2) Copiar y pegar: Remote-Containers: Attach to Running Container
3) Elegir el KERNEL ya creado: EDA Kernel


<!-- export PYTHONPATH=/opt/airflow -->



# 🌀 Proyecto de Orquestación de Workflows con Apache Airflow y Análisis Exploratorio de Datos

Este proyecto utiliza **Apache Airflow** como motor de orquestación de workflows dentro de un entorno **Dockerizado**, facilitando la automatización de pipelines de datos. Además, incluye un entorno de desarrollo con Jupyter Notebook para realizar análisis exploratorio de datos (**EDA**) utilizando librerías de Python.

---

## 📦 Tecnologías y Versiones

| Herramienta     | Versión         | Notas                                               |
|------------------|------------------|------------------------------------------------------|
| Docker           | latest           | Se requiere Docker instalado                        |
| Docker Compose   | latest           |                                                     |
| Apache Airflow   | `2.10.5`         | Desde imagen: `apache/airflow:2.10.5`               |
| Python (host)    | `3.13.2`         | Versión de Python en tu máquina local               |
| Python (contenedor) | ~3.10 (estimado) | Incluido en la imagen de Airflow                   |
| Jupyter Notebook | (via kernel)     | Usado para análisis exploratorio (EDA)              |

### Principales librerías utilizadas en el entorno EDA:

- `pandas==2.2.3`
- `numpy==2.2.3`
- `matplotlib==3.10.1`
- `seaborn==0.13.2`
- `scikit-learn==1.6.1`
- `plotly==6.0.0`

---

## 📁 Estructura del Proyecto


desafio01-airflow/
│
├── dags/                          # DAGs de Airflow
│   └── ejemplo_dag.py             # DAG de ejemplo definido con Python
│
├── tests/                         # Pruebas con Pytest
│   └── test_dag_validacion.py     # Validación de estructura de DAG
│
├── notebooks/                     # Notebooks para EDA
│   └── EDA.ipynb                  # Análisis exploratorio de datos
│
├── docker-compose.yml             # Orquestación de servicios con Docker
├── .env                           # Variables de entorno (si aplica)
├── requirements.txt               # Requisitos opcionales para entorno local (EDA)
└── README.md                      # Documentación del proyect



🚀 Instalación y Uso

1. Clonar el repositorio

    git clone https://github.com/tu-usuario/desafio01-airflow.git
    cd desafio01-airflow

2. Levantar los contenedores
    
    docker-compose up -d




🧑‍💻 Autor
Nombre: Ariel Salas Díaz
Email: [arielsd12@gmail.com]
