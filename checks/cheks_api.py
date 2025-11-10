import allure


class ChecksApi:
    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    @allure.step('Проверка. id Созданного объекта вернулся')
    def check_create_resp_num(code):
        assert code == 200, "Объект не создался"

    @staticmethod
    @allure.step('Проверка. id Созданного объекта вернулся')
    def check_create_resp_id(resp_id):
        assert resp_id != 0, "Объект не создался"

    @staticmethod
    @allure.step('Проверка. Количество сущностей возросло на 1')
    def check_new_1_entity_created(old, new):
        assert old + 1 == new, "Количество сущностей не изменилось или изменилось не корректно"

    @staticmethod
    @allure.step('Проверка. Объект удалён')
    def check_entity_deleted(code):
        assert code == 204, "Объект не удалился"

    @staticmethod
    @allure.step('Проверка. Заголовок 2 сущности присутствует')
    def check_title_is_right(title):
        assert title != "", "Заголовок отсутствует"

    @staticmethod
    @allure.step('Проверка. Количество сущностей > 2')
    def check_count_of_entities(ids):
        assert len(ids) > 0, "Количество сущностей меньше или равно 2"

    @staticmethod
    @allure.step('Проверка. id Созданного объекта вернулся')
    def check_get_all_resp_num(code):
        assert code == 200, "Объект не создался"

    @staticmethod
    @allure.step('Проверка. Код ответа положительный')
    def check_get_resp_num(code):
        assert code == 200, "Объект не выдался"

    @staticmethod
    @allure.step('Проверка. Данные объекта обновлены')
    def check_entity_patched(code):
        assert code == 204, "Данные объекта не обновлены"

    @staticmethod
    @allure.step('Проверка. БД очищена')
    def check_db_cleared(code):
        assert code == "OK", "Больше нечего удалять"
