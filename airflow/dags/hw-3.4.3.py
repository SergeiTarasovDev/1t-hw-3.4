from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'start_date': '2023-10-29',
    'owner': 'starasov',
    'tag': '1thw'
}

dag = DAG(
    dag_id='hw-3.4.3',
    default_args=default_args,
    schedule='0 0 * * *'
)

printHello = BashOperator(
    task_id='print_hello',
    bash_command=f'echo "Good morning my diggers"',
    dag=dag
)

printHello
