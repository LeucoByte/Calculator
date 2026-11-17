# Contributing to Calculator

Thank you for helping improve this project. This guide explains how work is organised
and how to propose changes.

## 1. Plan the work with issues

- Every change starts from an **issue**. Search for an existing one before opening a new one.
- Work is organised in **milestones**, one per development phase, each with a due date.
- Every issue carries **labels**:
  - kind: `enhancement`, `documentation`, `testing`, `ci`
  - status: `status: todo`, `status: in progress`, `status: in review`, `status: done`
- Dependencies are written as `Blocked by #N` in the issue body and recorded with the
  "blocked by" relation. Do not start an issue until the issues blocking it are closed.
- Keep issues small: one unit of work with a clear way to verify it.

## 2. Branches

- Branch from an up-to-date `main`:
  ```bash
  git checkout main && git pull
  git checkout -b feature/<issue-number>-<short-slug>
  ```
  Example: `feature/3-add-addition`.
- Never commit directly to `main` once the initial setup is done.

## 3. Commits

- Make **one logical change per commit**. For example, one arithmetic operation together
  with its tests is one commit.
- Subject line: imperative mood, at most 72 characters, referencing the issue,
  e.g. `Add subtraction operation (#4)`.
- Optional body: explain *why* the change was made, wrap at about 72 characters.
- Run the test suite before every commit:
  ```bash
  python -m unittest discover -s tests -v
  ```

## 4. Tests

- New behaviour must come with unit tests in `tests/`.
- Tests use the standard library `unittest` module only. The project has no third-party dependencies.
- A pull request whose tests fail is not merged.

## 5. Pull requests

- Open a pull request from your branch into `main`.
- Use the title format `<Imperative summary> (#<issue>)`.
- In the description, state what changed, how you tested it, and link the issue with
  `Closes #<issue>` so the issue closes automatically on merge.
- Set the matching milestone and labels, and move the issue to `status: in review`.
- The **CI** workflow must pass before merging.
- Every pull request receives a review. Address each comment with a new commit or a reply.
- Merge with a **merge commit** (`--no-ff`) so that each commit stays visible in history,
  then delete the branch.

## 6. Closing issues and milestones

- An issue is closed when its pull request is merged. Set its label to `status: done`
  and post a short final comment with the pull request number and test result.
- A milestone is closed only when **all** of its issues are closed.

## 7. Code style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Keep functions small and documented with a short docstring.
- Raise clear exceptions for invalid input (for example, `ZeroDivisionError` with a message
  when dividing by zero).

## 8. Reporting bugs

Open an issue with the label `bug` (or `enhancement` for a feature request), the Python
version, the exact steps, the expected result and the actual result.
