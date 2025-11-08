import allure
import pytest
from helpers.api_helper import ApiHelper
from checks.cheks_api import ChecksApi
from data.data_ids import DEL_ID, GET_ID, PATCH_ID


class TestCustomAPI:
    @allure.title('Проверка создания сущности')
    @pytest.mark.create
    def test_create(self):
        obj = ApiHelper()
        results_count_before = len(obj.get_msgs_response())
        obj.create_model_request()
        results_count_after = len(obj.get_msgs_response())
        ChecksApi.check_new_1_entity_created(results_count_before, results_count_after)


    @allure.title('Проверка удаления сущности по id')
    @pytest.mark.delete_id
    def test_delete_id(self):
        test_obj = ApiHelper()
        resp = test_obj.delete_by_id(DEL_ID)
        ChecksApi.check_entity_deleted(resp.status_code)


    @allure.title('Проверка удаления сущности по id')
    @pytest.mark.delete_last
    def test_delete_last(self):
        test_obj = ApiHelper()
        resp = test_obj.delete_last_entity()
        ChecksApi.check_entity_deleted(resp.status_code)


    @allure.title('Проверка получения сущности по id')
    @pytest.mark.get_by_id
    def test_get_by_id(self):
        test_obj = ApiHelper()
        title = test_obj.get_msg_response_by_id(GET_ID)
        ChecksApi.check_title_is_right(title)


    @allure.title('Проверка получения всех сущностей')
    @pytest.mark.get_all
    def test_get_all(self):
        test_obj = ApiHelper()
        ids = test_obj.get_ids_msgs_response()
        ChecksApi.check_count_of_entities(ids)


    @allure.title('Изменение параметров сущности')
    @pytest.mark.patch
    def test_patch(self):
        test_obj = ApiHelper()
        resp = test_obj.patch_by_id(PATCH_ID)
        ChecksApi.check_entity_patched(resp.status_code)
