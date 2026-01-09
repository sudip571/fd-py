from typing import Tuple, Type, ClassVar
from pathlib import Path
from .config_properties import PropertiesSettings
from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    JsonConfigSettingsSource,
    EnvSettingsSource,
    DotEnvSettingsSource,
    SettingsConfigDict,
)


class AppSettings(BaseSettings, PropertiesSettings):

    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent
    CONFIG_FILE_PATH: ClassVar[str] = str(
        BASE_DIR.parent / "configuration" / "appsettings.json"
    )
    ENV_FILE_PATH: ClassVar[str] = str(
        BASE_DIR.parent.parent / ".env"
    )

    model_config = SettingsConfigDict(
        populate_by_name=True,
        extra="ignore",
        env_prefix="APP_",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:

        # Explicitly create all sources with proper configuration
        return (
            DotEnvSettingsSource(
                settings_cls=settings_cls,
                env_file=cls.ENV_FILE_PATH,
                env_file_encoding="utf-8",
                case_sensitive=False,
                env_prefix="APP_",
                env_nested_delimiter="__",
            ),
            EnvSettingsSource(
                settings_cls=settings_cls,
                case_sensitive=False,
                env_prefix="APP_",
                env_nested_delimiter="__",
            ),
            init_settings,
            JsonConfigSettingsSource(
                settings_cls=settings_cls,
                json_file=cls.CONFIG_FILE_PATH,
            )
        )

    @property
    def is_development(self) -> bool:
        return self.environment.lower() == "development"

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"
