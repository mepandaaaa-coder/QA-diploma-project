from typing import Generator
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура инициализации Chrome драйвера."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser: WebDriver = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
