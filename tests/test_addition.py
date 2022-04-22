from ctypes import CDLL

import pytest

@pytest.fixture
def calculator():
    yield CDLL("./src/calculator.so")

@pytest.mark.parametrize("first,second,result", [(0, 2, 2), (5, 1, 6), (9, 3, 12), (5, 3, 8)])
def test_addition(calculator, first, second, result):
    assert calculator.add(first, second) == result