# src/common/logging.py
import logging
import structlog
from structlog.stdlib import BoundLogger
from typing import Protocol


class LoggerProtocol(Protocol):
    def info(self, msg: str, *args, **kwargs): ...
    def debug(self, msg: str, *args, **kwargs): ...
    def warning(self, msg: str, *args, **kwargs): ...
    def error(self, msg: str, *args, **kwargs): ...
    def exception(self, msg: str, *args, **kwargs): ...


def configure_logging(level: str = "INFO") -> BoundLogger:
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(message)s",
    )
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="ISO"),
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
    )
    return structlog.get_logger()


# Explicit type hint for IDE autocomplete
Log: LoggerProtocol = configure_logging()


# Usage Example

# Log.info("Starting app", user="sudip", job="flightdeck")
# Log.error("Something went wrong", error_code=500)
