docker-compose up -d
docker-compose down -v

docker-compose up airflow-init
wsl --shutdown

variables:
from airflow.models import Variable
conn_id = Variable.get("conn_name")
RANDOMUSER_URL_API = Variable.get("RANDOMUSER_URL_API")