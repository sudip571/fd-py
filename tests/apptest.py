from flightdeck_etl.configurations.config import AppSettings
from flightdeck_etl.di_container.di import build_container

tt = build_container().build_provider()

print(tt.get(AppSettings).External_api_base_url)
