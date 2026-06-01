install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=hello --cov=greeting \
		--cov=smath --cov=web tests
	python -m pytest -nbval notebook.ipynb #test our jupiter notebook

debug:
	python -m pytest -vv --pdb #debugger is invoked

one-test:
	python -m pytest -vv tests/test_greeting.py::test_myname4
