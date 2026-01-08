
from datetime import datetime, timezone


class DateTimeProvider:
    """Default datetime provider implementation"""

    def now(self) -> datetime:
        return datetime.now(timezone.utc)

    def today(self) -> datetime:
        return datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
