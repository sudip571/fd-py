from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSetting(BaseModel):
    Host: str
    Database: str
    User: str
    Password: str
    Port: int


class SnowflakeSetting(BaseModel):
    Account: str
    User: str
    Password: str
    Warehouse: str
    Database: str
    Schema: str


class DatabricksSetting(BaseModel):
    ServerHostname: str
    HttpPath: str
    AccessToken: str


class SMTPSettings(BaseModel):
    Host: str
    Port: int
    From: str
    UserName: str
    Password: str


class PropertiesSettings(BaseModel):
    Environment: str = "development"
    App_name: str
    Mssql: str
    Mssql_dag_hook_id: str
    Openai_api_key: str
    External_api_base_url: str | None = None
    Postgres: PostgresSetting
    Snowflake: SnowflakeSetting
    Databricks: DatabricksSetting
    SMTPConfiguration: SMTPSettings
