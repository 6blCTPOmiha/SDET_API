import allure
from api.requests.base_requests_api import BaseApi
from data.data_api import URL_CREATE, URL_DELETE, URL_GET, URL_GET_ALL, URL_PATCH
from data.data_objs import EMREQ0
from helpers.convert_helper import ConvertHelper



class ApiHelper(BaseApi):
    def __init__(self):
        super().__init__()

    @allure.step("Проверка кода ответа")
    def give_msg_response_code(self, response, obj='obj'):
        if response.status_code == 200:
            print(f'\nОперация прошла успешно!')
        elif response.status_code == 201:
            print(f'\nОбъект  успешно создан!')
        elif response.status_code == 202:
            if obj == 'dir':
                print(f'\nНепустой каталог  поставлен в очередь на удаление!')
        elif response.status_code == 204:
            if obj == 'obj':
                print(f'\nОбъект  успешно удалён!')
        elif response.status_code == 404:
            print(f'\nОбъект  не найден!')
        elif response.status_code == 405:
            print(f'\nМетод не поддерживается!')
        elif response.status_code == 409:
            print(f'\nПо пути уже существует объект с таким же...')
        else:
            json_response = response.json()
            print(response, json_response)


    def create_model_request(self):
        url = URL_CREATE
        payload = EMREQ0.model_dump()
        response = self.request_post(url, json_req=payload)
        response.raise_for_status()
        return response


    def get_msg_response_by_id(self, element_id: int):
        url_id = f'{URL_GET}/{element_id}'
        response_text = self.request_get(url_id).text
        response_ch = ConvertHelper.deserialize_response(response_text)
        return response_ch.title


    def get_ids_msgs_response(self):
        url = URL_GET_ALL
        response_text = self.request_get(url).text
        response_chs = ConvertHelper.deserialize_responses(response_text)
        ids = []
        for ch in response_chs:
            ids.append(ch.id)
        return ids

    def get_msgs_response(self):
        url = URL_GET_ALL
        response_text = self.request_get(url).text
        response_chs = ConvertHelper.deserialize_responses(response_text)
        """
        for ch in response_chs:
            print(f'\n{ch}\n')
        """
        return response_chs

    def delete_by_id(self, element_id: int):
        url_id = f'{URL_DELETE}/{element_id}'
        response = self.request_delete(url_id)
        response.raise_for_status()
        return response

    def delete_last_entity(self):
        ids = self.get_ids_msgs_response()
        url_id = f'{URL_DELETE}/{ids[-1]}'
        response = self.request_delete(url_id)
        response.raise_for_status()
        return response

    def patch_by_id(self, element_id: int):
        url = f'{URL_PATCH}/{element_id}'
        payload = EMREQ0.model_dump()
        response = self.request_patch(url, json_req=payload)
        response.raise_for_status()
        return response
