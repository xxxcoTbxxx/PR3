import pytest
from calc import FinanceCalculator

@pytest.fixture
def calculator():
    """Фикстура для создания экземпляра калькулятора."""
    return FinanceCalculator()

def test_initial_balance(calculator):
    """Тест начального баланса."""
    assert calculator.get_balance() == 0

def test_add_income(calculator):
    """Тест добавления дохода."""
    calculator.add_income(1000)
    assert calculator.get_balance() == 1000

def test_add_expense(calculator):
    """Тест добавления расхода."""
    calculator.add_income(1000)
    calculator.add_expense(300)
    assert calculator.get_balance() == 700

def test_negative_balance(calculator):
    """Тест отрицательного баланса."""
    calculator.add_expense(500)
    assert calculator.get_balance() == -500

def test_add_tax(calculator):
    calculator.add_income(1000)
    calculator.add_tax(200)
    assert calculator.get_balance() == 700

