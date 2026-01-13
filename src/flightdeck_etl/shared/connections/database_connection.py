import pyodbc
import psycopg2
import snowflake.connector
import databricks.sql
# from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
from flightdeck_etl.configurations.config import AppSettings


class DatabaseConnection:
    def __init__(self, settings: AppSettings):
        self._settings = settings
        self._mssql_conn = None
        self._postgres_conn = None
        self._snowflake_conn = None
        self._databricks_conn = None
        self._mssql_dag_hook_conn = None

    # Context manager support (like using{} in .NET)
    def __enter__(self):
        print("Enabling all connections…")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_all()

    # -----------------------------
    # Connection helpers
    # -----------------------------

    def connect_mssql(self):
        if not self._mssql_conn:
            self._mssql_conn = pyodbc.connect(self._settings.Mssql)
        return self._mssql_conn

    def connect_postgres(self):
        if not self._postgres_conn:
            pg = self._settings.Postgres
            self._postgres_conn = psycopg2.connect(
                host=pg.Host,
                database=pg.Database,
                user=pg.User,
                password=pg.Password,
                port=pg.Port,
            )
        return self._postgres_conn

    def connect_snowflake(self):
        if not self._snowflake_conn:
            sf = self._settings.Snowflake
            self._snowflake_conn = snowflake.connector.connect(
                account=sf.Account,
                user=sf.User,
                password=sf.Password,
                warehouse=sf.Warehouse,
                database=sf.Database,
                schema=sf.Schema,
            )
        return self._snowflake_conn

    def connect_databricks(self):
        if not self._databricks_conn:
            db = self._settings.Databricks
            self._databricks_conn = databricks.sql.connect(
                server_hostname=db.ServerHostname,
                http_path=db.HttpPath,
                access_token=db.AccessToken,
            )
        return self._databricks_conn

    # def get_mssql_hook(self) -> MsSqlHook:
    #     if not self._mssql_dag_hook_conn:
    #         self._mssql_dag_hook_conn = MsSqlHook(
    #             mssql_conn_id=self._settings.Mssql_dag_hook_id)
    #     return self._mssql_dag_hook_conn

    # -----------------------------
    # Cleanup helpers
    # -----------------------------

    def close_mssql(self):
        if self._mssql_conn:
            self._mssql_conn.close()
            self._mssql_conn = None

    def close_postgres(self):
        if self._postgres_conn:
            self._postgres_conn.close()
            self._postgres_conn = None

    def close_snowflake(self):
        if self._snowflake_conn:
            self._snowflake_conn.close()
            self._snowflake_conn = None

    def close_databricks(self):
        if self._databricks_conn:
            self._databricks_conn.close()
            self._databricks_conn = None

    def close_all(self):
        print("Closing all connections…")
        self.close_mssql()
        self.close_postgres()
        self.close_snowflake()
        self.close_databricks()
