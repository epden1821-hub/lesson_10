from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List


class ProductsPage:
    """Page Object для страницы товаров"""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы товаров
        
        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
    
    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по названию
        
        Args:
            product_name: название товара (частичное или полное совпадение)
        """
        # Находим все товары
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        for product in products:
            name_element = product.find_element(By.CLASS_NAME, "inventory_item_name")
            if product_name in name_element.text:
                add_button = product.find_element(By.CSS_SELECTOR, "button")
                add_button.click()
                return
    
    def go_to_cart(self) -> None:
        """Переходит в корзину"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    def get_cart_count(self) -> int:
        """
        Возвращает количество товаров в корзине
        
        Returns:
            Количество товаров в корзине (0 если корзина пуста)
        """
        cart_badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge[0].text) if cart_badge else 0