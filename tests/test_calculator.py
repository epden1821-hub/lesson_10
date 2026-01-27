import allure
import pytest
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Математические операции с задержкой")
class TestCalculator:
    """Тесты для функциональности калькулятора с задержкой выполнения"""
    
    @allure.title("Тестирование медленного калькулятора")
    @allure.description("""
    Тест проверяет работу калькулятора с установленной задержкой вычислений.
    Выполняется операция сложения 7 + 8 с задержкой 45 секунд.
    Проверяется корректность результата после ожидания.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.calculator
    @pytest.mark.slow
    def test_slow_calculator(self, chrome_driver):
        """
        Тест медленного калькулятора
        
        Steps:
        1. Открыть страницу калькулятора
        2. Установить задержку 45 секунд
        3. Выполнить операцию 7 + 8
        4. Ожидать результат в течение 50 секунд
        5. Проверить корректность результата
        """
        with allure.step("Инициализация драйвера и страницы"):
            driver = chrome_driver
            calculator = CalculatorPage(driver)
        
        with allure.step("1. Открыть страницу калькулятора"):
            calculator.open()
        
        with allure.step("2. Установить задержку 45 секунд"):
            calculator.set_delay(45)
            allure.attach(
                "Задержка установлена на 45 секунд",
                name="Информация о задержке",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("3. Выполнить операцию 7 + 8"):
            calculator.click_button("7")
            calculator.click_button("+")
            calculator.click_button("8")
            calculator.click_button("=")
            allure.attach(
                "Выполнена операция: 7 + 8 =",
                name="Выполненная операция",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("4. Ожидать результат в течение 50 секунд"):
            result = calculator.wait_for_result("15", timeout=50)
            allure.attach(
                f"Полученный результат: {result}",
                name="Результат вычислений",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("5. Проверить корректность результата"):
            assert result == "15", f"Ожидался результат 15, получен {result}"
            allure.attach(
                f"Проверка пройдена: ожидалось 15, получено {result}",
                name="Результат проверки",
                attachment_type=allure.attachment_type.TEXT
            )
    
    @allure.title("Быстрые вычисления без задержки")
    @allure.description("Проверка работы калькулятора без задержки вычислений")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.calculator
    @pytest.mark.fast
    @pytest.mark.parametrize("expression,expected", [
        ("1+2=", "3"),
        ("5-3=", "2"),
        ("4*3=", "12"),
        ("10/2=", "5")
    ])
    def test_fast_calculations(self, chrome_driver, expression, expected):
        """
        Параметризованный тест быстрых вычислений
        
        Args:
            expression: математическое выражение для выполнения
            expected: ожидаемый результат
        """
        with allure.step(f"Тестирование выражения: {expression}"):
            driver = chrome_driver
            calculator = CalculatorPage(driver)
            
            with allure.step("Открыть страницу калькулятора"):
                calculator.open()
            
            with allure.step("Установить задержку 0 секунд"):
                calculator.set_delay(0)
            
            with allure.step(f"Выполнить выражение: {expression}"):
                # Разбиваем выражение на символы и нажимаем соответствующие кнопки
                for char in expression:
                    if char != '=':
                        calculator.click_button(char)
                    else:
                        calculator.click_button("=")
            
            with allure.step(f"Получить и проверить результат"):
                actual_result = calculator.get_result()
                assert actual_result == expected, f"Ожидалось {expected}, получено {actual_result}"
                
                allure.attach(
                    f"Выражение: {expression}\nОжидалось: {expected}\nПолучено: {actual_result}",
                    name="Результаты вычисления",
                    attachment_type=allure.attachment_type.TEXT
                )