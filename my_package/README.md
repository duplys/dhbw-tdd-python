## Explanation of the package structure

Directory `my_package` contains the Python package code:

* `__init__.py` file turns the directory into a Python package. This file can be empty or include package initialization code.
* `addition.py` and `multiplication.py` are example Python modules that contain the actual code you want to distribute.

Directory `tests` contains your unit tests, e.g., for Test-Driven Development (TDD)

* `test_addition.py` and `test_multiplication.py` are unit test files corresponding to `addition.py` and `multiplication.py`. Each file should contain tests for the respective module.

`setup.py` is the setup script used to package and distribute your Python package. It can include information like the package name, version, author, and other metadata.

## Running the unit tests

To ensure that the Python interpreter finds the `my_package` module when trying to import it, you must first add `my_package` directory to the Python path:

```bash
export PYTHONPATH=/Users/paulduplys/Repositories/dhbw-tdd-python:$PYTHONPATH
```

You can then use the following command to run the tests from within the `my_package` directory:

```bash
python3 -m unittest discover -s tests
```
