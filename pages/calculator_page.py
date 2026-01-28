from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Page Object для страницы калькулятора"""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора

        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

    def open(self) -> None:
        """Открывает страницу калькулятора"""
        self.driver.get(self.url)

    def set_delay(self, delay_value: int) -> None:
        """
        Устанавливает значение задержки вычислений

        Args:
            delay_value: время задержки в секундах
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку с указанным текстом

        Args:
            button_text: текст на кнопке (цифра или оператор)
        """
        # Ищем кнопку по содержащемуся тексту
        buttons = self.driver.find_elements(By.CSS_SELECTOR, ".keys span")
        for button in buttons:
            if button.text == button_text:
                button.click()
                return

        # Альтернативный способ: поиск по классам для цифр
        if button_text.isdigit():
            xpath = f"//span[text()='{button_text}']"
            self.driver.find_element(By.XPATH, xpath).click()
        elif button_text == "+":
            self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        elif button_text == "=":
            self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self) -> str:
        """
        Возвращает текущее значение из поля результата

        Returns:
            Текущий результат вычислений в виде строки
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

    def wait_for_result(self, expected_result: str,
                        timeout: int = 50) -> str:
        """
        Ожидает появления ожидаемого результата с таймаутом

        Args:
            expected_result: ожидаемый результат
            timeout: максимальное время ожидания в секундах

        Returns:
            Фактический результат вычислений

        Raises:
            TimeoutException: если результат не появился за указанное время
        """
        wait = WebDriverWait(self.driver, timeout)
        locator = (By.CSS_SELECTOR, ".screen")
        condition = EC.text_to_be_present_in_element(locator, expected_result)
        wait.until(condition)
        return self.get_result()
