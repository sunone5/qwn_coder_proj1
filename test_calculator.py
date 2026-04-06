"""
Test module for the Calculator class using TDD approach with pytest.
"""

import pytest
from calculator import Calculator


class TestCalculator:
    """Test cases for the Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calculator = Calculator()

    def test_product_less_than_threshold(self):
        """Test when product is less than 1000 - should return product."""
        result = self.calculator.calculate(10, 20)
        assert result == 200  # 10 * 20 = 200 <= 1000

    def test_product_equals_threshold(self):
        """Test when product equals 1000 - should return product."""
        result = self.calculator.calculate(25, 40)
        assert result == 1000  # 25 * 40 = 1000 <= 1000

    def test_product_greater_than_threshold(self):
        """Test when product is greater than 1000 - should return sum."""
        result = self.calculator.calculate(50, 30)
        assert result == 80  # 50 * 30 = 1500 > 1000, so return 50 + 30 = 80

    def test_with_zero(self):
        """Test with zero - product is 0, should return 0."""
        result = self.calculator.calculate(0, 100)
        assert result == 0  # 0 * 100 = 0 <= 1000

    def test_with_negative_numbers_product_under_threshold(self):
        """Test with negative numbers where product is under threshold."""
        result = self.calculator.calculate(-10, -20)
        assert result == 200  # -10 * -20 = 200 <= 1000

    def test_with_negative_numbers_product_over_threshold(self):
        """Test with negative numbers where product exceeds threshold."""
        result = self.calculator.calculate(-50, -30)
        assert result == -80  # -50 * -30 = 1500 > 1000, so return -50 + -30 = -80

    def test_mixed_positive_negative_under_threshold(self):
        """Test with mixed signs where product is under threshold."""
        result = self.calculator.calculate(-10, 50)
        assert result == -500  # -10 * 50 = -500 <= 1000

    def test_large_numbers_exceeding_threshold(self):
        """Test with large numbers that exceed threshold."""
        result = self.calculator.calculate(100, 100)
        assert result == 200  # 100 * 100 = 10000 > 1000, so return 100 + 100 = 200

    def test_edge_case_threshold_minus_one(self):
        """Test edge case: product is 999 (threshold - 1)."""
        result = self.calculator.calculate(33, 30)
        assert result == 990  # 33 * 30 = 990 <= 1000

    def test_edge_case_threshold_plus_one(self):
        """Test edge case: product is 1001 (threshold + 1)."""
        result = self.calculator.calculate(1001, 1)
        assert result == 1002  # 1001 * 1 = 1001 > 1000, so return 1001 + 1 = 1002
