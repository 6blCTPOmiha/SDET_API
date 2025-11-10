import pytest
from helpers.entity_api import EntityApi
from data.data_objs import EMREQ0


@pytest.fixture(scope="function")
def ent_api():
    ent_api = EntityApi()
    ent_api.create_model_request(EMREQ0)
    yield ent_api
    ent_api.delete_last_entity()


@pytest.fixture(scope="class", autouse=True)
def cleanup_after_all_tests():
    ent_api = EntityApi()
    ent_api.create_model_request(EMREQ0)
    yield ent_api
    ids = ent_api.get_ids_msgs_response()
    for ent_id in ids:
        ent_api.delete_by_id(ent_id)
