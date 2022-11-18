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