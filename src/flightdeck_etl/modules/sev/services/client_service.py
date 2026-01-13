import asyncio
from flightdeck_etl.shared.connections.database_connection import DatabaseConnection
from flightdeck_etl.shared.models.client_model import Client
from ..contracts.iclient_service import IClientService
from typing import Optional


class ClientService(IClientService):
    def __init__(self, db: DatabaseConnection):
        self._db = db

    async def get_top_client(self) -> Optional[Client]:
        mssql_conn = self._db.connect_mssql()
        cursor = mssql_conn.cursor()
        cursor.execute(
            "SELECT TOP 1 client_id, name, website FROM tbl_clients")
        row = cursor.fetchone()
        await asyncio.sleep(0) 
        if row is None:
            return None 
        return Client(client_id=row[0], name=row[1], website=row[2])
    
