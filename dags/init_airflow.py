from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'start_date': '2023-11-05',
    'owner': 'starasov'
}

dag = DAG(
    dag_id='airflow_init',
    default_args=default_args,
    schedule_interval='0 0 * * *'
)

start = DummyOperator(
    task_id='start',
    dag=dag
)

end = DummyOperator(
    task_id='end',
    dag=dag
)

set_variables = BashOperator(
    task_id='set_variables',
    bash_command='airflow variables import opt/airflow/input/variables.json',
    dag=dag
)

set_connections = BashOperator(
    task_id='set_connections',
    bash_command='airflow connections import opt/airflow/input/connections.json',
    dag=dag
)

start >> [set_variables, set_connections] >> end
