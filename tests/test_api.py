import allure
import pytest
from helpers.api_helper import ApiHelper


class TestCustomAPI:


    def test_create(self):
        test_obj = ApiHelper()
        test_obj.request_get('http://127.0.0.1:8003')

