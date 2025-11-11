import allure


class AssertionsApi:
    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    @allure.step('Проверка. Заголовок у сущности присутствует')
    def check_title_exists(title):
        assert title != "", "Заголовок отсутствует"

    @staticmethod
    def assert_status_code(expected: int, actual: int):
        assert expected == actual, f"Должен быть статус-код {expected}"
