"""Command-line interface.

Usage::

    python -m calculator OPERATION A B

``OPERATION`` is one of ``add``, ``subtract``, ``multiply`` or ``divide``. ``A`` and
``B`` are numbers; integers are kept as integers, anything else is read as a float.

Exit codes: ``0`` success; ``1`` invalid operand or division by zero; ``2`` usage
error (wrong number of arguments or unknown operation), as reported by argparse.
"""

import argparse
import sys

from calculator.operations import add, divide, multiply, subtract

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def parse_number(text):
    """Convert ``text`` to an ``int`` if possible, otherwise to a ``float``.

    Raises ``ValueError`` with a readable message when ``text`` is not a number.
    """
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"invalid number: {text!r}") from None


def build_parser():
    """Return the argument parser for the command line."""
    parser = argparse.ArgumentParser(
        prog="python -m calculator",
        description="Perform a basic arithmetic operation on two numbers.",
    )
    parser.add_argument("operation", choices=sorted(OPERATIONS), help="operation to perform")
    parser.add_argument("a", help="first operand")
    parser.add_argument("b", help="second operand")
    return parser


def main(argv=None):
    """Run the calculator with ``argv`` (defaults to ``sys.argv[1:]``) and return the exit code."""
    args = build_parser().parse_args(argv)
    try:
        a = parse_number(args.a)
        b = parse_number(args.b)
        result = OPERATIONS[args.operation](a, b)
    except (ValueError, TypeError, ZeroDivisionError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
