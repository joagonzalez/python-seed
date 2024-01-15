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
    def suma(a: int = 1, b: int = 1) -> int:
        """Function that returns addition of two integer numbers

        Args:
            a (int, optional): first number to add. Defaults to 1.
            b (int, optional): second number to add. Defaults to 1.

        Returns:
            int: addition of a and b
        """
        return a + b

    @staticmethod
    def resta(a: int = 1, b: int = 1) -> int:
        """Function that returns difference of two integer numbers

        Args:
            a (int, optional): _description_. Defaults to 1.
            b (int, optional): _description_. Defaults to 1.

        Returns:
            int: difference of a and b
        """
        return a - b
