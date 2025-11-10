import requests
from requests import Response


class BaseApi:


    @staticmethod
    def request_get(url: str) -> Response:
        return requests.get(url)

    @staticmethod
    def request_post(url: str, json_req, **kwargs: dict) -> Response:
        return requests.post(url, json=json_req, timeout=10, **kwargs)

    @staticmethod
    def request_delete(url: str, **kwargs: dict) -> Response:
        return requests.delete(url, **kwargs)

    @staticmethod
    def request_patch(url: str, json_req, **kwargs: dict) -> Response:
        return requests.patch(url, json=json_req, timeout=10, **kwargs)
