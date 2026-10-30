import requests


class ApiClient:
    """Вспомогательный класс для выполнения API-запросов."""

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.default_headers = {
            "X-API-KEY": self.token,
            "accept": "application/json"
        }

    def get(self, endpoint, params=None, use_auth=True):
        """Выполнение GET-запроса."""
        url = f"{self.base_url}{endpoint}"
        headers = (
            self.default_headers
            if use_auth
            else {"accept": "application/json"}
        )
        return requests.get(url, headers=headers, params=params)
