from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
import modules.rate as rate

default_args = {
    'start_date': '2023-10-29',
    'owner': 'starasov',
    'tag': '1thw'
}

dag = DAG(
    dag_id='hw-3.4.5',
    default_args=default_args,
    schedule='*/10 * * * *'
)

start = DummyOperator(
    task_id='start'
)

end = DummyOperator(
    task_id='end'
)

def read_var():
    print("hello_menaasdf")

getRates = PythonOperator(
    task_id='get_rates',
    python_callable=read_var,
    dag=dag
)
#
# createDatamart = PythonOperator(
#     task_id='create_datamart',
#     python_callable=rate.create_datamart,
#     dag=dag
# )
# >> createDatamart >>
start >> getRates >> end
