"""
A Python OOP module that provides a Calculator class with methods
to compute product or sum based on specific conditions.
"""


class Calculator:
    """A calculator class that performs operations based on product threshold."""

    THRESHOLD = 1000

    def calculate(self, num1: int, num2: int) -> int:
        """
        Calculate the result based on the product of two numbers.

        If the product of the two numbers is less than or equal to 1000,
        return their product; otherwise, return their sum.

        Args:
            num1: First integer number.
            num2: Second integer number.

        Returns:
            The product if product <= 1000, otherwise the sum.
        """
        product = num1 * num2
        if product <= self.THRESHOLD:
            return product
        else:
            return num1 + num2
