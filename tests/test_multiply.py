from ctypes import CDLL

import pytest

@pytest.fixture
def calculator():
    yield CDLL("./src/calculator.so")

@pytest.mark.parametrize("first,second,result", [(2, 1, 2), (6, 7, 42), (3, 6, 18), (4, 3, 12)])
def test_multiply(calculator, first, second, result):
    assert calculator.multiply(first, second) == result