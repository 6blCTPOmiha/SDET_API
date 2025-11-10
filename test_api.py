import allure
import pytest
from assertions.api import AssertionsApi
from data.data_objs import EMREQ0


@allure.feature('Тестирование работы api сервиса')
class TestCustomAPI:
    @allure.title('Проверка создания сущности')
    @pytest.mark.create
    def test_create(self, ent_api):
        resp = ent_api.create_model_request(EMREQ0)
        AssertionsApi.assert_status_code(200, resp.status_code)
        AssertionsApi.check_create_resp_id(resp.text)

    @allure.title('Проверка удаления последней сущности')
    @pytest.mark.delete
    def test_delete_last(self, ent_api):
        resp = ent_api.delete_last_entity()
        AssertionsApi.assert_status_code(204, resp.status_code)

    @allure.title('Проверка получения последней сущности')
    @pytest.mark.get
    def test_get_last(self, ent_api):
        status_code, title = ent_api.get_msg_response_by_last_id()
        AssertionsApi.assert_status_code(200, status_code)
        AssertionsApi.check_title_is_right(title)

    @allure.title('Проверка получения всех сущностей')
    @pytest.mark.get_all
    def test_get_all(self, ent_api):
        status_code, full = ent_api.get_msgs_response()
        AssertionsApi.assert_status_code(200, status_code)

    @allure.title('Проверка изменения параметров последней сущности')
    @pytest.mark.patch
    def test_patch(self, ent_api):
        status_code = ent_api.patch_by_last_id(EMREQ0)
        AssertionsApi.assert_status_code(204, status_code)
