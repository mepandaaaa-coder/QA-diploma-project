import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.top250_page import Top250Page


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Карточка фильма")
@allure.story("Открытие карточки первого фильма из раздела Top 250")
def test_open_movie_card(driver: WebDriver) -> None:
    """Тест проверки открытия карточки фильма из списка Top 250."""
    top250_page = Top250Page(driver)

    with allure.step("Перейти на страницу Top 250 фильмов"):
        top250_page.open()

    with allure.step("Кликнуть на постер первого фильма в списке"):
        top250_page.click_first_movie()

    with allure.step("Дождаться перехода на страницу фильма и проверить URL"):
        WebDriverWait(driver, 10).until(EC.url_contains("/film/"))
        assert "/film/" in driver.current_url

    with allure.step("Проверить название фильма в карточке"):
        movie_title: str = top250_page.get_opened_movie_title()
        assert len(movie_title) > 0
        assert "Интерстеллар" in movie_title
