import allure
import pytest
from assertions.api import AssertionsApi
from data.data_objs import EMREQ0


@allure.feature('Тестирование работы api сервиса')
class TestCustomAPI:
    @allure.title('Проверка создания сущности')
    @pytest.mark.create
    def test_create_entity(self, new_obj):
        resp = new_obj.create_model_request(EMREQ0)
        status_code, title = new_obj.get_msg_response_by_id(int(resp.text))
        AssertionsApi.assert_status_code(200, resp.status_code)
        AssertionsApi.check_title_exists(title)

    @allure.title('Проверка удаления сущности по id')
    @pytest.mark.delete
    def test_delete_entity(self, new_obj, ent_api):
        resp = new_obj.delete_by_id(ent_api)
        AssertionsApi.assert_status_code(204, resp.status_code)

    @allure.title('Проверка получения сущности по id')
    @pytest.mark.get
    def test_get_entity(self, new_obj, ent_api):
        status_code, title = new_obj.get_msg_response_by_id(ent_api)
        AssertionsApi.assert_status_code(200, status_code)
        AssertionsApi.check_title_exists(title)

    @allure.title('Проверка получения всех сущностей')
    @pytest.mark.get_all
    def test_get_all_entities(self, new_obj):
        status_code, full = new_obj.get_msgs_response()
        AssertionsApi.assert_status_code(200, status_code)

    @allure.title('Проверка изменения параметров сущности по id')
    @pytest.mark.patch
    def test_patch_entity(self, new_obj, ent_api):
        status_code = new_obj.patch_by_id(EMREQ0, ent_api)
        AssertionsApi.assert_status_code(204, status_code)
