import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.top250_page import Top250Page


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Быстрые фильтры")
@allure.story("Проверка фильтрации по категории «Зарубежные» в Top 250")
def test_foreign_movies_filter(driver: WebDriver) -> None:
    """
    Тест проверяет применение фильтра
    «Зарубежные» и изменение счетчика фильмов на 196.
    """
    top250_page = Top250Page(driver)

    with allure.step("Открыть страницу Топ-250 фильмов"):
        top250_page.open()

    with allure.step("Кликнуть на кнопку «Зарубежные»"):
        top250_page.click_foreign_filter()

    with allure.step("Дождаться перехода на отфильтрованный URL"):
        WebDriverWait(driver, 10).until(EC.url_contains("foreign"))

    with allure.step(
        "Проверить, что в тексте"
        "страницы отображается количество '196'"
    ):
        WebDriverWait(driver, 10).until(
            lambda d: "196" in d.page_source
        )
        assert "196" in driver.page_source
