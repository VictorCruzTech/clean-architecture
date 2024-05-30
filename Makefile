install:
	pip install -e requirements.txt


format:
	black .


test:
	pytest -vvv