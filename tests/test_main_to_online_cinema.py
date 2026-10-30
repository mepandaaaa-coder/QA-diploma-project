import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Главная страница")
@allure.story("Переход с главной страницы в онлайн-кинотеатр")
def test_navigate_to_online_cinema(driver: WebDriver) -> None:
    """
    Тест проверяет переход с главной страницы Кинопоиска
    в раздел Онлайн-кинотеатр.
    """
    main_page = MainPage(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        main_page.open()
        assert "kinopoisk.ru" in driver.current_url

    with allure.step("Кликнуть на «Онлайн-кинотеатр» в меню"):
        main_page.click_online_cinema()

    with allure.step(
        "Проверить успешность перехода"
        "на домен онлайн-кинотеатра"
    ):
        WebDriverWait(driver, 10).until(EC.url_contains("hd.kinopoisk.ru"))
        assert "hd.kinopoisk.ru" in driver.current_url
