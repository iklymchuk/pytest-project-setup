[![Github build](https://github.com/iklymchuk/pytest-project-setup/actions/workflows/github-build.yml/badge.svg)](https://github.com/iklymchuk/pytest-project-setup/actions/workflows/github-build.yml)

# pytest-project-setup
This is a pytest project setup

## Note on Codespaces Virtualenv 
Checkout how if you run `pip freeze | wc -l` there are many packages we may not want
Try `which python`
1. `virtualenv ~/.venv` 
2. Always source this virt env:
`vim ~/.bashrc` and put in `source ~/.venv/bin/activate`
3. Verify the right python `which python` and try `pip freeze | wc -l` it should be 0

## Make file
* `make install` install the project dependencies
* `make test` perform tests execution and coverage stat
* `make format` formatting the code
* `make lint` static code validation
* `make all` perform all operations (from step 1 to step 4) one after each other

## Dummy user cli function for testing purposes
* `python src/user.py` return the default greeting `Hello guest user!`
* `python src/user.py --user=superadmin` return the greeting with custom user value `Hello superadmin user!`

## Pytest execution
* Library style: `python -m pytest -vv --cov=src testing/`
* Run tests by keyword expressions: `python -m pytest -vv -k "user"`
* Run a specific test within a modele: `python -m pytest testing/test_user.py::test_random_user`
* Run tests by marker expressions: `https://docs.pytest.org/en/7.2.x/how-to/usage.html#usage`
* Profile tests: `python -m pytest -vv --durations=10 --durations-min=1.0`
* Distributed testing `https://pypi.org/project/pytest-xdist/`