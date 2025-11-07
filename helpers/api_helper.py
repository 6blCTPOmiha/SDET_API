import allure
from api.requests.base_requests_api import BaseApi
from data.data_api import BaseApiLocators


class ApiHelper(BaseApi):
    def __init__(self):
        super().__init__()
        self.token = BaseApiLocators.TOKEN

    @allure.step("Проверка кода ответа")
    def msg_response_code(self, response, path, obj='obj'):
        if response.status_code == 200:
            print(f'\nОбъект "{path}" существует!')
        elif response.status_code == 201:  # 201 Created
            print(f'\nОбъект "{path}" успешно создан!')
        elif response.status_code == 202:  # Acceted
            if obj == 'dir':
                print(f'\nНепустой каталог "{path}" поставлен в очередь на удаление!')
        elif response.status_code == 204:
            if obj == 'obj':
                print(f'\nОбъект "{path}" успешно удалён!')  # not check
        elif response.status_code == 404:
            print(f'\nОбъект "{path}" не найден!')
        elif response.status_code == 405:
            print(f'\nМетод не поддерживается!')
        elif response.status_code == 409:
            print(f'\nПо пути "{path}" уже существует объект с таким же...')
        else:
            json_response = response.json()
            print(path, response, json_response)

    @allure.step("Создание каталога")
    def dir_create(self, path):
        req_path = f'{BaseApiLocators.URL}?path={path}'
        response = self.request_put(req_path)
        self.msg_response_code(response, path=path)
        assert response.status_code == 201, "Directory not created!"

    @allure.step("Удаление каталога")
    def dir_delete(self, path):
        req_path = f'{BaseApiLocators.URL}?path={path}'
        response = self.request_put(req_path)
        self.msg_response_code(response, path=path)
        assert response.status_code == 201, "Directory not created!"

    @allure.step("Сканирование каталога")
    def dir_create(self, path):
        req_path = f'{BaseApiLocators.URL}?path={path}'
        response = self.request_put(req_path)
        self.msg_response_code(response, path=path)
        assert response.status_code == 201, "Directory not created!"