"""
Пакет Page Objects для автоматизации тестирования
"""

from .calculator_page import CalculatorPage
from .login_page import LoginPage
from .products_page import ProductsPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage

__all__ = [
    'CalculatorPage',
    'LoginPage',
    'ProductsPage',
    'CartPage',
    'CheckoutPage'
]
