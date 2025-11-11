import requests
from requests import Response


class BaseApi:
    @staticmethod
    def request_get(url: str) -> Response:
        req = requests.get(url)
        if req.status_code == 200:
            return req
        else:
            print(f"\nОшибка! Получен код: {req.status_code}")
            raise

    @staticmethod
    def request_post(url: str, json_req, **kwargs: dict) -> Response:
        req = requests.post(url, json=json_req, **kwargs)
        if req.status_code == 200:
            return req
        else:
            print(f"\nОшибка! Получен код: {req.status_code}")
            raise

    @staticmethod
    def request_delete(url: str, **kwargs: dict) -> Response:
        req = requests.delete(url, **kwargs)
        if req.status_code == 204:
            return req
        else:
            print(f"\nОшибка! Получен код: {req.status_code}")
            raise

    @staticmethod
    def request_patch(url: str, json_req, **kwargs: dict) -> Response:
        req = requests.patch(url, json=json_req, **kwargs)
        if req.status_code == 204:
            return req
        else:
            print(f"\nОшибка! Получен код: {req.status_code}")
            raise
