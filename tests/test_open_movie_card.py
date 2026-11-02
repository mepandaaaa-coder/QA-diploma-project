import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.top250_page import Top250Page


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Карточка фильма")
@allure.story(
    "Открытие карточки первого фильма из раздела Top 250"
)
def test_open_movie_card(driver: WebDriver) -> None:
    """
    Тест проверки открытия карточки фильма из раздела Top 250
    с динамической проверкой названия.
    """
    top250_page = Top250Page(driver)

    with allure.step("Перейти на страницу Top 250 фильмов"):
        top250_page.open()

    with allure.step("Получить название первого фильма в списке до клика"):
        expected_title = top250_page.get_first_movie_title()

    with allure.step("Кликнуть на постер первого фильма в списке"):
        top250_page.click_first_movie()

    with allure.step("Дождаться перехода на страницу фильма и проверить URL"):
        WebDriverWait(driver, 10).until(EC.url_contains("/film/"))
        assert "/film/" in driver.current_url

    with allure.step(
        "Проверить, что название открытого"
        "фильма совпадает с названием в списке"
    ):
        movie_title: str = top250_page.get_opened_movie_title()
        assert len(movie_title) > 0, "Название фильма в карточке пустое."
        assert expected_title.lower() in movie_title.lower(), (
            f"Ожидалось название '{expected_title}', "
            f"но в карточке открылось: '{movie_title}'"
        )
