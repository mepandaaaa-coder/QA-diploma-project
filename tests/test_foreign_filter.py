import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.top250_page import Top250Page


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Быстрые фильтры")
@allure.story("Проверка фильтрации по категории «Зарубежные» в Топ 250")
def test_foreign_movies_filter(driver: WebDriver) -> None:
    """
    Тест проверяет применение фильтра
    «Зарубежные» и изменение счётчика фильмов.
    """
    top250_page = Top250Page(driver)

    with allure.step("Открыть страницу Топ-250 фильмов"):
        top250_page.open()

    with allure.step(
        "Получить начальное значение счётчика до применения фильтра"
    ):
        initial_counter = top250_page.get_movie_counter_text()

    with allure.step("Кликнуть на кнопку «Зарубежные»"):
        top250_page.click_foreign_filter()

    with allure.step("Дождаться перехода на отфильтрованный URL"):
        WebDriverWait(driver, 10).until(EC.url_contains("foreign"))

    with allure.step(
        "Проверить, что счётчик обновился и отличается от начального"
    ):
        counter_text = top250_page.wait_for_counter_update(initial_counter)
        assert counter_text != initial_counter and counter_text != "", (
            f"Счётчик не изменился после фильтрации. "
            f"Было: '{initial_counter}', стало: '{counter_text}'"
        )
