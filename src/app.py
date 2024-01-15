"""
This is an example app in order to give some examples
on how to build a python app repo using good practices
in terms of linting, testing and documentation automation
"""


def suma(a: int = 1, b: int = 1) -> int:
    """
    Returns the addition of two integer numbers

    :param a: int number, defaults to 1
    :param b: int number, defaults to 1
    :return: sum of a and b as int
    """
    return a + b
