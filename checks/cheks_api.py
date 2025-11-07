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
    @allure.step('Проверка. Заголовок 3 сущности верный')
    def check_title_is_right(title):
        assert title == "Заголовок сущности", "Заголовок не верный"
