import logging
import structlog
import os
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from ..constants import app_constants


def order_keys(_, __, event_dict):
    ordered = {"level": event_dict.pop("level", "info")}
    ordered.update(event_dict)
    return ordered


def configure_logging(
    logger_name: str = "FlightDeck",
    log_path: str = app_constants.DEFAULT_LOG_PATH,
    level: str = app_constants.MINIMUM_LOG_LEVEL,
    retention_days: int = 7,
):
    # Ensure log directory exists
    Path(os.path.dirname(log_path)).mkdir(parents=True, exist_ok=True)

    # Timed rotating handler: rotates daily, keeps N backups
    file_handler = TimedRotatingFileHandler(
        filename=log_path,
        when="D",              # rotate daily
        interval=1,            # every 1 day
        backupCount=retention_days,  # keep N days of logs
        encoding="utf-8"
    )

    # Configure stdlib logging
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(message)s",
        handlers=[
            logging.StreamHandler(),  # console
            file_handler,             # rotating file
        ],
    )

    # Configure structlog
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="ISO"),
            order_keys,
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    return structlog.get_logger(logger_name)


# Global logger
Log = configure_logging(retention_days=7)
