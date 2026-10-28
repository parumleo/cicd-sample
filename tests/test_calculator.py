import pytest
from src.calculator import add, calculate_total

def test_adds_two_numbers():
    assert add(2, 3) == 5

def test_calculates_total_without_discount():
    assert calculate_total(10, 3) == 30

def test_calculates_total_with_discount():
    assert calculate_total(25, 2, 10) == 45

def test_zero_quantity_returns_zero():
    assert calculate_total(25, 0) == 0

@pytest.mark.parametrize("unit_price, quantity, discount", [
    (-1, 2, 0),
    (10, -2, 0),
    (10, 2, -1),
    (10, 2, 101),
])
def test_invalid_inputs_raise_value_error(unit_price, quantity, discount):
    with pytest.raises(ValueError):
        calculate_total(unit_price, quantity, discount)
