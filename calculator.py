
"""Simple calculator with basic arithmetic operations."""


class Calculator:
    """Calculator for two numbers."""

    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        """Return the sum of two numbers."""
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        """Return the difference of two numbers."""
        return self.__op1 - self.__op2

    def multiply(self) -> float:
        """Return the product of two numbers."""
        return self.__op1 * self.__op2

    def divide(self) -> float:
        """Return the quotient of two numbers."""
        return self.__op1 / self.__op2
