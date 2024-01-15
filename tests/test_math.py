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


def test_resta_1():
    """
    Test 1 for resta()
    """
    assert Calculator.resta(1, 1) == 0


def test_resta_2():
    """
    Test 2 for resta()
    """
    assert Calculator.resta(-1, -1) == 0


def test_resta_3():
    """
    Test 3 for resta()
    """
    assert Calculator.resta(-1, 1) == -2


def test_resta_4():
    """
    Test 4 for resta()
    """
    assert Calculator.resta(0, 0) == 0
