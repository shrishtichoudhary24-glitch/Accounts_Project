.PHONY: install lint test run
install:
	pip install -r requirements.txt
lint:
	flake8 service --count --max-complexity=10 --max-line-length=127 --statistics
test:
	nosetests
run:
	flask --app service run --port 5000
