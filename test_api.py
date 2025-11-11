import allure
import pytest
from assertions.api import AssertionsApi
from data.data_objs import EMREQ0


@allure.feature('Тестирование работы api сервиса')
class TestCustomAPI:
    @allure.title('Проверка создания сущности')
    @pytest.mark.create
    def test_create_entity(self, ent_api):
        resp = ent_api[0].create_model_request(EMREQ0)
        status_code, title = ent_api[0].get_msg_response_by_id(int(resp.text))
        AssertionsApi.assert_status_code(200, resp.status_code)
        AssertionsApi.check_title_exists(title)

    @allure.title('Проверка удаления сущности по id')
    @pytest.mark.delete
    def test_delete_entity(self, ent_api):
        resp = ent_api[0].delete_by_id(ent_api[1])
        AssertionsApi.assert_status_code(204, resp.status_code)

    @allure.title('Проверка получения сущности по id')
    @pytest.mark.get
    def test_get_entity(self, ent_api):
        status_code, title = ent_api[0].get_msg_response_by_id(ent_api[1])
        AssertionsApi.assert_status_code(200, status_code)
        AssertionsApi.check_title_exists(title)

    @allure.title('Проверка получения всех сущностей')
    @pytest.mark.get_all
    def test_get_all_entities(self, ent_api):
        status_code, full = ent_api[0].get_msgs_response()
        AssertionsApi.assert_status_code(200, status_code)

    @allure.title('Проверка изменения параметров сущности по id')
    @pytest.mark.patch
    def test_patch_entity(self, ent_api):
        status_code = ent_api[0].patch_by_id(EMREQ0, ent_api[1])
        AssertionsApi.assert_status_code(204, status_code)
