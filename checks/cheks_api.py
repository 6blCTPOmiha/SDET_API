import allure


class ChecksApi:
    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    @allure.step('Проверка. Количество сущностей > 2')
    def check_count_of_entities(ids):
        assert len(ids) > 2, "Количество сущностей меньше или равно 2"

    @staticmethod
    @allure.step('Проверка. id Созданного объекта вернулся')
    def check_entity_created(obj_id):
        assert obj_id > 0, "Объект не создался"

    @staticmethod
    @allure.step('Проверка. Количество сущностей возросло на 1')
    def check_new_1_entity_created(old, new):
        assert old + 1 == new, "Количество сущностей не изменилось или изменилось не корректно"

    @staticmethod
    @allure.step('Проверка. Объект удалён')
    def check_entity_deleted(resp_num):
        assert resp_num == 204, "Объект не удалился"

    @staticmethod
    @allure.step('Проверка. Заголовок 2 сущности верный')
    def check_title_is_right(title):
        assert title == "Заголовок сущности", "Заголовок не верный"

    @staticmethod
    @allure.step('Проверка. Данные объекта обновлены')
    def check_entity_patched(resp_num):
        assert resp_num == 204, "Данные объекта не обновлены"
