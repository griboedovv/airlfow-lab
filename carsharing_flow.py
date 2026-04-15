from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Путь к твоей рабочей папке
WORKING_DIR = "/home/administrator/airflow_sharing"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'carsharing_pipeline',
    default_args=default_args,
    description='Pipeline для Каршеринга: Generator -> Producer -> Consumer',
    schedule='*/5 * * * *', # Запуск каждые 5 минут
    catchup=False,
    tags=['big_data', 'carsharing'],
) as dag:

    # 1. Запуск генерации данных (сущности и состояние)
    generate_data = BashOperator(
        task_id='run_generator',
        bash_command=f'python3 {WORKING_DIR}/generator.py'
    )

    # 2. Отправка данных в Kafka
    produce_to_kafka = BashOperator(
        task_id='run_producer',
        bash_command=f'python3 {WORKING_DIR}/producer.py'
    )

    # 3. Обработка данных (Консьюмер)
    consume_from_kafka = BashOperator(
        task_id='run_consumer',
        bash_command=f'python3 {WORKING_DIR}/consumer.py'
    )

    # Очередность выполнения
    generate_data >> produce_to_kafka >> consume_from_kafka
