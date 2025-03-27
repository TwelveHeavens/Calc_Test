from src.calc import Calculator

calc = Calculator()

def test_sum():
    assert calc.sum(32,55) == 87
    assert calc.sum(7.7,4) == 11.7

def test_multiply():
    assert calc.multiply(5,7) == 35
    assert calc.multiply(3.2,4) == 12.8

def test_divide():
    assert calc.divide(276,6) == 46
    assert calc.divide(1192.4,22) == 54.2