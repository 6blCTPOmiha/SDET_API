import pytest
from api.entity_api import EntityApi
from data.data_objs import EMREQ0


@pytest.fixture(scope="function")
def ent_api(new_obj):
    ent = new_obj.create_model_request(EMREQ0)
    ent_id = int(ent.text)
    yield ent_id
    ids = new_obj.get_ids_msgs_response()
    if ent_id in ids:
        new_obj.delete_by_id(element_id=ent_id)


@pytest.fixture(scope="session")
def new_obj():
    new_obj = EntityApi()
    yield new_obj


@pytest.fixture(scope="class", autouse=True)
def cleanup_after_all_tests():
    ent_api = EntityApi()
    ent_api.create_model_request(EMREQ0)
    yield ent_api
    ids = ent_api.get_ids_msgs_response()
    for ent_id in ids:
        ent_api.delete_by_id(ent_id)
