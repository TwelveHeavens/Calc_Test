from src.calc import Calculator

calc = Calculator()

def test_sum():
    assert calc.sum(32,55) == 87
    assert calc.sum(7,4) == 11

def test_multiply():
    assert calc.multiply(5,7) == 35
    assert calc.multiply(32,4) == 128