from ctypes import CDLL

import pytest

@pytest.fixture
def calculator():
    yield CDLL("./src/calculator.so")

@pytest.mark.parametrize("first,second,result", [(16, 4, 4), (45, 9, 5), (28, 7, 4), (72, 9, 8)])
def test_divide(calculator, first, second, result):
    calculator.divide(first, second) == result