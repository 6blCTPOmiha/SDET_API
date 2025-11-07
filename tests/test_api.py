import allure
import pytest
from helpers.api_helper import ApiHelper
from checks.cheks_api import ChecksApi


class TestCustomAPI:
    @allure.title('Прикол')
    @pytest.mark.hz(reason="Test for myself")
    def test_working(self):
        test_obj = ApiHelper()
        #  test_obj.request_get('http://localhost:8003/api/_/docs/swagger/index.html#')
        #  ids = test_obj.get_ids_msg_response()
        #  title = test_obj.get_msg_response_by_id(3)


    @allure.title('Проверка создания сущности')
    @pytest.mark.create
    def test_create(self):
        test_obj = ApiHelper()
        new_obj_id = test_obj.create_model_request()
        ChecksApi.check_entity_created(new_obj_id)


    @allure.title('Проверка удаления сущности')
    @pytest.mark.delete
    def test_delete(self):
        test_obj = ApiHelper()
        test_obj.request_get('http://127.0.0.1:8003')


    @allure.title('Проверка получения сущности по id')
    @pytest.mark.get_by_id
    def test_get_by_id(self):
        test_obj = ApiHelper()
        title = test_obj.get_msg_response_by_id(3)
        ChecksApi.check_title_is_right(title)


    @allure.title('Проверка получения всех сущностей')
    @pytest.mark.get_all
    def test_get_all(self):
        test_obj = ApiHelper()
        ids = test_obj.get_ids_msg_response()
        ChecksApi.check_count_of_entities(ids)


    @allure.title('Изменение параметров сущности')
    @pytest.mark.patch
    def test_patch(self):
        test_obj = ApiHelper()
        test_obj.request_get('http://127.0.0.1:8003')
