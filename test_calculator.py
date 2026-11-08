
import pytest
from calculator import Calculator


def test_sum():
    calc = Calculator(8, 2)
    assert calc.sum() == 10


def test_subtract():
    calc = Calculator(8, 2)
    assert calc.subtract() == 6


def test_multiply():
    calc = Calculator(8, 2)
    assert calc.multiply() == 16


def test_divide():
    calc = Calculator(8, 2)
    assert calc.divide() == 4


def test_divide_by_zero():
    calc = Calculator(8, 0)
    with pytest.raises(ValueError):
        calc.divide()

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -2, -3),
    (2.5, 3.5, 6.0),
])
def test_sum_parametrized(a, b, expected):
    calc = Calculator(a, b)
    assert calc.sum() == expected
    