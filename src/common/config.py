
from typing import Tuple, Type, ClassVar
from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    JsonConfigSettingsSource,
    EnvSettingsSource,
    DotEnvSettingsSource,
)


class DbSettings(BaseModel):
    url: str
    pool_size: int


class AppSettings(BaseSettings):

    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent
    CONFIG_FILE_PATH: ClassVar[str] = str(
        BASE_DIR.parent / "configuration" / "appsettings.json"
    )

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    environment: str = Field(default="development")
    app_name: str
    external_api_base_url: str | None = None
    database: DbSettings

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:

        return (
            # 1️⃣ Lowest priority
            JsonConfigSettingsSource(
                settings_cls=settings_cls,
                json_file=cls.CONFIG_FILE_PATH,
            ),

            # 2️⃣ .env (MUST be explicitly configured)
            DotEnvSettingsSource(
                settings_cls=settings_cls,
                env_file=".env",
                env_prefix="APP_",
                env_nested_delimiter="__",
            ),

            # 3️⃣ Real environment variables
            EnvSettingsSource(
                settings_cls=settings_cls,
                env_prefix="APP_",
                env_nested_delimiter="__",
            ),

            # 4️⃣ Constructor args (highest)
            init_settings,
        )

    @property
    def is_development(self) -> bool:
        """Check if running in development"""
        return self.environment.lower() == "development"

    @property
    def is_production(self) -> bool:
        """Check if running in production"""
        return self.environment.lower() == "production"
