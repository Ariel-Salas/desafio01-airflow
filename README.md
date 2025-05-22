
# 🌀 Proyecto de Orquestación de Workflows con Apache Airflow y Análisis Exploratorio de Datos

Este proyecto implementa un pipeline de datos automatizado usando **Apache Airflow** dentro de un entorno **Dockerizado**. Además, integra un análisis exploratorio de datos (EDA) en **Jupyter Notebook**, utilizando librerías como `pandas`, `seaborn`, entre otras.

Es ideal para demostrar habilidades en orquestación de workflows, procesamiento de datos y análisis exploratorio con Python.

---

## 📦 Tecnologías y Versiones

| Herramienta         | Versión               | Notas                                               |
|---------------------|------------------------|------------------------------------------------------|
| Docker              | 28.0.1                 | Requiere instalación previa en el sistema host       |
| Docker Compose      | v2.33.1-desktop.1      |                                                     |
| Apache Airflow      | 2.10.5                 | Imagen base: `apache/airflow:2.10.5`                 |
| Python (host)       | 3.13.2                 | Versión de Python en la máquina local                |
| Python (contenedor) | 3.12.9                 | Versión utilizada dentro del contenedor de Airflow   |
| Jupyter Notebook    | vía Dev Containers     | Utilizado para el análisis exploratorio              |

### 📚 Librerías principales para EDA

- `pandas==2.2.3`
- `numpy==2.2.3`
- `matplotlib==3.10.1`
- `seaborn==0.13.2`
- `plotly==6.0.0`
- `scikit-learn==1.6.1`

---

## 📁 Estructura del Proyecto


desafio01-airflow/
│
├── dags/                          # DAGs de Airflow
│   └── ejemplo_dag.py             # DAG de ejemplo
│
├── tests/                         # Pruebas con Pytest
│   └── test_dag_validacion.py     # Validación de DAGs
│
├── notebooks/                     # Notebooks para análisis EDA
│   └── EDA.ipynb
│
├── docker-compose.yml             # Orquestación de servicios con Docker
├── .env                           # Variables de entorno (si aplica)
├── requirements.txt               # Librerías del entorno local (opcional)
└── README.md                      # Documentación del proyecto




🚀 Instalación y Uso

1. Clonar el repositorio

    git clone https://github.com/Ariel-Salas/desafio01-airflow.git
    cd desafio01-airflow

2. Levantar los contenedores
    
    docker-compose up -d




3. Verificar que Airflow está corriendo

    Accede a la interfaz web de Airflow:
    http://localhost:8080
    Usuario: admin
    Contraseña: admin



🧪 Ejecutar Pruebas
    Para ejecutar los tests desde dentro del contenedor airflow-scheduler:

    docker-compose exec airflow-scheduler bash
    pytest tests/



🧠  Cambiar el kernel del notebook EDA.ipynb
   
   1. Instalar la extensión Dev Containers en Visual Studio Code

   2. Presionar F1 → seleccionar Remote-Containers: Attach to Running Container

   3. Seleccionar Jupiter

   3. Elegir el contenedor con el kernel para notebooks (EDA Kernel)


 📄 Documentación Adicional

    Este proyecto se acompaña de un documento que explica cómo se resolvió el desafío, con capturas y explicación técnica.

    📎 Instrucciones detalladas en este link documento (Word/PDF)

🧑‍💻Autor
    Nombre: Ariel Salas Díaz
    Email: [arielsd12@gmail.com]


    Estado del proyecto
✅ Finalizado – listo para revisión y despliegue.
