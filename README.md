[![Github build](https://github.com/iklymchuk/pytest-project-setup/actions/workflows/github-build.yml/badge.svg)](https://github.com/iklymchuk/pytest-project-setup/actions/workflows/github-build.yml)

# pytest-project-setup
This is a pytest project setup

# Note on Codespaces Virtualenv 
Checkout how if you run `pip freeze | wc -l` there are many packages we may not want
Try `which python`
1. `virtualenv ~/.venv` 
2. Always source this virt env:
`vim ~/.bashrc` and put in `source ~/.venv/bin/activate`
3. Verify the right python `which python` and try `pip freeze | wc -l` it should be 0

# Make file
1. `make install` install the project dependencies
2. `make test` perform tests execution and coverage stat
3. `make format` formatting the code
4. `make lint` static code validation
5. `make all` perform all operations (from step 1 to step 4) one after each other

# Dummy user cli function for testing purposes
1. `python src/user.py` return the default greeting `Hello guest user!`
2. `python src/user.py --user=superadmin` return the greeting with custom user value `Hello superadmin user!`
