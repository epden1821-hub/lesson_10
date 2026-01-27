Проект автоматизированного тестирования веб-приложений с использованием Page Object Pattern, Selenium WebDriver и Allure для создания детальных отчетов.



# Установка Python зависимостей
pip install -r requirements.txt

# Запуск всех тестов
pytest

# Запуск тестов калькулятора
pytest tests/test_calculator.py -v

# Запуск тестов магазина
pytest tests/test_shop.py -v

# Запуск тестов с сохранением результатов для Allure
pytest --alluredir=allure-results

# Просмотр отчета (после завершения тестов)
allure serve allure-result