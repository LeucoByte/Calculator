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
