
from rodi import Container
from flightdeck_etl.configurations.config import AppSettings
from flightdeck_etl.shared.emails.email_service import EmailService
from flightdeck_etl.shared.connections.database_connection import DatabaseConnection
from flightdeck_etl.modules.sev.contracts.iclient_service import IClientService
from flightdeck_etl.modules.sev.services.client_service import ClientService


def build_container() -> Container:
    container = Container()

    # SINGLETON (created once)
    # container.add_singleton(AppSettings)
    settings = AppSettings()
    container.add_instance(settings, AppSettings)

    # TRANSIENT (new every time)

    # SCOPED (once per scope)
    container.add_scoped(DatabaseConnection)
    container.add_scoped(IClientService, ClientService)
    container.add_scoped(EmailService)

    return container
