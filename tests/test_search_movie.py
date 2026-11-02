import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Поиск")
@allure.story("Поиск фильма по названию")
def test_search_movie(driver: WebDriver) -> None:
    """
    Тест проверки поиска фильма по ключевому слову с проверкой результатов.
    """
    main_page = MainPage(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        main_page.open()

    with allure.step("Ввести название фильма в строку поиска"):
        query: str = "Побег из Шоушенка"
        main_page.input_search_query(query)

    with allure.step("Нажать клавишу Enter"):
        main_page.press_enter_in_search()

    with allure.step(
        "Проверить, что в результатах поиска отображается искомый фильм"
    ):
        result_title = main_page.get_first_search_result_text()
        assert query.lower() in result_title.lower(), (
            f"Ожидалось, что результат содержит '{query}', "
            f"но получено: '{result_title}'"
        )
