from abc import ABC, abstractmethod
from typing import List
from flightdeck_etl.shared.models.client_model import Client
from typing import Optional


class IClientService(ABC):
    @abstractmethod
    async def get_top_client(self) -> Optional[Client]:
        """Fetch top client from tbl_clients"""
        pass
