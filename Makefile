install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

tests:
	python -m pytest -vv 

format:
	black *.py

lint: 
	pylint --disable=R,C $$(git ls-files '*.py')

all: install lint tests format