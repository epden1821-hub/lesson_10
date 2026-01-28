from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы авторизации"""
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации
        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    """Открывает страницу авторизации"""
    def open(self) -> None:
        self.driver.get(self.url)

    """
    Выполняет вход с указанными логином и паролем
    Args:
        username: имя пользователя
        password: пароль пользователя
    """
    def login(self, username: str, password: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
