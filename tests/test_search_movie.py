import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Поиск")
@allure.story("Поиск фильма по названию")
def test_search_movie(driver: WebDriver) -> None:
    """Тест проверки поиска фильма по ключевому слову."""
    main_page = MainPage(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        main_page.open()

    with allure.step("Ввести название фильма в поиск и нажать Enter"):
        query: str = "Побег из Шоушенка"
        main_page.search_movie(query)

    with allure.step("Проверить, что заголовок или URL содержит запрос"):
        assert (
            query.lower() in driver.page_source.lower()
            or "search" in driver.current_url
        )
