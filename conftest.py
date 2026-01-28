import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
@allure.step("Инициализация Chrome драйвера")
def chrome_driver():
    """
    Фикстура для создания Chrome драйвера
    Returns:
        WebDriver: Экземпляр Chrome драйвера
    Yields:
        WebDriver: Готовый к использованию драйвер
    """
    # Настройки Chrome для headless режима
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")  # Запуск без GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    # Создаем драйвер с автоматической установкой
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    # Настраиваем неявные ожидания
    driver.implicitly_wait(10)
    # Возвращаем драйвер для использования в тестах
    yield driver
    # Закрываем драйвер после теста
    with allure.step("Закрытие Chrome драйвера"):
        driver.quit()


@pytest.fixture
@allure.step("Инициализация Firefox драйвера")
def firefox_driver():
    """
    Фикстура для создания Firefox драйвера
    Returns:
        WebDriver: Экземпляр Firefox драйвера
    Yields:
        WebDriver: Готовый к использованию драйвер
    """
    # Настройки Firefox для headless режима
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    # Создаем драйвер с автоматической установкой
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=firefox_options
    )
    # Настраиваем неявные ожидания
    driver.implicitly_wait(10)
    # Возвращаем драйвер для использования в тестах
    yield driver
    # Закрываем драйвер после теста
    with allure.step("Закрытие Firefox драйвера"):
        driver.quit()
