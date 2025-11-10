import allure
import pytest
from helpers.api_helper import ApiHelper
from checks.cheks_api import ChecksApi


@allure.feature('Тестирование работы api сервиса')
class TestCustomAPI:
    @allure.title('Проверка создания сущности')
    @pytest.mark.create
    def test_create(self):
        obj = ApiHelper()
        resp = obj.create_model_request()
        ChecksApi.check_create_resp_num(resp.status_code)
        ChecksApi.check_create_resp_id(resp.text)
        obj.delete_last_entity()

    @allure.title('Проверка удаления последней сущности')
    @pytest.mark.delete_by_id
    def test_delete_last(self):
        obj = ApiHelper()
        obj.create_model_request()
        resp = obj.delete_last_entity()
        ChecksApi.check_entity_deleted(resp.status_code)

    @allure.title('Проверка получения последней сущности')
    @pytest.mark.get_by_id
    def test_get_last(self):
        obj = ApiHelper()
        obj.create_model_request()
        status_code, title = obj.get_msg_response_by_last_id()
        ChecksApi.check_get_resp_num(status_code)
        ChecksApi.check_title_is_right(title)
        obj.delete_last_entity()

    @allure.title('Проверка получения всех сущностей')
    @pytest.mark.get_all
    def test_get_all(self):
        obj = ApiHelper()
        obj.create_model_request()
        status_code, full = obj.get_msgs_response()
        ChecksApi.check_get_all_resp_num(status_code)
        ChecksApi.check_count_of_entities(len(full))
        obj.delete_last_entity()

    @allure.title('Проверка изменения параметров последней сущности')
    @pytest.mark.patch_by_id
    def test_patch(self):
        obj = ApiHelper()
        obj.create_model_request()
        status_code = obj.patch_by_last_id()
        ChecksApi.check_entity_patched(status_code)
        obj.delete_last_entity()
