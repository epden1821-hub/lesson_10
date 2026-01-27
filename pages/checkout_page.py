from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Page Object для страницы оформления заказа"""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа
        
        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
    
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа
        
        Args:
            first_name: имя покупателя
            last_name: фамилия покупателя
            postal_code: почтовый индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
    
    def get_total_price(self) -> str:
        """
        Возвращает итоговую стоимость заказа
        
        Returns:
            Итоговая стоимость в виде строки (без валюты)
        """
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text.replace("Total: $", "")
    
    def finish_checkout(self) -> None:
        """Завершает оформление заказа"""
        self.driver.find_element(By.ID, "finish").click()