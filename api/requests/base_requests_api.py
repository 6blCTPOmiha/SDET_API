import json

import allure
import requests
from requests import Response


class BaseApi:
    def __init__(self):
        self.token = None
        self.headers = None
        self.user_id = None
        self.body = None

    @staticmethod
    def request_get(url: str) -> Response:
        return requests.get(url)

    @staticmethod
    def request_post(url: str, json_req, **kwargs: dict) -> Response:
        return requests.post(url, json=json_req, timeout=10, **kwargs)

    def request_put(self, url: str, **kwargs: dict) -> Response:
        return requests.put(url, headers=self.headers, **kwargs)

    def request_delete(self, url: str, **kwargs: dict) -> Response:
        return requests.delete(url, headers=self.headers, **kwargs)

    @allure.step("Проверка формата JSON")
    def json_check(self, json_data):
        try:
            json.loads(str(json_data).replace("'", '"'))
        except ValueError as err:
            return False
        return True
