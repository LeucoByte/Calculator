"""Unit tests for the arithmetic operations."""

import unittest

from calculator.operations import add


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


if __name__ == "__main__":
    unittest.main()
