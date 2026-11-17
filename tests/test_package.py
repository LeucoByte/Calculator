"""Smoke tests for the calculator package."""

import unittest

import calculator


class TestPackage(unittest.TestCase):
    def test_package_imports(self):
        self.assertIsNotNone(calculator)

    def test_version_is_exposed(self):
        self.assertEqual(calculator.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
