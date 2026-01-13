
from datetime import datetime, timezone, timedelta
from dateutil.relativedelta import relativedelta
from typing import Dict,Any,Optional
from ..logging.loggers import Log
import calendar
import json


class DateTimeProvider:

    def now_in_utc(self) -> datetime:
        return datetime.now(timezone.utc)

    @staticmethod
    def today() -> datetime:
        return datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def get_range_based_on_break_down_type(break_down: int) -> dict:
        """_summary_

        Args:
            break_down (int): _description_

        Raises:
            ValueError: _description_

        Returns:
            dict: _description_
        """
        current_date = datetime.now().date()
        if break_down == 30:
            ago = current_date - relativedelta(months=1)
            _, last = calendar.monthrange(ago.year, ago.month)
            return {
                'from': datetime(ago.year, ago.month, 1).strftime('%Y-%m-%d'),
                'to': datetime(ago.year, ago.month, last).strftime('%Y-%m-%d')
            }
        elif break_down == 0:
            yesterday = (current_date - timedelta(days=1)).strftime('%Y-%m-%d')
            return {'from': yesterday, 'to': yesterday}

        raise ValueError(f"Invalid breakdown: {break_down}")

    @staticmethod
    def get_first_and_last_day_of_month(month: int) -> Optional[Dict[str, Any]]:
        """_summary_

        Args:
            month (int): _description_

        Returns:
            json: _description_
        """

        try:
            current_date = datetime.now().date()
            one_month_ago = current_date - relativedelta(months=month)

            year = str(one_month_ago).split('-')[0]
            month = one_month_ago.month

            first, last = calendar.monthrange(int(year), int(month))

            first_day = datetime(int(year), int(month), 1)
            last_day = datetime(int(year), int(month), last)

            Log.info(f"date_from: {first_day}, date_to: {last_day}")

            return {
                'date_from': first_day.strftime('%Y-%m-%d'),
                'date_to': last_day.strftime('%Y-%m-%d')
            }

        except Exception as e:
            Log.error("Got unexcepted error:", error=e)
            return None
            
