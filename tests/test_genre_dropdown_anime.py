import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.top250_page import Top250Page


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Фильтр по жанрам")
@allure.story(
    "Проверка выбора жанра «Аниме» в выпадающем списке Топ 250"
)
def test_genre_dropdown_anime(driver: WebDriver) -> None:
    """
    Тест проверяет выбор жанра «Аниме», изменение URL
    и динамическое отображение фильмов.
    """
    top250_page = Top250Page(driver)

    with allure.step("Открыть страницу Топ-250 фильмов"):
        top250_page.open()

    with allure.step("Открыть выпадающий список фильтра по жанрам"):
        top250_page.open_genre_filter()

    with allure.step("Выбрать жанр «Аниме»"):
        top250_page.select_anime_genre()

    with allure.step(
        "Дождаться перехода на отфильтрованный URL с жанром аниме"
    ):
        WebDriverWait(driver, 10).until(
            EC.url_contains("genre--anime")
        )

    with allure.step(
        "Проверить, что URL содержит параметр выбора жанра аниме"
    ):
        current_url = driver.current_url
        assert "genre--anime" in current_url, (
            f"Ожидался URL с 'genre--anime', но получен: '{current_url}'"
        )

    with allure.step(
        "Проверить, что в выдаче отображаются фильмы с жанром «аниме»"
    ):
        assert "аниме" in driver.page_source.lower(), (
            "В результатах фильтрации не найдены фильмы с жанром «аниме»."
        )
