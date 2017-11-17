# Contributing

Thank you for taking the time to contribute to this project!

To get started:
```
pip install -r dev-requirements.txt
pip install -r requirements.txt
```

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code.
Please report unacceptable behavior at
[pytest-annotate-maintainer@kensho.com](mailto:pytest-annotate-maintainer@kensho.com).

## Contributor License Agreement

Each contributor is required to agree to our
[Contributor License Agreement](https://www.clahub.com/agreements/kensho-technologies/pytest-annotate),
to ensure that their contribution may be safely merged into the project codebase and
released under the existing code license. This agreement does not change contributors'
rights to use the contributions for any other purpose -- it is simply used for the protection
of both the contributors and the project.

## Style Guide

This project follows the
[Google Python style guide](https://google.github.io/styleguide/pyguide.html).

Additionally, any contributions must pass the following set of lint and style checks with no issues:
```
flake8 pytest_annotate/

pydocstyle pytest_annotate/

isort --check-only --verbose --recursive pytest_annotate/

pylint pytest_annotate/

bandit -r pytest_annotate/
```
