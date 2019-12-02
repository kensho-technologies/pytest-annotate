# pytest-annotate

[![Build Status](https://travis-ci.org/kensho-technologies/pytest-annotate.svg?branch=master)](https://travis-ci.org/kensho-technologies/pytest-annotate)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI Python](https://img.shields.io/pypi/pyversions/pytest-annotate.svg)](https://pypi.python.org/pypi/pytest-annotate)
[![PyPI Version](https://img.shields.io/pypi/v/pytest-annotate.svg)](https://pypi.python.org/pypi/pytest-annotate)
[![PyPI Status](https://img.shields.io/pypi/status/pytest-annotate.svg)](https://pypi.python.org/pypi/pytest-annotate)
[![PyPI Wheel](https://img.shields.io/pypi/wheel/pytest-annotate.svg)](https://pypi.python.org/pypi/pytest-annotate)


[PyAnnotate](https://github.com/dropbox/pyannotate) as a
[pytest](https://docs.pytest.org/en/latest/) plugin.

```
pip install pytest-annotate

# Generate annotations by running your pytest tests as usual:
pytest --annotate-output=./annotations.json

# Apply those annotations using pyannotate:
pyannotate --type-info ./annotations.json .
```
