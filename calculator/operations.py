"""Arithmetic operations for the calculator.

Every operation accepts two real numbers (``int`` or ``float``) and returns the result.
Boolean values are rejected even though ``bool`` is a subclass of ``int``.
"""

from numbers import Real


def _check_operands(a, b):
    """Raise ``TypeError`` unless both operands are real, non-boolean numbers."""
    for name, value in (("a", a), ("b", b)):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(f"operand '{name}' must be a number, not {type(value).__name__}")


def add(a, b):
    """Return the sum of ``a`` and ``b``."""
    _check_operands(a, b)
    return a + b


def subtract(a, b):
    """Return ``a`` minus ``b``."""
    _check_operands(a, b)
    return a - b


def multiply(a, b):
    """Return the product of ``a`` and ``b``."""
    _check_operands(a, b)
    return a * b


def divide(a, b):
    """Return ``a`` divided by ``b`` as a float.

    Raises ``ZeroDivisionError`` when ``b`` is zero.
    """
    _check_operands(a, b)
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b
