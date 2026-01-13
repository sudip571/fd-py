# from airflow import DAG
# from airflow.operators.python import PythonOperator
import asyncio
from datetime import datetime, timedelta

from flightdeck_etl.di_container.di import build_container
from flightdeck_etl.modules.sev.contracts.iclient_service import IClientService

default_args = {
    "owner": "Sudip",
    "depends_on_past": False,
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(seconds=45),
}
dag_id = "print_top_client"
task_id = "print_client_tk"


def print_top_client():
    container = build_container()
    provider = container.build_provider()
    with provider.create_scope() as scope:
        service = scope.get(IClientService)
        client = asyncio.run(service.get_top_client())
        if client is None:
            print("No client found")
            return

        print(client)
        print(client.name)
        print(client.website)


with DAG(
    dag_id=dag_id,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
    tags=["Client", "Python", "FlightDeck"],
    description="Print top client from tbl_clients",
) as dag:
    print_client_task = PythonOperator(
        task_id=task_id,
        python_callable=print_top_client,
    )
