from ctypes import CDLL

import pytest

@pytest.fixture
def calculator():
    yield CDLL("./src/calculator.so")

@pytest.mark.parametrize("first,second,result", [(5, 4, 1), (3, 0, 3), (9, 7, 2), (13, 8, 5)])
def test_subtracting(calculator, first, second, result):
    assert calculator.subtract(first, second) == result