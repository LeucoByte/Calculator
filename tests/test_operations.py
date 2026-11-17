"""Unit tests for the arithmetic operations."""

import unittest

from calculator.operations import add, divide, multiply, subtract


class TestAdd(unittest.TestCase):
    def test_adds_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_adds_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_adds_mixed_signs(self):
        self.assertEqual(add(-2, 3), 1)

    def test_adding_zero_returns_the_other_operand(self):
        self.assertEqual(add(0, 7), 7)
        self.assertEqual(add(7, 0), 7)

    def test_adds_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_mixed_int_and_float_returns_float(self):
        self.assertEqual(add(1, 2.5), 3.5)

    def test_rejects_string_operand(self):
        with self.assertRaises(TypeError):
            add("2", 3)

    def test_rejects_none_operand(self):
        with self.assertRaises(TypeError):
            add(2, None)

    def test_rejects_boolean_operand(self):
        with self.assertRaises(TypeError):
            add(True, 1)



class TestSubtract(unittest.TestCase):
    def test_subtracts_positive_integers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_result_can_be_negative(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtracting_negative_adds(self):
        self.assertEqual(subtract(-2, -3), 1)

    def test_subtracting_zero_returns_the_first_operand(self):
        self.assertEqual(subtract(7, 0), 7)

    def test_subtracts_floats(self):
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)

    def test_mixed_int_and_float_returns_float(self):
        self.assertEqual(subtract(5, 2.5), 2.5)

    def test_rejects_string_operand(self):
        with self.assertRaises(TypeError):
            subtract(5, "3")

    def test_rejects_boolean_operand(self):
        with self.assertRaises(TypeError):
            subtract(True, 1)


class TestMultiply(unittest.TestCase):
    def test_multiplies_positive_integers(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_multiplying_by_zero_gives_zero(self):
        self.assertEqual(multiply(7, 0), 0)

    def test_multiplying_by_one_is_identity(self):
        self.assertEqual(multiply(7, 1), 7)

    def test_negative_times_positive_is_negative(self):
        self.assertEqual(multiply(-4, 3), -12)

    def test_negative_times_negative_is_positive(self):
        self.assertEqual(multiply(-4, -3), 12)

    def test_multiplies_floats(self):
        self.assertAlmostEqual(multiply(1.5, 2.0), 3.0)

    def test_mixed_int_and_float_returns_float(self):
        self.assertEqual(multiply(2, 2.5), 5.0)

    def test_rejects_string_operand(self):
        with self.assertRaises(TypeError):
            multiply("2", 3)

    def test_rejects_boolean_operand(self):
        with self.assertRaises(TypeError):
            multiply(3, False)


class TestDivide(unittest.TestCase):
    def test_divides_exactly(self):
        self.assertEqual(divide(6, 3), 2.0)

    def test_returns_float_for_fractional_result(self):
        self.assertAlmostEqual(divide(1, 4), 0.25)
        self.assertIsInstance(divide(1, 4), float)

    def test_negative_dividend(self):
        self.assertEqual(divide(-6, 3), -2.0)

    def test_negative_divisor(self):
        self.assertEqual(divide(6, -3), -2.0)

    def test_zero_dividend_gives_zero(self):
        self.assertEqual(divide(0, 5), 0.0)

    def test_divides_floats(self):
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)

    def test_division_by_zero_raises(self):
        with self.assertRaisesRegex(ZeroDivisionError, "cannot divide by zero"):
            divide(1, 0)

    def test_division_by_zero_float_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0.0)

    def test_rejects_string_operand(self):
        with self.assertRaises(TypeError):
            divide("6", 3)

    def test_rejects_boolean_operand(self):
        with self.assertRaises(TypeError):
            divide(True, 1)


if __name__ == "__main__":
    unittest.main()
