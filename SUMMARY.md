# Project summary: Calculator

A simple, dependency-free Python calculator that performs addition, subtraction,
multiplication and division. It runs as a library (`calculator.operations`) and from the
command line (`python -m calculator`). Everything was built through issues, branches,
pull requests with review, and continuous integration.

## Milestones

| Milestone | Due | Status | Issues |
|-----------|-----|--------|--------|
| Phase 1 - Foundation | 20 Nov 2026 | Closed 17 Nov 2026 | #1, #2 |
| Phase 2 - Arithmetic operations | 27 Nov 2026 | Closed 17 Nov 2026 | #3, #4, #5, #6 |
| Phase 3 - Command-line interface and documentation | 4 Dec 2026 | Closed 17 Nov 2026 | #7, #8, #9 |

All three milestones were completed before their due dates.

## Issues and pull requests

| Issue | Title | Pull request | Merge commit |
|-------|-------|--------------|--------------|
| #1 | Create package skeleton and test layout | #10 | `efa5d24` |
| #2 | Add CI workflow that runs the unit tests | #11 | `cd5edaa` |
| #3 | Implement addition operation | #12 | `c0603ca` |
| #4 | Implement subtraction operation | #13 | `f107b9b` |
| #5 | Implement multiplication operation | #14 | `5310097` |
| #6 | Implement division with zero-division check | #15 | `df425cc` |
| #7 | Add command-line interface | #16 | `b1da4a7` |
| #8 | Document usage in README | #17 | `278c25c` |
| #9 | Publish project summary (SUMMARY.md) | this pull request | |

The initial README and CONTRIBUTING.md were committed to `main` as the setup commit
`dc8eea5`. Each operation was delivered in its own commit (one per issue, with its tests),
and each pull request was merged with a merge commit so that every commit stays visible
in the history.

## Result

- `calculator/operations.py`: `add`, `subtract`, `multiply` and `divide`, all sharing one
  operand check. Booleans and non-numbers raise `TypeError`. `divide` returns a float and
  raises `ZeroDivisionError("cannot divide by zero")` for a zero divisor.
- `calculator/__main__.py`: the command-line interface. Exit codes are `0` for success,
  `1` for an invalid operand or division by zero, and `2` for a usage error.
- `tests/`: 52 unit tests (`unittest`, standard library only) covering the package,
  the four operations, the command-line interface, and a subprocess run of
  `python -m calculator`.

## Continuous integration

The `CI` workflow (`.github/workflows/ci.yml`) runs the unit tests on every push and pull
request, on Python 3.10 and 3.12 (`ubuntu-latest`). Up to the merge of #17, all 21 runs
passed: one push run and one pull request run for each feature branch, plus a push run on
`main` after each merge. The last run on `main` before this summary was run 44141674000
(for `278c25c`). The run for this pull request is linked from the pull request itself.

## Usage

```bash
python -m calculator add 2 3         # 5
python -m calculator divide 6 3      # 2.0
python -m calculator divide 1 0      # error: cannot divide by zero (exit 1)
```

The full usage guide is in [README.md](README.md). Contribution rules are in
[CONTRIBUTING.md](CONTRIBUTING.md).
