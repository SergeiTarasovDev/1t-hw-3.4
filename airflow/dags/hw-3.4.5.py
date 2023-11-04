# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from airflow.operators.bash_operator import BashOperator
# from airflow.operators.dummy_operator import DummyOperator
# import modules.rate as rate
#
# default_args = {
#     'start_date': '2023-10-29',
#     'owner': 'starasov',
#     'tag': '1thw'
# }
#
# dag = DAG(
#     dag_id='hw-3.4.5',
#     default_args=default_args,
#     schedule='*/10 * * * *'
# )
#
# start = DummyOperator(
#     task_id='start'
# )
#
# end = DummyOperator(
#     task_id='end'
# )
#
# set_variables = BashOperator(
#     task_id='set_variables',
#     bash_command='airflow variables import /opt/airflow/input/variables.json'
# )
#
# set_connections = BashOperator(
#     task_id='set_connections',
#     bash_command='airflow connections import /opt/airflow/input/connections.json'
# )
#
#
# def read_var():
#     print("hello_menaasdf")
#
#
# getRates = PythonOperator(
#     task_id='get_rates',
#     python_callable=read_var,
#     dag=dag
# )
#
# start >> set_variables >> set_connections >> getRates >> end
