import allure
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Магазин SauceDemo")
@allure.story("Процесс покупки товаров")
class TestSauceDemo:
    """Тесты для сайта интернет-магазина SauceDemo"""
    
    @allure.title("Полный цикл покупки товаров")
    @allure.description("""
    Энд-ту-энд тест полного процесса покупки в интернет-магазине.
    Включает: авторизацию, выбор товаров, оформление заказа и проверку итогов.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.shop
    @pytest.mark.e2e
    def test_complete_purchase(self, firefox_driver):
        """
        Тест полного процесса покупки
        
        Steps:
        1. Авторизация на сайте
        2. Добавление товаров в корзину
        3. Проверка корзины
        4. Переход к оформлению заказа
        5. Заполнение данных покупателя
        6. Проверка итоговой стоимости
        7. Завершение покупки
        """
        with allure.step("Инициализация драйверов и страниц"):
            driver = firefox_driver
            login_page = LoginPage(driver)
            products_page = ProductsPage(driver)
            cart_page = CartPage(driver)
            checkout_page = CheckoutPage(driver)
        
        with allure.step("1. Открыть сайт и авторизоваться"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")
            
            allure.attach(
                "Использованы учетные данные:\nЛогин: standard_user\nПароль: secret_sauce",
                name="Данные авторизации",
                attachment_type=allure.attachment_type.TEXT
            )
            
            # Проверка успешной авторизации
            assert "inventory" in driver.current_url, "Авторизация не удалась"
            allure.attach(
                f"Текущий URL: {driver.current_url}",
                name="URL после авторизации",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("2. Добавить товары в корзину"):
            products_to_add = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt", 
                "Sauce Labs Onesie"
            ]
            
            for product in products_to_add:
                products_page.add_to_cart(product)
                allure.attach(
                    f"Добавлен товар: {product}",
                    name=f"Добавление товара",
                    attachment_type=allure.attachment_type.TEXT
                )
        
        with allure.step("3. Проверить количество товаров в корзине"):
            cart_count = products_page.get_cart_count()
            expected_count = 3
            
            with allure.step(f"Проверить: ожидается {expected_count}, получено {cart_count}"):
                assert cart_count == expected_count, \
                    f"Ожидалось {expected_count} товара в корзине, получено {cart_count}"
                
                allure.attach(
                    f"Количество товаров в корзине: {cart_count}",
                    name="Счетчик корзины",
                    attachment_type=allure.attachment_type.TEXT
                )
        
        with allure.step("4. Перейти в корзину"):
            products_page.go_to_cart()
            assert "cart" in driver.current_url.lower(), "Не удалось перейти в корзину"
        
        with allure.step("5. Проверить содержимое корзины"):
            cart_items = cart_page.get_cart_items()
            
            with allure.step("Проверить наличие всех добавленных товаров"):
                for product in products_to_add:
                    assert any(product in item for item in cart_items), \
                        f"Товар {product} не найден в корзине"
            
            allure.attach(
                f"Товары в корзине:\n" + "\n".join(cart_items),
                name="Содержимое корзины",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("6. Начать оформление заказа"):
            cart_page.click_checkout()
        
        with allure.step("7. Заполнить форму оформления заказа"):
            checkout_data = {
                "first_name": "Ivan",
                "last_name": "Ivanov", 
                "postal_code": "123456"
            }
            
            checkout_page.fill_checkout_form(**checkout_data)
            
            allure.attach(
                f"Данные покупателя:\n"
                f"Имя: {checkout_data['first_name']}\n"
                f"Фамилия: {checkout_data['last_name']}\n"
                f"Почтовый индекс: {checkout_data['postal_code']}",
                name="Данные заказа",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("8. Проверить итоговую стоимость"):
            total_price = checkout_page.get_total_price()
            expected_total = "58.29"
            
            with allure.step(f"Сравнить: ожидается ${expected_total}, получено ${total_price}"):
                assert total_price == expected_total, \
                    f"Ожидалась сумма ${expected_total}, получена ${total_price}"
                
                allure.attach(
                    f"Итоговая стоимость заказа: ${total_price}",
                    name="Итоговая стоимость",
                    attachment_type=allure.attachment_type.TEXT
                )
        
        with allure.step("9. Завершить покупку"):
            checkout_page.finish_checkout()
            
            # Проверка успешного завершения
            success_element = driver.find_element("class name", "complete-header")
            success_text = success_element.text
            assert "Thank you for your order" in success_text, "Заказ не завершен успешно"
            
            allure.attach(
                f"Сообщение об успешном заказе: {success_text}",
                name="Завершение покупки",
                attachment_type=allure.attachment_type.TEXT
            )
    
    @allure.title("Добавление одного товара в корзину")
    @allure.description("Проверка добавления одного товара и обновления счетчика корзины")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.shop
    @pytest.mark.smoke
    @pytest.mark.parametrize("product_name", [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ])
    def test_add_single_product_to_cart(self, firefox_driver, product_name):
        """
        Тест добавления одного товара в корзину
        
        Args:
            product_name: название товара для добавления
        """
        with allure.step(f"Тестирование добавления товара: {product_name}"):
            driver = firefox_driver
            login_page = LoginPage(driver)
            products_page = ProductsPage(driver)
            
            with allure.step("Авторизация"):
                login_page.open()
                login_page.login("standard_user", "secret_sauce")
            
            with allure.step(f"Добавить товар '{product_name}' в корзину"):
                initial_count = products_page.get_cart_count()
                products_page.add_to_cart(product_name)
            
            with allure.step("Проверить обновление счетчика корзины"):
                new_count = products_page.get_cart_count()
                assert new_count == initial_count + 1, \
                    f"Счетчик не увеличился. Было: {initial_count}, стало: {new_count}"
                
                allure.attach(
                    f"Товар: {product_name}\n"
                    f"Количество до: {initial_count}\n"
                    f"Количество после: {new_count}",
                    name="Изменение корзины",
                    attachment_type=allure.attachment_type.TEXT
                )