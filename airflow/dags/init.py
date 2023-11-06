from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'start_date': '2023-10-29',
    'owner': 'starasov',
    'tag': '1thw'
}

dag = DAG(
    dag_id='init',
    default_args=default_args,
    schedule='0 10 * * *'
)

# start = DummyOperator(
#     task_id='start'
# )
#
# end = DummyOperator(
#     task_id='end'
# )

set_variables = BashOperator(
    task_id='set_variables',
    bash_command="pwd"
                 "cd /opt/airflow"
                 "pwd",
    #    bash_command=f'airflow variables import /opt/airflow/input/variables.json',
    dag=dag
)

set_variables
# set_connections = BashOperator(
#     task_id='set_connections',
#     bash_command='airflow connections import /opt/airflow/input/connections.json',
#       dag=dag
# )


# def read_var():
#     print("hello_menaasdf")
#
#
# get_rates = PythonOperator(
#     task_id='get_rates',
#     python_callable=read_var,
#     dag=dag
# )
# start >> set_variables >> set_connections >> end
# start >> get_rates >> end
