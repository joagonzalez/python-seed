"""
Tests for math functions.
"""
from src.app import Calculator


def test_suma_1():
    """
    Test 1 for suma()
    """
    assert Calculator.suma(1, 1) == 2


def test_suma_2():
    """
    Test 2 for suma()
    """
    assert Calculator.suma(-1, -1) == -2


def test_suma_3():
    """
    Test 3 for suma()
    """
    assert Calculator.suma(-1, 1) == 0


def test_suma_4():
    """
    Test 4 for suma()
    """
    assert Calculator.suma(0, 0) == 0
