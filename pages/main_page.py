from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class MainPage(BasePage):
    """Page Object главной страницы Кинопоиска."""

    # Локаторы на основе DevTools
    SEARCH_INPUT: tuple[str, str] = (By.CSS_SELECTOR, 'input[name="text"]')

    # Локатор ссылки на «Онлайн-кинотеатр» в левом меню
    ONLINE_CINEMA_LINK: tuple[str, str] = (
        By.CSS_SELECTOR,
        'a[href*="hd.kinopoisk.ru"]'
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url: str = "https://www.kinopoisk.ru/"

    def open(self) -> None:
        """Открытие главной страницы."""
        self.driver.get(self.url)

    def search_movie(self, movie_title: str) -> None:
        """Поиск фильма по названию с нажатием Enter."""
        self.send_keys(self.SEARCH_INPUT, movie_title)
        self.send_keys(self.SEARCH_INPUT, Keys.ENTER)

    def input_search_query(self, query: str) -> None:
        """Вводит поисковый запрос в строку поиска."""
        element = self.find_element(self.SEARCH_INPUT)
        element.click()
        element.send_keys(query)

    def press_enter_in_search(self) -> None:
        """Отправляет клавишу Enter в поле поиска."""
        element = self.find_element(self.SEARCH_INPUT)
        element.send_keys(Keys.ENTER)

    def get_first_search_result_text(self) -> str:
        """Возвращает текст первого результата в поисковой выдаче."""
        result_locator = (
            By.CSS_SELECTOR,
            'span[class*="mainTitle"], a[data-tid="48719fbc"]'
        )
        element = self.find_element(result_locator)
        return element.text

    def click_online_cinema(self) -> None:
        """Клик по пункту «Онлайн-кинотеатр» в левом меню."""
        self.click_element(self.ONLINE_CINEMA_LINK)
