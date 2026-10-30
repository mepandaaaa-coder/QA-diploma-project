from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для работы со страницами."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, timeout)

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        """Поиск элемента с явным ожиданием."""
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def send_keys(self, locator: tuple[str, str], text: str) -> None:
        """Ввод текста в поле."""
        element: WebElement = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator: tuple[str, str]) -> WebElement:
        """Прокрутка страницы к элементу с предварительным ожиданием."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView("
            "{block: 'center', inline: 'nearest'});", element
        )
        return element

    def click_element(self, locator: tuple[str, str]) -> None:
        """
        Клик по элементу с предварительной
        прокруткой и ожиданием кликабельности.
        """
        self.driver.execute_script("window.scrollBy(0, 400);")

        self.scroll_to_element(locator)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
