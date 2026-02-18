# Contributing to SC2AnonServerPy

Contributions are welcome - thank you for helping improve SC2AnonServerPy!

Any contribution, big or small, is appreciated and credit will always be given.

## Types of Contributions

### Report Bugs

When reporting a bug, please include:

* Any relevant details about your local setup (Python version, virtualenv/poetry, etc.).
* Exact steps to reproduce the issue and any error output or logs.

### Fix Bugs

Check the GitHub issues for items labeled `bug` and `help wanted`. Those are
good places to start. If you pick up an issue, leave a comment to let others
know you're working on it.

### Implement Features

Please discuss the feature you would like to implement in an issue before starting work.
This helps to ensure that the feature aligns with the project's goals and avoids duplication of effort.

### Write Documentation

Improvements to docs, docstrings, or examples are always welcome. Small
clarifications or examples can make a big difference for new users.

### Submit Feedback

If you propose a change to the project (bugfix or feature):

* Explain clearly what you want to change and why.
* Keep the scope small to make review and testing easier.
* Be patient — maintainers are volunteers and review times may vary.

## Get Started

### Development with Docker

This repository includes development Dockerfiles under the `docker/` folder.

Build the development image:

```bash
docker build --tag=sc2anonserverpy:dev -f ./docker/Dockerfile.dev .
```

Run the development container (mounts current directory):

```bash
docker run -it -v "$(pwd)":/app sc2anonserverpy:dev
```

If you prefer Windows PowerShell, replace `$(pwd)` with `${PWD}`.

### Local Development

1. Clone the repository locally.
2. Install dependencies using `uv` (recommended) or your preferred tool:

```bash
uv sync
```

3. Create a branch for your work:

```bash
git checkout -b name-of-your-bugfix-or-feature
```

4. Ensure your changes follow existing code style and type hints. This
project ships with type hints; please keep them up to date when changing
public APIs.

5. Commit your changes and open a pull request.

## Pull Request Guidelines

Before submitting a pull request, please ensure:

1. The PR includes tests for new behavior where appropriate.
2. Documentation is updated for any user-facing changes.
3. Changes are backwards-compatible or clearly documented.

## Code of Conduct

By contributing to SC2AnonServerPy you agree to follow the project's Code of
Conduct. Treat other contributors with respect and be constructive in code
reviews and discussions.

If you have questions about contributing or want help getting started, please
open an issue or contact the maintainers via the project's issue tracker.

Thank you for contributing!
