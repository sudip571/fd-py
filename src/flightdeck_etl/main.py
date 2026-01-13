import asyncio

from pydantic import BaseModel

from flightdeck_etl.airflow_dag.airflow_helpers import run_service
from flightdeck_etl.di_container.di import build_container
from flightdeck_etl.modules.sev.contracts.iclient_service import IClientService
from flightdeck_etl.shared import ApiClient, Log, json_helpers
from flightdeck_etl.shared.emails.email_service import EmailService
from flightdeck_etl.shared.models.client_model import Client

Log.debug("Something went wrong", error_code=500)





# testing custom json helper
# Create instance
client = Client(
    client_id=1, name="Bruce Clay Australia", website="www.bruceclay.com/au"
)

# Serialize
json_str = json_helpers.serialize(client)
print(json_str)

# Deserialize back to Client
client_obj = json_helpers.deserialize(json_str, Client)
print(client_obj.name)  # Bruce Clay Australia


# testing DI helper method
def print_top_client1():
    client = run_service(IClientService, "get_top_client")
    print(client)
    print(client.name)
    print(client.website)


print_top_client1()


# testing async inside sync with DI
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


print_top_client()


# testing complete async method with DI
async def mainn():
    container = build_container()
    provider = container.build_provider()

    with provider.create_scope() as scope:
        service = scope.get(IClientService)
        client = await service.get_top_client()
        print(client)


if __name__ == "__main__":
    asyncio.run(mainn())


# testing email sending
def run_email_task():
    container = build_container()
    provider = container.build_provider()

    with provider.create_scope() as scope:
        email_service = scope.get(EmailService)
        asyncio.run(
            email_service.send_email(
                user_name="Sudip",
                client_name="Bruce Clay Australia",
                project_name="SEO Campaign",
                email_template_path="templates/welcome.html",
                email_subject="Welcome to FlightDeck",
                user_email="sudip@example.com",
            )
        )


run_email_task()


# testing custom idisposable
# async def mainn():

#     container = build_container()
#     # db = container.resolve(DatabaseConnection)

#     with container.resolve(DatabaseConnection) as db:  # calls __enter__ and __exit__
#         mssql_conn = db.connect_mssql()
#         cursor = mssql_conn.cursor()
#         cursor.execute(
#             "SELECT top 1 client_id,name,website from tbl_clients")
#         row = cursor.fetchone()
#         # print(cursor.fetchone())
#         # Bind to model
#         client = Client(client_id=row[0], name=row[1], website=row[2])
#         print(client)
#         print(client.name)  # "Bruce Clay Australia"
#         print(client.website)


# if __name__ == "__main__":
#     asyncio.run(mainn())


# print(DateTimeProvider.today())
# print(Status.PENDING.name)
# print(Status.PENDING.value)
# print(app_constants.USER_NOT_FOUND)
#

# Logging test
# Log.debug("Something went wrong", error_code=500) # or
# db_logger = configure_logging(logger_name="Database", log_path="./logs/db.log")
# db_logger.info("Connected to MSSQL", server="SQLAUAWSFDB01DV")


# enable or disable ruff warning per line or per method or whole file use # ruff: noqa  and # ruff: enable


# testing api request


# class PostResponse(BaseModel):
#     userId: int
#     id: int
#     title: str
#     body: str


# async def maink():
#     api = ApiClient(base_url="https://jsonplaceholder.typicode.com")

#     post = await api.get(
#         endpoint="/posts/1", params=None, headers=None, response_model=PostResponse
#     )

#     print("Post ID:", post.id)
#     print("Title:", post.title)
#     print("Body:", post.body[:50], "...")  # preview


# async def mainp():
#     api = ApiClient(base_url="https://jsonplaceholder.typicode.com")

#     payload = {
#         "title": "FlightDeck Test",
#         "body": "This is a test post from Sudip's DAG.",
#         "userId": 99,
#     }
#     headers = {"Content-Type": "application/json"}

#     post = await api.post(
#         endpoint="/posts", payload=payload, headers=headers, response_model=PostResponse
#     )

#     print("Created Post ID:", post.id)
#     print("Title:", post.title)
#     print("Body:", post.body)


# asyncio.run(mainp())


# asyncio.run(maink())
