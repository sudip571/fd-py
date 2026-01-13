import httpx
from ..logging.loggers import Log, configure_logging
from typing import Any, Dict, Optional, Type, TypeVar
from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


class ApiClient:
    def __init__(self, base_url: str, default_headers: Optional[Dict[str, str]] = None, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.default_headers = default_headers or {}
        self.timeout = timeout

    async def post(self, endpoint: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]], response_model: Type[T]) -> T:
        """Generic async POST request returning a strongly typed response."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        merged_headers = {**self.default_headers, **(headers or {})}

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                resp = await client.post(url, json=payload, headers=merged_headers)
                resp.raise_for_status()
                Log.info("POST %s succeeded with status %s",
                         url, resp.status_code)
                return response_model.model_validate(resp.json())
        except Exception as e:
            Log.error("POST %s failed: %s", url, e)
            raise

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]], headers: Optional[Dict[str, str]], response_model: Type[T]) -> T:
        """Generic async GET request returning a strongly typed response."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        merged_headers = {**self.default_headers, **(headers or {})}

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                resp = await client.get(url, params=params, headers=merged_headers)
                resp.raise_for_status()
                Log.info("GET %s succeeded with status %s",
                         url, resp.status_code)
                return response_model.model_validate(resp.json())
        except Exception as e:
            Log.error("GET %s failed: %s", url, e)
            raise
