install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=src testing/

format:
	black *.py

lint: 
	pylint --disable=R,C $$(git ls-files '*.py')

all: install lint tests format