
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
        if self.__op2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.__op1 / self.__op2


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator(10, 2)

    print("Sum:", calc.sum())
    print("Subtract:", calc.subtract())
    print("Multiply:", calc.multiply())
    print("Divide:", calc.divide())
