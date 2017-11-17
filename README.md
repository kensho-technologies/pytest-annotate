# pytest-annotate

[PyAnnotate](https://github.com/dropbox/pyannotate) as a
[pytest](https://docs.pytest.org/en/latest/) plugin.

```
pip install pytest-annotate

# Generate annotations by running your pytest tests as usual:
py.test --annotate-output=./annotations.json

# Apply those annotations using pyannotate:
pyannotate --type-info ./annotations.json .
```
