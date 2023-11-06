import requests
from datetime import datetime
from airflow.models import Variable
from airflow.hooks.postgres_hook import PostgresHook

conn_id = Variable.get("conn_name")
RATE_URL_API = Variable.get("RATE_URL_API")
API_KEY = Variable.get("API_KEY")
RATE_BASE = Variable.get("RATE_BASE")
RATE_TARGET = Variable.get("RATE_TARGET")


def get_url():
    api_method = 'live'

    url = RATE_URL_API + api_method
    return requests.get(url, params={'access_key': API_KEY,
                                     'source': RATE_BASE,
                                     'currencies': RATE_TARGET,
                                     'format': 1})


def load_data_psql():
    hook = PostgresHook(postgres_conn_id=conn_id)
    conn = hook.get_conn()
    cursor = conn.cursor()
    try:
        response = get_url()
        data = response.json()
        get_date = datetime.utcfromtimestamp(data["timestamp"]).strftime('%Y-%m-%d %H:%M:%S')
        rate = data["quotes"]["BTCUSD"]
        query = f"""
                INSERT INTO rates (get_date, rate_base, rate_target, rate)
                VALUES ('{get_date}', '{RATE_BASE}', '{RATE_TARGET}', '{rate}');
        """
        cursor.execute(query)
        conn.commit()

        cursor.close()
        conn.close()
    except Exception as error:
        conn.rollback()
        raise Exception(f'Ошибка записи данных: {error}')
