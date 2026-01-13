from typing import Final
from datetime import datetime

# database and api constants
MAX_CONNECTIONS: Final = 100
API_TIMEOUT: Final = 30.5

# Error Message
USER_NOT_FOUND: str = "The user is not availabe."
DATA_NOT_RECEIVED: str = "No data is received."

# logging
DEFAULT_LOG_PATH: str = f"./logs/flightdeck-{datetime.now().strftime("%Y-%m-%d")}.log"
MINIMUM_LOG_LEVEL: str = "DEBUG"
