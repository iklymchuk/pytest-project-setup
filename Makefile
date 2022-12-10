install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src testing/ -m "skip_agnostic"

parallel-test:
	python -m pytest -n auto -vv --cov=src testing/ 

profile-test-code:
	python -m pytest -vv --durations=10 --durations-min=1.0

format:
	black .

lint: 
	pylint --disable=R,C $$(git ls-files '*.py')

all: install lint test format