"""Tests for the command-line interface."""

import contextlib
import io
import os
import subprocess
import sys
import unittest

from calculator.__main__ import main, parse_number

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_cli(*argv):
    """Run the CLI in-process and return (exit_code, stdout, stderr)."""
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(list(argv))
    return code, out.getvalue(), err.getvalue()


class TestParseNumber(unittest.TestCase):
    def test_integer_text_gives_int(self):
        self.assertEqual(parse_number("42"), 42)
        self.assertIsInstance(parse_number("42"), int)

    def test_negative_integer(self):
        self.assertEqual(parse_number("-7"), -7)

    def test_decimal_text_gives_float(self):
        self.assertEqual(parse_number("2.5"), 2.5)
        self.assertIsInstance(parse_number("2.5"), float)

    def test_invalid_text_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "invalid number: 'abc'"):
            parse_number("abc")


class TestCliOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(run_cli("add", "2", "3"), (0, "5\n", ""))

    def test_subtract(self):
        self.assertEqual(run_cli("subtract", "2", "3"), (0, "-1\n", ""))

    def test_multiply(self):
        self.assertEqual(run_cli("multiply", "2", "3"), (0, "6\n", ""))

    def test_divide_prints_float(self):
        self.assertEqual(run_cli("divide", "6", "3"), (0, "2.0\n", ""))

    def test_accepts_decimal_operands(self):
        self.assertEqual(run_cli("add", "1.5", "2"), (0, "3.5\n", ""))


class TestCliErrors(unittest.TestCase):
    def test_division_by_zero_exits_1_with_message(self):
        code, out, err = run_cli("divide", "1", "0")
        self.assertEqual(code, 1)
        self.assertEqual(out, "")
        self.assertEqual(err, "error: cannot divide by zero\n")

    def test_invalid_operand_exits_1_with_message(self):
        code, out, err = run_cli("add", "two", "3")
        self.assertEqual(code, 1)
        self.assertEqual(out, "")
        self.assertIn("invalid number: 'two'", err)

    def test_missing_arguments_exit_2(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as ctx:
            main(["add", "2"])
        self.assertEqual(ctx.exception.code, 2)

    def test_unknown_operation_exits_2(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as ctx:
            main(["power", "2", "3"])
        self.assertEqual(ctx.exception.code, 2)


class TestCliAsModule(unittest.TestCase):
    def test_python_m_calculator_runs(self):
        result = subprocess.run(
            [sys.executable, "-m", "calculator", "multiply", "2", "3"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "6\n")


if __name__ == "__main__":
    unittest.main()
