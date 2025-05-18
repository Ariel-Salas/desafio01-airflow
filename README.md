













Para correr los test se deben ejecutar en bash el sgte comando: 

docker-compose exec airflow-scheduler bash
pytest tests/


para cambair el motor de kernel para el EDA.ipynb:
1) Tener la extensión instalada de Dev Containers
1) Presionar f1 en VSC
2) copiar y pegar: Remote-Containers: Attach to Running Container
3) Elegir el KERNEL ya creado: EDA Kernel


<!-- export PYTHONPATH=/opt/airflow -->
