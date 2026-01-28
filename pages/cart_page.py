from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List


class CartPage:
    """Page Object для страницы корзины"""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины

        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """Нажимает кнопку Checkout для начала оформления заказа"""
        self.driver.find_element(By.ID, "checkout").click()

    def get_cart_items(self) -> List[str]:
        """
        Возвращает список товаров в корзине

        Returns:
            Список названий товаров в корзине
        """
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        item_names = []
        for item in items:
            name_element = item.find_element(By.CLASS_NAME,
                                             "inventory_item_name")
            item_names.append(name_element.text)
        return item_names
