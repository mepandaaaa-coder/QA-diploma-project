from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class Top250Page(BasePage):
    """Page Object для страницы Топ 250 фильмов."""

    FIRST_MOVIE_LINK: tuple[str, str] = (
        By.CSS_SELECTOR,
        'div[data-test-id="movie-list-item"]:first-child '
        'a[class*="styles_poster"]'
    )

    FIRST_MOVIE_TITLE: tuple[str, str] = (
        By.CSS_SELECTOR,
        'div[data-test-id="movie-list-item"]:first-child '
        'span[class*="styles_mainTitle"]'
    )

    MOVIE_TITLE_HEADER: tuple[str, str] = (
        By.CSS_SELECTOR,
        'h1[data-tid], span[class*="styles_mainTitle"]'
    )

    GENRE_DROPDOWN: tuple[str, str] = (
        By.CSS_SELECTOR,
        'button[aria-label="Жанры"]'
    )

    ANIME_GENRE_OPTION: tuple[str, str] = (
        By.XPATH,
        '//div[@role="option" and contains(., "Аниме")]'
    )

    FOREIGN_FILTER_BUTTON: tuple[str, str] = (
        By.CSS_SELECTOR,
        'a[href*="foreign"]'
    )

    MOVIE_COUNTER: tuple[str, str] = (
        By.CSS_SELECTOR,
        'span[class*="styles_subtitle"]'
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url: str = "https://www.kinopoisk.ru/lists/movies/top250/"

    def open(self) -> None:
        """Открытие страницы Топ-250."""
        self.driver.get(self.url)

    def click_first_movie(self) -> None:
        """Клик по постеру первого фильма в списке."""
        self.click_element(self.FIRST_MOVIE_LINK)

    def get_opened_movie_title(self) -> str:
        """Получение названия фильма на открывшейся карточке."""
        element = self.find_element(self.MOVIE_TITLE_HEADER)
        return element.text

    def open_genre_filter(self) -> None:
        """Открытие выпадающего списка фильтра по жанрам."""
        self.click_element(self.GENRE_DROPDOWN)

    def select_anime_genre(self) -> None:
        """Выбор жанра «Аниме» в выпадающем списке."""
        self.click_element(self.ANIME_GENRE_OPTION)

    def click_foreign_filter(self) -> None:
        """Клик по быстрому фильтру «Зарубежные»."""
        self.click_element(self.FOREIGN_FILTER_BUTTON)

    def get_movie_counter_text(self) -> str:
        """Получение текста счётчика фильмов на странице."""
        element = self.find_element(self.MOVIE_COUNTER)
        return (
            element.text
            or element.get_attribute("textContent")
            or element.get_attribute("innerText")
            or ""
        )

    def wait_for_counter_update(self, initial_value: str) -> str:
        """Ожидание обновления счётчика (защита от race condition)."""
        def _check_counter(driver):
            try:
                elem = self.find_element(self.MOVIE_COUNTER)
                text = (
                    elem.text
                    or elem.get_attribute("textContent")
                    or elem.get_attribute("innerText")
                    or ""
                )
                text = text.strip()
                if text and text != initial_value:
                    return text
            except Exception:
                pass
            return False

        return WebDriverWait(self.driver, 10).until(_check_counter)

    def get_first_movie_title(self) -> str:
        """Получение названия первого фильма в списке до клика."""
        element = self.find_element(self.FIRST_MOVIE_TITLE)
        return (
            element.text
            or element.get_attribute("textContent")
            or element.get_attribute("innerText")
            or ""
        )
