# Calculator

A simple, dependency-free calculator written in Python. It supports the four basic
arithmetic operations:

- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`), with an explicit error when dividing by zero

## Requirements

- Python 3.10 or newer
- No third-party packages

## Usage

Run the calculator from the project root:

```bash
python -m calculator OPERATION A B
```

`OPERATION` is one of `add`, `subtract`, `multiply` or `divide`. `A` and `B` are numbers.
Integers are kept as integers; other numbers are read as floats.

```bash
python -m calculator add 2 3         # 5
python -m calculator subtract 2 3    # -1
python -m calculator multiply 2 3    # 6
python -m calculator divide 6 3      # 2.0
python -m calculator add 1.5 2       # 3.5
```

### Errors and exit codes

| Exit code | Meaning |
|-----------|---------|
| `0` | Success; the result is printed to standard output. |
| `1` | Invalid operand, or division by zero. The message is printed to standard error. |
| `2` | Usage error: wrong number of arguments or unknown operation (reported by argparse). |

```bash
python -m calculator divide 1 0      # error: cannot divide by zero (exit 1)
python -m calculator add two 3       # error: invalid number: 'two' (exit 1)
python -m calculator power 2 3       # usage error (exit 2)
```

The calculator can also be used from Python:

```python
from calculator.operations import add, subtract, multiply, divide

print(add(2, 3))       # 5
print(divide(6, 3))    # 2.0
```

## Running the tests

```bash
python -m unittest discover -s tests -v
```

## Project layout

```
calculator/      Package with the arithmetic operations
tests/           Unit tests (unittest, standard library only)
.github/workflows/  GitHub Actions workflows (CI)
README.md
CONTRIBUTING.md  How to contribute: branches, commits, pull requests, issues
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or a pull request.

## License

Released under the MIT License. See [LICENSE](LICENSE).
