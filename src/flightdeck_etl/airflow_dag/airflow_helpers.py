import asyncio

from flightdeck_etl.di_container.di import build_container

# ruff: noqa


def run_service(service_type, method_name: str, *args, **kwargs):
    """
    Resolve a service from DI and run its async method.
    """
    container = build_container()
    provider = container.build_provider()
    with provider.create_scope() as scope:
        service = scope.get(service_type)
        method = getattr(service, method_name)
        return asyncio.run(method(*args, **kwargs))
