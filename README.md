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

Usage documentation will be added as the project develops. See the milestones and
issues of this repository for the current plan.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or a pull request.

## License

Released under the MIT License. See [LICENSE](LICENSE).
