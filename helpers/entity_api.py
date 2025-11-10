from api.requests.base_requests_api import BaseApi
from config import Config
from helpers.convert_helper import ConvertHelper


class EntityApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.base_url = Config.BASE_URL

    def create_model_request(self, base_model):
        url = f'{self.base_url}/create'
        payload = base_model.model_dump()
        response = self.request_post(url, json_req=payload)
        response.raise_for_status()
        return response

    def get_msg_response_by_last_id(self):
        ids = self.get_ids_msgs_response()
        url_id = f'{self.base_url}/get/{ids[-1]}'
        response = self.request_get(url_id)
        response_text = response.text
        response_ch = ConvertHelper.deserialize_response(response_text)
        return response.status_code, response_ch.title

    def get_ids_msgs_response(self):
        url = f'{self.base_url}/getAll'
        response_text = self.request_get(url).text
        response_chs = ConvertHelper.deserialize_responses(response_text)
        ids = []
        for ch in response_chs:
            ids.append(ch.id)
        return ids

    def get_msgs_response(self):
        url = f'{self.base_url}/getAll'
        response = self.request_get(url)
        response_text = self.request_get(url).text
        response_chs = ConvertHelper.deserialize_responses(response_text)
        return response.status_code, response_chs

    def delete_by_id(self, element_id: int):
        ids = self.get_ids_msgs_response()
        if element_id in ids:
            url_id = f'{self.base_url}/delete/{element_id}'
            response = self.request_delete(url_id)
            response.raise_for_status()
            return response
        else:
            print(f'Ошибка! Сущность с {element_id} id отсутствует в БД ')
            raise

    def delete_last_entity(self):
        ids = self.get_ids_msgs_response()
        url_id = f'{self.base_url}/delete/{ids[-1]}'
        response = self.request_delete(url_id)
        response.raise_for_status()
        return response

    def patch_by_last_id(self, base_model):
        ids = self.get_ids_msgs_response()
        url = f'{self.base_url}/patch/{ids[-1]}'
        payload = base_model.model_dump()
        response = self.request_patch(url, json_req=payload)
        response.raise_for_status()
        return response.status_code

    def get_msg_response_by_id(self, element_id: int):
        ids = self.get_ids_msgs_response()
        if element_id in ids:
            url_id = f'{self.base_url}/get/{ids[-1]}'
            response = self.request_get(url_id)
            response_text = response.text
            response_ch = ConvertHelper.deserialize_response(response_text)
            return response.status_code, response_ch.title
        else:
            print(f'Ошибка! Сущность с {element_id} id отсутствует в БД ')
            raise

    def patch_by_id(self, base_model, element_id: int):
        ids = self.get_ids_msgs_response()
        if element_id in ids:
            url = f'{self.base_url}/patch/{ids[-1]}'
            payload = base_model.model_dump()
            response = self.request_patch(url, json_req=payload)
            response.raise_for_status()
            return response.status_code
        else:
            print(f'Ошибка! Сущность с {element_id} id отсутствует в БД ')
            raise
