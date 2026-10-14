
import pytest
from app import add, multiply, divide

def test_addition():
    assert add(10, 5) == 15

def test_multiplication():
    assert multiply(10, 5) == 50

def test_subraction():
    assert subraction(10,5)==5

def test_division():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
