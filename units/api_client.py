import requests
from typing import Any, Optional, Dict


class ApiClient:
    """Вспомогательный класс для выполнения API-запросов."""

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url: str = base_url
        self.token: str = token
        self.default_headers: Dict[str, str] = {
            "X-API-KEY": self.token,
            "accept": "application/json"
        }

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        use_auth: bool = True,
        timeout: int = 10
    ) -> requests.Response:
        """Выполнение GET-запроса."""
        url = f"{self.base_url}{endpoint}"
        headers = (
            self.default_headers
            if use_auth
            else {"accept": "application/json"}
        )
        return requests.get(
            url,
            headers=headers,
            params=params,
            timeout=timeout,
        )
