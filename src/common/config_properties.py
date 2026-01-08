from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseModel):
    url: str
    pool_size: int


class PropertiesSettings(BaseModel):
    environment: str = "development"
    app_name: str
    external_api_base_url: str | None = None
    database: DbSettings
