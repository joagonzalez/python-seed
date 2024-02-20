"""
This is an example app in order to give some examples
on how to build a python app repo using good practices
in terms of linting, testing and documentation automation
"""

from typing import Any


class Calculator:
    """
    Calculator App class
    """

    def __init__(self, *args: Any, **kwds: Any) -> None:
        pass

    def __str__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __del__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    @staticmethod
    def suma(a: float = 1, b: float = 1) -> float:
        """Function that returns addition of two integer numbers

        Args:
            a (float, optional): first number to add. Defaults to 1.
            b (float, optional): second number to add. Defaults to 1.

        Returns:
            float: addition of a and b
        """
        return a + b

    @staticmethod
    def resta(a: float = 1, b: float = 1) -> float:
        """Function that returns difference of two integer numbers

        Args:
            a (float, optional): _description_. Defaults to 1.
            b (float, optional): _description_. Defaults to 1.

        Returns:
            float: difference of a and b
        """
        return a - b

    @staticmethod
    def multiplicacion(a: float = 1, b: float = 1) -> float:
        """Function that multiplies two float values

        Args:
            a (float, optional): First parameter. Defaults to 1.
            b (float, optional): Second parameter. Defaults to 1.

        Returns:
            float: multiplication of a and b params
        """
        return a * b

    @staticmethod
    def division(a: float = 1, b: float = 1) -> float:
        """Function that returns division of two values where
           b is non zero

        Args:
            a (float, optional): First param. Defaults to 1.
            b (float, optional): Second param (non-zero). Defaults to 1.

        Returns:
            float: division result of a / b where b is non-zero
        """
        try:
            return a / b
        except ZeroDivisionError:
            print("Division by 0 not allowed!")
            return 0
