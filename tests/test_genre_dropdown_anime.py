import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from pages.top250_page import Top250Page


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Фильтрация")
@allure.story("Выбор жанра из выпадающего списка в Top 250")
def test_genre_dropdown(driver: WebDriver) -> None:
    """Тест проверяет открытие списка жанров и применение фильтра по жанру."""
    top250_page = Top250Page(driver)

    with allure.step("Открыть страницу Топ-250 фильмов"):
        top250_page.open()

    with allure.step("Кликнуть на фильтр «Жанр»"):
        top250_page.open_genre_filter()

    with allure.step("Проверить, что выпадающий список успешно открылся"):
        dropdown_element = top250_page.find_element(top250_page.GENRE_DROPDOWN)
        assert dropdown_element.get_attribute("aria-expanded") == "true"

    with allure.step("Выбрать жанр «Аниме» из списка"):
        top250_page.select_anime_genre()

    with allure.step(
        "Проверить, что страница обновилась"
        "под выбранный фильтр"
    ):
        WebDriverWait(driver, 10).until(
            lambda d: (
                "m_act%5Bgenre%5D" in d.current_url or "genre" in d.current_url
            )
        )
        assert "kinopoisk.ru/lists/movies/top250" in driver.current_url
